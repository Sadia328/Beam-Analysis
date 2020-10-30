# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:07:17 2020

@author:Sadia
"""

import openseespy.opensees as op
import numpy as np
import matplotlib.pyplot as plt
from openseespy.postprocessing.Get_Rendering import* 
op.wipe()
#=======================================================================
# Units
# =============================================================================
#m, N/m2, 
#
# =============================================================================
# Input Variables
# =============================================================================
x1 = 0.
y1 = 2.
x2 = 10.
y2 = 2.
x3 = 20.
y3 = 2.
E1 =2e+11#steel in N/m2
E2= 2.5e+10 #concrete
n=E1/E2 #8.055557106540777
h=0.5
b=0.3
#As=0.08
#A1 = h*b
#A2=As(n-1)
#A=A1+A2# overall tranformed area into concrete so we will use concrete elastic modulus.
A=0.718
#I=(b*(h^3)/12=3.12e-3
Px=0
Py =-25000
#u=(P*(L^3)/(48*E*I)=0.05m
#max allowed def. span L / 250 = 80mm
# Define transform and integration
op.geomTransf('Linear', 1)
   
#  beamIntegration('Lobatto', tag, secTag, N)
op.beamIntegration('Lobatto', 1, 1, 3)
# ===================================================================
# OpenSees Analysis
# =============================================================================
op.wipe()
# set modelbuilder
op.model('basic', '-ndm', 2, '-ndf', 2)

# define materials
op.uniaxialMaterial("Elastic", 1, E2)
# create nodes
op.node(1, x1, y1)
op.node(2, x2, y2)
op.node(3, x3, y3)
nodeY = np.array([0.,0.,0.])# definining nodes on beam 
nodeX = np.array([0.,1.,2.])
# set boundary condition
#op.fix(1, 1, 1)
#op.fix(2, 0, 0)
#op.fix(3, 0, 1)
op.fix(1, 1, 1)
op.fix(2, 0, 0)
op.fix(3, 0, 1)
# define elements
# op.element('Truss', eleTag, *eleNodes, A, matTag[, '-rho', rho][, '-cMass', cFlag][, '-doRayleigh', rFlag])
#  element('elasticBeamColumn', eleTag, *eleNodes, transfTag, integrationTag, '-iter', maxIter=10, tol=1e-12, '-mass', mass=0.0)  
op.element('elasticBeamColumn', 1, *[1,2], 1, 1, '-iter', 30, 1e-12)
op.element('elasticBeamColumn', 2, *[2,3], 1, 1, '-iter', 30, 1e-12)

# create TimeSeries
op.timeSeries("Linear", 1)
# create a plain load pattern
op.pattern("Plain", 1, 1)
# Create the nodal load - command: load nodeID xForce yForce
op.load(2, Px, Py,)
# Record Results
op.recorder('Node', '-file', "NodeDisp.out", '-time', '-node', 2, '-dof', 1,2,'disp')
op.recorder('Node', '-file', "Reaction.out", '-time', '-node', 1,2,3, '-dof', 1,2,'reaction')
op.recorder('Element', '-file', "Elements.out",'-time','-ele', 1,2,3, 'forces')
# create SOE
op.system("BandSPD")
# create DOF number
op.numberer("RCM")
# create constraint handler
op.constraints("Plain")
# create integrator
op.integrator("LoadControl", 1.0)
# create algorithm
op.algorithm("Linear")
# create analysis object
op.analysis("Static")
# perform the analysis
op.initialize() 
ok = op.analyze(1)
ux2 = op.nodeDisp(2,1)
uy2 = op.nodeDisp(2,2)
 #   print("Failed!")
print("Nodal Displacements")
print("ux2")
print(ux2) 
print("uy2")
print(uy2)   
plot_model()


op.wipe()




