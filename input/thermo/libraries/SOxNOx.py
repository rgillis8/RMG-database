#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u"SOxNOx"
longDesc = u"""

"""

entry(
    index = 1,
    label = "HOSH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([49.66,56.19,60.09,64.27,68.62,71.38,75.68],'J/(mol*K)'),
        H298 = (-236.3,'kJ/mol'),
        S298 = (270.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
UMP2=full/6-31G+
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall
The Journal of Chemical Physics 101, 9405 (1994); doi: http://dx.doi.org/10.1063/1.467971
As reported by: M.U. Alzueta, R. Bilbao, P. Glarborg, Comb. Flame, 2001, 127(4) 2234-2251, doi: 10.1016/S0010-2180(01)00325-X 
""",
)

entry(
    index = 4,
    label = "SO",
    molecule = 
"""
multiplicity 3
1 S u2 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.22,7.55,7.84,8.08,8.43,8.62,8.95],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (53.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
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
""",
)

entry(
    index = 4,
    label = "SO3",
    molecule = 
"""
1 S u0 p0 c0 {2,D} {3,D} {4,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.17,13.76,15.05,16.07,17.45,18.16,19.02],'cal/(mol*K)'),
        H298 = (-94.6,'kcal/mol'),
        S298 = (61.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
    label = "HSO",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.02,9.93,10.73,11.36,12.22,12.73,13.34],'cal/(mol*K)'),
        H298 = (-5.4,'kcal/mol'),
        S298 = (57.80,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
    label = "HOS",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.71,9.42,10.00,10.45,11.08,11.53,12.33],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (57.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
    label = "H2SO",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.53,11.13,12.66,13.95,15.82,17.00,18.44],'cal/(mol*K)'),
        H298 = (-11.3,'kcal/mol'),
        S298 = (57.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
    label = "HOSO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.87,13.43,14.56,15.36,16.40,17.06,18.09],'cal/(mol*K)'),
        H298 = (-57.7,'kcal/mol'),
        S298 = (64.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
    label = "HSO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 S u1 p0 c0 {1,D} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.94,13.68,14.99,15.97,17.28,18.05,18.98],'cal/(mol*K)'),
        H298 = (-33.8,'kcal/mol'),
        S298 = (63.68,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
    label = "HOSHO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 S u0 p1 c0 {1,S} {3,D} {5,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.58,15.84,17.65,19.01,20.82,21.95,23.54],'cal/(mol*K)'),
        H298 = (-64.5,'kcal/mol'),
        S298 = (64.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
    label = "HOSO2",
    molecule = 
"""
multiplicity 2
1 S u1 p0 c0 {2,S} {3,D} {4,D}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.74,18.76,20.13,21.07,22.22,22.94,24.02],'cal/(mol*K)'),
        H298 = (-93.5,'kcal/mol'),
        S298 = (70.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
""",
)

entry(
    index = 4,
    label = "HSOO",
    molecule = 
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,700,1000,1300,2500],'K'),
        Cpdata = ([51.7,56.8,60.5,65.6,70.2,72.9,76.0],'J/(mol*K)'),
        H298 = (111.5,'kJ/mol'),
        S298 = (283.0,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Table 5
MP2=FULL/6-31G(d)
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall
J. Phys. Chem. A, 1999, 103, 11328-11335, doi: 10.1021/jp9924070
""",
)

entry(
    index = 4,
    label = "TrinitroMethane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {11,S}
2  N u0 p0 c+1 {1,S} {3,D} {4,S}
3  O u0 p2 c0 {2,D}
4  O u0 p3 c-1 {2,S}
5  N u0 p0 c+1 {1,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p3 c-1 {5,S}
8  N u0 p0 c+1 {1,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p3 c-1 {8,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.27,45.71,47.02,48.21,50.27,51.92,54.65],'cal/(mol*K)'),
        H298 = (-5.69,'kcal/mol'),
        S298 = (98.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
517-25-9 CH(NO2)3 Tri-Nitro Methane
REF= A.BURCAT PM3 JPCRD 28,(1999),63
Moments=Melius HF298=-3.2 kcal  REF=Carpenter et. al. JCED 15,(1970),535
Max Lst Sq Error Cp @ 1300 K 0.50%

Alexander Burcat and Branko Ruscic
"Third Millennium Ideal Gas and Condensed Phase Thermochemical Database for
Combustion with updates from Active Thermochemical Tables" TAE # 960; ANL-50/20
Technion-IIT, Aerospace Engineering, and Argonne National Laboratory, Chemistry
Division, 2005.
""",
)

entry(
    index = 4,
    label = "CNH2",
    molecule = 
"""
multiplicity 4
1 C u3 p0 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.42,11.22,11.96,12.65,13.87,14.89,16.79],'cal/(mol*K)'),
        H298 = (87.84,'kcal/mol'),
        S298 = (52.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
35430-17-2
CNH2  triradical  SIGMA=2.  STATWT=2.  IA=0.2456  IB=2.2408  IC=2.4865
Nu=3331.5,3304,1652,1438,1029,718  HF298=368.7+/-1.45 kJ  REF=ATcT C 2011
{HF298=366.7+/-8. kJ  REF=Burcat G3B3}  Max Lst Sq Error Cp @ 6000 K 0.40%.

Alexander Burcat and Branko Ruscic
"Third Millennium Ideal Gas and Condensed Phase Thermochemical Database for
Combustion with updates from Active Thermochemical Tables" TAE # 960; ANL-50/20
Technion-IIT, Aerospace Engineering, and Argonne National Laboratory, Chemistry
Division, 2005.
""",
)

entry(
    index = 4,
    label = "NH2CO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.49,14.04,15.42,16.60,18.46,19.86,22.10],'cal/(mol*K)'),
        H298 = (-3.23,'kcal/mol'),
        S298 = (62.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
3858-51-7
CH2NO  H2N-C(*)=O RADICAL   STATWT=2  SIGMA=2  IA=0.6788  IB=7.7562  IC=8.4350
NU=3695,3484,1871,1626,1233,1090,641,521,211.  HF298=-3.225+/-2. kcal REF=Burcat
G3B3   {HF298=-5.57 +/-2.37 kcal  REF= C. Melius Database BAC/MP4 C37;
HF298=-15.1+/-4. kJ  REF=Luo Comprehensive Handbook Chem. Bond Energ. CRC press
2007; HF298=-15.7 kJ REF=Morochkin & Dorofeeva Comp.& Theo Chem. 991,(2012),182}
Max Lst Sq Error Cp @ 6000 K 0.36%.

Alexander Burcat and Branko Ruscic
"Third Millennium Ideal Gas and Condensed Phase Thermochemical Database for
Combustion with updates from Active Thermochemical Tables" TAE # 960; ANL-50/20
Technion-IIT, Aerospace Engineering, and Argonne National Laboratory, Chemistry
Division, 2005.
""",
)



















"""

check Burcat?


Add:

HOSO2


N2H3NO
HNNO2 - bad
H2NONO
NH2NHNO
NH2NHNO2
NH2NHONO
CH2N2 - radical, but no data for non-rad
CHN2 - same
cN2CH2 - same
CNNH - same
CNN - same
CH2NC - same
CH2NCN
NCCHN
NCNCN
cNCN
OHNHCN - bad
HONCNH
NCOHNH
HN(O)CN - bad
HNC(O)N




HOOS
NS
SNO




"""




































