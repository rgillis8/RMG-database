#!/usr/bin/env python
# encoding: utf-8

name = "SulfurOxyAddition/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "S_CS;O_C",
    kinetics = ArrheniusEP(
        A = (100000, 's^-1'),
        n = 2,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Ryan Gillis calculationat b3lyp/6-31g**""",
)




