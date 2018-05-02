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

