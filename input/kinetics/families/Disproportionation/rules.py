#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 485,
    label = "Y_rad_birad_trirad_quadrad;XH_Rrad_birad",
    kinetics = ArrheniusEP(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 556,
    label = "O2b;XH_Rrad_birad",
    kinetics = ArrheniusEP(
        A = (5e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A.G. Vandeputte estimated value""",
)

entry(
    index = 556,
    label = "Y_rad_birad_trirad_quadrad;Cdpri_Csrad",
    kinetics = ArrheniusEP(
        A = (1e+09, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Estimated value, AG Vandeputte""",
)

entry(
    index = 658,
    label = "O_rad/NonDeO;Cmethyl_Srad",
    kinetics = ArrheniusEP(
        A = (5.91E10, 'cm^3/(mol*s)'),
        n = 2.93,
        alpha = 0,
        E0 = (102926, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Ryan Gillis, 2018""",
    longDesc =
"""
Author(s):   Zhu, L.; Bozzelli, J.W.
Title:   Kinetics of the multichannel reaction of methanethiyl radical (CH3S center dot) with O-3(2) - Pressure Independent
Journal:   J. Phys. Chem. A
"""
)
