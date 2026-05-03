"""
Example: Hubble Parameter Evolution Comparison
YuanXian-Cosmology Repository
Author: Zhenyuan Acharya
Date: 2026-05-03
"""

import numpy as np
import matplotlib.pyplot as plt
from yuanxian_cosmo.background import YuanXianCosmology

# Initialize models
lcdm = YuanXianCosmology(w0=-1.0, wa=0.0)   # Standard ΛCDM
yx = YuanXianCosmology(w0=-0.998, wa=0.0012)  # YuanXian TCSR model

z = np.linspace(0, 10, 500)

h_lcdm = lcdm.Hubble(z)
h_yx = yx.Hubble(z)

plt.figure(figsize=(9, 6))
plt.plot(z, h_lcdm, 'b-', linewidth=2.2, label='ΛCDM')
plt.plot(z, h_yx, 'r--', linewidth=2.2, label='YuanXian (TCSR)')

plt.xlabel('Redshift $z$', fontsize=14)
plt.ylabel('Hubble Parameter $H(z)$ [km/s/Mpc]', fontsize=14)
plt.title('Hubble Parameter Evolution', fontsize=15)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.6)

# Highlight difference region
plt.axvspan(0.5, 3, alpha=0.08, color='red')
plt.annotate('Slight deviation due to dynamical dark energy', 
             xy=(1.5, 120), xytext=(3, 135),
             arrowprops=dict(arrowstyle='->'), fontsize=11)

plt.tight_layout()
plt.savefig('../figures/hubble_evolution.png', dpi=300, bbox_inches='tight')
plt.show()

print("Hubble evolution plot saved.")
