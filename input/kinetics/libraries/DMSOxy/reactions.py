#!/usr/bin/env python
# encoding: utf-8

name = "DMSOxy"
shortDesc = u"Dimethyl Sulide Oxidation library"
longDesc = u"""
Created by Ryan Gillis
"""

entry(
    index = 1,
    label = "O2 + DMSOH <=> DMSO + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(298, 'K')),
    longDesc = 
u"""
Value at 298K reported by Ravishankara et al in "Reaction of OH with Dimethyl Sulfide. 2. Products and Mechanisms
""",
)

entry(
    index = 2,
    label = "OH + DMS  <=> DMSOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
Experimentally observed by Atkinson at 298K
""",
)

#entry(
#    index = 3,
#    label = "OH + DMSO  <=> DMSO2H",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(126020, 'cm^3/(mol*s)'), n=2.38788, Ea=(-31.4797, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#Ryan calculated at b3lyp/3-21g
#""",
#)

#entry(
#    index = 4,
#    label = "O2 + DMSO2H <=> DMSO2 + HO2",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#""",
#)

#entry(
#    index = 5,
#    label = "CSCOO + OH <=> CSCradOO + H2O",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(4.31e+4, 'cm^3/(mol*s)'), n=2.6, Ea=(-7.271, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#""",
#)

#entry(
#    index = 6,
#    label = "CSCOO + O2 <=> CSCradOO + HO2",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(4.31e+4, 'cm^3/(mol*s)'), n=2.6, Ea=(-7.271, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#""",
#)

#entry(
#    index = 7,
#    label = "CSCradOO <=> CSC=O + OH",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(4.31e+4, 'cm^3/(mol*s)'), n=2.6, Ea=(-7.271, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#""",
#)

