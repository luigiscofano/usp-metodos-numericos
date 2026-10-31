"""Experimento sintético de pseudodistâncias; não é receptor GNSS operacional."""
from dataclasses import dataclass
import numpy as np

A_WGS84 = 6378137.0
F_WGS84 = 1/298.257223563
E2_WGS84 = F_WGS84*(2-F_WGS84)


def geodesicas_para_ecef(latitude, longitude, altitude=0):
    if not np.isfinite([latitude, longitude, altitude]).all() or abs(latitude) > 90:
        raise ValueError('Coordenadas geodésicas inválidas.')
    lat, lon = np.deg2rad([latitude, longitude])
    n = A_WGS84/np.sqrt(1-E2_WGS84*np.sin(lat)**2)
    return np.array([(n+altitude)*np.cos(lat)*np.cos(lon),
                     (n+altitude)*np.cos(lat)*np.sin(lon),
                     (n*(1-E2_WGS84)+altitude)*np.sin(lat)])


def ecef_para_geodesicas(xyz):
    xyz = np.asarray(xyz, dtype=float)
    if xyz.shape != (3,) or not np.isfinite(xyz).all() or np.linalg.norm(xyz) < 1:
        raise ValueError('ECEF deve ser vetor finito fora do centro da Terra.')
    x, y, z = xyz
    p = np.hypot(x, y)
    if p < 1e-9:
        return np.array([np.copysign(90, z), 0, abs(z)-A_WGS84*(1-F_WGS84)])
    lat = np.arctan2(z, p*(1-E2_WGS84))
    for _ in range(30):
        n = A_WGS84/np.sqrt(1-E2_WGS84*np.sin(lat)**2)
        new_lat = np.arctan2(z+E2_WGS84*n*np.sin(lat), p)
        if abs(new_lat-lat) < 1e-14:
            lat = new_lat; break
        lat = new_lat
    else:
        raise RuntimeError('Conversão geodésica não convergiu.')
    n = A_WGS84/np.sqrt(1-E2_WGS84*np.sin(lat)**2)
    # Fórmula projetada evita divisão por cos(lat) perto dos polos.
    height = p*np.cos(lat)+z*np.sin(lat)-n*(1-E2_WGS84*np.sin(lat)**2)
    return np.array([np.rad2deg(lat), np.rad2deg(np.arctan2(y, x)), height])


@dataclass(frozen=True)
class PosicaoGPS:
    ecef: np.ndarray
    vies_metros: float
    residuos: np.ndarray
    iteracoes: int
    condicao_jacobiana: float


def estimar_posicao(satelites, pseudodistancias, *, inicial=None, tol=1e-5, maxiter=30):
    satellites = np.asarray(satelites, dtype=float)
    rho = np.asarray(pseudodistancias, dtype=float)
    if satellites.ndim != 2 or satellites.shape[1] != 3 or len(satellites) < 4:
        raise ValueError('São necessárias ao menos quatro posições 3D.')
    if rho.shape != (len(satellites),) or not np.isfinite(satellites).all() or not np.isfinite(rho).all() or (rho <= 0).any():
        raise ValueError('Pseudodistâncias incompatíveis ou valores inválidos.')
    if tol <= 0 or not np.isfinite(tol) or int(maxiter) != maxiter or maxiter < 1:
        raise ValueError('Parâmetros de convergência inválidos.')
    state = np.zeros(4) if inicial is None else np.array(inicial, dtype=float, copy=True)
    if state.shape != (4,) or not np.isfinite(state).all():
        raise ValueError('Inicial deve conter x,y,z e viés de relógio em metros.')
    for iteration in range(1, int(maxiter)+1):
        difference = state[:3]-satellites
        distances = np.linalg.norm(difference, axis=1)
        if (distances == 0).any():
            raise ValueError('Chute coincide com um satélite.')
        jacobian = np.column_stack((difference/distances[:, None], np.ones(len(rho))))
        residual = distances+state[3]-rho
        step, _, rank, _ = np.linalg.lstsq(jacobian, -residual, rcond=None)
        if rank < 4:
            raise np.linalg.LinAlgError('Geometria insuficiente para estimar quatro incógnitas.')
        state += step
        if np.linalg.norm(step) <= tol:
            final_j = np.column_stack(((state[:3]-satellites)/np.linalg.norm(state[:3]-satellites, axis=1)[:, None], np.ones(len(rho))))
            return PosicaoGPS(state[:3].copy(), float(state[3]),
                              np.linalg.norm(state[:3]-satellites, axis=1)+state[3]-rho,
                              iteration, float(np.linalg.cond(final_j)))
    raise RuntimeError('Gauss–Newton não convergiu no limite de iterações.')
