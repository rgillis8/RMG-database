#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = u""
longDesc = u"""
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""

entry(
    index = 3001,
    label = "O_rad/NonDe;SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1.8e+6, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Experimental rate of OO + CSrad at 298. Demore 1997, JPL Publications""",
)
