#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "HNNO <=> O + NNH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.79e+28, 'cm^3/(mol*s)'), n=-3.44, Ea=(64502, 'cal/mol'), T0 = (1, 'K'))),
    rank = 3,
    shortDesc = u"""""",
    longDesc = 
u"""
Taken from the SOxNOx library
Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen, in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341, doi: 10.1007/978-1-4612-1310-9_2
2.6.3, p. 158, and Table 2.6 on p. 163
""",
)

entry(
    index = 2,
    label = "HSOO <=> HSO + O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.01e+19, 's^-1'), n=-1.07, Ea=(28377, 'cal/mol'), T0=(1, 'K'), Tmin = (200, 'K'), Tmax = (2000, 'K')),
        arrheniusLow = Arrhenius(A=(9.27e+34, 'cm^3/(mol*s)'), n=-5.87, Ea=(30960, 'cal/mol'), T0=(1, 'K'), Tmin = (200, 'K'), Tmax = (2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
Taken from the SOxNOx library, Part of the "SOx" subset
T range: 200-2000 K
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103(51), 11328–11335 doi: 10.1021/jp9924070
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
""",
)

entry(
    index = 3,
    label = "NO2_p <=> NO + O",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.98e+14, 's^-1'), n=0, Ea=(71700, 'cal/mol'), T0=(1, 'K'), Tmin = (1350, 'K'), Tmax = (2100, 'K')),
        arrheniusLow = Arrhenius(A=(3.98e+15, 'cm^3/(mol*s)'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K'), Tmin = (1350, 'K'), Tmax = (2100, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    rank = 1,
    shortDesc = u"""""",
    longDesc = 
u"""
Taken from the SOxNOx library, Part of the "NO2 decomposition" subset
T range: 1350-2100 K
M. Rohrig, E.L. Petersen, D.F. Davidson, R.K. Hanson, Int. J. Chem. Kin., 1997, 29(7), 483-493, doi: 10.1002/(SICI)1097-4601(1997)29:7<483::AID-KIN2>3.0.CO;2-Q
Shock tube measurement
""",
)

entry(
    index = 4,
    label = "NH + NO2_c-res_r <=> HNNO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.42e+16, 'cm^3/(mol*s)'), n=-0.75, Ea=(1226, 'cal/mol'), T0=(1, 'K'), Tmin = (500, 'K'), Tmax = (3000, 'K')),
        arrheniusLow = Arrhenius(A=(0, 'cm^6/(mol^2*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
    rank = 3,
    shortDesc = u"""""",
    longDesc = 
u"""
Part of the "NOx" subset
T range: 500-3000 K
calculations done at the B3LYP/6-311D(d,p)//B3LYP/6-311D(d,p) level of theory
No stabilization at low pressures
""",
)

