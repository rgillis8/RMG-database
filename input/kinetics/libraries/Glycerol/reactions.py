#!/usr/bin/env python
# encoding: utf-8

name = "Glycerol"
shortDesc = u"Glycerol in supercritical water"
longDesc = u"""
Taken from NIST databases for use fixing the RMG model used to model glycerol treatment in supercritical water\
"""

entry(
    index = 1,
    label = "hydroxyacetone + OH <=> acetic_acid + methanol_rad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6022140857, 'cm^3/(mol*s)'), n=0, Ea=(35.04, 'kcal/mol'), T0=(1, 'K')),
)