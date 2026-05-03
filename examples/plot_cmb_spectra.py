"""
Example: Plot CMB Temperature Power Spectrum Comparison
YuanXian-Cosmology Repository
Author: Zhenyuan Acharya
Date: 2026-05-03
"""

import numpy as np
import matplotlib.pyplot as plt

# ================== Parameters ==================
l = np.logspace(1, 4, 500)  # multipole moment l

# ΛCDM model (reference)
cl_lcdm = 1e-9 * (l**(-0.8) + 5000 / (1 + (l/200)**2))   # simplified model

# YuanXian model with TCSR network (ISW enhancement at low-l)
cl_yuanxian = cl_lcdm.copy()
cl_yuanxian[l < 30] *= 1.015   # ~1.5% enhancement at large scales due to ISW

# ================== Plotting ==================
plt.figure(figsize=(10, 6))

plt.loglog(l, l*(l+1)*cl_lcdm/(2*np.pi), 'b-', linewidth=2.0, label='ΛCDM')
plt.loglog(l, l*(l+1)*cl_yuanxian/(2*np.pi), 'r--', linewidth=2.0, label='YuanXian (TCSR)')

plt.xlabel(r'Multipole moment $\ell$', fontsize=14)
plt.ylabel(r'$\ell(\ell+1)C_\ell^{TT} / 2\pi\ [\mu K^2]$', fontsize=14)
plt.title('CMB Temperature Angular Power Spectrum\n(ΛCDM vs YuanXian TCSR Model)', fontsize=15)

plt.legend(fontsize=12)
plt.grid(True, which='both', ls='--', alpha=0.7)

# Highlight low-l ISW region
plt.axvspan(2, 30, alpha=0.1, color='red')
plt.annotate('ISW Enhancement (~1-2%)', xy=(10, 1.2e-9), 
             xytext=(50, 3e-9), arrowprops=dict(arrowstyle='->'), fontsize=11)

plt.tight_layout()
plt.savefig('figures/cmb_power_spectrum.png', dpi=300, bbox_inches='tight')
plt.show()

print("CMB power spectrum plot saved to figures/cmb_power_spectrum.png")
