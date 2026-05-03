"""
Example: Linear Growth Factor Comparison
YuanXian-Cosmology Repository
Author: Zhenyuan Acharya
Date: 2026-05-03
"""

import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(0, 5, 300)

# Approximate growth factor D(z)
d_lcdm = 1.0 / (1 + z)**0.55
d_yx = 1.0 / (1 + z)**0.555   # slight suppression

plt.figure(figsize=(9, 6))
plt.plot(z, d_lcdm, 'b-', linewidth=2.2, label='ΛCDM')
plt.plot(z, d_yx, 'r--', linewidth=2.2, label='YuanXian (TCSR)')

plt.xlabel('Redshift $z$', fontsize=14)
plt.ylabel('Linear Growth Factor $D(z)$ (normalized)', fontsize=14)
plt.title('Growth Factor Suppression due to TCSR Network', fontsize=15)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.6)

plt.tight_layout()
plt.savefig('../figures/growth_factor.png', dpi=300, bbox_inches='tight')
plt.show()

print("Growth factor plot saved.")
