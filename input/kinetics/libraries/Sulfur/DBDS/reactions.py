#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DBDS"
shortDesc = u"dibenzyl disulfide library"
longDesc = u"""
Sulfur library originally created by Ryan Gillis
"""
#entry(
#    index = 1,
#    label = "C7H7 + C7H6S <=> C14H13S",
#    degeneracy = 1,
#   kinetics = Arrhenius(A=(2096, 'cm^3/(mol*s)'),
#                       n= 2.526,
#                      Ea=(1.15, 'kcal/mol'),
#                     T0=(1, 'K')
#                    ),
#longDesc = 
#u"""
#""",
#)

#entry(
#    index = 2,
#    label = "C7H7 + C7H6S <=> DBMS_rad",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(646.3, 'cm^3/(mol*s)'),
#                         n= 2.978,
#                         Ea=(0.1, 'kcal/mol'),
#                         T0=(1, 'K')
#                         ),
#    longDesc =
#u"""
#""",
#)

entry(
    index = 3,
    label = "DBMS + C7H7S3 <=> C7H7 + DB4S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.214, 'cm^3/(mol*s)'),
                         n= 3.8,
                         Ea=(25.6, 'kcal/mol'),
                         T0=(1, 'K')
                         ),
    longDesc =
u"""
""",
)

entry(
    index = 4,
    label = "DBMS + C7H7S2 <=> C7H7 + DB3S",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.214, 'cm^3/(mol*s)'),
                         n= 3.8,
                         Ea=(25.6, 'kcal/mol'),
                         T0=(1, 'K')
                         ),
    longDesc =
u"""
""",
)
