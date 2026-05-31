# -*- coding: utf-8 -*-
"""
Simply-supported composite beam analysis using OpenSeesPy
20m span | Steel-concrete transformed section | Mid-span point load

@created on Wed Oct 28 14:07:17 2020

@author: Sadia Umer
"""

import openseespy.opensees as op
from openseespy.postprocessing.Get_Rendering import *

# =============================================================================
# Input Variables (Units: m, N, N/m2)
# =============================================================================
x1, y1 = 0.,  2.
x2, y2 = 10., 2.
x3, y3 = 20., 2.

E1 = 2e+11    # Steel elastic modulus (N/m2)
E2 = 2.5e+10  # Concrete elastic modulus (N/m2)
n  = E1 / E2  # Modular ratio = 8.06

h = 0.5
b = 0.3
A = 0.718
I = (b * h**3) / 12

Px = 0
Py = -25000

# =============================================================================
# OpenSeesPy Model
# =============================================================================
op.wipe()
op.model('basic', '-ndm', 2, '-ndf', 3)
op.geomTransf('Linear', 1)

op.node(1, x1, y1)
op.node(2, x2, y2)
op.node(3, x3, y3)

op.fix(1, 1, 1, 0)
op.fix(2, 0, 0, 0)
op.fix(3, 0, 1, 0)

op.element('elasticBeamColumn', 1, 1, 2, A, E2, I, 1)
op.element('elasticBeamColumn', 2, 2, 3, A, E2, I, 1)

op.timeSeries('Linear', 1)
op.pattern('Plain', 1, 1)
op.load(2, Px, Py, 0)

op.recorder('Node',    '-file', 'NodeDisp.out',  '-time', '-node', 2,    '-dof', 1, 2, 'disp')
op.recorder('Node',    '-file', 'Reaction.out',  '-time', '-node', 1, 3, '-dof', 1, 2, 'reaction')
op.recorder('Element', '-file', 'Elements.out',  '-time', '-ele',  1, 2, 'forces')

op.system('BandSPD')
op.numberer('RCM')
op.constraints('Plain')
op.integrator('LoadControl', 1.0)
op.algorithm('Linear')
op.analysis('Static')
op.analyze(1)

ux2 = op.nodeDisp(2, 1)
uy2 = op.nodeDisp(2, 2)
print(f"Mid-span displacement — ux: {ux2:.6f} m  |  uy: {uy2:.6f} m")

plot_model()
op.wipe()
