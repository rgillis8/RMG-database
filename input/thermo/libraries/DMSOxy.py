#!/usr/bin/env python
# encoding: utf-8

name = "DMSOxy"
shortDesc = u"DMSOxy Thermo library"
longDesc = u"""
A few supplemental species that are poorly estimated by group additivity. Compiled by Ryan Gillis 2017-2018
"""

entry(
    index = 1,
    label = "DMSOH",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  S u1 p1 c0 {1,S} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.3978, 0.051857, -9.62442e-05, 1.2396e-07, -6.39971e-11, -7116.83, 11.3494],
                Tmin = (10, 'K'),
                Tmax = (582.107, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.06588, 0.0307344, -1.69216e-05, 4.6058e-09, -4.93548e-13, -7147.36, 5.61026],
                Tmin = (582.107, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CBS-QB3 Calculation, Ryan Gillis 5/2017
""",
)

entry(
    index = 1,
    label = "C=[S+]O[O-]",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u0 p1 c+1 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.92612, 0.00447826, 8.05198e-05, -1.68533e-07, 1.03893e-10, 21380.7, 10.0719],
                Tmin = (10, 'K'),
                Tmax = (543.079, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.21859, 0.025153, -1.92954e-05, 6.42745e-09, -7.83633e-13, 21229.5, 10.9538],
                Tmin = (543.079, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CBS-QB3 Calculation, Ryan Gillis 5/2017
""",
)

entry(
    index = 1,
    label = "C=S(O)[O]",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 S u0 p1 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {7,S}
4 O u1 p2 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.8411, 0.0108234, 0.000105105, -3.00353e-07, 2.36396e-10, -14984.4, 9.87259],
                Tmin = (10, 'K'),
                Tmax = (465.546, 'K'),
            ),
            NASAPolynomial(
                coeffs = [6.52732, 0.0174145, -1.17329e-05, 3.86273e-09, -4.8606e-13, -15556, -4.48646],
                Tmin = (465.546, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CBS-QB3 Calculation, Ryan Gillis 5/2017
""",
)

entry(
    index = 1,
    label = "[O-]O[S+](H)#C",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u0 p0 c+1 {2,S} {4,S} {5,T}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {3,T} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5,5,5,5,5,5,5],'cal/(mol*K)'),
        H298 = (50,'kcal/mol'),
        S298 = (20,'cal/(mol*K)','+|-',0.0007),
    ),
    shortDesc = u"""Arbitrary high thermo for an unstable species""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "[O-]O[S+](=O)=C",
    molecule =
"""
1 O u0 p3 c-1 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u0 p0 c+1 {2,S} {4,D} {5,D}
4 O u0 p2 c0 {3,D}
5 C u0 p0 c0 {3,D} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5,5,5,5,5,5,5],'cal/(mol*K)'),
        H298 = (50,'kcal/mol'),
        S298 = (20,'cal/(mol*K)','+|-',0.0007),
    ),
    shortDesc = u"""Arbitrary high thermo for an unstable species""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "C=S(=O)=O",
    molecule =
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 S u0 p0 c0 {1,D} {3,D} {4,D}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.94543, 0.00311211, 6.05764e-05, -1.15814e-07, 6.56678e-11, -19088.8, 8.49158],
                Tmin = (10, 'K'),
                Tmax = (593.934, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.45685, 0.0194573, -1.36739e-05, 4.5367e-09, -5.67612e-13, -19261, 8.65573],
                Tmin = (593.934, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CBS-QB3 Calculation, Ryan Gillis 5/2017
""",
)

entry(
    index = 1,
    label = "CSOOrad",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 S u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.595,21.737,23.387,24.748,27.026,28.814,31.606],'cal/(mol*K)'),
        H298 = (21.388,'kcal/mol'),
        S298 = (79.357,'cal/(mol*K)','+|-',0.0007),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
CBS-QB3 Calculation, Ryan Gillis 5/2017
""",
)


