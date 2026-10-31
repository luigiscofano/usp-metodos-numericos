"""Oráculos analíticos e comparação com bibliotecas independentes do código didático."""
import numpy as np
import pytest
from numpy.testing import assert_allclose
from numericos.raizes import newton, bacias_newton
from numericos.lineares import fatorar_plu, resolver, residuo_relativo, gauss_reduzido, arredondar
from numericos.interpolacao import diferencas_divididas, avaliar_newton, baricentrica, nos_chebyshev
from numericos.fourier import dft, fft, ifft
from numericos.edo import integrar, corrente_chua, circuito_chua
from numericos.gps import geodesicas_para_ecef, ecef_para_geodesicas, estimar_posicao


def test_newton_raiz_e_diagnosticos():
    r = newton(lambda x:x*x-2, lambda x:2*x, 1)
    assert r.convergiu and abs(r.raiz-np.sqrt(2)) < 1e-10
    assert not newton(lambda x:x*x+1, lambda x:2*x, 0).convergiu
    assert not newton(lambda x:x*x-2, lambda x:2*x, 100, maxiter=1).convergiu
    r = newton(lambda z:z*z+1, lambda z:2*z, 1j)
    assert r.convergiu and abs(r.raiz-1j) < 1e-14
    with pytest.raises(ValueError):newton(lambda x:x,lambda x:1,0,tol=-1)


def test_bacias_mantem_pontos_nao_classificados():
    _, labels = bacias_newton(tamanho=41)
    assert set(np.unique(labels)) == {-1, 0, 1, 2}
    assert labels[20, 20] == -1


@pytest.mark.parametrize('seed',range(6))
def test_plu_resolve_sem_mudar_entrada(seed):
    rng=np.random.default_rng(seed)
    a=rng.normal(size=(8,8)); saved=a.copy(); exact=rng.normal(size=8); b=a@exact
    p,l,u=fatorar_plu(a)
    assert_allclose(p@a,l@u,atol=1e-13)
    assert_allclose(resolver(a,b),exact,atol=1e-12)
    assert_allclose(resolver(a,b),np.linalg.solve(a,b),atol=1e-12)
    assert np.array_equal(saved,a)
    assert residuo_relativo(a,resolver(a,b),b)<1e-14


def test_plu_pivo_zero_e_escalas():
    a=np.array([[0.,1.],[2.,3.]])
    assert_allclose(resolver(a,[1,5]),[1,1])
    assert_allclose(resolver(a*1e-100,np.array([1,5])*1e-100),[1,1])
    with pytest.raises(np.linalg.LinAlgError):resolver([[1,2],[2,4]],[1,2])
    with pytest.raises(ValueError):resolver(np.ones((2,3)),[1,2])
    with pytest.raises(ValueError):resolver(np.eye(2),[1])


def test_aritmetica_reduzida_pivotamento():
    a=np.array([[1e-8,1.],[1.,1.]])
    b=a@np.ones(2)
    pivot=gauss_reduzido(a,b,algarismos=5,pivotar=True)
    unpivot=gauss_reduzido(a,b,algarismos=5,pivotar=False)
    assert np.linalg.norm(pivot-1)<np.linalg.norm(unpivot-1)
    assert arredondar(1234.567,3)==1230
    with pytest.raises(ValueError):arredondar(1,0)


def test_interpolacao_reproduz_polinomio_e_nos():
    x=np.array([2.,-1.,0.,1.]);f=lambda t:t**3-2*t+1
    points=np.linspace(-1,2,53); y=f(x)
    c=diferencas_divididas(x,y)
    assert_allclose(avaliar_newton(points,x,c),f(points),atol=1e-12)
    assert_allclose(baricentrica(points,x,y),f(points),atol=1e-12)
    assert_allclose(baricentrica(x,x,y),y,atol=0)
    assert baricentrica(2,[2],[7])==7
    assert_allclose(nos_chebyshev(5,2,4)[[0,-1]],[2,4])
    with pytest.raises(ValueError):baricentrica(1,[0,0],[1,2])


@pytest.mark.parametrize('n',[1,2,4,8,32,128])
def test_fourier_complexo_e_inversa(n):
    rng=np.random.default_rng(42);x=rng.normal(size=n)+1j*rng.normal(size=n)
    assert_allclose(fft(x),np.fft.fft(x),atol=1e-11)
    assert_allclose(dft(x),np.fft.fft(x),atol=1e-10)
    assert_allclose(ifft(fft(x)),x,atol=1e-12)
    assert_allclose(dft(dft(x),inversa=True),x,atol=1e-11)


def test_fft_rejeita_comprimento_inadequado():
    with pytest.raises(ValueError):fft([1,2,3])
    with pytest.raises(ValueError):fft([])
    with pytest.raises(ValueError):dft(np.zeros(2049))


@pytest.mark.parametrize('method,minimum',[('euler',1.8),('heun',3.5),('rk4',12)])
def test_ordem_edo_por_refinamento(method,minimum):
    errors=[]
    for n in [20,40]:
        t,u=integrar(lambda t,u:u,(0,1),1.,n,metodo=method)
        errors.append(abs(u[-1]-np.e))
    assert errors[0]/errors[1]>minimum
    assert t[0]==0 and t[-1]==1


def test_edo_oscilador_e_validacao():
    t,u=integrar(lambda t,u:np.array([u[1],-u[0]]),(0,2*np.pi),[1,0],200)
    assert_allclose(u[-1],[1,0],atol=1e-6)
    assert_allclose((u*u).sum(axis=1),1,atol=1e-7)
    with pytest.raises(ValueError):integrar(lambda t,u:u,(0,1),1,0)
    with pytest.raises(ValueError):integrar(lambda t,u:[u],(0,1),1,10)


def test_chua_corrente_continua_e_equilibrio():
    for value in [-8.1818,-1.17391304,1.17391304,8.1818]:
        assert abs(corrente_chua(value-1e-9)-corrente_chua(value+1e-9))<1e-10
    assert_allclose(circuito_chua()(0,[0,0,0]),[0,0,0])
    t,u=integrar(circuito_chua(),(0,0.002),[-0.5,-0.2,0],2000)
    assert np.isfinite(u).all()


@pytest.mark.parametrize('lla',[[0,0,0],[-20,-45,750],[89.9,30,1000],[90,0,50],[-90,0,0]])
def test_geodesia_ida_e_volta(lla):
    assert_allclose(ecef_para_geodesicas(geodesicas_para_ecef(*lla)),lla,atol=1e-6)
    with pytest.raises(ValueError):ecef_para_geodesicas([0,0,0])


def test_gps_sintetico_e_geometria():
    rng=np.random.default_rng(42);sat=rng.normal(size=(8,3));sat*=2.66e7/np.linalg.norm(sat,axis=1)[:,None]
    exact=geodesicas_para_ecef(-20,-45,750);rho=np.linalg.norm(exact-sat,axis=1)+12000
    result=estimar_posicao(sat,rho)
    assert_allclose(result.ecef,exact,atol=1e-5)
    assert abs(result.vies_metros-12000)<1e-5
    assert np.max(abs(result.residuos))<1e-5
    with pytest.raises(np.linalg.LinAlgError):estimar_posicao(np.tile([2e7,0,0],(4,1)),np.full(4,2e7))
