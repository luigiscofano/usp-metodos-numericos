"""Interpolação de Newton e fórmula baricêntrica com nós distintos."""
import numpy as np


def _dados(x, y=None):
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or not len(x) or not np.isfinite(x).all() or len(np.unique(x)) != len(x):
        raise ValueError('Nós devem ser um vetor finito, não vazio e sem repetições.')
    if y is not None:
        y = np.asarray(y, dtype=float)
        if y.shape != x.shape or not np.isfinite(y).all():
            raise ValueError('Valores incompatíveis com os nós.')
    return x, y


def diferencas_divididas(x, y):
    x, y = _dados(x, y)
    coefficients = y.copy()
    for order in range(1, len(x)):
        coefficients[order:] = (coefficients[order:]-coefficients[order-1:-1])/(x[order:]-x[:-order])
    return coefficients


def avaliar_newton(pontos, nos, coeficientes):
    nos, coeficientes = _dados(nos, coeficientes)
    points = np.asarray(pontos, dtype=float)
    if not np.isfinite(points).all():
        raise ValueError('Pontos de avaliação não finitos.')
    result = np.full_like(points, coeficientes[-1])
    for j in range(len(nos)-2, -1, -1):
        result = coeficientes[j] + (points-nos[j])*result
    return result.item() if points.ndim == 0 else result


def pesos_baricentricos(nos):
    nos, _ = _dados(nos)
    if len(nos) == 1:
        return np.ones(1)
    # Uma escala comum não altera a fórmula; logs evitam produtos extremos.
    center = (nos.max()/2 + nos.min()/2)
    scale = np.max(abs(nos-center))
    normalized = (nos-center)/scale
    logs, signs = np.empty(len(nos)), np.empty(len(nos))
    for j in range(len(nos)):
        difference = normalized[j]-np.delete(normalized, j)
        logs[j] = -np.log(abs(difference)).sum()
        signs[j] = np.prod(np.sign(difference))
    return signs*np.exp(logs-logs.max())


def baricentrica(pontos, nos, valores, pesos=None):
    nos, valores = _dados(nos, valores)
    weights = pesos_baricentricos(nos) if pesos is None else np.asarray(pesos, dtype=float)
    if weights.shape != nos.shape or not np.isfinite(weights).all() or (weights == 0).any():
        raise ValueError('Pesos incompatíveis, nulos ou não finitos.')
    points = np.asarray(pontos, dtype=float)
    if not np.isfinite(points).all():
        raise ValueError('Pontos de avaliação não finitos.')
    flat = points.reshape(-1)
    result = np.empty(len(flat))
    for i, point in enumerate(flat):
        exact = np.flatnonzero(point == nos)
        if len(exact):
            result[i] = valores[exact[0]]
        else:
            terms = weights/(point-nos)
            # Reescala cada consulta para reduzir overflow perto de um nó.
            terms /= np.max(abs(terms))
            denominator = terms.sum()
            if denominator == 0:
                raise FloatingPointError('Cancelamento no denominador baricêntrico.')
            result[i] = (terms @ valores)/denominator
    return result[0].item() if points.ndim == 0 else result.reshape(points.shape)


def nos_chebyshev(n, a=-1, b=1):
    """n nós de Chebyshev-Lobatto, incluindo as extremidades."""
    if int(n) != n or n < 2 or not np.isfinite([a, b]).all() or not a < b:
        raise ValueError('Use n inteiro >=2 e intervalo finito crescente.')
    return (a+b)/2-(b-a)/2*np.cos(np.pi*np.arange(n)/(n-1))
