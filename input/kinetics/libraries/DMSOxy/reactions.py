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
    label = "O2 + DMSO2H <=> DMSO2 + OOH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to value at 298K reported by Ravishankara et al in "Reaction of OH with Dimethyl Sulfide. 2. Products and Mechanisms
""",
)

entry(
    index = 3,
    label = "O2 + CS(OH)OH <=> CS(=O)OH + OOH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to value at 298K reported by Ravishankara et al in "Reaction of OH with Dimethyl Sulfide. 2. Products and Mechanisms
""",
)

entry(
    index = 4,
    label = "O2 + CS(OH)OOH <=> CS(=O)OOH + OOH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to value at 298K reported by Ravishankara et al in "Reaction of OH with Dimethyl Sulfide. 2. Products and Mechanisms
""",
)

entry(
    index = 5,
    label = "O2 + CS(OH)OO <=> CS(=O)OO + OOH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to value at 298K reported by Ravishankara et al in "Reaction of OH with Dimethyl Sulfide. 2. Products and Mechanisms
""",
)

entry(
    index = 6,
    label = "OH + DMS  <=> DMSOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 7,
    label = "OH + DMSO  <=> DMSO2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 8,
    label = "OH + CSOH  <=> CS(OH)OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 9,
    label = "OH + CSOOH  <=> CS(OH)OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 10,
    label = "OH + CSOOrad  <=> CS(OH)OO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 11,
    label = "OH + CSOrad  <=> CS(=O)OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 20,
    label = "CSrad + CradS(=O)OOH  <=> CH2=S + CS(=O)OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.91e+12, 'cm^3/(mol*s)'), n=2.93, Ea=(100.3, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to experimentally observed by Atkinson at 298K
""",
)

entry(
    index = 21,
    label = "CS(=O)OOH <=> CS(=O)Orad + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+13, 's^-1'), n=0, Ea=(42.9, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to experimentally observed by Atkinson at 298K
""",
)

#entry(
#    index = 11,
#    label = "O2 + CSrad  <=> OOH + CH2=S",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(5.91e+12, 'cm^3/(mol*s)'), n=2.93, Ea=(100.3, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#From Bozelli and Zhu, 2006
#""",
#)

#entry(
#    index = 3,
#    label = "CSrad + OOH  <=> CSOOH",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(3.104e+14, 'cm^3/(mol*s)'), n=0, Ea=(-6.753, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - CSrad + OOH - Rxn #1
#Calculated at CBS-QB3 with pdep and fitted to Arrhenius parameters for 260K to 310K by Ryan Gillis
#""",
#)

#entry(
#    index = 4,
#    label = "CSOOH  <=> CS(=O)OH",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(1.964e+12, 's^-1'), n=0, Ea=(40.945, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - CSrad + OOH - Rxn #2
#Calculated at CBS-QB3 with pdep and fitted to Arrhenius parameters for 260K to 310K by Ryan Gillis
#""",
#)

#entry(
#    index = 5,
#    label = "CSrad + OOH  <=> CS(=O)OH",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(1.773e+17, 'cm^3/(mol*s)'), n=0, Ea=(-5.577, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - CSrad + OOH - Rxn #3
#Calculated at CBS-QB3 with pdep and fitted to Arrhenius parameters for 260K to 310K by Ryan Gillis
#""",
#)

#entry(
#    index = 6,
#    label = "CSrad + O2  <=> CSOOrad",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(5.5709e+8, 'cm^3/(mol*s)'), n=0, Ea=(-9.35, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - CSrad + OO - Rxn #1
#Calculated at CBS-QB3 by Ryan Gillis - Calculated separate from the rest of the Pdep system
#""",
#)

#entry(
#    index = 7,
#    label = "CSOOrad  <=> CS(=O)Orad",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(4.67589e+10, 's^-1'), n=0.510239, Ea=(65.5504, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - CSrad + OO - Rxn #2
#Calculated at CBS-QB3 by Ryan Gillis
#""",
#)

#entry(
#    index = 8,
#    label = "CSrad + O2  <=> CS(=O)Orad",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(6.081e+14, 'cm^3/(mol*s)'), n=0, Ea=(35.65, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - CSrad + OO - Rxn #3
#Calculated at CBS-QB3 by Ryan Gillis
#""",
#)

entry(
    index = 12,
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
    index = 13,
    label = "CSCOOrad + CSCOOrad  <=> CSCOH + MTF + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.43E+10, 'cm^3/(mol*s)'), n=0, Ea=(-6.236, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
by comparison to HOCOO rates given in Atkinson, R.; Baulch, D.L.; Cox, R.A.; Crowley, J.N.; Hampson, R.F, Jr.; Kerr, J.A.; Rossi, M.J.; Troe, J.
Title: Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry reaction for COOrad + COOrad -> COrad + COrad + O2
""",
)

#entry(
#    index = 11,
#    label = "DMSOH + OOH  <=> DMSOHOOH",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(2.67e+13, 'cm^3/(mol*s)'), n=0, Ea=(-1.66, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - DMSOH + OOH - Rxn #1
#Calculated at CBS-QB3 by Ryan Gillis
#""",
#)

#entry(
#    index = 12,
#    label = "DMSOH + OOH  <=> DMSO2 + H2O",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(6.074e+12, 'cm^3/(mol*s)'), n=0, Ea=(8.24, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - DMSOH + OOH - Rxn #2
#Calculated at CBS-QB3 by Ryan Gillis
#""",
#)

#entry(
#    index = 13,
#    label = "DMSOH + O2  <=> DMSOHOO",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(2.67e+13, 'cm^3/(mol*s)'), n=0, Ea=(-1.66, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - DMSOH + OOH - Rxn #1
#Calculated at CBS-QB3 by Ryan Gillis
#""",
#)

#entry(
#    index = 14,
#    label = "DMSOH + O2  <=> DMSO2 + OH",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(6.074e+12, 'cm^3/(mol*s)'), n=0, Ea=(8.24, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Pdep System - DMSOH + OOH - Rxn #2
#Calculated at CBS-QB3 by Ryan Gillis
#""",
#)

#Test reaction
entry(
    index = 15,
    label = "SO2 + CH3 <=> CS(=O)Orad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.11975e+3, 'cm^3/(mol*s)'), n=2.94, Ea=(5.69, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Previous RMG estimate for the rate of this reaction
""",
)
