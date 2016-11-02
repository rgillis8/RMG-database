#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DBDS"
shortDesc = u"dibenzyl disulfide library"
longDesc = u"""
Sulfur library originally created by Ryan Gillis
"""
entry(
    index = 1,
    label = "C7H7 + C7H6S <=> C14H13S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00850306, 's^-1'),
                         n= 2.52,
                         Ea=(12.78, 'kcal/mol'),
                         T0=(1, 'K')
                         ),
    longDesc = 
u"""
""",
)
