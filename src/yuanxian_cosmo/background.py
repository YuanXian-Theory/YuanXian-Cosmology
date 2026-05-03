import numpy as np
from scipy.integrate import quad

class YuanXianCosmology:
    def __init__(self, H0=67.4, Omega_m=0.315, w0=-0.998, wa=0.0012):
        self.H0 = H0
        self.Omega_m = Omega_m
        self.Omega_r = 2.47e-5
        self.w0 = w0
        self.wa = wa
        self.Omega_net0 = 1.0 - Omega_m - self.Omega_r

    def w_TCSR(self, a: float) -> float:
        """CPL parameterization"""
        return self.w0 + self.wa * (1.0 - a)

    def Omega_net(self, a: float) -> float:
        def integrand(log_a):
            ap = np.exp(log_a)
            return (1 + self.w_TCSR(ap)) / ap
        result, _ = quad(integrand, np.log(a), 0.0)
        return self.Omega_net0 * np.exp(-3 * result)

    def Hubble(self, z: float) -> float:
        a = 1.0 / (1.0 + z)
        H2 = self.H0**2 * (
            self.Omega_m * (1 + z)**3 +
            self.Omega_r * (1 + z)**4 +
            self.Omega_net(a)
        )
        return np.sqrt(H2)
