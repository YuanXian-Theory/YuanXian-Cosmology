"""
Example: Dark Energy Equation of State w(z) Evolution
YuanXian-Cosmology Repository
Author: Zhenyuan Acharya
Date: 2026-05-03
"""

import numpy as np
import matplotlib.pyplot as plt
from yuanxian_cosmo.background import YuanXianCosmology

yx = YuanXianCosmology(w0=-0.998, wa=0.0012)

z = np.linspace(0, 10, 400)
w = [yx.w_TCSR(1/(1+zi)) for zi in z]

plt.figure(figsize=(9, 6))
plt.plot(z, w, 'r-', linewidth=2.5, label='YuanXian TCSR Model')
plt.axhline(-1.0, color='blue', linestyle='--', alpha=0.7, label='ΛCDM (w = -1)')

plt.xlabel('Redshift $z$', fontsize=14)
plt.ylabel('Equation of State $w(z)$', fontsize=14)
plt.title('Dark Energy Equation of State Evolution', fontsize=15)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.6)

plt.annotate('$w_0 = -0.998$\n$w_a = +0.0012$', 
             xy=(1, -0.997), fontsize=12, bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))

plt.tight_layout()
plt.savefig('../figures/w_evolution.png', dpi=300, bbox_inches='tight')
plt.show()

print("w(z) evolution plot saved.")
