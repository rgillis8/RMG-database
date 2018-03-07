#!/usr/bin/env python
# encoding: utf-8

name = "SulfurOxyAddition/groups"
shortDesc = u""
longDesc = u"""
Based on several experimental observations especially bye Atkinson et al. and calculations by Ryan Gillis.
"""

template(reactants=["S_RR", "OR"], products=["S_ORR"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['GAIN_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
        index = 1,
        label = 'S_RR',
        group = 
"""
1 *1 S u0 px c0 {2,S} {3,S}
2 R ux px c0 {1,S}
3 R ux px c0 {1,S}
""",
    kinetics = None,
)

entry(
        index = 2,
        label = 'S_CC',
        group =
"""
1 *1 S u0 px c0 {2,S} {3,S}
2 C ux px c0 {1,S}
3 C ux px c0 {1,S}
""",
    kinetics = None,
)

entry(
        index = 3,
        label = 'S_CO',
        group =
"""
1 *1 S u0 px c0 {2,S} {3,S}
2 C ux px c0 {1,S}
3 O ux px c0 {1,S}
""",
    kinetics = None,
)

entry(
        index = 4,
        label = 'S_CS',
        group =
"""
1 *1 S u0 px c0 {2,S} {3,S}
2 C ux px c0 {1,S}
3 S ux px c0 {1,S}
""",
    kinetics = None,
)

entry(
        index = 5,
        label = 'O_R',
        group =
"""
1 *2 O u1 px c0 {2,S}
2 R ux px c0 {1,S}
""",
    kinetics = None,
)

entry(
        index = 6,
        label = 'O_H',
        group =
"""
1 *2 O u1 px c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
        index = 7,
        label = 'O_C',
        group =
"""
1 *2 O u1 px c0 {2,S}
2 C ux px c0 {1,S}
""",
    kinetics = None,
)

entry(
        index = 8,
        label = 'O_O',
        group =
"""
1 *2 O u1 px c0 {2,S}
2 O ux px c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: S_RR
    L2: S_CC
    L2: S_CO
    L3: S_CS

L1: O_R
    L2:O_H
    L2:O_C
    L2:O_O
"""
)

