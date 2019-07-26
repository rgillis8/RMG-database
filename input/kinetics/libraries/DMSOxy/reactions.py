#!/usr/bin/env python
# encoding: utf-8

name = "DMSOxy"
shortDesc = u"Dimethyl Sulfide Oxidation kinetic library"
longDesc = u"""
Created by Ryan Gillis
"""
entry(
    index = 1,
    label = "O2 + DMSOH <=> DMSO + OOH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Value at 298K reported by Ravishankara et al in "Reaction of OH with Dimethyl Sulfide. 2. Products and Mechanisms
""",
)

entry(
    index = 2,
    label = "OH + DMS  <=> DMSOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 3,
    label = "O2 + DMSO2H <=> DMSO2 + OOH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogy to value at 298K reported by Ravishankara et al in "Reaction of OH with Dimethyl Sulfide. 2. Products and Mechanisms
""",
)

entry(
    index = 4,
    label = "OH + DMSO  <=> DMSO2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogy to experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 5,
    label = "CH3 + CS(=O)OH <=> DMSO2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.723e-06, 'cm^3/(mol*s)'), n=5.78, Ea=(130.188, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

entry(
    index = 6,
    label = "CSCOOrad + CSCOOrad  <=> CSCOrad + CSCOrad + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.312e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
by comparison to HOCOO rates given in Atkinson, R.; Baulch, D.L.; Cox, R.A.; Crowley, J.N.; Hampson, R.F, Jr.; Kerr, J.A.; Rossi, M.J.; Troe, J.
Title: Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry reaction for COOrad + COOrad -> COrad + COrad + O2
""",
)

entry(
    index = 7,
    label = "CSCOOrad + CSCOOrad  <=> CSCOH + MTF + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.43E+10, 'cm^3/(mol*s)'), n=0, Ea=(-6.236, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
by comparison to HOCOO rates given in Atkinson, R.; Baulch, D.L.; Cox, R.A.; Crowley, J.N.; Hampson, R.F, Jr.; Kerr, J.A.; Rossi, M.J.; Troe, J.
Title: Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry reaction for COOrad + COOrad -> COrad + COrad + O2
""",
)

entry(
    index = 8,
    label = "MTF + CH3 <=> MTFrad + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.949e+10, 'cm^3/(mol*s)'), n=0, Ea=(37.66, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Thynne, J.C.j.; Reaction of alkyl radicals. Part 1. - Methyl radical photosensitized decomposition of ethyl formate, analogy from COC=O
""",
)

entry(
    index = 9,
    label = "MTF + OH <=> MTFrad + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.69e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Good and Jeong, 1999
""",
)

entry(
    index = 11,
    label = "CSrad + O2 <=> CSOOrad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39E+43, 'cm^3/(mol*s)'), n=-11.3, Ea=(24.69, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Bozelli high pressure number.
""",
)

entry(
    index = 12,
    label = "CSrad + O2 <=> CH2=S + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.25E+24, 'cm^3/(mol*s)'), n=-4.7, Ea=(34.73, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Bozelli high pressure number.
""",
)

entry(
    index = 13,
    label = "CSrad + O2 <=> CSOrad + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.19E+13, 'cm^3/(mol*s)'), n=-1.5, Ea=(70.71, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Bozelli high pressure number.
""",
)

entry(
    index = 14,
    label = "CSrad + O2 <=> CH3 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.77E+25, 'cm^3/(mol*s)'), n=-3.8, Ea=(51.5, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Bozelli high pressure number.
""",
)


entry(
    index = 15,
    label = "SO2 + CH3 <=> CS(=O)Orad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.547E+12, 'cm^3/(mol*s)'), n=0, Ea=(5.4, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Frank, A.J.; Turecek, F., Methylsulfonyl and Methoxysulfinyl Radicals and Cations in the Gas Phase. A Variable-Time and Photoexcitation Neutralization-Reionization Mass Spectrometric and ab Initio/RRKM Study, 
""",
)

entry(
    index = 16,
    label = "HOOC=O <=> H2O + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.14e+11, 's^-1'), n=0, Ea=(118.9, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Devush, S.S.; Prisyazhnyuk, Z.P.; Koval'skaya, A.M., Kinetics of the thermal gas phase decomposition of C1-C4 organic peracids, 1983 
""",
)

entry(
    index = 17,
    label = "CSCOOH + O2 <=> CSCOOrad + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+01, 'cm^3/(mol*s)'), n=3, Ea=(149.114, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

