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
    kinetics = Arrhenius(A=(1.82e+57, 'cm^3/(mol*s)'), n=-17.172, Ea=(14.7, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 3,
    label = "OH + DMS  <=> H2O + DMSrad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.80e+12, 'cm^3/(mol*s)'), n=0, Ea=(2.11, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 4,
    label = "O2 + DMSO2H <=> DMSO2 + OOH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(2.568e+7, 'cm^3/(mol*s)'), n=0.523, Ea=(14.42, 'kJ/mol'), T0=(1, 'K')), 
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019
""",
)

entry(
    index = 5,
    label = "OH + DMSO  <=> DMSO2H",
    degeneracy = 1,
   kinetics = Arrhenius(A=(7.23e+12, 'cm^3/(mol*s)'), n=0, Ea=(3, 'kJ/mol'), T0=(1, 'K')), 
    longDesc =
u"""
#Analogy to... 

Author(s):   Fulle, D.; Hamann, H.F.; Hippler, H.
Title:   The Pressure and Temperature Dependence of the Recombination Reaction HO· + SO2 + M → HOSO2· + M
Journal:   Phys. Chem. Chem. Phys.
""",
)

entry(
    index = 6,
    label = "O2 + DMSO2H  <=> DMSO4H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.14E+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
#Analogy to... 

Author(s):   Koch, L.C.; Marshall, P.; Ravishankara, A.R.
Title:   An investigation of the reaction of CH3S with CO
Journal:   J. Phys. Chem. A
Volume:   108
Page(s):   5205 - 5212
Year:   2004
""",
)

entry(
    index = 7,
    label = "CH3 + CS(=O)OH <=> DMSO2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.723e-06, 'cm^3/(mol*s)'), n=5.78, Ea=(130.188, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019
""",
)

entry(
    index = 8,
    label = "DMSO2 <=> CS(=O)Orad + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.14e+14, 's^-1'), n=0, Ea=(253, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Author(s):   Busfield, W.K.; Ivin, K.J.
Title:   The thermochemistry of some sulphones. Part 1. The kinetics of decomposition of dimethyl sulphone, benzyl methyl sulphone and allyl methyl sulphone. The dissociation energies of the bonds R-SO2CH3
Journal:   Trans. Faraday Soc.
Volume:   57
Page(s):   1044 - 1053
Year:   1961

Near the collision limit for the reverse reaction
""",
)

entry(
    index = 9,
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
    index = 10,
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
    index = 11,
    label = "MTF + CH3 <=> MTFrad + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.949e+10, 'cm^3/(mol*s)'), n=0, Ea=(37.66, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Thynne, J.C.j.; Reaction of alkyl radicals. Part 1. - Methyl radical photosensitized decomposition of ethyl formate, analogy from COC=O
""",
)

entry(
    index = 12,
    label = "MTF + OH <=> MTFrad + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.69e+10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Good and Jeong, 1999
""",
)

entry(
    index = 13,
    label = "CSrad + O2 <=> CSOOrad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39E+43, 'cm^3/(mol*s)'), n=-11.3, Ea=(24.69, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Bozelli high pressure number.
""",
)

entry(
    index = 14,
    label = "CSrad + O2 <=> CH2=S + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.25E+24, 'cm^3/(mol*s)'), n=-4.7, Ea=(34.73, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Bozelli high pressure number.
""",
)

entry(
    index = 15,
    label = "CSrad + O2 <=> CSOrad + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.19E+13, 'cm^3/(mol*s)'), n=-1.5, Ea=(70.71, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Bozelli high pressure number.
""",
)

entry(
    index = 16,
    label = "CSrad + O2 <=> CH3 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.77E+25, 'cm^3/(mol*s)'), n=-3.8, Ea=(51.5, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Bozelli high pressure number.
""",
)


entry(
    index = 17,
    label = "SO2 + CH3 <=> CS(=O)Orad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.547E+12, 'cm^3/(mol*s)'), n=0, Ea=(5.4, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Frank, A.J.; Turecek, F., Methylsulfonyl and Methoxysulfinyl Radicals and Cations in the Gas Phase. A Variable-Time and Photoexcitation Neutralization-Reionization Mass Spectrometric and ab Initio/RRKM Study, 
""",
)

entry(
    index = 18,
    label = "HOOC=O <=> H2O + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.14e+11, 's^-1'), n=0, Ea=(118.9, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Devush, S.S.; Prisyazhnyuk, Z.P.; Koval'skaya, A.M., Kinetics of the thermal gas phase decomposition of C1-C4 organic peracids, 1983 
""",
)

entry(
    index = 19,
    label = "CSCOOH + O2 <=> CSCOOrad + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+01, 'cm^3/(mol*s)'), n=3, Ea=(149.114, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

entry(
    index = 20,
    label = "DMS + OOH <=> DMSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.97e-04, 'cm^3/(mol*s)'), n=4.13, Ea=(49.92, 'kJ/mol'), T0=(1, 'K')), #my calculation
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

entry(
    index = 21,
    label = "DMSO + OOH <=> DMSO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.64e-03, 'cm^3/(mol*s)'), n=4.435, Ea=(28.68, 'kJ/mol'), T0=(1, 'K')), #my calculation
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

entry(
    index = 22,
    label = "DMSO + HOOH <=> DMSO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.538e-08, 'cm^3/(mol*s)'), n=5.955, Ea=(93.83, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

entry(
    index = 23,
    label = "DMSO + O2 <=> DMSO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.42e-25, 'cm^3/(mol*s)'), n=11.4, Ea=(201.8, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

entry(
    index = 24,
    label = "DMSOH + O2 <=> DMSO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e-43, 'cm^3/(mol*s)'), n=15.01, Ea=(7.75, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - m06-2x
""",
)

entry(
    index = 25,
    label = "DMSO3H2 <=> DMSO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.97e+10, 's^-1'), n=0.69, Ea=(13.48, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

entry(
    index = 26,
    label = "DMSOHOOH <=> DMSO3H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.24e+12, 's^-1'), n=0.53, Ea=(146.3, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

entry(
    index = 27,
    label = "DMSOHOO <=> DMSO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.24e+12, 's^-1'), n=0.53, Ea=(146.3, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculation by Ryan Gillis in July 2019 - CBS-QB3
""",
)

entry(
    index = 28,
    label = "DMSO4H <=> DMSO2 + OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.64e+12, 's^-1'), n=0.236, Ea=(48.08, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
my calculation
""",
)

