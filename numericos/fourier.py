"""DFT e FFT radix-2 com a mesma convenção da numpy.fft."""
import numpy as np


def _vetor(x):
    x = np.asarray(x, dtype=complex)
    if x.ndim != 1 or not len(x) or not np.isfinite(x).all():
        raise ValueError('A entrada deve ser vetor complexo finito e não vazio.')
    return x


def dft(x, *, inversa=False):
    x = _vetor(x)
    n = len(x)
    if n > 2048:
        raise ValueError('DFT densa limitada a 2048 pontos para controlar memória O(N²).')
    indices = np.arange(n)
    sign = 1 if inversa else -1
    matrix = np.exp(sign*2j*np.pi*np.outer(indices, indices)/n)
    result = matrix @ x
    return result/n if inversa else result


def fft(x):
    x = _vetor(x)
    n = len(x)
    if n & (n-1):
        raise ValueError('A FFT didática radix-2 exige tamanho potência de dois.')

    def recursive(values):
        if len(values) == 1:
            return values.copy()
        even, odd = recursive(values[::2]), recursive(values[1::2])
        twiddle = np.exp(-2j*np.pi*np.arange(len(values)//2)/len(values))*odd
        return np.concatenate((even+twiddle, even-twiddle))

    return recursive(x)


def ifft(x):
    x = _vetor(x)
    return fft(x.conjugate()).conjugate()/len(x)
