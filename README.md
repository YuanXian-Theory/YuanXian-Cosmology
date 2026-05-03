# YuanXian Cosmology: Modified Friedmann Equations with True Circle Self-Referon Network

This repository contains the formalization and numerical implementation accompanying the paper:

**"Cosmological Evolution Equations in YuanXian Theory: Modified Friedmann Equations with True Circle Self-Referon Contributions"**

## Contents

- **Lean 4 Formalization**: Complete machine-verified derivation from YuanXian action to modified Friedmann equations.
- **YuanXian-Cosmo**: Python package for background evolution and perturbation calculations, compatible with CLASS and CAMB.
- **Reproducibility**: All results in the paper can be reproduced using the provided code.

## Quick Start

```bash
pip install yuanxian-cosmo
lake exe cache get   # for Lean

## Key Results
•  Modified Friedmann equations with dynamic dark energy component (ρ_net, p_net)
•  CPL parameterization: w(z) = -0.998 + 0.0012 z/(1+z)
•  Open-source cosmology module + Lean proofs
DOI (Zenodo): [10.5281/zenodo.20001946]
