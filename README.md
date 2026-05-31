
# Beam-Analysis — OpenSeesPy Structural Modelling

FEM analysis of a simply-supported composite beam under mid-span point loading.

## Problem Definition
- 20m simply-supported beam, composite steel-concrete section
- Concrete E = 25 GPa, modular ratio n = 8.06
- Transformed area A = 0.718 m², moment of inertia I = bh³/12 ≈ 0.003125 m⁴
- Mid-span point load: 25 kN
- Theoretical deflection: u = PL³/(48EI) ≈ 50mm | Allowable: span/250 = 80mm ✓

## Files
| File | Description |
|------|-------------|
| `beam1.py` | Simply-supported beam with composite transformed section |
| `beamWithSection.py` | Extended analysis with explicit section definition |
| `ModelFunctions.py` | Reusable modelling functions |

## Run Online
▶ open in colab:
https://colab.research.google.com/drive/1A6-aeewysVOuhIz8dTLMFGMdc6nECTY-?usp=sharing

## Context
Developed during PhD research (2020–2023) at Chung-Ang University as part of
structural dynamics and SHM work on civil infrastructure.
