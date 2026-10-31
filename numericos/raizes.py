"""Newton escalar real/complexo com diagnóstico explícito de parada."""
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class ResultadoNewton:
    raiz: complex | float
    iteradas: np.ndarray
    residuos: np.ndarray
    convergiu: bool
    motivo: str


def newton(f, df, x0, *, tol=1e-10, maxiter=100, derivada_min=1e-14):
    """Exige resíduo pequeno; passo pequeno sozinho não prova convergência."""
    if tol <= 0 or not np.isfinite(tol) or maxiter < 1 or int(maxiter) != maxiter:
        raise ValueError('Tolerância positiva e maxiter inteiro positivo são necessários.')
    if derivada_min < 0 or not np.isfinite(derivada_min):
        raise ValueError('Limite de derivada inválido.')
    if np.ndim(x0) != 0 or not np.isfinite(x0):
        raise ValueError('O chute inicial deve ser escalar finito.')
    x = complex(x0) if np.iscomplexobj(x0) else float(x0)
    history, residuals = [x], []
    reason, converged = 'máximo de iterações', False
    for iteration in range(int(maxiter) + 1):
        fx = f(x)
        if np.ndim(fx) != 0 or not np.isfinite(fx):
            reason = 'função não finita'; break
        residuals.append(abs(fx))
        if abs(fx) <= tol:
            reason, converged = 'resíduo abaixo da tolerância', True; break
        if iteration == maxiter:
            break
        derivative = df(x)
        if not np.isfinite(derivative) or abs(derivative) <= derivada_min:
            reason = 'derivada pequena ou não finita'; break
        candidate = x - fx / derivative
        if not np.isfinite(candidate):
            reason = 'iterada não finita'; break
        if candidate == x:
            reason = 'estagnação sem resíduo aceitável'; break
        x = candidate
        history.append(x)
    return ResultadoNewton(x, np.asarray(history), np.asarray(residuals), converged, reason)


def bacias_newton(*, tamanho=241, limite=2, maxiter=50, tol=1e-8):
    """Classifica z³−1; -1 significa ponto sem convergência certificada."""
    if int(tamanho) != tamanho or tamanho < 2 or limite <= 0 or maxiter < 1 or tol <= 0:
        raise ValueError('Malha e parâmetros inválidos.')
    axis = np.linspace(-limite, limite, int(tamanho))
    z = axis[None, :] + 1j * axis[:, None]
    labels = np.full(z.shape, -1, dtype=int)
    active = np.ones(z.shape, dtype=bool)
    roots = np.exp(2j * np.pi * np.arange(3) / 3)
    for _ in range(maxiter):
        residual = np.abs(z**3 - 1)
        done = active & (residual <= tol)
        if done.any():
            labels[done] = np.argmin(abs(z[done, None] - roots), axis=1)
        active[done] = False
        derivative = 3 * z**2
        active &= np.isfinite(z) & (abs(derivative) > 1e-14)
        if not active.any():
            break
        z[active] -= (z[active]**3 - 1) / derivative[active]
    done = active & (abs(z**3 - 1) <= tol)
    labels[done] = np.argmin(abs(z[done, None] - roots), axis=1)
    return axis, labels
