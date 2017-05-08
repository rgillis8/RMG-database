#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_Sulfur/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "S4dss-OdCC;O_rad",
    kinetics = ArrheniusEP(
        A = (9.6e-12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (15.1, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""NIST, (CH3)2S + IO → (CH3)2SO + I, Gravestock, T.; Blitz, M.A.; Heard, D.E.
Title:   Kinetics study of the reaction of iodine monoxide radicals with dimethyl sulfide""",
)

entry(
    index = 2,
    label = "S4dss-OdCC;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (3.02e-31, 'cm^3/(mol*s)'),
        n = -6.24,
        alpha = 0,
        E0 = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (300, 'K'),
    ),
    rank = 4,
    shortDesc = u"""NIST, (CH3)2S + OH → (CH3)2SOH, Williams, M.B.; Campuzano-Jost, P.; Hynes, A.J.; Pounds, A.J.
Title:   Experimental and Theoretical Studies of the Reaction of the OH Radical with Alkyl Sulfides: 3. Kinetics and\
Mechanism of the OH Initiated Oxidation of Dimethyl, Dipropyl, and Dibutyl Sulfides:Reactivity Trends in the Alkyl \
Sulfides and Development of a Predictive Expression for the Reaction of OH with DMS""",
)