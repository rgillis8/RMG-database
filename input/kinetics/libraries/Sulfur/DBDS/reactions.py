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
    kinetics = Arrhenius(A=(38.2, 'cm^3/(mol*s)'),
                         n= 2.76,
                         Ea=(2.19, 'kcal/mol'),
                         T0=(1, 'K')
                         ),
    longDesc = 
u"""
Combination of GAV value and calculated value
""",
)

entry(
    index = 2,
    label = "C14H13S3 <=> C14H12S3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(92.2, 's^-1'),
                         n= 3.22,
                         Ea=(13.1, 'kcal/mol'),
                         T0=(1, 'K')
                         ),
    longDesc =
u"""
forward reaction estimated by RMG... but not thermo favored so they use the reverse reaction. Changed by Ryan Gillis.
""",
)

entry(
    index = 3,
    label = "C14H13S4 <=> C14H12S4H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(92.2, 's^-1'),
                         n= 3.22,
                         Ea=(13.1, 'kcal/mol'),
                         T0=(1, 'K')
                         ),
    longDesc =
u"""
forward reaction estimated by RMG... but not thermo favored so they use the reverse reaction. Changed by Ryan Gillis.
""",
)

entry(
    index = 4,
    label = "C14H13S2 <=> C14H12S2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3560000, 's^-1'),
                         n= 1.75,
                         Ea=(25.3, 'kcal/mol'),
                         T0=(1, 'K')
                         ),
    longDesc =
u"""
forward reaction estimated by RMG... but not thermo favored so they use the reverse reaction. Changed by Ryan Gillis.
""",
)

