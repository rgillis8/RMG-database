#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "CH3O2 <=> O2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.09e+14, 's^-1'), n=0.25, Ea=(33.3, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
)

entry(
    index = 2,
    label = "C2H5O2 <=> O2 + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.49e+21, 's^-1'), n=-2.41, Ea=(35.8, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
)

entry(
    index = 3,
    label = "C3H7O2 <=> O2 + C3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.52e+23, 's^-1'), n=-2.71, Ea=(36.4, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
)

entry(
    index = 4,
    label = "1-hydroxybutyl + O2 <=> 1-hydroxybutylO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.36e+12, 'cm^3/(mol*s)'),
        n = -0.085,
        Ea = (-567.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"""CBS-QB3 w/ 1-d HR""",
    longDesc = 
u"""
Reference: Low-Temperature Combustion Chemistry of n-Butanol: Principal Oxidation Pathways of Hydroxybutyl Radicals 
DOI: 10.1021/jp403792t
""",
)

entry(
    index = 5,
    label = "NO2 + NO2 <=> N2O4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.63e+08, 'm^3/(mol*s)', '+|-', 3.16e+07),
        n = -1.1,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (600, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (2.09e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["Borrell, P.", "Cobos, C.J.", "Luther, K."],
        title = u'Falloff curve and specific rate constants for the reaction NO2 + NO2 N2O4',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4377-4384""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988BOR/COB4377-4384:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 6,
    label = "NO + O2 <=> NO3",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (117000, 'm^3/(mol*s)', '*|/', -1),
        n = 0,
        Ea = (13.386, 'kJ/mol', '+|-', -0.001),
        T0 = (1, 'K'),
        Tmin = (473, 'K'),
        Tmax = (703, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (33600, 'Pa'),
    ),
    reference = Article(
        authors = ["Ashmore, P.G.", "Burnett, M.G."],
        title = u'Concurrent molecular and free radical mechanisms in the thermal decomposition of nitrogen dioxide',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "58",
        pages = """253""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962ASH/BUR253:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
Uncertainty: 3.0
Bath gas: NO2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 7,
    label = "NO2 + NO3-2 <=> N2O5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (366000, 'm^3/(mol*s)', '+|-', 57700),
        n = 0.2,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (400, 'K'),
        Pmin = (100000, 'Pa'),
        Pmax = (9e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["Hahn, J.", "Luther, K.", "Troe, J."],
        title = u'Experimental and Theoretical Study of the Temperature and Pressure Dependences of the Recombination Reactions O+NO2(+M)\u2192\x92NO3(+M) and NO2+NO3(+M)\u2192\x92N-2O5(+M)',
        journal = "Phys. Chem. Chem. Phys.",
        pages = """5098-5104""",
        year = "2000",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2000HAH/LUT5098-5104:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption

Theoretical modeling of k0, k and Fc=0.38 exp(-T/4900K) led to consistency with the experimental data.
""",
)

entry(
    index = 8,
    label = "NO2 + OH <=> HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.41e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Williams, C.F.", "Pogrebnya, S.K.", "Clary, D.C."],
        title = u'Quantum study on the branching ratio of the reaction NO2+OH',
        journal = "J. Chem. Phys.",
        volume = "126",
        pages = """154321""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007WIL/POG154321:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit

Quantum dynamics calculations. Reaction potential energy suraface was studied using quantum chemistry.
""",
)

entry(
    index = 9,
    label = "NO2-2 + OH <=> HNO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.205e+06, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Williams, C.F.", "Pogrebnya, S.K.", "Clary, D.C."],
        title = u'Quantum study on the branching ratio of the reaction NO2+OH',
        journal = "J. Chem. Phys.",
        volume = "126",
        pages = """154321""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007WIL/POG154321:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit
Reference reaction: 2007WIL/POG154321:4
Branching ration: 0.05
Quantum dynamics calculations. Reaction potential energy suraface was studied using quantum chemistry.
""",
)

entry(
    index = 10,
    label = "C5H5 + C2H5 <=> C7H10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: ethyl + CPDyl <=> ethylCPD
""",
)



entry(
    index = 15,
    label = "CH3NO2 <=> CH3 + NO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.88e+24, 's^-1'), n=-2.35, Ea=(62398, 'cal/mol'), T0=(1, 'K'), Tmin = (500, 'K'), Tmax = (3000, 'K')),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
R.S. Zhu, P. Raghunath, M.C. Lin, J. Phys. Chem. A, 2013, 117, 7308-7313, doi: 10.1021/jp401148q
p. 7311
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
The high pressure limit rate is giving here. A 1 atm rate is also available from the same source.

Also available (experimental) from:
P. Glarborg, A.B. Bendtsen, J.A. Miller
Nitromethane Dissociation: Implications for the CH3 + NO2 Reaction
International Journal of Chemical Kinetics Volume 31, Issue 9, pages 591–602, 1999
DOI: 10.1002/(SICI)1097-4601(1999)31:9<591::AID-KIN1>3.0.CO;2-E
    kinetics = Arrhenius(A=(1.8e+16, 's^-1'), n=0, Ea=(58500, 'cal/mol'), T0=(1, 'K')),
""",
)

entry(
    index = 16,
    label = "CN + CN <=> NCCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.251e+14, 'cm^3/(mol*s)'), n=0, Ea=(8020, 'cal/mol'), T0=(1, 'K'), Tmin = (2000, 'K'), Tmax = (4000, 'K')),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
See Table 1 on p. 2397 in L.V Moskaleva, M.C. Lin, Proceedings of the Combustion Institute, 2000, 28(2), 2393-2401, doi: 10.1016/S0082-0784(00)80652-9
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
In the original paper this reaction appears as "CN + NCN = (CN)2", which is not stoichiometric.
It is ASSUMED that the explicit dimer product is correct, and that the reactants are two CN rads.
""",
)

entry(
    index = 17,
    label = "CN + NCN <=> NCNCN",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.010e+09, 'cm^3/(mol*s)'), n=0, Ea=(-34691, 'cal/mol'), T0=(1, 'K'), Tmin = (2000, 'K'), Tmax = (4000, 'K')),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
See Table 1 on p. 2397 in L.V Moskaleva, M.C. Lin, Proceedings of the Combustion Institute, 2000, 28(2), 2393-2401, doi: 10.1016/S0082-0784(00)80652-9
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 18,
    label = "HNCN_r + OH <=> HONCNH",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100, 300, 760, 7600], 'torr'),
        arrhenius = [
            Arrhenius(A=(8.85e+35, 'cm^3/(mol*s)'), n=-9.02, Ea=(1304, 'cal/mol'), T0 = (1, 'K'), Tmin = (300, 'K'), Tmax = (3000, 'K')),
            Arrhenius(A=(6.26e+38, 'cm^3/(mol*s)'), n=-9.54, Ea=(2579, 'cal/mol'), T0 = (1, 'K'), Tmin = (300, 'K'), Tmax = (3000, 'K')),
            Arrhenius(A=(2.05e+41, 'cm^3/(mol*s)'), n=-9.95, Ea=(3768, 'cal/mol'), T0 = (1, 'K'), Tmin = (300, 'K'), Tmax = (3000, 'K')),
            Arrhenius(A=(5.49e+41, 'cm^3/(mol*s)'), n=-9.93, Ea=(3873, 'cal/mol'), T0 = (1, 'K'), Tmin = (300, 'K'), Tmax = (3000, 'K')),
            Arrhenius(A=(1.87e+43, 'cm^3/(mol*s)'), n=-10.25, Ea=(4660, 'cal/mol'), T0 = (1, 'K'), Tmin = (300, 'K'), Tmax = (3000, 'K')),
            Arrhenius(A=(2.46e+44, 'cm^3/(mol*s)'), n=-10.26, Ea=(5475, 'cal/mol'), T0 = (1, 'K'), Tmin = (300, 'K'), Tmax = (3000, 'K')),
        ],
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
k4 in S. Xu, M.C. Lin, J. Phys. Chem. A, 2007, 111, 6730-6740, doi: 10.1021/jp069038+
Done at the CCSD(T)/6-311+G(3df,2p)//B3LYP/6-311+G(3df,2p) level of theory
""",
)

entry(
    index = 19,
    label = "HNCN_p <=> H + NCN",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.79e+28, 'cm^3/(mol*s)'), n=-3.44, Ea=(64502, 'cal/mol'), T0 = (1, 'K'), Tmin = (2000, 'K'), Tmax = (4000, 'K'))),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
See Table 1 on p. 2397 in L.V Moskaleva, M.C. Lin, Proceedings of the Combustion Institute, 2000, 28(2), 2393-2401, doi: 10.1016/S0082-0784(00)80652-9
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 20,
    label = "N2H4 <=> NH2 + NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.57e+21, 's^-1'), n=-1.04, Ea=(66565, 'cal/mol'), T0=(1, 'K'), Tmin = (700, 'K'), Tmax = (2000, 'K')),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
P. Raghunath, N.T. Nghia, M.C. Lin, Advances in Quantum Chemistry, 2014, 69, 253-301, doi: 10.1016/B978-0-12-800345-9.00007-6
p. 264
calculations done at the RCCSD(T)/6-311þG(3df,2p)//B3LYP/6-311G(d,p) level of theoty
Only High Pressure Limit rate was taken; low limit and 1 atm rate are also available from the same source
""",
)

entry(
    index = 21,
    label = "N2H4 <=> N2H3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.57e+21, 's^-1'), n=-1.04, Ea=(66565, 'cal/mol'), T0=(1, 'K'), Tmin = (700, 'K'), Tmax = (2000, 'K')),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
P. Raghunath, N.T. Nghia, M.C. Lin, Advances in Quantum Chemistry, 2014, 69, 253-301, doi: 10.1016/B978-0-12-800345-9.00007-6
p. 264
calculations done at the RCCSD(T)/6-311þG(3df,2p)//B3LYP/6-311G(d,p) level of theoty
Only High Pressure Limit rate was taken; low limit and 1 atm rate are also available from the same source
""",
)

entry(
    index = 22,
    label = "ONONO2 <=> NO + NO3-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+21, 's^-1'), n=-1.76, Ea=(31535, 'cal/mol'), T0=(1, 'K'), Tmin = (700, 'K'), Tmax = (2000, 'K')),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
P. Raghunath, N.T. Nghia, M.C. Lin, Advances in Quantum Chemistry, 2014, 69, 253-301, doi: 10.1016/B978-0-12-800345-9.00007-6
p. 265
calculations done at the RCCSD(T)/6-311þG(3df,2p)//B3LYP/6-311G(d,p) level of theoty
Only High Pressure Limit rate was taken; low limit and 1 atm rate are also available from the same source
""",
)

entry(
    index = 23,
    label = "NH2NHNO <=> N2H3 + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.24e+15, 's^-1'), n=-0.15, Ea=(35611, 'cal/mol'), T0=(1, 'K'), Tmin = (250, 'K'), Tmax = (1500, 'K')),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
P. Raghunath, N.T. Nghia, M.C. Lin, Advances in Quantum Chemistry, 2014, 69, 253-301, doi: 10.1016/B978-0-12-800345-9.00007-6
p. 274
calculations done at the CCSD(T)/6-311þG(3df,2p) level of theoty
""",
)

entry(
    index = 24,
    label = "CH3ONO <=> CH3O + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+23, 's^-1'), n=-2.18, Ea=(41930, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (3000, 'K')),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
R.S. Zhu, P. Raghunath, M.C. Lin, J. Phys. Chem. A, 2013, 117, 7308-7313, doi: 10.1021/jp401148q
p. 7311
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
The high pressure limit rate is giving here. A 1 atm rate is akso available from the same source.
""",
)

entry(
    index = 25,
    label = "HSOO <=> SH + O2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.41e+18, 's^-1'), n=-1.07, Ea=(7750, 'cal/mol'), T0=(1, 'K'), Tmin = (200, 'K'), Tmax = (2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.56e+23, 'cm^3/(mol*s)'), n=-2.82, Ea=(-7450, 'cal/mol'), T0=(1, 'K'), Tmin = (200, 'K'), Tmax = (2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103(51), 11328–11335 doi: 10.1021/jp9924070
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
""",
)

entry(
    index = 26,
    label = "H + S2 <=> HSS",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.60e+24, 'cm^3/(mol*s)'), n=-2.613, Ea=(89173, 'cal/mol'), T0 = (1, 'K'), Tmin = (873, 'K'), Tmax = (1423, 'K')),
        efficiencies={'N#N': 1, 'S': 1.1, '[Ar]': 0.88, '[He]': 1.39}),
    rank = 3,
    shortDesc = u"""""",
    longDesc = 
u"""
K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
UNIMOL calculation
""",
)

entry(
    index = 27,
    label = "HSSH <=> SH + SH_r1",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.31e+14, 'cm^3/(mol*s)'), n=1, Ea=(57030, 'cal/mol'), T0 = (1, 'K'), Tmin = (873, 'K'), Tmax = (1423, 'K')),
        efficiencies={'N#N': 1, 'S': 1.1, '[Ar]': 0.88, '[He]': 1.39}),
    rank = 3,
    shortDesc = u"""""",
    longDesc = 
u"""
K. Sendt, M. Jazbec, B.S. Haynes, Proceedings of the Combustion Institute, 2002, 29, 2439-2446, doi: 10.1016/S1540-7489(02)80297-8
UNIMOL calculation
""",
)

entry(
    index = 28,
    label = "OH + NO2-2 <=> HOONO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.32e-06, 'cm^3/(mol*s)'), n=-0.24, Ea=(-200, 'cal/mol'), T0=(1, 'K'), Tmin = (200, 'K'), Tmax = (2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.14e+50, 'cm^6/(mol^2*s)'), n=-12.3, Ea=(5137, 'cal/mol'), T0=(1, 'K'), Tmin = (200, 'K'), Tmax = (2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    rank = 3,
    shortDesc = u"""""",
    longDesc = 
u"""
R.S. Zhu, M.C. Lin, J. Chem. Phys., 2003, 119, 10667, doi: 10.1063/1.1619373
""",
)

entry(
    index = 29,
    label = "S + NO <=> SNO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (800, 'K')),
        arrheniusLow = Arrhenius(A=(2.25e+15, 'cm^6/(mol^2*s)'), n=0, Ea=(-1868, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (800, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    rank = 1,
    shortDesc = u"""""",
    longDesc = 
u"""
A. Goumri, D.D. Shao, P. Marshall, J. Chem. Phys., 2004, 121, 9999, doi: 10.1063/1.1806419
Experimentally measured, and PES verified using CBS-QB3
""",
)

