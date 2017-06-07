#!/usr/bin/env python
# encoding: utf-8

name = "DMSOxy"
shortDesc = u""
longDesc = u"""
CBS-QB3 calculations of sulfur species by Ryan Gillis
"""

entry(
    index = 1,
    label = "CH3OOH",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.99152, 0.00032481, 4.32337e-05, -6.42217e-08, 3.10571e-11, -17462, 7.10521],
                Tmin = (10, 'K'),
                Tmax = (534.135, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.44062, 0.0194278, -1.0413e-05, 2.73613e-09, -2.82323e-13, -17189.5, 17.8121],
                Tmin = (534.135, 'K'),
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
    index = 2,
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
    index = 3,
    label = "MSOOrad",
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

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.63192, 0.0367425, -0.000103907, 1.97034e-07, -1.43355e-10, 8778.46, 9.18041],
                Tmin = (10, 'K'),
                Tmax = (424.086, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.51856, 0.0195672, -1.19878e-05, 3.53562e-09, -4.02249e-13, 8782.51, 6.5978],
                Tmin = (424.086, 'K'),
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
    index = 4,
    label = "MTF",
    molecule =
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 S u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.74684, 0.0253934, -4.73216e-05, 1.02947e-07, -8.57246e-11, -18404, 9.89795],
                Tmin = (10, 'K'),
                Tmax = (432.179, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.78775, 0.0251699, -1.49611e-05, 4.30628e-09, -4.8062e-13, -18236.1, 14.7036],
                Tmin = (432.179, 'K'),
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
    index = 5,
    label = "SCH",
    molecule =
"""
multiplicity 2
1 S u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.52985, -0.00244734, 2.14021e-05, -3.3594e-08, 1.74052e-11, 36983.7, 6.29231],
                Tmin = (10, 'K'),
                Tmax = (604.97, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.95954, 0.00425256, -2.47254e-06, 7.1867e-10, -8.15399e-14, 36999.1, 8.3141],
                Tmin = (604.97, 'K'),
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
    index = 6,
    label = "SCH2",
    molecule =
"""
1 S u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.05784, -0.00390443, 2.79775e-05, -3.36582e-08, 1.33135e-11, 12584.2, 4.81332],
                Tmin = (10, 'K'),
                Tmax = (767.659, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.23013, 0.00932641, -5.11947e-06, 1.37563e-09, -1.44573e-13, 12755.6, 12.4362],
                Tmin = (767.659, 'K'),
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
    index = 7,
    label = "CH3SCH3",
    molecule =
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 S u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.91,21.13,24.08,26.61,30.7,33.9,39.27],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-8.96,'kcal/mol','+|-',0.48),
        S298 = (69.68,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [5]""",
    longDesc =
u"""
Copied from SulfurLibrary
""",
)

entry(
    index = 8,
    label = "SO2",
    molecule =
"""
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.54,10.41,11.12,11.71,12.55,13.03,13.61],'cal/(mol*K)'),
        H298 = (-71.0,'kcal/mol'),
        S298 = (59.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
Copied from SOxNOx library
""",
)

entry(
    index = 9,
    label = "DMSO",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  S u0 p1 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.93179, 0.00591038, 0.000163061, -5.16828e-07, 5.39445e-10, -20056.3, 9.1764],
                Tmin = (10, 'K'),
                Tmax = (288.534, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.61003, 0.0326269, -1.94616e-05, 5.70774e-09, -6.53381e-13, -20015, 13.3048],
                Tmin = (288.534, 'K'),
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
    index = 10,
    label = "DMSO2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  S u0 p0 c0 {1,S} {3,D} {4,S} {11,D}
3  O u0 p2 c0 {2,D}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.88952, 0.00899965, 0.000169123, -4.99931e-07, 4.69338e-10, -47258.9, 9.2353],
                Tmin = (10, 'K'),
                Tmax = (335.713, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.62138, 0.0381212, -2.36009e-05, 7.10922e-09, -8.28608e-13, -47252.7, 12.7932],
                Tmin = (335.713, 'K'),
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
    index = 11,
    label = "COS",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,D}
2 S u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.81,10.8,11.6,12.21,13.03,13.51,14.12],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-35.96,'kcal/mol','+|-',0.25),
        S298 = (55.34,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Copied from Sulfur Library
""",
)

entry(
    index = 12,
    label = "OH(D)",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.954,6.946,6.951,6.973,7.08,7.251,7.719],'cal/(mol*K)'),
        H298 = (8.863,'kcal/mol'),
        S298 = (43.958,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
Copied from PrimaryThermoLibarry
""",
)

entry(
    index = 8,
    label = "H2O2",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.42,11.45,12.35,13.11,14.29,15.21,16.85],'cal/(mol*K)'),
        H298 = (-32.53,'kcal/mol'),
        S298 = (55.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.""",
    longDesc =
u"""
H2O2             120186 H   2O   2          G   298.00   5000.00  1000.00      1
 0.04573167E+02 0.04336136E-01-0.01474689E-04 0.02348904E-08-0.01431654E-12    2
-0.01800696E+06 0.05011370E+01 0.03388754E+02 0.06569226E-01-0.01485013E-05    3
-0.04625806E-07 0.02471515E-10-0.01766315E+06 0.06785363E+02                   4
""",
)




