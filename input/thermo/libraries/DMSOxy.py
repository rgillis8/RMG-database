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
                coeffs = [3.63192, 0.0367425, -0.000103907, 1.97034e-07, -1.43355e-10, 8778.46, 10.5667],
                Tmin = (10, 'K'),
                Tmax = (424.086, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.51856, 0.0195672, -1.19878e-05, 3.53562e-09, -4.02249e-13, 8782.51, 7.9841],
                Tmin = (424.086, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (72.9793, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (157.975, 'J/(mol*K)'),
    ),
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
11 O u0 p2 c0 {2,D}
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


entry(
    index = 20,
    label = "SO2precursor",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 S u0 p1 c0 {1,S} {6,S} {7,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
7 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
	polynomials = [
            NASAPolynomial(
                coeffs = [3.92389, 0.0055321, 8.71223e-05, -2.26325e-07, 1.79812e-10, -28341.4, 9.8581],
                Tmin = (10, 'K'),
                Tmax = (413.469, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.43131, 0.0218522, -1.40037e-05, 4.31702e-09, -5.10543e-13, -28399.4, 10.6051],
                Tmin = (413.469, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-235.644, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (157.975, 'J/(mol*K)'),
    ),
)

entry(
    index = 21,
    label = "OSC",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 S u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
       polynomials = [
            NASAPolynomial(
                coeffs = [3.89857, 0.00877916, 1.32559e-05, -2.51593e-08, 1.18525e-11, -10548.6, 8.814],
                Tmin = (10, 'K'),
                Tmax = (703.398, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.15581, 0.016169, -9.25458e-06, 2.57471e-09, -2.78966e-13, -10522.5, 11.5793],
                Tmin = (703.398, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-87.7171, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
)

entry(
    index = 22,
    label = "CSO3H3",
    molecule =
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 S u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.80553, 0.0242755, 0.000234481, -1.99675e-06, 4.51857e-09, -21026, 11.3853],
                Tmin = (10, 'K'),
                Tmax = (165.716, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.92031, 0.0246605, -1.60508e-05, 4.98533e-09, -5.91868e-13, -21100.4, 6.8802],
                Tmin = (165.716, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-173.891, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (182.918, 'J/(mol*K)'),
    ),
)

entry(
    index = 22,
    label = "C2SO3H6",
    molecule =
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  S u0 p1 c0 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.43199, 0.0457443, -3.45576e-05, 1.40476e-08, -2.41672e-12, -32113.8, 11.6013],
                Tmin = (10, 'K'),
                Tmax = (1229.45, 'K'),
            ),
            NASAPolynomial(
                coeffs = [7.94267, 0.0310687, -1.66524e-05, 4.33854e-09, -4.42426e-13, -33222.9, -11.0918],
                Tmin = (1229.45, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-267.079, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (282.692, 'J/(mol*K)'),
    ),
)

entry(
    index = 23,
    label = "S6dssss-OdOCCH",
    molecule =
"""
multiplicity 2
1 S u0 p0 c0 {2,S} {3,S} {4,S} {5,D} {6,S}
2 C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4 O u1 p2 c0 {1,S}
5 O u0 p2 c0 {1,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.74817, 0.0248086, 9.21681e-05, -3.65068e-07, 4.44095e-10, 1978.07, 10.9225],
                Tmin = (10, 'K'),
                Tmax = (209.134, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.89711, 0.0410864, -2.45821e-05, 7.09902e-09, -7.92502e-13, 2013.66, 13.6967],
                Tmin = (209.134, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (16.4667, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (282.692, 'J/(mol*K)'),
    ),
)

entry(
    index = 24,
    label = "CSCOO",
    molecule =
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  S u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.7963, 0.0247435, -1.61177e-06, -8.88917e-09, 3.44328e-12, -14209.3, 10.5323],
                Tmin = (10, 'K'),
                Tmax = (1195.9, 'K'),
            ),
            NASAPolynomial(
                coeffs = [6.70867, 0.0237358, -1.1302e-05, 2.61922e-09, -2.3906e-13, -15530.4, -6.65025],
                Tmin = (1195.9, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-118.14, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (241.12, 'J/(mol*K)'),
    ),
)

entry(
    index = 25,
    label = "CSHOradC",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  S u0 p1 c0 {1,S} {3,S} {4,S} {5,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.87896, 0.0103026, 0.000151354, -4.31958e-07, 3.92813e-10, 7735.33, 10.217],
                Tmin = (10, 'K'),
                Tmax = (335.316, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.23162, 0.0398857, -2.54112e-05, 7.81488e-09, -9.23372e-13, 7789.97, 15.5319],
                Tmin = (335.316, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (64.3357, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (257.749, 'J/(mol*K)'),
    ),
)

entry(
    index = 26,
    label = "C=S=C",
    molecule =
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 S u0 p1 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.9432, 0.00330695, 6.73601e-05, -1.30025e-07, 7.56087e-11, 25508.3, 6.65103],
                Tmin = (10, 'K'),
                Tmax = (573.43, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.30981, 0.0209777, -1.35302e-05, 4.32035e-09, -5.33479e-13, 25363.1, 7.45466],
                Tmin = (573.43, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (212.064, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (157.975, 'J/(mol*K)'),
    ),
)

entry(
    index = 27,
    label = "CSCOOO",
    molecule =
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  S u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.83721, 0.0194302, 0.000339273, -2.04557e-06, 3.91122e-09, -11955.2, 10.9547],
                Tmin = (10, 'K'),
                Tmax = (171.082, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.60492, 0.0430939, -2.80626e-05, 8.78574e-09, -1.05321e-12, -11974, 10.8854],
                Tmin = (171.082, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-98.843, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (282.692, 'J/(mol*K)'),
    ),
)

entry(
    index = 28,
    label = "CSOC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  S u0 p2 c0 {1,S} {3,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
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
                coeffs = [3.78704, 0.0175339, 1.24907e-05, -2.30791e-08, 8.86528e-12, -15550.2, 9.38601],
                Tmin = (10, 'K'),
                Tmax = (905.112, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.3451, 0.0291955, -1.56012e-05, 4.0685e-09, -4.16424e-13, -15505.8, 15.0019],
                Tmin = (905.112, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-129.311, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (224.491, 'J/(mol*K)'),
    ),
)

entry(
    index = 28,
    label = "CSCOrad",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 S u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 O u1 p2 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.63738, 0.0359084, -7.85075e-05, 1.53425e-07, -1.16623e-10, 3102.87, 10.5193],
                Tmin = (10, 'K'),
                Tmax = (438.068, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.29985, 0.0284618, -1.69582e-05, 4.89316e-09, -5.47361e-13, 3233.47, 13.0222],
                Tmin = (438.068, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (25.7889, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (207.862, 'J/(mol*K)'),
    ),
)

entry(
    index = 28,
    label = "CSOOH",
    molecule =
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 S u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 O u0 p2 c0 {3,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.80926, 0.0183388, 0.000115892, -5.6455e-07, 7.44462e-10, -11219.6, 9.56715],
                Tmin = (10, 'K'),
                Tmax = (276.442, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.8415, 0.0228752, -1.43819e-05, 4.4271e-09, -5.26755e-13, -11351.1, 4.56863],
                Tmin = (276.442, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-93.2646, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (182.918, 'J/(mol*K)'),
    ),
)

entry(
    index = 29,
    label = "CSOH",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 S u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.97221, 0.00197535, 6.79005e-05, -1.5612e-07, 1.17147e-10, -17184, 8.29951],
                Tmin = (10, 'K'),
                Tmax = (396.386, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.76058, 0.0184629, -1.06156e-05, 3.05187e-09, -3.45934e-13, -17121.5, 12.6015],
                Tmin = (396.386, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-142.875, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (149.66, 'J/(mol*K)'),
    ),
)

entry(
    index = 21,
    label = "OSrad=O",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 S u1 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
       polynomials = [
            NASAPolynomial(
                coeffs = [3.89857, 0.00877916, 1.32559e-05, -2.51593e-08, 1.18525e-11, -10548.6, 8.814],
                Tmin = (10, 'K'),
                Tmax = (703.398, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.15581, 0.016169, -9.25458e-06, 2.57471e-09, -2.78966e-13, -10522.5, 11.5793],
                Tmin = (703.398, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-87.7171, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
)

entry(
    index = 21,
    label = "CS=OOOH",
    molecule =
"""
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 S u0 p1 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {5,S}
5 O u0 p2 c0 {4,S} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.7838, 0.0169979, 0.000137784, -4.68603e-07, 4.43361e-10, -29999.6, 10.2455],
                Tmin = (10, 'K'),
                Tmax = (380.316, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.56092, 0.027407, -1.80428e-05, 5.73903e-09, -6.97956e-13, -30345.3, 0.623152],
                Tmin = (380.316, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-249.414, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (207.862, 'J/(mol*K)'),
    ),
)

entry(
    index = 21,
    label = "S6ddd-OdOdCd",
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
        E0 = (-158.737, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (133.032, 'J/(mol*K)'),
    ),
)

entry(
    index = 21,
    label = "CSOOC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  S u0 p2 c0 {1,S} {3,S}
3  O u0 p2 c0 {2,S} {4,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.50097, 0.047325, -8.83228e-05, 1.42709e-07, -9.51965e-11, -11351.1, 11.4932],
                Tmin = (10, 'K'),
                Tmax = (470.347, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.84555, 0.0352917, -2.09167e-05, 6.02085e-09, -6.72927e-13, -11282.8, 11.1611],
                Tmin = (470.347, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-94.3968, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (257.749, 'J/(mol*K)'),
    ),
)
