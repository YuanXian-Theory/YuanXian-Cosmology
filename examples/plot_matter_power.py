"""
Example: Plot Matter Power Spectrum Ratio
YuanXian-Cosmology Repository
Author: Zhenyuan Acharya
Date: 2026-05-03
"""

import numpy as np
import matplotlib.pyplot as plt

# ================== Parameters ==================
k = np.logspace(-3, 1, 400)   # h/Mpc

# ΛCDM matter power spectrum (simplified)
p_lcdm = 1e4 * k**(-1.2) / (1 + (k/0.1)**4)

# YuanXian model with TCSR suppression
p_yuanxian = p_lcdm.copy()
p_yuanxian[(k > 0.05) & (k < 0.3)] *= 0.992   # ~0.8% suppression around k~0.1 h/Mpc

ratio = p_yuanxian / p_lcdm

# ================== Plotting ==================
fig, axs = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[3, 1], sharex=True)

# Top: Power spectrum
axs[0].loglog(k, p_lcdm, 'b-', linewidth=2.0, label='ΛCDM')
axs[0].loglog(k, p_yuanxian, 'r--', linewidth=2.0, label='YuanXian (TCSR)')
axs[0].set_ylabel(r'$P(k)\ [h^{-3}{\rm Mpc}^3]$', fontsize=14)
axs[0].set_title('Matter Power Spectrum Comparison\n(ΛCDM vs YuanXian TCSR Model)', fontsize=15)
axs[0].legend(fontsize=12)
axs[0].grid(True, which='both', ls='--', alpha=0.6)

# Bottom: Ratio
axs[1].semilogx(k, ratio, 'k-', linewidth=2.0)
axs[1].axhline(1.0, color='gray', linestyle='--', alpha=0.7)
axs[1].set_xlabel(r'Wavenumber $k\ [h\,{\rm Mpc}^{-1}]$', fontsize=14)
axs[1].set_ylabel(r'$P_{\rm YuanXian}(k)/P_{\rm ΛCDM}(k)$', fontsize=14)
axs[1].grid(True, which='both', ls='--', alpha=0.6)

# Highlight suppression region
axs[1].axvspan(0.05, 0.3, alpha=0.15, color='red')
axs[1].annotate('~0.8% Suppression', xy=(0.1, 0.993), 
                xytext=(0.03, 0.985), arrowprops=dict(arrowstyle='->'), fontsize=11)

plt.tight_layout()
plt.savefig('figures/matter_power_spectrum.png', dpi=300, bbox_inches='tight')
plt.show()

print("Matter power spectrum plot saved to figures/matter_power_spectrum.png")
