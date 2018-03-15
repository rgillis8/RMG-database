#!/usr/bin/env python
# encoding: utf-8

name = "DMSOxy"
shortDesc = u"Dimethyl Sulide Oxidation library"
longDesc = u"""
Created by Ryan Gillis
"""

entry(
    index = 1,
    label = "O2 + DMSOH <=> DMSO + HO2",
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
    label = "OH + DMSO  <=> DMSO2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
From comparison to the experimentally observed by Atkinson at 298K for OH + DMSO
""",
)

entry(
    index = 4,
    label = "CSOOH  <=> OH + CSOrad",
    degeneracy = 1,
#    kinetics = Arrhenius(A=(5.74e+1, 's^-1'), n=0, Ea=(99.807, 'kJ/mol'), T0=(1, 'K')),
    kinetics = Arrhenius(A=(5.74e+11, 's^-1'), n=0, Ea=(33.807, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Ryan Gillis pdep calculations
""",
)

entry(
    index = 5,
    label = "OH + CSOOH  <=> CS(OH)OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
From comparison to the experimentally observed by Atkinson at 298K for OH + DMSO
""",
)

entry(
    index = 6,
    label = "CSOOrad  <=> CS(=O)Orad",
    degeneracy = 1,
#    kinetics = Arrhenius(A=(4.67589e+10, 's^-1'), n=0.510239, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    kinetics = Arrhenius(A=(4.67589e+10, 's^-1'), n=0.510239, Ea=(65.5504, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculated at CBS-QB3 by Ryan Gillis
""",
)

entry(
    index = 7,
    label = "CSOOH  <=> CS(=O)OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.964e+12, 's^-1'), n=0, Ea=(40.945, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculated at CBS-QB3 with pdep and fitted to Arrhenius parameters for 260K to 310K by Ryan Gillis
""",
)

entry(
    index = 8,
    label = "CSrad + OOH  <=> CS(=O)OH",
    degeneracy = 1,
#    kinetics = Arrhenius(A=(5.82e+9, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    kinetics = Arrhenius(A=(1.773e+17, 'cm^3/(mol*s)'), n=0, Ea=(-5.577, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculated at CBS-QB3 with pdep and fitted to Arrhenius parameters for 260K to 310K by Ryan Gillis
""",
)

entry(
    index = 9,
    label = "CSrad + O2  <=> CS(=O)Orad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6081212881, 'cm^3/(mol*s)'), n=0, Ea=(35.647, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculated at CBS-QB3 with pdep and fitted to Arrhenius parameters for 260K to 310K by Ryan Gillis
""",
)

entry(
    index = 10,
    label = "CSCOOrad + DMS  <=> DMSO + CSCOrad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.45722, 'cm^3/(mol*s)'), n=3.45093, Ea=(84.1291, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Calculated at b3lyp/6-31g** by Ryan Gillis
""",
)

entry(
    index = 11,
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
    index = 12,
    label = "CSCOOrad + CSCOOrad  <=> CSCOH + MTF + O2",
    degeneracy = 1,
#    kinetics = Arrhenius(A=(1.5E+25, 'cm^3/(mol*s)'), n=0, Ea=(9.728, 'kJ/mol'), T0=(1, 'K')),
    kinetics = Arrhenius(A=(3.43E+10, 'cm^3/(mol*s)'), n=0, Ea=(-6.236, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
by comparison to HOCOO rates given in Atkinson, R.; Baulch, D.L.; Cox, R.A.; Crowley, J.N.; Hampson, R.F, Jr.; Kerr, J.A.; Rossi, M.J.; Troe, J.
Title: Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry reaction for COOrad + COOrad -> COrad + COrad + O2
""",
)

entry(
    index = 13,
    label = "CSOrad  <=> CSrad=O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1E+10, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Sulfur resonance reaction
""",
)

entry(
    index = 14,
    label = "CSrad + COOrad  <=> CSOOC",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8E+06, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Experimental rate of OO + CSrad at 298. DeMore 1997 JPL Publications.
""",
)

entry(
    index = 15,
    label = "CSrad + CHO3rad  <=> CSOOC=O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8E+06, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Experimental rate of OO + CSrad at 298. DeMore 1997 JPL Publications.
""",
)

entry(
    index = 16,
    label = "CSrad + CSCOOrad  <=> S=CH2 + CSCOO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.91E10, 'cm^3/(mol*s)'), n=2.93, Ea=(102926, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
Author(s):   Zhu, L.; Bozzelli, J.W.
Title:   Kinetics of the multichannel reaction of methanethiyl radical (CH3S center dot) with O-3(2) - Pressure Independent
Journal:   J. Phys. Chem. A
""",
)

entry(
    index = 17,
    label = "DMSOH + O2 <=> DMSO3H",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.68E+13, 'cm^3/(mol*s)'), n=-0.06, Ea=(7.11, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
RMG group additivity estimate for this reaction.
""",
)

entry(
    index = 18,
    label = "S4s-OsradOsCsCs <=> S6drad-OdOsCsCs",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1E+15, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
In place of a resonance rule.
""",
)

entry(
    index = 19,
    label = "S4s-OsradOHCsCs <=> S6drad-OdOHCsCs",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1E+15, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
In place of a resonance rule.
""",
)

entry(
    index = 20,
    label = "CHOrad + CS(=O)OH <=> CS(=O)Orad + O=CH2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.81e+14, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to CHOrad disprop to form DMSO. Test in this case, if my hypothesis is correct.
""",
)

entry(
    index = 21,
    label = "COOrad + CS(=O)OH <=> CS(=O)Orad + COOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-13.7, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to Habs from O/H/OneDeN which is the closest implemented group.
""",
)

entry(
    index = 22,
    label = "MTF + COOrad <=> MTFrad + COOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.024e+13, 'cm^3/(mol*s)'), n=0, Ea=(34.3, 'kJ/mol'), T0=(1, 'K')),
    longDesc =
u"""
Analogous to Habs from Author(s):   Thynne, J.C.J.; Gray, P.
Title:   The reactions of methoxyl radicals with methyl formate; comparisons between alkoxyl and alkyl
Journal:   Proc. Chem. Soc. London
""",
)

entry(
    index = 23,
    label = "DMSOH + OOH <=> DMSO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.074e+12, 'cm^3/(mol*s)'), n=0, Ea=(8.24, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
Ryan Gillis calculated pdep reaction.
""",
)

entry(
    index = 24,
    label = "DMSOH + O2 <=> DMSO2 + OH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(6.074e+12, 'cm^3/(mol*s)'), n=0, Ea=(8.24, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
Ryan Gillis calculated pdep reaction for DMSOH + OOH.
""",
)

entry(
    index = 25,
    label = "CSrad + OOH <=> CSOOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.97e+6, 'cm^3/(mol*s)'), n=0, Ea=(-1.34, 'kJ/mol'), T0=(298, 'K')),
    longDesc =
u"""
Ryan Gillis calculated pdep reaction.
""",
)


#entry(
#    index = 20,
#    label = "COOrad + CS(=O)OH <=> CS(=O)Orad + COOH",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(6.495e-04, 'cm^3/(mol*s)'), n=4.95, Ea=(2.37, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Test the one of the rate rules and if my hypothesis is correct.
#""",
#)

#entry(
#    index = 20,
#    label = "O2 + CS(=O)OH <=> SO2 + CH3 + OOH",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Analogous to O2 + DMSOH going to DMSO and peroxy radical. Test in this case, if my hypothesis is correct.
#""",
#)

#entry(
#    index = 19,
#    label = "DMSOH + OOH <=> DMSO2 + H2O",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(1E+20, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#Test to see if equilbrium along this pathway makes sense
#""",
#)

#entry(
#    index = 13,
#    label = "CSCOO  <=> CSCOrad + OH",
#    degeneracy = 1,
#   kinetics = Arrhenius(A=(2e+15, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Ryan Gillis test
#""",
#)

#entry(
#    index = 10,
#    label = "HOOH  <=> OH + OH",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(3.125e-0, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
#    longDesc =
#u"""
#Fitted to the degradation rate.
#""",
#)

#entry(
#    index = 3,
#    label = "OH + DMSO  <=> DMSO2H",
#    degeneracy = 1,
#    kinetics = Arrhenius(A=(126020, 'cm^3/(mol*s)'), n=2.38788, Ea=(-31.4797, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#Ryan calculated at b3lyp/3-21g
#""",
#)

#entry(
#    index = 4,
#    label = "O2 + DMSO2H <=> DMSO2 + HO2",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(3.01e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#""",
#)

#entry(
#    index = 5,
#    label = "CSCOO + OH <=> CSCradOO + H2O",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(4.31e+4, 'cm^3/(mol*s)'), n=2.6, Ea=(-7.271, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#""",
#)

#entry(
#    index = 6,
#    label = "CSCOO + O2 <=> CSCradOO + HO2",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(4.31e+4, 'cm^3/(mol*s)'), n=2.6, Ea=(-7.271, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#""",
#)

#entry(
#    index = 7,
#    label = "CSCradOO <=> CSC=O + OH",
#    degeneracy = 2,
#    kinetics = Arrhenius(A=(4.31e+4, 'cm^3/(mol*s)'), n=2.6, Ea=(-7.271, 'kJ/mol'), T0=(298, 'K')),
#    longDesc =
#u"""
#""",
#)

