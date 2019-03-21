#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
entry(
    index = 0,
    label = "X_H_or_Xrad_H_Xbirad_H_Xtrirad_H;Y_rad_birad_trirad_quadrad",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""
If a biradical CH2JJ can abstract from RCH4 to make RCH3J and CH3J 
then a Y_rad CH3J should be able to abstract from RCH3J which means X_H needs 
to include Xrad_H. I.e. you can abstract from a radical. To make this possible
a head node has been created X_H_or_Xrad_H which is a union of X_H and Xrad_H.
The kinetics for it have just been copied from X_H and are only defined for 
abstraction by Y_rad_birad. I.e. the top level very approximate guess.

Do better kinetics for this exist? Do we in fact use the reverse kinetics anyway?
""",
)

entry(
    index = 1,
    label = "X_H;Y_rad_birad_trirad_quadrad",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 7046,
    label = "CO/H/NonDeO;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (6.99e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (.11, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""""",
    longDesc = """
Analogous to Habs from Author(s):   Thynne, J.C.J.; Gray, P.
Title:   The reactions of methoxyl radicals with methyl formate; comparisons between alkoxyl and alkyl
Journal:   Proc. Chem. Soc. London

Author(s):   Good, D.A.; Francisco, LJ.S.
Title:   A Computational Study of the Reaction of Methyl Formate with H and CH3 Radicals
Journal:   J. Phys. Chem. A
""",
)



entry(
    index = 7047,
    label = "O/H/OneDeS;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (9.03e+09, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""""",
    longDesc = """
Author(s):   Anglada, J.M.;Olivella, S.;Sole, A.
Title:   Hydrogen transfer between sulfuric acid and hydroxyl radical in the gas phase: Competition among hydrogen atom transfer, proton-coupled electron-transfer, and double proton transfer
Journal:   J. Phys. Chem. A
""",
)
