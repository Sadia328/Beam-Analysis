# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:14:29 2020

@author: Sadia
"""
import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np
#units in N, m, N/m2,
op.wipe()
#m = 1
#mm = 0.001*m
#Pa = 1.
#MPa = 10**6*Pa
#GPa = 10**9*Pa

#Beam model

op.model('basic', '-ndm', 2, '-ndf', 3)
#E=1000ksi
E=16000000
op.uniaxialMaterial("Elastic", 1, E)

# section parameters in mm
h=600
w=400
A=24000
#define nodes
op.node(1,0.,0.)
op.node(2,10.,0.)
op.node(3,20.,0.)
 #definining nodes on beam
#nodeX = np.array([0.,1.,2.])
#nodeY = np.array([0.,0.,0.])
#Boundry condition
op.fix(1, 1, 1,0)
op.fix(3, 0, 1,0)
#define eam element
op.geomTransf('Linear', 1)
#p.beamIntegration('Lobatto', 1, 1, 3)
print("5")
 #                          tag, ndI, ndJ, A,     E,    Iz, transfTag
op.element('elasticBeamColumn', 1, 1, 2, 24000.0, 16000.0, 11000.0, 1)
op.element('elasticBeamColumn', 2, 2, 3, 24000.0, 16000.0, 11000.0, 1)
print("7")
    #
#set recorders
op.recorder('Node', '-file', "NodeDisp.out", '-time', '-node', 2, '-dof', 1,2,'disp')
#op.recorder('Node', '-file', "Reaction.out", '-time', '-node', 1,2, '-dof', 1,2,'reaction')
#op.recorder('Element', '-file', "Elements.out",'-time','-ele', 1,2, 'forces')
#Set Analysis options
op.timeSeries("Linear", 1)
# create a plain load pattern
op.pattern("Plain", 1, 1)
Px=0
Py =-25000
op.load(2, Px, Py,)
op.integrator("LoadControl", 1.0)
op.algorithm("Newton")
op.numberer("RCM")
op.constraints("Plain")
op.system("BandSPD")
op.analysis("Static")
# perform the analysis
op.initialize() 
ok = op.analyze(1)
#on node 2 and in y direction 2
uy2 = op.nodeDisp(2,2)
print("3")
 #   print("Results")
print("Nodal Displacements")

print("uy2")
print(uy2)   
opp.plot_model()





