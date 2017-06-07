#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_Sulfur/groups"
shortDesc = u""
longDesc = u"""
This family allows the lone pairs on sulfur atoms to react with radicals to produce sulfur atoms with greater valency
"""

template(reactants=["S", "Y_rad"], products=["Srad-Y"], ownReverse=False)

reverse = "SulfurDisprop"

recipe(actions=[
    ['LOSE_PAIR', '*1', '1'],
    ['GAIN_RADICAL', '*1', '1'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "S",
    group = 
"""
1 *1 S u0
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Y_rad",
    group = 
"""
1 *2 R u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "S2",
    group =
"""
1 *1 S u0 p2
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "S2s",
    group =
"""
1 *1 S2s u0 p2
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "S2s-CC",
    group =
"""
1 *1 S2s u0 p2 {2,S} {3,S}
2    C ux p0 {1,S}
3    C ux p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "S2s-CH",
    group =
"""
1 *1 S2s u0 p2 {2,S} {3,S}
2    C ux p0 {1,S}
3    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "S2s-CO",
    group =
"""
1 *1 S2s u0 p2 {2,S} {3,S}
2    C ux p0 {1,S}
3    O ux p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "S2s-OO",
    group =
"""
1 *1 S2s u0 p2 {2,S} {3,S}
2    O ux p2 {1,S}
3    O ux p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "S2s-OH",
    group =
"""
1 *1 S2s u0 p2 {2,S} {3,S}
2    O ux p2 {1,S}
3    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "S2s-HH",
    group =
"""
1 *1 S2s u0 p2 {2,S} {3,S}
2    H u0 p0 {1,S}
3    H u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "S2d",
    group =
"""
1 *1 S2d u0 p2
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "S2d-Od",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2    Od  u0 p2 {2,D}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "S2d-Cd",
    group =
"""
1 *1 S2d u0 p2 {2,D}
2    Cd  ux p0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "S4",
    group =
"""
1 *1 S u0 p1
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "S4dd",
    group =
"""
1 *1 S4dd u0 p1
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "S4dd-OdOd",
    group =
"""
1 *1 S4dd u0 p1 {2,D} {3,D}
2    Od u0 p2 {1,D}
3    Od u0 p2 {1,D}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "S4dd-OdCd",
    group =
"""
1 *1 S4dd u0 p1 {2,D} {3,D}
2    Od u0 p2 {1,D}
3    C ux p0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "S4dss",
    group =
"""
1 *1 S4d u0 p1
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "S4dss-OdCC",
    group =
"""
1 *1 S4d u0 p1 {2,D} {3,S} {4,S}
2    Od u0 p2 {1,D}
3    C  ux p0 {1,S}
4    C  ux p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "S4dss-OdCO",
    group =
"""
1 *1 S4d u0 p1 {2,D} {3,S} {4,S}
2    Od u0 p2 {1,D}
3    C  ux p0 {1,S}
4    O  ux p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "S4dss-OdCH",
    group =
"""
1 *1 S4d u0 p1 {2,D} {3,S} {4,S}
2    Od u0 p2 {1,D}
3    C  ux p0 {1,S}
4    H  u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "S4dss-OdOO",
    group =
"""
1 *1 S4d u0 p1 {2,D} {3,S} {4,S}
2    Od u0 p2 {1,D}
3    O  ux p2 {1,S}
4    O  ux p2 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "S4dss-OdOH",
    group =
"""
1 *1 S4d u0 p1 {2,D} {3,S} {4,S}
2    Od u0 p2 {1,D}
3    O  ux p2 {1,S}
4    H  u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "S4dss-OdHH",
    group =
"""
1 *1 S4d u0 p1 {2,D} {3,S} {4,S}
2    Od u0 p2 {1,D}
3    H  u0 p0 {1,S}
4    H  u0 p0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "S4s",
    group =
"""
1 *1 S4s u0 p1
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "O_rad",
    group =
"""
1 *2 O u1
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "O_pri_rad",
    group =
"""
1 *2 O u1 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "O_sec_rad",
    group =
"""
1 *2 O u1 {2,S}
2    !H ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "O_sec_rad/NonDe",
    group =
"""
1 *2 O u1 {2,S}
2    [Cs,O] ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "O_sec_rad/OneDe",
    group =
"""
1 *2 O u1 {2,S}
2    [Cd,Ct,Cb,CO] ux {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "!O_rad",
    group =
"""
1 *2 [C,S,N,H] u1
""",
    kinetics = None,
)

tree(
"""
L1: S
    L2: S2
        L3: S2s
            L4: S2s-CC
            L4: S2s-CH
            L4: S2s-CO
            L4: S2s-OO
            L4: S2s-OH
            L4: S2s-HH
        L3: S2d
            L4: S2d-Od
            L4: S2d-Cd
    L2: S4
        L3: S4dd
            L4: S4dd-OdOd
            L4: S4dd-OdCd
        L3: S4dss
            L4: S4dd-OdCC
            L4: S4dd-OdCO
            L4: S4dd-OdCH
            L4: S4dd-OdOO
            L4: S4dd-OdOH
            L4: S4dd-OdHH
        L3: S4s
L1: Y_rad
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
    L2: !O_rad
"""
)



