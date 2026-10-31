"""Fatoração PLU e comparação de precisão; preserva as entradas."""
import numpy as np


def _matriz(a):
    a = np.array(a, dtype=float, copy=True)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or a.shape[0] == 0:
        raise ValueError('A deve ser quadrada e não vazia.')
    if not np.isfinite(a).all():
        raise ValueError('A deve conter apenas valores finitos.')
    return a


def fatorar_plu(a):
    """Retorna P,L,U com P@A=L@U; usa pivotamento parcial."""
    u = _matriz(a)
    n = len(u)
    l, p = np.eye(n), np.eye(n)
    threshold = np.finfo(float).eps * n * np.linalg.norm(u, ord=np.inf)
    for k in range(n):
        pivot = k + np.argmax(abs(u[k:, k]))
        if abs(u[pivot, k]) <= threshold:
            raise np.linalg.LinAlgError('Pivô numericamente nulo na escala de A.')
        if pivot != k:
            u[[k, pivot]] = u[[pivot, k]]
            p[[k, pivot]] = p[[pivot, k]]
            l[[k, pivot], :k] = l[[pivot, k], :k]
        for i in range(k + 1, n):
            l[i, k] = u[i, k] / u[k, k]
            u[i, k:] -= l[i, k] * u[k, k:]
            u[i, k] = 0
    return p, l, u


def resolver(a, b):
    """Resolve Ax=b, para um vetor b, usando a fatoração PLU didática."""
    a = _matriz(a)
    b = np.asarray(b, dtype=float)
    if b.shape != (len(a),) or not np.isfinite(b).all():
        raise ValueError('b deve ser vetor finito compatível com A.')
    p, l, u = fatorar_plu(a)
    pb, y, x = p @ b, np.zeros(len(a)), np.zeros(len(a))
    for i in range(len(a)):
        y[i] = pb[i] - l[i, :i] @ y[:i]
    for i in range(len(a)-1, -1, -1):
        x[i] = (y[i] - u[i, i+1:] @ x[i+1:]) / u[i, i]
    return x


def residuo_relativo(a, x, b):
    """Resíduo normalizado: ||Ax-b||∞/(||A||∞||x||∞+||b||∞)."""
    a, x, b = np.asarray(a), np.asarray(x), np.asarray(b)
    denominator = np.linalg.norm(a, np.inf)*np.linalg.norm(x, np.inf)+np.linalg.norm(b, np.inf)
    numerator = np.linalg.norm(a @ x-b, np.inf)
    return float(numerator/denominator) if denominator else float(numerator)


def arredondar(x, algarismos):
    """Simula algarismos significativos decimais, não um formato IEEE menor."""
    if int(algarismos) != algarismos or not 1 <= algarismos <= 17:
        raise ValueError('Use de 1 a 17 algarismos.')
    if not np.isfinite(x):
        raise ValueError('Valor não finito.')
    return float(f'{float(x):.{int(algarismos)}g}')


def gauss_reduzido(a, b, *, algarismos=5, pivotar=True):
    """Arredonda entradas e operações escalares para um experimento didático."""
    a = _matriz(a)
    b = np.asarray(b, dtype=float)
    if b.shape != (len(a),) or not np.isfinite(b).all():
        raise ValueError('b incompatível ou não finito.')
    rnd = lambda value: arredondar(value, algarismos)
    augmented = np.vectorize(rnd)(np.column_stack((a, b)))
    n = len(a)
    for k in range(n):
        if pivotar:
            pivot = k + np.argmax(abs(augmented[k:, k]))
            augmented[[k, pivot]] = augmented[[pivot, k]]
        if augmented[k, k] == 0:
            raise np.linalg.LinAlgError('Pivô zero na aritmética simulada.')
        for i in range(k+1, n):
            ratio = rnd(augmented[i, k]/augmented[k, k])
            for j in range(k, n+1):
                augmented[i, j] = rnd(augmented[i, j]-rnd(ratio*augmented[k, j]))
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        value = augmented[i, -1]
        for j in range(i+1, n):
            value = rnd(value-rnd(augmented[i, j]*x[j]))
        x[i] = rnd(value/augmented[i, i])
    return x
