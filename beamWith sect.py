# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:07:17 2020

@author:Sadia
"""
import openseespy.opensees as op
import numpy as np
import matplotlib.pyplot as plt
from openseespy.postprocessing.Get_Rendering import* 

import ModelFunctions as mf
op.wipe()
#=======================================================================
# Units
# =============================================================================
#m, N/m2, 
#
# =============================================================================
# Input Variables
# =============================================================================
Px=0
Py =-25000
#u=(P*(L^3)/(48*E*I)=0.05m
#max allowed def. span L / 250 = 80mm
# ===================================================================
# OpenSees Analysis
# =============================================================================
op.wipe()
# set modelbuilder
#calling functions from model file
mf.getSections()
mf.buildModel()
# create TimeSeries
op.timeSeries("Linear", 1)
# create a plain load pattern
op.pattern("Plain", 1, 1)
# Create the nodal load - command: load nodeID xForce yForce
op.load(2, Px, Py,)
# Record Results
op.recorder('Node', '-file', "NodeDisp.out", '-time', '-node', 2, '-dof', 1,2,'disp')
op.recorder('Node', '-file', "Reaction.out", '-time', '-node', 1,2,3, '-dof', 1,2,'reaction')
op.recorder('Element', '-file', "Elements.out",'-time','-ele', 1,2, 'forces')
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
uy2 = op.nodeDisp(2,2)
 #   print("Results")
print("Nodal Displacements")

print("uy2")
print(uy2)   
plot_model()


op.wipe()




