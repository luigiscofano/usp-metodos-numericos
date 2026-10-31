"""Euler, Heun e RK4 de passo fixo para PVIs escalares e vetoriais."""
import numpy as np


def integrar(f, intervalo, inicial, passos, *, metodo='rk4'):
    if metodo not in {'euler', 'heun', 'rk4'}:
        raise ValueError('Método desconhecido.')
    t0, tf = intervalo
    if not np.isfinite([t0, tf]).all() or tf <= t0 or int(passos) != passos or passos < 1:
        raise ValueError('Intervalo crescente e passos inteiros positivos são necessários.')
    u0 = np.asarray(inicial, dtype=float)
    if u0.ndim > 1 or not u0.size or not np.isfinite(u0).all():
        raise ValueError('Inicial deve ser escalar ou vetor finito não vazio.')
    times = np.linspace(t0, tf, int(passos)+1)
    values = np.empty((int(passos)+1,)+u0.shape)
    values[0] = u0
    h = (tf-t0)/passos

    def derivative(t, u):
        v = np.asarray(f(t, u), dtype=float)
        if v.shape != u0.shape or not np.isfinite(v).all():
            raise ValueError('Derivada com forma incompatível ou valores não finitos.')
        return v

    for k, t in enumerate(times[:-1]):
        u = values[k]
        k1 = derivative(t, u)
        if metodo == 'euler':
            increment = k1
        elif metodo == 'heun':
            increment = (k1+derivative(t+h, u+h*k1))/2
        else:
            k2 = derivative(t+h/2, u+h*k1/2)
            k3 = derivative(t+h/2, u+h*k2/2)
            k4 = derivative(t+h, u+h*k3)
            increment = (k1+2*k2+2*k3+k4)/6
        values[k+1] = u+h*increment
        if not np.isfinite(values[k+1]).all():
            raise FloatingPointError('Solução não finita; revise passo e problema.')
    return times, values


def corrente_chua(v):
    """Curva por trechos em SI, com parâmetros do notebook recuperado."""
    e, emax = 1.17391304, 8.1818
    ga, gb, gc = -(50/66)*1e-3, -(9/22)*1e-3, 4.591e-3
    if v <= -emax:
        return gc*v+emax*(gc-gb)+e*(gb-ga)
    if v <= -e:
        return gb*v+e*(gb-ga)
    if v <= e:
        return ga*v
    if v <= emax:
        return gb*v+e*(ga-gb)
    return gc*v+emax*(gb-gc)+e*(ga-gb)


def circuito_chua(resistencia=1800):
    if not np.isfinite(resistencia) or resistencia <= 0:
        raise ValueError('Resistência deve ser positiva e finita.')

    def f(t, u):
        del t
        v1, v2, current = u
        return np.array([((v2-v1)/resistencia-corrente_chua(v1))/1e-8,
                         ((v1-v2)/resistencia+current)/1e-7,
                         -v2/0.018])
    return f
