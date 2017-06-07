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
    kinetics = Arrhenius(A=(4.47*10^8, 'cm^3/(mol*s)'), n=3.38, Ea=(-19.2, 'kJ/mol'), T0=(298, 'K')),
    longDesc = 
u"""
NIST - Gross, A.; Barnes, I.; Sorensen, R.M.; Kongsted, J.; Mikkelsen, K.V.
Title:   A theoretical study of the reaction between CH3S(OH)CH3 and O2
""",
)

entry(
    index = 2,
    label = "OH + DMS  <=> DMSOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01*10^12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
Value at 298K reported by Ravishankara et al in "Reaction of OH with Dimethyl Sulfide. 2. Products and Mechanisms
""",
)

entry(
    index = 2,
    label = "O2 + DMSOH  <=> DMSO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01*10^12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
Value at 298K reported by Ravishankara et al in "Reaction of OH with Dimethyl Sulfide. 2. Products and Mechanisms
""",
)