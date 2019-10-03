#!/usr/bin/env python
# encoding: utf-8

name = "Functional Group Additivity Values"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = -1,
    label = "R",
    group = 
"""
1 * R u0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "C",
    group = 
"""
1 * C u0
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Cbf",
    group = 
"""
1 * Cbf u0
""",
    thermo = u'Cbf-CbCbCbf',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Cbf-CbCbCbf",
    group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cb  u0 {1,B}
4   Cbf u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.01,3.68,4.2,4.61,5.2,5.7,6.2],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (4.8,'kcal/mol','+|-',0.17),
        S298 = (-5,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cbf-CbfCbCb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "Cbf-CbCbfCbf",
    group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cbf u0 {1,B}
4   Cbf u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.01,3.68,4.2,4.61,5.2,5.7,6.2],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (3.7,'kcal/mol','+|-',0.3),
        S298 = (-5,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cbf-CbfCbfCb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "Cbf-CbfCbfCbf",
    group = 
"""
1 * Cbf u0 p0 c0 {3,B} {6,B} {2,B}
2   Cbf u0 p0 c0 {4,B} {5,B} {1,B}
3   Cbf u0 p0 c0 {8,B} {9,B} {1,B}
4   Cbf u0 p0 c0 {10,B} {11,B} {2,B}
5   Cbf u0 p0 c0 {13,B} {14,B} {2,B}
6   Cbf u0 p0 c0 {15,B} {16,B} {1,B}
7   C   u0 p0 c0 {8,B} {16,B}
8   C   u0 p0 c0 {7,B} {3,B}
9   C   u0 p0 c0 {3,B} {10,B}
10  C   u0 p0 c0 {9,B} {4,B}
11  C   u0 p0 c0 {4,B} {12,B}
12  C   u0 p0 c0 {11,B} {13,B}
13  C   u0 p0 c0 {12,B} {5,B}
14  C   u0 p0 c0 {5,B} {15,B}
15  C   u0 p0 c0 {14,B} {6,B}
16  C   u0 p0 c0 {7,B} {6,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2,3.11,3.9,4.42,5,5.3,5.7],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (1.5,'kcal/mol','+|-',0.3),
        S298 = (1.8,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cbf-CbfCbfCbf STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""
The smallest PAH that can have Cbf-CbfCbfCbf is pyrene. Currently the database is restricted
that any group with more three Cbf atoms must have all benzene rings explicitly written out.
Previously, this node would also match one carbon on Benzo[c]phenanthrene and does not now.
Examples from the original source do not include Benzo[c]phenanthrene. 
""",
)

entry(
    index = 6,
    label = "Cb",
    group = 
"""
1 * Cb u0
""",
    thermo = u'Cb-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "Cb-H",
    group = 
"""
1 * Cb u0 {2,S}
2   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.24,4.44,5.46,6.3,7.54,8.41,9.73],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.3,'kcal/mol','+|-',0.11),
        S298 = (11.53,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cb-H BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "Cb-O2s",
    group = 
"""
1 * Cb u0 {2,S}
2   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,5.3,6.2,6.6,6.9,6.9,7.07],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-0.9,'kcal/mol','+|-',0.16),
        S298 = (-10.2,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cb-O BENSON Cp1500=3D Cp1000*(Cp1500/Cp1000: Cb/Cd)""",
    longDesc = 
u"""

""",
)

entry(
    index = 1197,
    label = "Cb-S",
    group = 
"""
1 * Cb u0 {2,S}
2   S u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.76884859206, 2.90049786765, 2.65234888601, 2.65783005365, 4.2011256022, 5.11337252346, 3.60230772928], 'cal/(mol*K)'),
        H298 = (23.9791361203,'kcal/mol'),
        S298 = (-5.77307512412,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 9,
    label = "Cb-C",
    group = 
"""
1 * Cb u0 {2,S}
2   C  u0 {1,S}
""",
    thermo = u'Cb-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Cb-Cs",
    group = 
"""
1 * Cb u0 {2,S}
2   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.67,3.14,3.68,4.15,4.96,5.44,5.98],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (5.51,'kcal/mol','+|-',0.13),
        S298 = (-7.69,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cb-Cs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Cb-Cds",
    group = 
"""
1 * Cb      u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
    thermo = u'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "Cb-(Cds-O2d)",
    group = 
"""
1 * Cb u0 {2,S}
2   CO u0 {1,S} {3,D}
3   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.69,'kcal/mol','+|-',0.2),
        S298 = (-7.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Enthalpy from Cb-CO, entropies and heat capacities assigned value of Cb-Cd""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "Cb-(Cds-Cd)",
    group = 
"""
1 * Cb u0 {2,S}
2   Cd u0 {1,S} {3,D}
3   C  u0 {2,D}
""",
    thermo = u'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "Cb-(Cds-Cds)",
    group = 
"""
1 * Cb u0 {2,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (5.69,'kcal/mol','+|-',0.2),
        S298 = (-7.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cb-Cd STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "Cb-(Cds-Cdd)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D}
""",
    thermo = u'Cb-(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "Cb-(Cds-Cdd-O2d)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {4,D}
4   O2d  u0 {3,D}
""",
    thermo = u'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cb-(Cds-Cdd-S2d)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {4,D}
4   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "Cb-(Cds-Cdd-Cd)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {4,D}
4   C   u0 {3,D}
""",
    thermo = u'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "Cb-Ct",
    group = 
"""
1 * Cb u0 {2,S}
2   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (5.69,'kcal/mol','+|-',0.3),
        S298 = (-7.8,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cb-Ct STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index = 1839,
    label = "Cb-(CtN3t)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.8,11.2,12.3,13.1,14.2,14.9,16.65],'cal/(mol*K)'),
        H298 = (35.8,'kcal/mol'),
        S298 = (20.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "Cb-Cb",
    group = 
"""
1 * Cb u0 {2,S}
2   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.33,4.22,4.89,5.27,5.76,5.95,6.05],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (4.96,'kcal/mol','+|-',0.3),
        S298 = (-8.64,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cb-Cb BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 1821,
    label = "Cb-N3s",
    group = 
"""
1 * Cb  u0 {2,S}
2   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.95,5.21,5.94,6.32,6.53,6.56,6.635],'cal/(mol*K)'),
        H298 = (-0.5,'kcal/mol'),
        S298 = (-9.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "Ct",
    group = 
"""
1 * Ct u0
""",
    thermo = u'Ct-CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1849,
    label = "Ct-CtN3s",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   N3s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1853,
    label = "Ct-N3tN3s",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "Ct-CtH",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28,5.99,6.49,6.87,7.47,7.96,8.85],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (26.93,'kcal/mol','+|-',0.05),
        S298 = (24.7,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Ct-H STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "Ct-StH",
    group =
"""
1 * Ct                 u0 {2,T} {3,S}
2   [S4t,S6t,S6td]     u0 {1,T}
3   H                  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.08103105033, 3.72743085567, 4.37092973826, 4.84140287844, 4.59173464362, 4.53885739091, 5.60643495043], 'cal/(mol*K)'),
        H298 = (77.8607721919,'kcal/mol'),
        S298 = (10.4264941308,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 22,
    label = "Ct-CtOs",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.64,4.39,4.85,5.63,5.66,5.73,5.73],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (31.4,'kcal/mol','+|-',0.27),
        S298 = (4.91,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-O MELIUS / hc#coh !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1852,
    label = "Ct-N3tOs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   O2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1195,
    label = "Ct-CtS",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   S u0 {1,S}
""",
    thermo = u'Ct-CtS2',
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1195,
    label = "Ct-CtS2",
    group =
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.71848530206, 2.61910206765, 2.11913664601, 2.02492374365, 3.5754850722, 4.64314308346, 3.67955438928], 'cal/(mol*K)'),
        H298 = (50.4516217803,'kcal/mol'),
        S298 = (9.41879867588,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 1195,
    label = "Ct-CtS4",
    group =
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22281492058, 2.05384907283, 1.75526932364, 1.82002938423, 3.72998757681, 4.90178212264, 4.49971819577], 'cal/(mol*K)'),
        H298 = (56.3939486467,'kcal/mol'),
        S298 = (12.5243287449,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 1195,
    label = "Ct-CtS6",
    group =
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.29,3.67,4,4.29,4.74,5.05,5.49],'cal/(mol*K)'),
        H298 = (27.63,'kcal/mol'),
        S298 = (6.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc =
u"""

""",
)

entry(
    index = 1942,
    label = "Ct-N3tC",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1850,
    label = "Ct-N3tCs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1851,
    label = "Ct-N3tCd",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "Ct-CtC",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   C  u0 {1,S}
""",
    thermo = u'Ct-CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Ct-CtCs",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.13,3.48,3.81,4.09,4.6,4.92,6.35],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (27.55,'kcal/mol','+|-',0.27),
        S298 = (6.35,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-Cs STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "Ct-CtCds",
    group = 
"""
1 * Ct      u0 {2,T} {3,S}
2   Ct      u0 {1,T}
3   [Cd,CO,CS] u0 {1,S}
""",
    thermo = u'Ct-Ct(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "Ct-Ct(Cds-O2d)",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   CO u0 {1,S} {4,D}
4   O2d u0 {3,D}
""",
    thermo = u'Ct-CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "Ct-Ct(Cds-Cd)",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cd u0 {1,S} {4,D}
4   C  u0 {3,D}
""",
    thermo = u'Ct-Ct(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "Ct-Ct(Cds-Cds)",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.57,3.54,3.5,4.92,5.34,5.5,5.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (28.2,'kcal/mol','+|-',0.27),
        S298 = (6.43,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-Cd STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "Ct-Ct(Cds-Cdd)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D}
""",
    thermo = u'Ct-Ct(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "Ct-Ct(Cds-Cdd-O2d)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {5,D}
5   O2d  u0 {4,D}
""",
    thermo = u'Ct-Ct(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Ct-Ct(Cds-Cdd-S2d)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {5,D}
5   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "Ct-Ct(Cds-Cdd-Cd)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Cd  u0 {1,S} {4,D}
4   Cdd u0 {3,D} {5,D}
5   C   u0 {4,D}
""",
    thermo = u'Ct-Ct(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "Ct-CtCt",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.54,4.06,4.4,4.64,5,5.23,5.57],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (25.6,'kcal/mol','+|-',0.27),
        S298 = (5.88,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-Ct STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index = 1840,
    label = "Ct-Ct(CtN3t)",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T}
3   Ct  u0 {1,S} {4,T}
4   N3t u0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,11.3,12.1,12.7,13.6,14.3,15.3],'cal/(mol*K)'),
        H298 = (63.8,'kcal/mol'),
        S298 = (35.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "Ct-CtCb",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.57,3.54,4.5,4.92,5.34,5.5,5.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (24.67,'kcal/mol','+|-',0.27),
        S298 = (6.43,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-Cb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)


entry(
    index = 34,
    label = "Cdd",
    group = 
"""
1 * Cdd u0
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1854,
    label = "Cdd-N3dCd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   N3d u0 {1,D}
3   Cd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.5,5.1,5.6,6,6.5,6.9,7.4],'cal/(mol*K)','+|-',[1.1,1.1,1.1,1.1,1.1,1.1,1.1]),
        H298 = (25.9,'kcal/mol','+|-',1.5),
        S298 = (19.7,'cal/(mol*K)','+|-',1.4),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "Cdd-OdOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   O2d  u0 {1,D}
3   O2d  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.91,9.86,10.65,11.31,12.32,12.99,13.93],'cal/(mol*K)'),
        H298 = (-94.05,'kcal/mol','+|-',0.03),
        S298 = (52.46,'cal/(mol*K)','+|-',0.002),
    ),
    shortDesc = u"""CHEMKIN DATABASE: S(group) = S(CO2) + Rln(2)""",
    longDesc = 
u"""

""",
)

entry(
    index = 1466,
    label = "Cdd-OdSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   O2d  u0 {1,D}
3   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.807, 10.837, 11.621, 12.184, 12.994, 13.521, 14.138], 'cal/(mol*K)'),
        H298 = (-34.785,'kcal/mol'),
        S298 = (55.339,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = 1199,
    label = "Cdd-SdSd",
    group =
"""
1 * Cdd u0 {2,D} {3,D}
2   S u0 {1,D}
3   S u0 {1,D}
""",
    thermo = u'Cdd-S2dS2d',
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc =
u"""

""",
)

entry(
    index = 1199,
    label = "Cdd-S2dS2d",
    group =
"""
1 * Cdd u0 {2,D} {3,D}
2   S2d u0 {1,D}
3   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.91,11.83,12.49,12.98,13.63,14.01,14.47],'cal/(mol*K)'),
        H298 = (24.5,'kcal/mol'),
        S298 = (58.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc =
u"""

""",
)

entry(
    index = 1199,
    label = "Cdd-S4S4",
    group =
"""
1 * Cdd u0 {2,D} {3,D}
2   [S4d,S4dd] u0 {1,D}
3   [S4d,S4dd] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.1153619681, 0.630199431979, 2.49388002067, 2.89149920751, 0.283543803635, -1.1915949218, 1.13021746318], 'cal/(mol*K)'),
        H298 = (20.1365176612,'kcal/mol'),
        S298 = (4.40342467981,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 1199,
    label = "Cdd-S2S4",
    group =
"""
1 * Cdd u0 {2,D} {3,D}
2   S2d u0 {1,D}
3   [S4d,S4dd] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.10681901595, 6.10259971599, 7.15094001034, 7.51074960375, 6.43877190182, 5.8057025391, 7.22710873159], 'cal/(mol*K)'),
        H298 = (43.9012588306,'kcal/mol'),
        S298 = (35.0337123399,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 36,
    label = "Cdd-CdOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   O2d  u0 {1,D}
""",
    thermo = u'Cdd-CdsOd',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "Cdd-CdsOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   O2d  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""O=C*=C< currently treat the adjacent C as Ck""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "Cdd-CddOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D}
3   O2d  u0 {1,D}
""",
    thermo = u'Cdd-(Cdd-Cd)O2d',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "Cdd-(Cdd-O2d)O2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   O2d  u0 {1,D}
4   O2d  u0 {2,D}
""",
    thermo = u'Cdd-CdsOd',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "Cdd-(Cdd-Cd)O2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   O2d  u0 {1,D}
4   C   u0 {2,D}
""",
    thermo = u'Cdd-CdsOd',
    shortDesc = u"""O=C*=C= currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""

""",
)

entry(
    index = 1200,
    label = "Cdd-CdSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   S   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.88,8.48,8.8,8.99,9.23,9.37,9.58],'cal/(mol*K)'),
        H298 = (40.33,'kcal/mol'),
        S298 = (34.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-CdsSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   S u0 {1,D}
""",
    thermo = u'Cdd-CdsS6d',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-CdsS6d",
    group =
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   [S6d,S6dd,S6ddd,S6td] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.36088989127, 6.28496892964, 6.76617539688, 7.0857883162, 7.66552251265, 8.0522128104, 8.44683718868], 'cal/(mol*K)'),
        H298 = (52.2311282113,'kcal/mol'),
        S298 = (27.9502135413,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-CdsS4d",
    group =
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   [S4d,S4dd] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.88,8.48,8.8,8.99,9.23,9.37,9.58],'cal/(mol*K)'),
        H298 = (40.33,'kcal/mol'),
        S298 = (34.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-CdsS2d",
    group =
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.88,8.48,8.8,8.99,9.23,9.37,9.58],'cal/(mol*K)'),
        H298 = (40.33,'kcal/mol'),
        S298 = (34.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-CddSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D}
3   S2d u0 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-(Cdd-S2d)S2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   S2d u0 {1,D}
4   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-(Cdd-Cd)S2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   S2d u0 {1,D}
4   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "Cdd-CdCd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   C   u0 {1,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "Cdd-CddCdd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D}
3   Cdd u0 {1,D}
""",
    thermo = u'Cdd-(Cdd-Cd)(Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "Cdd-(Cdd-O2d)(Cdd-O2d)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   O2d  u0 {2,D}
5   O2d  u0 {3,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""O=C=C*=C=O, currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-(Cdd-S2d)(Cdd-S2d)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   S2d u0 {2,D}
5   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "Cdd-(Cdd-O2d)(Cdd-Cd)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   O2d  u0 {2,D}
5   C   u0 {3,D}
""",
    thermo = u'Cdd-(Cdd-O2d)Cds',
    shortDesc = u"""O=C=C*=C=C, currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-(Cdd-S2d)(Cdd-Cd)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   S2d u0 {2,D}
5   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "Cdd-(Cdd-Cd)(Cdd-Cd)",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cdd u0 {1,D} {5,D}
4   C   u0 {2,D}
5   C   u0 {3,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""C=C=C*=C=C, currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "Cdd-CddCds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D}
3   Cd  u0 {1,D}
""",
    thermo = u'Cdd-(Cdd-Cd)(Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "Cdd-(Cdd-O2d)Cds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cd  u0 {1,D}
4   O2d  u0 {2,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""O=C=C*=C<, currently not defined. Assigned same value as Ca """,
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cdd-(Cdd-S2d)Cds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cd  u0 {1,D}
4   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "Cdd-(Cdd-Cd)Cds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {4,D}
3   Cd  u0 {1,D}
4   C   u0 {2,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""C=C=C*=C<, currently not defined. Assigned same value as Ca """,
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "Cdd-CdsCds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   Cd  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.4,4.7,5,5.3,5.5,5.7],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (34.2,'kcal/mol','+|-',0.2),
        S298 = (6,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Benson's Ca """,
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "Cds",
    group = 
"""
1 * [Cd,CO,CS] u0
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1823,
    label = "Cds-OdN3sH",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   O2d  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.03,7.87,8.82,9.68,11.16,12.2,14.8],'cal/(mol*K)'),
        H298 = (-29.6,'kcal/mol'),
        S298 = (34.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1824,
    label = "Cds-OdN3sCs",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   O2d  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.37,6.17,7.07,7.66,9.62,11.19,15.115],'cal/(mol*K)'),
        H298 = (-32.8,'kcal/mol'),
        S298 = (16.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1855,
    label = "Cd-N3dCsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,4.2,5,5.6,6.6,7.2,7.9],'cal/(mol*K)','+|-',[0.9,0.9,0.9,0.9,0.9,0.9,0.9]),
        H298 = (5.7,'kcal/mol','+|-',1.2),
        S298 = (2,'cal/(mol*K)','+|-',1.1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1856,
    label = "Cd-N3dCsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.3,7.2,8,9.3,10.2,11.6],'cal/(mol*K)','+|-',[0.9,0.9,0.9,0.9,0.9,0.9,0.9]),
        H298 = (3.3,'kcal/mol','+|-',1.3),
        S298 = (21.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1857,
    label = "Cd-N3dHH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.2,7.4,8.7,9.8,11.5,12.9,15],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (4.4,'kcal/mol','+|-',1.4),
        S298 = (40.8,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "Cds-OdHH",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.47,9.38,10.46,11.52,13.37,14.81,14.81],'cal/(mol*K)','+|-',[0.06,0.06,0.06,0.06,0.06,0.06,0.06]),
        H298 = (-25.95,'kcal/mol','+|-',0.11),
        S298 = (53.68,'cal/(mol*K)','+|-',0.06),
    ),
    shortDesc = u"""CO-HH BENSON !!!WARNING! Cp1500 value taken as Cp1000, S(group) = S(CH2O) + Rln(2)""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "Cds-OdOsH",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.88,34.56,42.08,48.16,56.57,61.38,65.84],'J/(mol*K)','+|-',[4.01,4.01,4.01,4.01,4.01,4.01,4.01]),
        H298 = (-211.8,'kJ/mol','+|-',3.42),
        S298 = (124.04,'J/(mol*K)','+|-',4.68),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1454,
    label = "CO-SH",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'CO-S2H',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1454,
    label = "CO-S2H",
    group =
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S2s  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.04699155431, 9.68815679754, 10.2267242741, 10.6586075823, 12.4810664708, 13.819966148, 13.9357824154], 'cal/(mol*K)'),
        H298 = (-16.2652964672,'kcal/mol'),
        S298 = (42.3930115801,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1454,
    label = "CO-S4H",
    group =
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.6236915003, 9.36015936623, 9.67492614645, 10.3465505874, 13.1633562053, 14.970802241, 15.2116924156], 'cal/(mol*K)'),
        H298 = (-7.98956667001,'kcal/mol'),
        S298 = (38.4190620387,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1454,
    label = "CO-S6H",
    group =
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.0397281303, 7.18524151288, 8.23683405279, 9.22668028391, 11.8201567179, 13.4916633512, 14.3427546283], 'cal/(mol*K)'),
        H298 = (-9.53898518777,'kcal/mol'),
        S298 = (50.092114381,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 53,
    label = "Cds-OdOsOs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.17,39.3,48.25,53.88,58.97,59.63,56.09],'J/(mol*K)','+|-',[6,6,6,6,6,6,6]),
        H298 = (-281.4,'kJ/mol','+|-',5.11),
        S298 = (22.66,'J/(mol*K)','+|-',7),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1455,
    label = "CO-CsSs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S2s u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.87838299719, 8.43317282236, 8.89243715078, 9.24871341302, 10.8100390301, 11.7438326894, 10.8169716926], 'cal/(mol*K)'),
        H298 = (-19.9716670716,'kcal/mol'),
        S298 = (21.2529697689,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1456,
    label = "CO-OsSs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.62809763512, 9.30023886554, 10.6110682292, 11.4909343453, 13.433306943, 14.3150741155, 12.7165752669], 'cal/(mol*K)'),
        H298 = (-36.5514428393,'kcal/mol'),
        S298 = (17.3830984295,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "Cds-OdCH",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cds-OdCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "Cds-OdCsH",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.24,31.22,35.94,40.13,46.74,51.39,57.73],'J/(mol*K)','+|-',[2.08,2.08,2.08,2.08,2.08,2.08,2.08]),
        H298 = (-123.4,'kJ/mol','+|-',1.77),
        S298 = (145.46,'J/(mol*K)','+|-',2.42),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 56,
    label = "Cds-OdCdsH",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "Cds-O2d(Cds-O2d)H",
    group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.76,34.63,39.25,43.32,49.57,53.77,59.32],'J/(mol*K)','+|-',[1.7,1.7,1.7,1.7,1.7,1.7,1.7]),
        H298 = (-104.8,'kJ/mol','+|-',1.45),
        S298 = (140.49,'J/(mol*K)','+|-',1.98),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 58,
    label = "Cds-O2d(Cds-Cd)H",
    group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H  u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.31,34,39.42,43.77,50.16,54.55,60.77],'J/(mol*K)','+|-',[4.9,4.9,4.9,4.9,4.9,4.9,4.9]),
        H298 = (-128.3,'kJ/mol','+|-',5.9),
        S298 = (129.26,'J/(mol*K)','+|-',5.71),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 59,
    label = "Cds-O2d(Cds-Cds)H",
    group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H  u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.45,8.77,9.82,10.7,12.14,12.9,12.9],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-30.9,'kcal/mol','+|-',0.3),
        S298 = (33.4,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-CdH Hf BOZZELLI S,Cp =3D CO/C/H-del(cd syst) !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "Cds-O2d(Cds-Cdd)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d  u0 {1,D}
4   H   u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "Cds-O2d(Cds-Cdd-O2d)H",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d  u0 {1,D}
5   H   u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "Cds-O2d(Cds-Cdd-Cd)H",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d  u0 {1,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "Cds-OdCtH",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "Cds-OdCbH",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "Cds-OdCOs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = u'Cds-OdCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "Cds-OdCsOs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.67,28.39,34.6,39.48,46.23,50.09,52.68],'J/(mol*K)','+|-',[2.85,2.85,2.85,2.85,2.85,2.85,2.85]),
        H298 = (-222,'kJ/mol','+|-',2.43),
        S298 = (43.52,'J/(mol*K)','+|-',3.33),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 67,
    label = "Cds-OdCdsOs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "Cds-O2d(Cds-O2d)O2s",
    group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.18,34.34,39.85,44.13,49.81,52.4,52.33],'J/(mol*K)','+|-',[3.36,3.36,3.36,3.36,3.36,3.36,3.36]),
        H298 = (-196.2,'kJ/mol','+|-',2.86),
        S298 = (39.37,'J/(mol*K)','+|-',3.92),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 69,
    label = "Cds-O2d(Cds-Cd)O2s",
    group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.33,37.84,44.54,49.34,55.45,58.73,60.61],'J/(mol*K)','+|-',[7.46,7.46,7.46,7.46,7.46,7.46,7.46]),
        H298 = (-218.6,'kJ/mol','+|-',6.36),
        S298 = (33.44,'J/(mol*K)','+|-',8.7),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 70,
    label = "Cds-O2d(Cds-Cds)O2s",
    group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-32.1,'kcal/mol','+|-',0.3),
        S298 = (14.78,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-OCd RPS + S Coreected !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "Cds-O2d(Cds-Cdd)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d  u0 {1,D}
4   O2s  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-Cd)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "Cds-O2d(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d  u0 {1,D}
5   O2s  u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "Cds-O2d(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d  u0 {1,D}
5   O2s  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "Cds-OdCtOs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "Cds-OdCbOs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-36.6,'kcal/mol','+|-',0.3),
        S298 = (14.78,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-OCb RPS + S Coreected !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "Cds-OdCC",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = u'Cds-OdCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "Cds-OdCsCs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.82,27.7,31.22,34.19,38.37,40.85,43.26],'J/(mol*K)','+|-',[2.08,2.08,2.08,2.08,2.08,2.08,2.08]),
        H298 = (-132.2,'kJ/mol','+|-',1.77),
        S298 = (61.78,'J/(mol*K)','+|-',2.42),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 78,
    label = "Cds-OdCdsCs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "Cds-O2d(Cds-O2d)Cs",
    group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.77,30.83,34.36,37.27,41.27,43.45,45.25],'J/(mol*K)','+|-',[1.28,1.28,1.28,1.28,1.28,1.28,1.28]),
        H298 = (-122,'kJ/mol','+|-',1.09),
        S298 = (57.8,'J/(mol*K)','+|-',1.5),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 80,
    label = "Cds-O2d(Cds-Cd)Cs",
    group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.26,30.66,34.68,37.69,41.62,43.93,46.69],'J/(mol*K)','+|-',[4.9,4.9,4.9,4.9,4.9,4.9,4.9]),
        H298 = (-130.4,'kJ/mol','+|-',4.17),
        S298 = (47.38,'J/(mol*K)','+|-',5.71),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 81,
    label = "Cds-O2d(Cds-Cds)Cs",
    group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-30.9,'kcal/mol','+|-',0.3),
        S298 = (14.6,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-CdCs Hf BENSON =3D CO/Cb/C S,Cp !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "Cds-O2d(Cds-Cdd)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d  u0 {1,D}
4   Cs  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "Cds-O2d(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d  u0 {1,D}
5   Cs  u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "Cds-O2d(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * CO  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   O2d  u0 {1,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "Cds-OdCdsCds",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "Cds-O2d(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * CO u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {5,D}
3   CO u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.75,33.35,34.1,34.51,35.19,36.06,38.14],'J/(mol*K)','+|-',[2.41,2.41,2.41,2.41,2.41,2.41,2.41]),
        H298 = (-89.3,'kJ/mol','+|-',2.05),
        S298 = (64.51,'J/(mol*K)','+|-',2.81),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 87,
    label = "Cds-O2d(Cds-Cd)(Cds-O2d)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   CO u0 {1,S} {6,D}
5   C  u0 {3,D}
6   O2d u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "Cds-O2d(Cds-Cds)(Cds-O2d)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   CO u0 {1,S} {6,D}
5   Cd u0 {3,D}
6   O2d u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "Cds-O2d(Cds-Cdd)(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   CO  u0 {1,S} {6,D}
5   Cdd u0 {3,D}
6   O2d  u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-Cd)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "Cds-O2d(Cds-Cdd-O2d)(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {3,D} {6,D}
6   O2d  u0 {5,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "Cds-O2d(Cds-Cdd-Cd)(Cds-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {3,D} {6,D}
6   C   u0 {5,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "Cds-O2d(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   C  u0 {3,D}
6   C  u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "Cds-O2d(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {3,D}
6   Cd u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-30.9,'kcal/mol','+|-',0.3),
        S298 = (14.6,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-CdCd Estimate BOZZELLI !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "Cds-O2d(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D}
6   Cd  u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cd  u0 {4,D}
7   O2d  u0 {5,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "Cds-O2d(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cd  u0 {4,D}
7   C   u0 {5,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "Cds-O2d(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D}
6   Cdd u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "Cds-O2d(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cdd u0 {4,D} {8,D}
7   O2d  u0 {5,D}
8   O2d  u0 {6,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cdd u0 {4,D} {8,D}
7   C   u0 {5,D}
8   O2d  u0 {6,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cdd u0 {3,D} {7,D}
6   Cdd u0 {4,D} {8,D}
7   C   u0 {5,D}
8   C   u0 {6,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "Cds-OdCtCs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "Cds-OdCtCds",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "Cds-OdCt(Cds-O2d)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S}
4   CO u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "Cds-OdCt(Cds-Cd)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   C  u0 {4,D}
""",
    thermo = u'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "Cds-OdCt(Cds-Cds)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "Cds-OdCt(Cds-Cdd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D}
""",
    thermo = u'Cds-OdCt(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "Cds-OdCt(Cds-Cdd-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   O2d  u0 {5,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "Cds-OdCt(Cds-Cdd-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Ct  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   C   u0 {5,D}
""",
    thermo = u'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "Cds-OdCtCt",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "Cds-OdCbCs",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "Cds-OdCbCds",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cds-OdCb(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "Cds-OdCb(Cds-O2d)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   CO u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "Cds-OdCb(Cds-Cd)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   C  u0 {4,D}
""",
    thermo = u'Cds-OdCb(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "Cds-OdCb(Cds-Cds)",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {4,D}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "Cds-OdCb(Cds-Cdd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D}
""",
    thermo = u'Cds-OdCb(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "Cds-OdCb(Cds-Cdd-O2d)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   O2d  u0 {5,D}
""",
    thermo = u'Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "Cds-OdCb(Cds-Cdd-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cb  u0 {1,S}
4   Cd  u0 {1,S} {5,D}
5   Cdd u0 {4,D} {6,D}
6   C   u0 {5,D}
""",
    thermo = u'Cds-OdCb(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "Cds-OdCbCt",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = u'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "Cds-OdCbCb",
    group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
    thermo = u'Cds-O2d(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "Cds-CdHH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cds-CdsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "Cds-CdsHH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.1,6.36,7.51,8.5,10.07,11.27,13.19],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (6.26,'kcal/mol','+|-',0.19),
        S298 = (27.61,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-HH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "Cds-CddHH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "Cds-(Cdd-O2d)HH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.08,13.91,15.4,16.64,18.61,20.1,22.47],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (-11.34,'kcal/mol','+|-',0.19),
        S298 = (57.47,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/H2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)HH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "Cds-(Cdd-Cd)HH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "Cds-CdOsH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.08,21.17,24.43,27.41,32.22,35.73,40.97],'J/(mol*K)'),
        H298 = (36.4,'kJ/mol'),
        S298 = (33.51,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 126,
    label = "Cds-CdsOsH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.75,6.46,7.64,8.35,9.1,9.56,10.46],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (2.03,'kcal/mol','+|-',0.19),
        S298 = (6.2,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OH BOZZELLI Hf vin-oh RADOM + C/Cd/H, S&Cp LAY""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "Cds-CddOsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   O2s  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "Cds-(Cdd-O2d)OsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   O2s  u0 {1,S}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.29,13.67,15.1,16.1,17.36,18.25,19.75],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (2.11,'kcal/mol','+|-',0.19),
        S298 = (38.17,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/O/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "Cds-(Cdd-Cd)OsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   O2s  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdSH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cds-CdsSsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1180,
    label = "Cds-CdsSH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cds-CdsS4H',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1180,
    label = "Cds-CdsS2H",
    group =
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   S2s  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.73447645728, 5.76163639111, 6.02073970975, 6.36640996978, 8.22726441005, 9.40583243769, 8.69490299934], 'cal/(mol*K)'),
        H298 = (23.8380551876,'kcal/mol'),
        S298 = (7.33606028248,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1180,
    label = "Cds-CdsS4H",
    group =
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   [S4s,S4d,S4b,S4t]  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.26069951797, 7.90641577705, 7.55613158497, 8.29118858296, 10.617469783, 11.915200124, 10.969396689], 'cal/(mol*K)'),
        H298 = (27.4431586506,'kcal/mol'),
        S298 = (5.07300387793,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1180,
    label = "Cds-CdsS6H",
    group =
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   [S6s,S6d,S6dd,S6t,S6td]  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.88814500441, 5.43665485509, 6.36348901786, 7.1908410186, 9.57132769397, 10.951231466, 10.8492813212], 'cal/(mol*K)'),
        H298 = (19.0582272643,'kcal/mol'),
        S298 = (16.5569928548,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cds-CddSsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   S2s  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)SsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   S2s  u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)SsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   S2s  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "Cds-CdOsOs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.34,11.93,14.86,17.95,22.31,24.6,26.92],'J/(mol*K)','+|-',[7.4,7.4,7.4,7.4,7.4,7.4,7.4]),
        H298 = (28.3,'kJ/mol','+|-',6.3),
        S298 = (-42.69,'J/(mol*K)','+|-',8.63),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 131,
    label = "Cds-CdsOsOs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "Cds-CddOsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   O2s  u0 {1,S}
4   O2s  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "Cds-(Cdd-O2d)OsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   O2s  u0 {1,S}
4   O2s  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.56,15.58,17.69,18.67,18.78,18.4,18.01],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (2.403,'kcal/mol','+|-',0.19),
        S298 = (13.42,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/O2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "Cds-(Cdd-Cd)OsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   O2s  u0 {1,S}
4   O2s  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdSsSs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsSsSs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CddSsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   S2s  u0 {1,S}
4   S2s  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)SsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   S2s  u0 {1,S}
4   S2s  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)SsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   S2s  u0 {1,S}
4   S2s  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "Cds-CdCH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'Cds-CdsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "Cds-CdsCsH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.03,5.81,6.5,7.65,8.45,9.62],'cal/(mol*K)','+|-',[0.06,0.06,0.06,0.06,0.06,0.06,0.06]),
        H298 = (8.59,'kcal/mol','+|-',0.17),
        S298 = (7.97,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-CsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "Cds-CdsCdsH",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "Cds-Cds(Cds-Cd)H",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "Cds-Cds(Cds-Cds)H",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.78,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-CdH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "Cds-Cds(Cds-Cdd)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   H   u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   H   u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "Cds-Cds(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "Cds-CdsCtH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.78,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-CtH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 1836,
    label = "Cds-CdsH(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Ct  u0 {1,S} {5,T}
3   Cd  u0 {1,D}
4   H   u0 {1,S}
5   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,12,13.4,14.6,16.3,17.5,19.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (38.5,'kcal/mol','+|-',1.3),
        S298 = (37.6,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "Cds-CdsCbH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.78,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-CbH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "Cds-CddCsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "Cds-(Cdd-O2d)CsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([43.83,50.1,55.5,60.05,67.09,72.13,79.55],'J/(mol*K)','+|-',[4,4,4,4,4,4,4]),
        H298 = (-17.6,'kJ/mol','+|-',3.41),
        S298 = (169.15,'J/(mol*K)','+|-',4.67),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "Cds-(Cdd-Cd)CsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "Cds-CddCdsH",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "Cds-(Cdd-O2d)(Cds-O2d)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "Cds-(Cdd-O2d)(Cds-Cd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([43.67,52.95,59.65,64.67,71.81,76.72,83.92],'J/(mol*K)','+|-',[5.66,5.66,5.66,5.66,5.66,5.66,5.66]),
        H298 = (-36,'kJ/mol','+|-',4.82),
        S298 = (152.19,'J/(mol*K)','+|-',6.6),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 152,
    label = "Cds-(Cdd-O2d)(Cds-Cds)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.55,12.41,13.82,14.91,16.51,17.62,19.24],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.998,'kcal/mol','+|-',0.2),
        S298 = (39.06,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/H/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   O2d  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cds)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "Cds-(Cdd-Cd)(Cds-O2d)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   O2d  u0 {3,D}
""",
    thermo = u'Cd-Cd(CO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "Cds-(Cdd-Cd)(Cds-Cd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "Cds-(Cdd-Cd)(Cds-Cds)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cd-Cd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "Cds-CddCtH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "Cds-(Cdd-O2d)CtH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CtH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "Cds-(Cdd-Cd)CtH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "Cds-CddCbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "Cds-(Cdd-O2d)CbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "Cds-(Cdd-Cd)CbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)C=SH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)C=SH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1182,
    label = "Cds-CdsC=SH",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.43320087294, 5.26470986824, 6.10619038173, 6.88615928098, 8.07976598086, 8.87744705947, 9.93769382321], 'cal/(mol*K)'),
        H298 = (7.48610682595,'kcal/mol'),
        S298 = (8.61433830596,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1999,
    label = "Cd-Cd(CO)H",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {5,D}
3   H  u0 {1,S}
4   Cd u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.08,21.17,24.43,27.41,32.22,35.73,40.97],'J/(mol*K)'),
        H298 = (36.4,'kJ/mol'),
        S298 = (33.51,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2000,
    label = "Cd-Cd(CCO)H",
    group = 
"""
1 * Cd  u0 {2,S} {4,S} {5,D}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   H   u0 {1,S}
5   Cd  u0 {1,D}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.08,21.17,24.43,27.41,32.22,35.73,40.97],'J/(mol*K)'),
        H298 = (36.4,'kJ/mol'),
        S298 = (33.51,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 168,
    label = "Cds-CdCO",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = u'Cds-CdsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "Cds-CdsCdsOs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "Cds-Cds(Cds-O2d)O2s",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (5.13,'kcal/mol','+|-',0.2),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OCO adj BENSON for RADOM c*coh""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "Cds-Cds(Cds-Cd)O2s",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   O2s u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "Cds-Cds(Cds-Cds)O2s",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   O2s u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (1.5,'kcal/mol','+|-',0.2),
        S298 = (-14.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OCd jwb need calc""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "Cds-Cds(Cds-Cdd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "Cds-Cds(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   O2s  u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "Cds-Cds(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   O2s  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "Cds-CdsCtOs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "Cds-CdsCbOs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (1.5,'kcal/mol','+|-',0.2),
        S298 = (-14.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OCb jwb need calc""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "Cds-CddCdsOs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "Cds-(Cdd-O2d)(Cds-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   O2s  u0 {1,S}
5   O2d  u0 {2,D}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "Cds-(Cdd-O2d)(Cds-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s  u0 {1,S}
5   O2d  u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "Cds-(Cdd-O2d)(Cds-Cds)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s  u0 {1,S}
5   O2d  u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s  u0 {1,S}
5   O2d  u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-Cd)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   O2s  u0 {1,S}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.01,12.97,14.17,14.97,15.8,16.26,16.88],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (1.607,'kcal/mol','+|-',0.2),
        S298 = (17.73,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/O/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   O2s  u0 {1,S}
6   O2d  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "Cds-(Cdd-Cd)(Cds-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s  u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "Cds-(Cdd-Cd)(Cds-Cds)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s  u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)O2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2s  u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   O2s  u0 {1,S}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   O2s  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    label = "Cds-CddCtOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   O2s  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    label = "Cds-(Cdd-O2d)CtOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   O2s  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    label = "Cds-(Cdd-Cd)CtOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   O2s  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "Cds-CddCbOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   O2s  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "Cds-(Cdd-O2d)CbOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   O2s  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "Cds-(Cdd-Cd)CbOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   O2s  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1995,
    label = "Cd-CdCsOs",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   C  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.79,15.86,19.67,22.91,26.55,27.85,28.45],'J/(mol*K)','+|-',[5.1,5.1,5.1,5.1,5.1,5.1,5.1]),
        H298 = (33,'kJ/mol','+|-',4.34),
        S298 = (-50.89,'J/(mol*K)','+|-',5.94),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 169,
    label = "Cds-CdsCsOs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,4.56,5.04,5.3,5.84,6.07,6.16],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.03,'kcal/mol','+|-',0.2),
        S298 = (-12.32,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OCs BOZZELLI-RADOM vin-oh and del (ccoh-ccohc)""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "Cds-CddCsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cs  u0 {1,S}
4   O2s  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "Cds-(Cdd-O2d)CsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   O2s  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.91,12.65,13.59,14.22,15,15.48,16.28],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.273,'kcal/mol','+|-',0.2),
        S298 = (18.58,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/O/C} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "Cds-(Cdd-Cd)CsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   O2s  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdCS",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   S  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1181,
    label = "Cds-CdsCsSs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   S  u0 {1,S}
""",
    thermo = u'Cds-CdsCsS2',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1181,
    label = "Cds-CdsCsS2",
    group =
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   S2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3247825942, 5.00232021662, 4.81503868621, 4.74156726606, 6.00082108993, 6.66867471103, 5.0781462772], 'cal/(mol*K)'),
        H298 = (25.5347990218,'kcal/mol'),
        S298 = (-13.292296294,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1181,
    label = "Cds-CdsCsS4",
    group =
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   [S4s,S4d,S4b,S4t]  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.78821987095, 5.62174788285, 4.95561812978, 5.59138537503, 7.74471202461, 8.8166856091, 7.34178883577], 'cal/(mol*K)'),
        H298 = (27.3401292857,'kcal/mol'),
        S298 = (-12.8382571725,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1181,
    label = "Cds-CdsCsS6",
    group =
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   [S6s,S6d,S6dd,S6t,S6td]  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.96863689534, 5.21797992081, 5.59384221868, 5.93576596344, 7.39166015735, 8.07476107798, 7.04207140922], 'cal/(mol*K)'),
        H298 = (21.4425502333,'kcal/mol'),
        S298 = (-2.48475725098,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cds-CdsCdsSs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cd u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cd)S2s",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   S2s u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cds)S2s",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   S2s u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cdd)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   S2s  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   S2s  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   S2s  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsCtSs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsCbSs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CddCsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cs  u0 {1,S}
4   S2s  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   S2s  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)CsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   S2s  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CddCdsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cd  u0 {1,S}
4   S2s  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s  u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cds)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s  u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s  u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2s  u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2s  u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s  u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cds)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s  u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)S2s",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2s  u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2s  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2s  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CddCtSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   S2s  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CtSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   S2s  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)CtSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   S2s  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CddCbSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   S2s  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CbSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   S2s  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)CbSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   S2s  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)C=SSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   S2s  u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsC=SSs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    label = "Cds-CdCC",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    label = "Cds-CdsCsCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.1,4.61,4.99,5.26,5.8,6.08,6.36],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (10.34,'kcal/mol','+|-',0.24),
        S298 = (-12.7,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "Cds-CdsCdsCs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "Cds-Cds(Cds-Cd)Cs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "Cds-Cds(Cds-Cds)Cs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.88,'kcal/mol','+|-',0.24),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CdCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "Cds-Cds(Cds-Cdd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Cs  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cs  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "Cds-Cds(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "Cds-CdsCdsCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "Cds-Cds(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {5,D}
3   CO u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "Cds-Cds(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {6,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,D}
5   C  u0 {3,D}
6   O2d u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "Cds-Cds(Cds-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {6,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,D}
5   Cd u0 {3,D}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (11.6,'kcal/mol','+|-',0.24),
        S298 = (-16.5,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-COCd from CD/CD2/ jwb est 6/97""",
    longDesc = 
u"""
AG Vandeputte, added 7 kcal/mol to the following value (see phd M Sabbe)
""",
)

entry(
    index = 213,
    label = "Cds-Cds(Cds-O2d)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   Cdd u0 {3,D}
6   O2d  u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-O2d)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "Cds-Cds(Cds-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cd-CdCs(CCO)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "Cds-Cds(Cds-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   O2d  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "Cds-Cds(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   C  u0 {2,D}
6   C  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "Cds-Cds(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   Cd u0 {2,D}
6   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.9,2.69,3.5,4.28,5.57,6.21,7.37],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (11.6,'kcal/mol','+|-',0.24),
        S298 = (-15.67,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CdCd Hf=3D est S,Cp mopac nov99""",
    longDesc = 
u"""
AG Vandeputte, added 7 kcal/mol to the following value (see phd M Sabbe)
""",
)

entry(
    index = 218,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,D}
5   Cd  u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   Cd  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cd-CdCs(CCO)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   Cd  u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   Cd  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "Cds-Cds(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,D}
5   Cdd u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   O2d  u0 {4,D}
8   O2d  u0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   O2d  u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   S2d u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   Cd  u0 {1,D}
7   C   u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "Cds-CdsCtCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.88,4.88,4.18,4.86,5.4,6.01],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.11,'kcal/mol','+|-',0.24),
        S298 = (-13.02,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CtCs RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 1858,
    label = "Cd-CdCs(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S} {6,S}
3   Ct  u0 {1,S} {7,T}
4   Cs  u0 {1,S}
5   R   u0 {2,S}
6   R   u0 {2,S}
7   N3t u0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.2,10.6,11.7,12.5,13.8,14.7,15.9],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (40.2,'kcal/mol','+|-',1.3),
        S298 = (17.9,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "Cds-CdsCtCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "Cds-CdsCt(Cds-O2d)",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "Cds-CdsCt(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "Cds-Cds(Cds-Cds)Ct",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.89,5.26,5.98,6.37,6.67,6.78,6.89],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (7.54,'kcal/mol','+|-',0.24),
        S298 = (-14.65,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CtCd RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    label = "Cds-Cds(Cds-Cdd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Ct  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 231,
    label = "Cds-Cds(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Ct  u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Ct  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 232,
    label = "Cds-Cds(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 233,
    label = "Cds-CdsCtCt",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.23,4.59,5.41,5.93,6.48,6.74,7.02],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.81,'kcal/mol','+|-',0.24),
        S298 = (-13.51,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CtCt RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 1837,
    label = "Cds-Cd(CtN3t)(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Ct  u0 {1,S} {5,T}
3   Ct  u0 {1,S} {6,T}
4   Cd  u0 {1,D}
5   N3t u0 {2,T}
6   N3t u0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (84.1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    label = "Cds-CdsCbCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.64,'kcal/mol','+|-',0.24),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CbCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "Cds-CdsCbCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "Cds-CdsCb(Cds-O2d)",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
    label = "Cds-Cds(Cds-Cd)Cb",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   C  u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
    label = "Cds-Cds(Cds-Cds)Cb",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (7.18,'kcal/mol','+|-',0.24),
        S298 = (-16.5,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CbCd BOZZELLI =3D Cd/Cs/Cb + (Cd/Cs/Cd - Cd/Cs/Cs)""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "Cds-Cds(Cds-Cdd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Cb  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "Cds-Cds(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cb  u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-Cds(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cb  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "Cds-Cds(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cd  u0 {1,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    label = "Cds-CdsCbCt",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22,3.14,4.54,4.11,5.06,5.79,6.71],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.7,'kcal/mol','+|-',0.24),
        S298 = (-17.04,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CbCt Hf=3D est S,Cp mopac nov99""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    label = "Cds-CdsCbCb",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8,'kcal/mol','+|-',0.24),
        S298 = (-16.5,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CbCb BOZZELLI =3D Cd/Cs/Cb + (Cd/Cs/Cb - Cd/Cs/Cs)""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    label = "Cds-CddCsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 245,
    label = "Cds-(Cdd-O2d)CsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([42.55,46.42,50,53.24,58.3,61.71,66.01],'J/(mol*K)','+|-',[4.76,4.76,4.76,4.76,4.76,4.76,4.76]),
        H298 = (0.5,'kJ/mol','+|-',4.06),
        S298 = (84.72,'J/(mol*K)','+|-',5.55),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 246,
    label = "Cds-(Cdd-Cd)CsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 247,
    label = "Cds-CddCdsCs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "Cds-(Cdd-O2d)(Cds-O2d)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "Cds-(Cdd-O2d)(Cds-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    label = "Cds-(Cdd-O2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.1,11.24,12.12,12.84,14,14.75,15.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-2.07,'kcal/mol','+|-',0.24),
        S298 = (19.65,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""{CCO/C/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   O2d  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cd-CdCs(CCO)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    label = "Cds-CddCdsCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    label = "Cds-(Cdd-O2d)(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   O2d  u0 {2,D}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 261,
    label = "Cds-(Cdd-O2d)(Cds-Cd)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   O2d  u0 {2,D}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 262,
    label = "Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   O2d  u0 {2,D}
6   Cd  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 263,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   O2d  u0 {2,D}
6   Cdd u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 264,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
8   O2d  u0 {5,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    label = "Cds-(Cdd-O2d)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2d  u0 {2,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 267,
    label = "Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2d  u0 {2,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2d  u0 {2,D}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   O2d  u0 {3,D}
7   Cd  u0 {4,D}
8   O2d  u0 {5,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   O2d  u0 {3,D}
7   Cd  u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 271,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2d  u0 {2,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   O2d  u0 {4,D}
8   O2d  u0 {5,D}
9   O2d  u0 {6,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 273,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   O2d  u0 {4,D}
8   O2d  u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 274,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   O2d  u0 {4,D}
8   C   u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 275,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   CO  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-O2d)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 276,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   C   u0 {4,D}
7   O2d  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 277,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   Cd  u0 {4,D}
7   O2d  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 278,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   Cdd u0 {4,D}
7   O2d  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
8   O2d  u0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 280,
    label = "Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CO  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   S2d u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   S2d u0 {3,D}
7   Cd  u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
9   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   S2d u0 {4,D}
8   C   u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 281,
    label = "Cds-(Cdd-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 283,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 284,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   Cd  u0 {4,D}
8   O2d  u0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 285,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   Cd  u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   O2d  u0 {5,D}
9   O2d  u0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   O2d  u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   S2d u0 {5,D}
9   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   S2d u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {1,D} {7,D}
5   Cdd u0 {2,D} {8,D}
6   Cdd u0 {3,D} {9,D}
7   C   u0 {4,D}
8   C   u0 {5,D}
9   C   u0 {6,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 290,
    label = "Cds-CddCtCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 291,
    label = "Cds-(Cdd-O2d)CtCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CtCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
    label = "Cds-(Cdd-Cd)CtCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
    label = "Cds-CddCtCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 294,
    label = "Cds-(Cdd-O2d)(Cds-O2d)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2d  u0 {2,D}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 295,
    label = "Cds-(Cdd-O2d)(Cds-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2d  u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 296,
    label = "Cds-(Cdd-O2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2d  u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 297,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2d  u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 299,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   O2d  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 300,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 303,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-O2d)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 304,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 305,
    label = "Cds-CddCtCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "Cds-(Cdd-O2d)CtCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CtCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 307,
    label = "Cds-(Cdd-Cd)CtCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    label = "Cds-CddCbCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 309,
    label = "Cds-(Cdd-O2d)CbCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CbCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "Cds-(Cdd-Cd)CbCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "Cds-CddCbCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cdd     u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 312,
    label = "Cds-(Cdd-O2d)(Cds-O2d)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d  u0 {2,D}
6   O2d  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 313,
    label = "Cds-(Cdd-O2d)(Cds-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d  u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "Cds-(Cdd-O2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d  u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 315,
    label = "Cds-(Cdd-O2d)(Cds-Cdd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d  u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 316,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   O2d  u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 317,
    label = "Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   O2d  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 318,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 319,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   C   u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 320,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   C   u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 321,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   O2d  u0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-O2d)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {5,S}
2   Cd  u0 {1,S} {4,D}
3   Cdd u0 {1,D} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "Cds-CddCbCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "Cds-(Cdd-O2d)CbCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CbCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 325,
    label = "Cds-(Cdd-Cd)CbCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 326,
    label = "Cds-CddCbCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 327,
    label = "Cds-(Cdd-O2d)CbCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = u'Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)CbCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "Cds-(Cdd-Cd)CbCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   C   u0 {2,D}
""",
    thermo = u'Cds-CdsCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsC=SC=S",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CS u0 {1,S} {5,D}
3   CS u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   C   u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   Cd  u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {2,D}
6   Cdd u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CS  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   S2d u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)C=S(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CS  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   C   u0 {3,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)C=SCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)C=SCt",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)C=SCb",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-Cd)C=SC=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   C   u0 {2,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cd)C=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   C   u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cds)C=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cd  u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd)C=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   Cd  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   Cdd u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-S2d)C=S",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CS  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)(Cds-Cdd-Cd)C=S",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cdd u0 {1,D} {6,D}
4   CS  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {8,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsCbC=S",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsCtC=S",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1204,
    label = "Cds-CdsC=SCs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.17744922706, 4.47896126176, 4.72673503827, 4.94835314901, 5.35598928914, 5.60960839053, 5.93003083679], 'cal/(mol*K)'),
        H298 = (9.54999260405,'kcal/mol'),
        S298 = (-11.561546716,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cds-CdsC=S(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CS u0 {1,S} {6,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,D}
5   C  u0 {3,D}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsC=S(Cds-Cds)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CS u0 {1,S} {6,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,D}
5   Cd u0 {3,D}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsC=S(Cds-Cdd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CS  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   Cdd u0 {3,D}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsC=S(Cds-Cdd-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   S2d u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-CdsC=S(Cds-Cdd-S2d)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   Cd  u0 {1,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cds-(Cdd-S2d)C=SC=S",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   CS  u0 {1,S} {6,D}
4   CS  u0 {1,S} {7,D}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1996,
    label = "Cd-CdCs(CO)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {5,D}
3   Cs u0 {1,S}
4   Cd u0 {1,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.33,16.82,18.64,20.42,23.2,25,27.1],'J/(mol*K)','+|-',[5.66,5.66,5.66,5.66,5.66,5.66,5.66]),
        H298 = (39,'kJ/mol','+|-',4.82),
        S298 = (-51.26,'J/(mol*K)','+|-',6.6),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 2011,
    label = "Cd-CdCs(CCO)",
    group = 
"""
1 * Cd  u0 {2,S} {4,S} {5,D}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   Cs  u0 {1,S}
5   Cd  u0 {1,D}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.68,24.05,24.63,25.07,25.64,25.84,25.7],'J/(mol*K)','+|-',[8,8,8,8,8,8,8]),
        H298 = (41.6,'kJ/mol','+|-',6.82),
        S298 = (-48.01,'J/(mol*K)','+|-',9.33),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1923,
    label = "Cds-CNH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1860,
    label = "Cd-CdHN3s",
    group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6,7,7.7,8.8,9.5,10.6],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2.2,'kcal/mol','+|-',1.4),
        S298 = (7.1,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1838,
    label = "Cd-CdH(N5dcOdOs)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S} {6,S}
3   N5dc u0 {1,S} {7,D} {8,S}
4   H   u0 {1,S}
5   R   u0 {2,S}
6   R   u0 {2,S}
7   O2d  u0 {3,D}
8   O2s  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.7,15.4,17.6,19.3,21.7,23.1,25],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2,'kcal/mol','+|-',1.3),
        S298 = (44.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1924,
    label = "Cds-CCN",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1859,
    label = "Cd-CdCsN3s",
    group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8,5,5.9,6.4,6.9,7.1,7.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (3.5,'kcal/mol','+|-',1.4),
        S298 = (-14.1,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1861,
    label = "Cd-CdCs(N5dcOdOs)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S} {6,S}
3   N5dc u0 {1,S} {7,D} {8,S}
4   Cs  u0 {1,S}
5   R   u0 {2,S}
6   R   u0 {2,S}
7   O2d  u0 {3,D}
8   O2s  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.1,14.3,16.1,17.5,19.3,20.3,21.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2.3,'kcal/mol','+|-',1.3),
        S298 = (24,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-SsSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'C=S-CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1184,
    label = "C=S-CsH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'C=S2-CsH',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1184,
    label = "C=S2-CsH",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d  u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95225814073, 7.63705491131, 8.40683220768, 9.10378489161, 10.0471814978, 10.6906716224, 11.9576252904], 'cal/(mol*K)'),
        H298 = (33.2342035561,'kcal/mol'),
        S298 = (28.5495829787,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1184,
    label = "C=S4-CsH",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   [S4d,S4dd]  u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.77881901595, 2.96959971599, 4.45094001034, 5.26374960375, 5.00177190182, 4.8377025391, 7.16010873159], 'cal/(mol*K)'),
        H298 = (-0.478741169387,'kcal/mol'),
        S298 = (7.3907123399,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1185,
    label = "C=S-CdsH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   [Cd,Cb] u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.40885277, 9.17894837, 10.55231358, 11.53334608, 12.80393881, 13.5732696, 14.6248566], 'cal/(mol*K)'),
        H298 = (24.84632887,'kcal/mol'),
        S298 = (33.96931166,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)H",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   H           u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)H",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   H   u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)H",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   H   u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-S2d)H",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   H   u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)H",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   H  u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1186,
    label = "C=S-CtH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.06778203, 8.96904398, 10.46889101, 10.17462715, 11.3773805, 12.32871893, 13.60047801], 'cal/(mol*K)'),
        H298 = (30.52965583,'kcal/mol'),
        S298 = (36.93883365,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)


entry(
    index = 1188,
    label = "C=S-C=SH",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   H  u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.79357871167, 9.17981198083, 10.4146749508, 11.4204907575, 12.8226577442, 13.6392606742, 14.5375239], 'cal/(mol*K)'),
        H298 = (26.959847035,'kcal/mol'),
        S298 = (35.6477055467,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "C=S-CC",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbCds",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cd)",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   Cb          u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cds)",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cb u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cdd)",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cb  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cdd-S2d)",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Cb  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Cb(Cds-Cdd-Cd)",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Cb  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CtCt",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbCb",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CdsCds",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cd u0 {1,S}
4   Cd u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * CS          u0 {2,S} {3,S} {4,D}
2   Cd          u0 {1,S} {5,D}
3   Cd          u0 {1,S} {6,D}
4   S2d         u0 {1,D}
5   [Cd,Cdd,CO] u0 {2,D}
6   [Cd,Cdd,CO] u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cdd u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2d u0 {1,D}
6   Cd  u0 {3,D}
7   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-S2d)(Cds-Cds)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {6,D}
4   Cdd u0 {2,D} {7,D}
5   S2d u0 {1,D}
6   Cd  u0 {3,D}
7   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * CS u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cd u0 {2,D}
6   Cd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cdd u0 {2,D}
6   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   S2d u0 {1,D}
7   C   u0 {4,D}
8   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   S2d u0 {1,D}
7   S2d u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)(Cds-Cdd-S2d)",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {6,D}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {7,D}
5   Cdd u0 {3,D} {8,D}
6   S2d u0 {1,D}
7   C   u0 {4,D}
8   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CtCds",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct u0 {1,S}
4   Cd u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cd)",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   Ct          u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cds)",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Ct u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cdd)",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Ct  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cdd-Cd)",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Ct  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-Ct(Cds-Cdd-S2d)",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Ct  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbCt",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1190,
    label = "C=S-CsCs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.6315349868, 3.88903959141, 4.29873787739, 4.73084194155, 5.05454023664, 5.14699169635, 5.62013561025], 'cal/(mol*K)'),
        H298 = (45.9721066913,'kcal/mol'),
        S298 = (-6.97470885371,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1191,
    label = "C=S-CdsCs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cd u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.14649045428, 7.30774449718, 8.03916845215, 8.47630549275, 8.72762424004, 8.70770162713, 8.82195641155], 'cal/(mol*K)'),
        H298 = (35.7486111616,'kcal/mol'),
        S298 = (1.21103537506,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)Cs",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   Cs          u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)Cs",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cs u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)Cs",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cs  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Cs  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   Cs  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1192,
    label = "C=S-CtCs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.96899473048, 6.19537092088, 7.18419887651, 6.54245688883, 7.05933692725, 7.4176532454, 7.98119046889], 'cal/(mol*K)'),
        H298 = (38.8862863267,'kcal/mol'),
        S298 = (5.05677970001,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = 1193,
    label = "C=S-CbCs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.4363793484, 6.5943094707, 7.4316060387, 7.98337508078, 8.34029114832, 8.35517844818, 8.46025901513], 'cal/(mol*K)'),
        H298 = (36.1211011497,'kcal/mol'),
        S298 = (1.88492091315,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1194,
    label = "C=S-C=SCs",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cs u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.40284525007, 6.15301246654, 6.82790622453, 7.36860771328, 7.88099860748, 8.03876034734, 8.26537373513], 'cal/(mol*K)'),
        H298 = (36.8722866147,'kcal/mol'),
        S298 = (4.08912740981,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "C=S-CtC=S",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Ct u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)C=S",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cd u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)C=S",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cdd u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)C=S",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {6,D}
5   S2d u0 {1,D}
6   C   u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-S2d)C=S",
    group = 
"""
1 * CS  u0 {2,S} {3,S} {5,D}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {6,D}
5   S2d u0 {1,D}
6   S2d u0 {4,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)C=S",
    group = 
"""
1 * CS u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   CS u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   Cd u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-C=SC=S",
    group = 
"""
1 * CS u0 {2,S} {3,S} {4,D}
2   CS u0 {1,S} {5,D}
3   CS u0 {1,S} {6,D}
4   S2d u0 {1,D}
5   S2d u0 {2,D}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbC=S",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   Cb u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1183,
    label = "C=S2d-HH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.082217973, 10.34894837, 11.52007648, 12.5, 14.07743786, 15.24856597, 17.13671128], 'cal/(mol*K)'),
        H298 = (27.70076482,'kcal/mol'),
        S298 = (56.50095602,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1183,
    label = "C=S4d-HH",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   [S4d,S4dd]  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.04281901595, 4.97859971599, 6.83894001034, 7.80174960375, 7.75477190182, 7.9497025391, 10.7851087316], 'cal/(mol*K)'),
        H298 = (-0.524741169388,'kcal/mol'),
        S298 = (26.8357123399,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

#entry(
#    index = 1183,
#    label = "C=S4dd-HH",
#    group =
#"""
#1 * CS u0 {2,D} {3,S} {4,S}
#2   S4dd  u0 {1,D}
#3   H  u0 {1,S}
#4   H  u0 {1,S}
#""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([9.08,10.35,11.52,12.50,14.08,15.25,17.14],'cal/(mol*K)'),
#        H298 = (27.70,'kcal/mol'),
#        S298 = (56.50,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
#    longDesc =
#u""""
#
#""",
#)

entry(
    index = 1183,
    label = "C=S6dd-HH",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S6dd  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.95579824536, 10.0277752396, 11.3648750033, 12.244198528, 13.5589902675, 14.5489075975, 15.9659730201], 'cal/(mol*K)'),
        H298 = (21.2831911444,'kcal/mol'),
        S298 = (48.0684224818,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1183,
    label = "C=S6ddd-HH",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   [S6ddd,S6td]  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.06116395226, 5.25141203381, 6.25460564926, 7.0126602295, 8.25123487459, 9.1285821619, 10.5825875859], 'cal/(mol*K)'),
        H298 = (51.4478684027,'kcal/mol'),
        S298 = (13.1959177111,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

#entry(
#    index = 1183,
#    label = "C=S6td-HH",
#    group =
#"""
#1 * CS u0 {2,D} {3,S} {4,S}
#2   S6td  u0 {1,D}
#3   H  u0 {1,S}
#4   H  u0 {1,S}
#""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([9.08,10.35,11.52,12.50,14.08,15.25,17.14],'cal/(mol*K)'),
#        H298 = (27.70,'kcal/mol'),
#        S298 = (56.50,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
#    longDesc =
#u""""
#
#""",
#)

entry(
    index = 1184,
    label = "C=S-HH",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'C=S2d-HH',
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 1189,
    label = "C=S-SH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'C=S-S2H',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1189,
    label = "C=S6-S2H",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   S2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.8063068392, 13.8828802176, 14.8642399279, 15.6959994354, 19.1295656113, 21.2791447402, 19.6062775134], 'cal/(mol*K)'),
        H298 = (35.4918464135,'kcal/mol'),
        S298 = (62.123120779,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1189,
    label = "C=S-S2H",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   S2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.0533481356, 9.15218051781, 9.60194321957, 10.1165535094, 12.4119530533, 13.8535912469, 13.3620031371], 'cal/(mol*K)'),
        H298 = (41.2463123033,'kcal/mol'),
        S298 = (28.2024548469,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1189,
    label = "C=S-S4H",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.1006915003, 9.34915936623, 9.56192614645, 10.2175505874, 13.0313562053, 14.858802241, 15.1716924156], 'cal/(mol*K)'),
        H298 = (45.89643333,'kcal/mol'),
        S298 = (41.7870620387,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1189,
    label = "C=S-S6H",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.50,9.98,11.08,11.93,13.14,13.95,15.08],'cal/(mol*K)'),
        H298 = (21.69,'kcal/mol'),
        S298 = (34.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1205,
    label = "C=S-CSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   C  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = u'C=S-CsSs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CbSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CdsSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cd u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cd)S2s",
    group = 
"""
1 * CS          u0 {2,S} {3,D} {4,S}
2   Cd          u0 {1,S} {5,D}
3   S2d         u0 {1,D}
4   S2s          u0 {1,S}
5   [Cd,Cdd,CO] u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cds)S2s",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   S2s u0 {1,S}
5   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd)S2s",
    group = 
"""
1 * CS  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   S2s  u0 {1,S}
5   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   S2s  u0 {1,S}
6   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * CS  u0 {2,S} {4,D} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {6,D}
4   S2d u0 {1,D}
5   S2s  u0 {1,S}
6   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "C=S-CtSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1206,
    label = "C=S-CsSs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.84556346258, 5.22827029389, 5.17153266391, 5.40431108429, 7.12234850701, 8.0817183396, 6.81739967109], 'cal/(mol*K)'),
        H298 = (56.1346270301,'kcal/mol'),
        S298 = (-9.69582189796,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = 1206,
    label = "C=S-S(CO)",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   CO u0 {1,S}
4   S  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.4,8.38,9.16,9.8,10.72,11.25,11.66],'cal/(mol*K)'),
        H298 = (21.35,'kcal/mol'),
        S298 = (14.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc =
u"""

""",
)

entry(
    index = -1,
    label = "C=S-C=SSs",
    group = 
"""
1 * CS u0 {2,S} {3,D} {4,S}
2   CS u0 {1,S} {5,D}
3   S2d u0 {1,D}
4   S2s u0 {1,S}
5   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1457,
    label = "C=S-OsH",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S  u0 {1,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = u'C=S2-OsH',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1457,
    label = "C=S2-OsH",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d  u0 {1,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.13313167017, 9.88093797664, 10.9119237115, 11.7070570064, 12.8773200938, 13.5771132715, 14.2635154964], 'cal/(mol*K)'),
        H298 = (22.6828162851,'kcal/mol'),
        S298 = (31.0247137104,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1457,
    label = "C=S4-OsH",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   [S4d,S4dd]  u0 {1,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.892979627798, 3.19728614046, 5.52167041187, 6.94889300719, 7.52040096492, 8.00349795019, 10.6631871255], 'cal/(mol*K)'),
        H298 = (-7.38399355949,'kcal/mol'),
        S298 = (1.7145134871,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1458,
    label = "C=S-CsOs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.09394187833, 7.07765404316, 7.60054264039, 8.11318792746, 8.79904631009, 9.05652205525, 9.03740155078], 'cal/(mol*K)'),
        H298 = (27.7301909574,'kcal/mol'),
        S298 = (-2.80932506824,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = 1459,
    label = "C=S-OsOs",
    group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.2956948106, 12.6669454475, 13.4222647329, 13.6755073124, 13.4978513997, 12.7808183775, 10.8772662834], 'cal/(mol*K)'),
        H298 = (17.1092825477,'kcal/mol'),
        S298 = (4.26991673259,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = 1459,
    label = "C=S-OsS",
    group =
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   S  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.48332224968, 9.80536676268, 10.2914472414, 10.9534328892, 13.5711209596, 14.9917430085, 13.6252566334], 'cal/(mol*K)'),
        H298 = (40.3869469458,'kcal/mol'),
        S298 = (13.4853425694,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 329,
    label = "Cs",
    group = 
"""
1 * Cs u0
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1919,
    label = "Cs-NHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1800,
    label = "Cs-N3sHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)'),
        H298 = (-10.08,'kcal/mol'),
        S298 = (30.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1920,
    label = "Cs-N3dHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1870,
    label = "Cs-(N3dCd)HHH",
    group = 
"""
1 * Cs       u0 {2,S} {3,S} {4,S} {5,S}
2   N3d      u0 {1,S} {6,D}
3   H        u0 {1,S}
4   H        u0 {1,S}
5   H        u0 {1,S}
6   [Cd,Cdd] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6,7.7,9.3,10.7,13.1,14.8,17.7],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-5.7,'kcal/mol','+|-',1.3),
        S298 = (30.4,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1801,
    label = "Cs-(N3dN3d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6,7.8,9.4,10.8,13.1,14.8,17.6],'cal/(mol*K)','+|-',[0.6,0.6,0.6,0.6,0.6,0.6,0.6]),
        H298 = (-9,'kcal/mol','+|-',0.8),
        S298 = (30.2,'cal/(mol*K)','+|-',0.8),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1921,
    label = "Cs-NCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1802,
    label = "Cs-N3sCsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.25,6.9,8.28,9.39,11.09,12.34,14.8],'cal/(mol*K)'),
        H298 = (-6.6,'kcal/mol'),
        S298 = (9.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1925,
    label = "Cs-N3dCHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1805,
    label = "Cs-(N3dN3d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,6.9,8.3,9.4,11.1,12.3,14.2],'cal/(mol*K)','+|-',[0.6,0.6,0.6,0.6,0.6,0.6,0.6]),
        H298 = (-5.5,'kcal/mol','+|-',0.8),
        S298 = (9.4,'cal/(mol*K)','+|-',0.8),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1869,
    label = "Cs-(N3dOd)CHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.8,13.6,15.2,16.7,18.9,20.5,23],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (21.4,'kcal/mol','+|-',1.3),
        S298 = (44.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1871,
    label = "Cs-(N3dCd)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,7.2,8.7,9.8,11.6,12.8,14.7],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (-2.9,'kcal/mol','+|-',1.7),
        S298 = (8.6,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1926,
    label = "Cs-N5dcCsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1841,
    label = "Cs-(N5dcOdOs)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d  u0 {2,D}
7   O2s  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.9,15.8,18.3,20.3,23.3,25.4,28.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-14.8,'kcal/mol','+|-',1.3),
        S298 = (48.9,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1927,
    label = "Cs-NCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1803,
    label = "Cs-N3sCsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.67,6.32,7.64,8.39,9.56,10.23,11.905],'cal/(mol*K)'),
        H298 = (-5.2,'kcal/mol'),
        S298 = (-11.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1928,
    label = "Cs-N3dCsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1868,
    label = "Cs-(N3dOd)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.2,12.7,14,15.1,16.8,17.9,19.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (23.4,'kcal/mol','+|-',1.3),
        S298 = (23.1,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1929,
    label = "Cs-N5dcCsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1842,
    label = "Cs-(N5dcOdOs)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d  u0 {2,D}
7   O2s  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.6,16.1,18.1,19.6,21.8,23.2,25.1],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-13.9,'kcal/mol','+|-',1.3),
        S298 = (27.5,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1930,
    label = "Cs-NCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1804,
    label = "Cs-N3sCsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.35,6.16,7.31,7.91,8.49,8.5,8.525],'cal/(mol*K)'),
        H298 = (-3.2,'kcal/mol'),
        S298 = (-34.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1806,
    label = "Cs-(N3dN3d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   N3d u0 {1,S} {3,D}
3   N3d u0 {2,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-3.3,'kcal/mol'),
        S298 = (-11.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1807,
    label = "Cs-(N3dN3d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   N3d u0 {1,S} {3,D}
3   N3d u0 {2,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-1.9,'kcal/mol'),
        S298 = (-34.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1931,
    label = "Cs-N3dCsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1867,
    label = "Cs-(N3dOd)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.2,13.3,14,14.5,15.3,15.7,16.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (24.1,'kcal/mol','+|-',1.3),
        S298 = (1.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1932,
    label = "Cs-N5dcCsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1843,
    label = "Cs-(N5dcOdOs)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d  u0 {2,D}
7   O2s  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.5,16,17.8,18.9,20.3,21.1,21.9],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-12.7,'kcal/mol','+|-',1.3),
        S298 = (5.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1933,
    label = "Cs-NNCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1934,
    label = "Cs-N5dcN5dcCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   N5dc u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1933,
    label = "Cs-NNCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1846,
    label = "Cs-(N5dcOdOs)(N5dcOdOs)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S} {6,D} {7,S}
3   N5dc u0 {1,S} {8,D} {9,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d  u0 {2,D}
7   O2s  u0 {2,S}
8   O2d  u0 {3,D}
9   O2s  u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-14.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 330,
    label = "Cs-HHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.43,9.84,11.14,12.41,15,17.25,20.63],'cal/(mol*K)','+|-',[0.06,0.06,0.06,0.06,0.06,0.06,0.06]),
        H298 = (-17.9,'kcal/mol','+|-',0.1),
        S298 = (49.41,'cal/(mol*K)','+|-',0.05),
    ),
    shortDesc = u"""CHEMKIN DATABASE S(group) = S(CH4) + Rln(12)""",
    longDesc = 
u"""

""",
)

entry(
    index = 331,
    label = "Cs-CHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsHHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "Cs-CsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-10.2,'kcal/mol','+|-',0.12),
        S298 = (30.41,'cal/(mol*K)','+|-',0.08),
    ),
    shortDesc = u"""Cs-CsHHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 333,
    label = "Cs-CdsHHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "Cs-(Cds-O2d)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.31,32.07,38.44,44.06,53.36,60.63,72.47],'J/(mol*K)'),
        H298 = (-42.9,'kJ/mol'),
        S298 = (127.12,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 335,
    label = "Cs-(Cds-Cd)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "Cs-(Cds-Cds)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.04,0.04,0.04,0.04,0.04,0.04,0.04]),
        H298 = (-10.2,'kcal/mol','+|-',0.08),
        S298 = (30.41,'cal/(mol*K)','+|-',0.04),
    ),
    shortDesc = u"""Cs-CdHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "Cs-(Cds-Cdd)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "Cs-(Cds-Cdd-O2d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.31,32.07,38.44,44.06,53.36,60.63,72.47],'J/(mol*K)'),
        H298 = (-42.9,'kJ/mol'),
        S298 = (127.12,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "Cs-(Cds-Cdd-Cd)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1862,
    label = "Cs-(CdN3d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.2,7.8,9.4,10.8,13,14.8,17.6],'cal/(mol*K)'),
        H298 = (-10.2,'kcal/mol'),
        S298 = (30.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 340,
    label = "Cs-CtHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-10.2,'kcal/mol','+|-',0.15),
        S298 = (30.41,'cal/(mol*K)','+|-',0.08),
    ),
    shortDesc = u"""Cs-CtHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 1863,
    label = "Cs-(CtN3t)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.5,14.6,16.6,18.3,21.1,23.4,26.9],'cal/(mol*K)','+|-',[1.3,1.3,1.3,1.3,1.3,1.3,1.3]),
        H298 = (17.7,'kcal/mol','+|-',1.9),
        S298 = (60.2,'cal/(mol*K)','+|-',1.7),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "Cs-CbHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-10.2,'kcal/mol','+|-',0.18),
        S298 = (30.41,'cal/(mol*K)','+|-',0.14),
    ),
    shortDesc = u"""Cs-CbHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 1176,
    label = "Cs-C=SHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.4935059316, 9.3724018093, 11.0556979813, 12.4887855292, 14.9559994817, 16.8815710718, 19.7162228249], 'cal/(mol*K)'),
        H298 = (-19.6399730397,'kcal/mol'),
        S298 = (42.8874500269,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 342,
    label = "Cs-OsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.31,32.07,38.44,44.06,53.36,60.63,72.47],'J/(mol*K)'),
        H298 = (-42.9,'kJ/mol'),
        S298 = (127.12,'J/(mol*K)'),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 343,
    label = "Cs-OsOsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.35,43.68,53.55,58.15,60.86,61.66,63.53],'J/(mol*K)','+|-',[5.77,5.77,5.77,5.77,5.77,5.77,5.77]),
        H298 = (-67.5,'kJ/mol','+|-',4.92),
        S298 = (17.89,'J/(mol*K)','+|-',6.74),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 344,
    label = "Cs-OsOsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.54,6,7.17,8.05,9.31,10.05,10.05],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-21.23,'kcal/mol','+|-',0.2),
        S298 = (-12.07,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OOOH BOZZELLI del C/C2/O - C/C3/O, series !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1451,
    label = "Cs-OsSHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-OsS2HH',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1451,
    label = "Cs-OsS2HH",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.58461692317, 10.174812054, 11.398259525, 12.336734417, 14.7520792095, 16.1563408637, 15.9749540541], 'cal/(mol*K)'),
        H298 = (0.705722681584,'kcal/mol'),
        S298 = (13.8721603447,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1451,
    label = "Cs-OsS4HH",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.03891418598, 7.95339440592, 9.32972409719, 10.660974759, 14.3902045552, 16.6197317611, 16.955551399], 'cal/(mol*K)'),
        H298 = (5.90878746573,'kcal/mol'),
        S298 = (7.94345635421,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1451,
    label = "Cs-OsSSH",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-OsS2S2H',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1451,
    label = "Cs-OsS2S2H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S2s  u0 {1,S}
4   S2s  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.48,8.15,9.41,10.40,11.71,12.83,14.46],'cal/(mol*K)'),
        H298 = (-10.34,'kcal/mol'),
        S298 = (6.83,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1451,
    label = "Cs-OsS4S2H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S2s  u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.66997099311, 9.00483461648, 10.5646632253, 11.984574224, 16.5986714005, 18.7774372943, 16.4993909768], 'cal/(mol*K)'),
        H298 = (16.6791013071,'kcal/mol'),
        S298 = (-9.97018023845,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1464,
    label = "Cs-OsOsSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-OsOsS2H',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1464,
    label = "Cs-OsOsS2H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   S2s  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.27783418733, 9.23511471152, 10.6840134718, 11.6953526612, 14.0731919328, 15.029634119, 13.762851273], 'cal/(mol*K)'),
        H298 = (-6.37416373208,'kcal/mol'),
        S298 = (-7.32747360597,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1464,
    label = "Cs-OsOsS4H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.76893433013, 7.61288594367, 8.69719383287, 9.84999035805, 13.1722510427, 15.0147869446, 14.5100079032], 'cal/(mol*K)'),
        H298 = (-3.26995672739,'kcal/mol'),
        S298 = (-13.065714252,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1162,
    label = "Cs-SsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-S2sHHH',
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1162,
    label = "Cs-S2sHHH",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S2s  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.62255088729, 8.818021004, 10.2204111633, 11.5277313902, 14.8728738391, 17.1400608138, 18.5155362331], 'cal/(mol*K)'),
        H298 = (-0.266824037763,'kcal/mol'),
        S298 = (38.1435056581,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1162,
    label = "Cs-S4HHH",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   [S4s,S4d,S4b,S4t]  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.51677394708, 6.86372625486, 8.09853487423, 9.44653401363, 13.6122958382, 16.4597030563, 18.2915425132], 'cal/(mol*K)'),
        H298 = (5.62317621346,'kcal/mol'),
        S298 = (33.6770940272,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1162,
    label = "Cs-S6HHH",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   [S6s,S6d,S6dd,S6t,S6td]  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.93420770036, 7.17735696483, 8.84577118379, 10.3803637665, 13.8558568671, 16.2223203738, 18.1814025585], 'cal/(mol*K)'),
        H298 = (-2.59179368118,'kcal/mol'),
        S298 = (43.2662575858,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1167,
    label = "Cs-SsSsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.08135961729, 11.1258813614, 12.1366013983, 13.0368579305, 16.9505393953, 19.0042436075, 17.4716320778], 'cal/(mol*K)'),
        H298 = (15.2589609227,'kcal/mol'),
        S298 = (20.0373165234,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1201,
    label = "Cs-SsSsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   S  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.12365553088, 12.0863192878, 12.8981207262, 13.4536488031, 17.7884094499, 19.6563019604, 16.0423779158], 'cal/(mol*K)'),
        H298 = (27.7513137844,'kcal/mol'),
        S298 = (7.69014132889,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 345,
    label = "Cs-CCHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsCsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 346,
    label = "Cs-CsCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.95,8.25,9.35,11.07,12.34,14.25],'cal/(mol*K)','+|-',[0.04,0.04,0.04,0.04,0.04,0.04,0.04]),
        H298 = (-4.93,'kcal/mol','+|-',0.05),
        S298 = (9.42,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CsCsHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 347,
    label = "Cs-CdsCsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 348,
    label = "Cs-(Cds-O2d)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.91,30.8,34.98,38.91,45.56,50.73,58.93],'J/(mol*K)','+|-',[1.53,1.53,1.53,1.53,1.53,1.53,1.53]),
        H298 = (-21.5,'kJ/mol','+|-',1.3),
        S298 = (40.32,'J/(mol*K)','+|-',1.78),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 349,
    label = "Cs-(Cds-Cd)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "Cs-(Cds-Cds)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.36],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.76,'kcal/mol','+|-',0.16),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-CdCsHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "Cs-(Cds-Cdd)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 352,
    label = "Cs-(Cds-Cdd-O2d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.35,6.83,8.25,9.45,11.19,12.46,14.34],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.723,'kcal/mol','+|-',0.16),
        S298 = (9.37,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{C/C/H2/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 353,
    label = "Cs-(Cds-Cdd-Cd)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1864,
    label = "Cs-(CdN3d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.9,8.1,9.2,10.9,12.2,14.1],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (-5.1,'kcal/mol','+|-',1.7),
        S298 = (10.1,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 354,
    label = "Cs-CdsCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 355,
    label = "Cs-(Cds-O2d)(Cds-O2d)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.77,32.81,37.1,40.67,46.39,50.85,58.25],'J/(mol*K)','+|-',[4.19,4.19,4.19,4.19,4.19,4.19,4.19]),
        H298 = (-10,'kJ/mol','+|-',3.57),
        S298 = (40.1,'J/(mol*K)','+|-',4.88),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 356,
    label = "Cs-(Cds-O2d)(Cds-Cd)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.94,31.41,36.47,40.49,46.72,51.49,59.29],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (-16.9,'kJ/mol','+|-',2.85),
        S298 = (40.18,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 357,
    label = "Cs-(Cds-O2d)(Cds-Cds)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.75,7.11,8.92,10.32,12.16,13.61,13.61],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-3.8,'kcal/mol','+|-',0.16),
        S298 = (6.31,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-COCdHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 358,
    label = "Cs-(Cds-O2d)(Cds-Cdd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 359,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 360,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 361,
    label = "Cs-(Cds-Cd)(Cds-Cd)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 362,
    label = "Cs-(Cds-Cds)(Cds-Cds)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.8,8.4,9.6,11.3,12.6,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.29,'kcal/mol','+|-',0.16),
        S298 = (10.2,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-CdCdHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 363,
    label = "Cs-(Cds-Cdd)(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 365,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 366,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 367,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.68,8.28,9.58,10.61,12.04,13.13,14.87],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.301,'kcal/mol','+|-',0.16),
        S298 = (7.18,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{C/H2/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 368,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-Cd(CCO)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 369,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   H   u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2010,
    label = "Cs-Cd(CCO)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.85,31.99,37.06,41.14,47.42,52.15,59.73],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-22.2,'kJ/mol','+|-',5.9),
        S298 = (37.92,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 370,
    label = "Cs-CtCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.95,6.56,7.93,9.08,10.86,12.19,14.2],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-4.73,'kcal/mol','+|-',0.28),
        S298 = (10.3,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CtCsHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 1832,
    label = "Cs-(CtN3t)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.3,13.5,15.3,16.8,19.2,20.9,23.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (22.9,'kcal/mol','+|-',1.3),
        S298 = (39.8,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 371,
    label = "Cs-CtCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 372,
    label = "Cs-(Cds-O2d)CtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.85,6.22,8.01,9.43,11.29,12.76,12.76],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-5.4,'kcal/mol','+|-',0.28),
        S298 = (7.68,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-COCtHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 373,
    label = "Cs-(Cds-Cd)CtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 374,
    label = "Cs-(Cds-Cds)CtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,6.33,7.9,9.16,10.93,12.29,13.43],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-3.49,'kcal/mol','+|-',0.28),
        S298 = (9.31,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CtCdHH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 375,
    label = "Cs-(Cds-Cdd)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 376,
    label = "Cs-(Cds-Cdd-O2d)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-Cd(CCO)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 377,
    label = "Cs-(Cds-Cdd-Cd)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 378,
    label = "Cs-CtCtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4,6.07,7.71,9.03,10.88,12.3,12.48],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-0.82,'kcal/mol','+|-',0.28),
        S298 = (10.04,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CtCtHH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 379,
    label = "Cs-CbCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.84,7.61,8.98,10.01,11.49,12.54,13.76],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.86,'kcal/mol','+|-',0.2),
        S298 = (9.34,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = u"""Cs-CbCsHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 380,
    label = "Cs-CbCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 381,
    label = "Cs-(Cds-O2d)CbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.38,7.59,9.25,10.51,12.19,13.52,13.52],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.4,'kcal/mol','+|-',0.2),
        S298 = (5.89,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = u"""Cs-COCbHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 382,
    label = "Cs-(Cds-Cd)CbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 383,
    label = "Cs-(Cds-Cds)CbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.51,6.76,8.61,10.01,11.97,13.4,15.47],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-4.29,'kcal/mol','+|-',0.2),
        S298 = (2,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = u"""Cs-CbCdHH Hf=Stein S,Cp=3D mopac nov99""",
    longDesc = 
u"""

""",
)

entry(
    index = 384,
    label = "Cs-(Cds-Cdd)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 385,
    label = "Cs-(Cds-Cdd-O2d)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-Cd(CCO)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 386,
    label = "Cs-(Cds-Cdd-Cd)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 387,
    label = "Cs-CbCtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.28,6.43,8.16,9.5,11.36,12.74,13.7],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-4.29,'kcal/mol','+|-',0.28),
        S298 = (9.84,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CbCtHH Hf=Stein S,Cp=3D mopac nov99""",
    longDesc = 
u"""

""",
)

entry(
    index = 388,
    label = "Cs-CbCbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.67,7.7,9.31,10.52,12.21,13.47,15.11],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-4.29,'kcal/mol','+|-',0.2),
        S298 = (8.07,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = u"""Cs-CbCbHH Hf=3Dbsn/Cs/Cd2/H2 S,Cp=3D mopac nov99""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1177,
    label = "Cs-C=SCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.47965183744, 8.26802269894, 9.70355245568, 10.8258991631, 12.7346574438, 14.1409235874, 16.0790635473], 'cal/(mol*K)'),
        H298 = (-13.6897315437,'kcal/mol'),
        S298 = (21.7286081631,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 389,
    label = "Cs-CCCH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsCsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 390,
    label = "Cs-CsCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.54,6,7.17,8.05,9.31,10.05,11.17],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (-1.9,'kcal/mol','+|-',0.15),
        S298 = (-12.07,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CsCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 391,
    label = "Cs-CdsCsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 392,
    label = "Cs-(Cds-O2d)CsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.68,27.86,31.26,34,38.07,41,45.46],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (-5.4,'kJ/mol','+|-',2.85),
        S298 = (-47.41,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 393,
    label = "Cs-(Cds-Cd)CsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 394,
    label = "Cs-(Cds-Cds)CsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,11.28],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.48,'kcal/mol','+|-',0.27),
        S298 = (-11.69,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 395,
    label = "Cs-(Cds-Cdd)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 396,
    label = "Cs-(Cds-Cdd-O2d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.23,27.55,32.36,35.85,40.37,43.16,46.94],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-11.1,'kJ/mol','+|-',5.9),
        S298 = (-47.59,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 397,
    label = "Cs-(Cds-Cdd-Cd)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,11.28],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.48,'kcal/mol','+|-',0.27),
        S298 = (-11.69,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 1865,
    label = "Cs-(CdN3d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5,6.5,7.5,8.2,9.3,9.9,10.9],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (-1.6,'kcal/mol','+|-',1.7),
        S298 = (-11.2,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 398,
    label = "Cs-CtCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,5.61,6.85,7.78,9.1,9.9,11.12],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.72,'kcal/mol','+|-',0.27),
        S298 = (-11.19,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 1833,
    label = "Cs-(CtN3t)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11,12.7,14.1,15.4,17.3,18.6,21.85],'cal/(mol*K)'),
        H298 = (25.8,'kcal/mol'),
        S298 = (19.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 399,
    label = "Cs-CbCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.88,6.66,7.9,8.75,9.73,10.25,10.68],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-0.98,'kcal/mol','+|-',0.27),
        S298 = (-12.15,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 400,
    label = "Cs-CdsCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 401,
    label = "Cs-(Cds-O2d)(Cds-O2d)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-CsCsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 402,
    label = "Cs-(Cds-O2d)(Cds-Cd)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.32,32.99,35.49,37.28,39.75,41.6,44.96],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (-2.2,'kJ/mol','+|-',2.85),
        S298 = (-50.47,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 403,
    label = "Cs-(Cds-O2d)(Cds-Cds)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 404,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 405,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 406,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 407,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 408,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28,6.54,7.67,8.48,9.45,10.18,11.24],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.1,'kcal/mol','+|-',0.27),
        S298 = (-13.03,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCdCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 409,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 411,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 412,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 413,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.19,28,33.91,38.75,46.07,51.36,59.45],'J/(mol*K)','+|-',[3.46,3.46,3.46,3.46,3.46,3.46,3.46]),
        H298 = (-21.1,'kJ/mol','+|-',2.95),
        S298 = (40.95,'J/(mol*K)','+|-',4.04),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 414,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-CsCd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 415,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2008,
    label = "Cs-CsCd(CCO)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.45,31.59,36.01,38.8,42.13,44.21,47.25],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-10.4,'kJ/mol','+|-',5.9),
        S298 = (-54.03,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 416,
    label = "Cs-CtCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 417,
    label = "Cs-(Cds-O2d)CtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 418,
    label = "Cs-(Cds-Cd)CtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 419,
    label = "Cs-(Cds-Cds)CtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.55,7.21,8.39,9.17,10,10.61,10.51],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-6.9,'kcal/mol','+|-',0.27),
        S298 = (-13.48,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCdCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 420,
    label = "Cs-(Cds-Cdd)CtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 421,
    label = "Cs-(Cds-Cdd-O2d)CtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-CsCd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 422,
    label = "Cs-(Cds-Cdd-Cd)CtCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 423,
    label = "Cs-CbCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 424,
    label = "Cs-(Cds-O2d)CbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 425,
    label = "Cs-(Cds-Cd)CbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 426,
    label = "Cs-(Cds-Cds)CbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.5,6.57,8.07,8.89,9.88,10.39,10.79],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.56,'kcal/mol','+|-',0.27),
        S298 = (-11.77,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCdCsH BOZZELLI =3D Cs/Cs2/Cd/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index = 427,
    label = "Cs-(Cds-Cdd)CbCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 428,
    label = "Cs-(Cds-Cdd-O2d)CbCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-CsCd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 429,
    label = "Cs-(Cds-Cdd-Cd)CbCsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 430,
    label = "Cs-CtCtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.27,5.32,6.9,8.03,9.33,10.21,9.38],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.72,'kcal/mol','+|-',0.27),
        S298 = (-11.61,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCtCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 431,
    label = "Cs-CbCtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.27,7.58,8.48,9.52,10.1,10.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.55,'kcal/mol','+|-',0.27),
        S298 = (-11.65,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCtCsH BOZZELLI =3D Cs/Cs2/Cb/H + (Cs/Cs2/Ct/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index = 432,
    label = "Cs-CbCbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.22,7.32,8.63,8.45,10.15,10.45,10.89],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.06,'kcal/mol','+|-',0.27),
        S298 = (-12.23,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCbCsCs BOZZELLI =3D Cs/Cs2/Cb/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index = 433,
    label = "Cs-CdsCdsCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 434,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   CO u0 {1,S} {8,D}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = u'Cs-CsCsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 435,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   H  u0 {1,S}
6   C  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 436,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   H  u0 {1,S}
6   Cd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 437,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   H   u0 {1,S}
6   Cdd u0 {4,D}
7   O2d  u0 {2,D}
8   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 438,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 439,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 440,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.26,34.41,37.4,39.22,41.43,43.04,46.12],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (2.9,'kJ/mol','+|-',2.85),
        S298 = (-53.2,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 441,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 442,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 443,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 444,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 445,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 446,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 447,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 448,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    O2d  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 449,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 450,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.51,5.96,7.13,7.98,9.06,9.9,11.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (0.41,'kcal/mol','+|-',0.27),
        S298 = (-11.82,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCdCdH RAMAN & GREEN JPC 2002""",
    longDesc = 
u"""

""",
)

entry(
    index = 451,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 453,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 454,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 455,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 456,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-CdCd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 457,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 458,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 459,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 460,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 461,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-CdCd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 462,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    H   u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2009,
    label = "Cs-CdCd(CCO)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.62,35.4,39.24,41.25,43.4,44.87,47.43],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-6.8,'kJ/mol','+|-',5.9),
        S298 = (-55.37,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 463,
    label = "Cs-CtCdsCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 464,
    label = "Cs-(Cds-O2d)(Cds-O2d)CtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 465,
    label = "Cs-(Cds-O2d)(Cds-Cd)CtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 466,
    label = "Cs-(Cds-O2d)(Cds-Cds)CtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 467,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 468,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 469,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 470,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 471,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.68,7.85,8.62,9.16,9.81,10.42,10.49],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.88,'kcal/mol','+|-',0.27),
        S298 = (-13.75,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCdCdH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 472,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 473,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-CdCd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 474,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 475,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 476,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 477,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 478,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 479,
    label = "Cs-CbCdsCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 480,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 481,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 482,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 483,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 484,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 485,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 486,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 487,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.12,6.51,8.24,9,10.03,10.53,10.89],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.39,'kcal/mol','+|-',0.27),
        S298 = (-11.39,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCdCdH BOZZELLI =3D Cs/Cs/Cd2/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index = 488,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 489,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-CdCd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 490,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 491,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 492,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 493,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 494,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 495,
    label = "Cs-CtCtCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 496,
    label = "Cs-CtCt(Cds-O2d)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 497,
    label = "Cs-CtCt(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 498,
    label = "Cs-CtCt(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.58,5.68,7.11,8.12,9.27,10.13,9.44],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (4.73,'kcal/mol','+|-',0.27),
        S298 = (-11.46,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCtCdH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 499,
    label = "Cs-CtCt(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-CtCt(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 500,
    label = "Cs-CtCt(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-CdCd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCt(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 501,
    label = "Cs-CtCt(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 502,
    label = "Cs-CbCtCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-CbCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 503,
    label = "Cs-CbCt(Cds-O2d)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 504,
    label = "Cs-CbCt(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-CbCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 505,
    label = "Cs-CbCt(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 506,
    label = "Cs-CbCt(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-CbCt(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 507,
    label = "Cs-CbCt(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCt(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 508,
    label = "Cs-CbCt(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-CbCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 509,
    label = "Cs-CbCbCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-CbCb(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 510,
    label = "Cs-CbCb(Cds-O2d)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCb(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 511,
    label = "Cs-CbCb(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 512,
    label = "Cs-CbCb(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-CbCb(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 513,
    label = "Cs-CbCb(Cds-Cdd-O2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-CdCd(CCO)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCb(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 514,
    label = "Cs-CbCb(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-CbCb(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 515,
    label = "Cs-CtCtCtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.03,5.27,6.78,7.88,9.14,10.08,8.47],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (10.11,'kcal/mol','+|-',0.27),
        S298 = (-10.46,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCtCtH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index = 516,
    label = "Cs-CbCtCtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 517,
    label = "Cs-CbCbCtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 518,
    label = "Cs-CbCbCbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.56,7.98,9.36,10.15,10.57,10.65,9.7],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-0.34,'kcal/mol','+|-',0.27),
        S298 = (-12.31,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCbCbH BOZZELLI =3D Cs/Cs/Cb2/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)H",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    H   u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CtH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCtH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCtCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CbH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCtC=SH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=SH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   CS u0 {1,S} {8,D}
5   H  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1178,
    label = "Cs-C=SCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.63002909103, 7.29241553164, 8.54462149922, 9.42731494233, 10.8633929156, 11.7650057155, 12.6640869024], 'cal/(mol*K)'),
        H298 = (-8.05815102131,'kcal/mol'),
        S298 = (-1.20970586483,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CtCtC=SH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCbC=SH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   H  u0 {1,S}
6   C  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   H  u0 {1,S}
6   Cd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   H   u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 519,
    label = "Cs-CCCC",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 520,
    label = "Cs-CsCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,6.13,7.36,8.12,8.77,8.76,8.12],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (0.5,'kcal/mol','+|-',0.27),
        S298 = (-35.1,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CsCsCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 521,
    label = "Cs-CdsCsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 522,
    label = "Cs-(Cds-O2d)CsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.68,27.48,30.12,31.51,32.36,32.39,32.42],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (4.6,'kJ/mol','+|-',2.85),
        S298 = (-140.94,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 523,
    label = "Cs-(Cds-Cd)CsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 524,
    label = "Cs-(Cds-Cds)CsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.68,'kcal/mol','+|-',0.27),
        S298 = (-34.72,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCsCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 525,
    label = "Cs-(Cds-Cdd)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 526,
    label = "Cs-(Cds-Cdd-O2d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.63,27.65,31.98,34.41,36.16,36.25,35.2],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (-4.5,'kJ/mol','+|-',5.9),
        S298 = (-144.08,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 527,
    label = "Cs-(Cds-Cdd-Cd)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1866,
    label = "Cs-(CdN3d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,6.6,7.3,7.5,7.8,7.8,7.7],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (0.6,'kcal/mol','+|-',1.7),
        S298 = (-33.5,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 528,
    label = "Cs-CtCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,6.79,8.09,8.78,9.19,8.96,7.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.81,'kcal/mol','+|-',0.27),
        S298 = (-35.18,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCsCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 1834,
    label = "Cs-(CtN3t)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3t u0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.4,13.4,14.6,15.3,16.3,16.7,17.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (28.3,'kcal/mol','+|-',1.3),
        S298 = (-3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 529,
    label = "Cs-CbCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,6.79,8.09,8.78,9.19,8.96,7.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.81,'kcal/mol','+|-',0.26),
        S298 = (-35.18,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCsCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 530,
    label = "Cs-CdsCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 531,
    label = "Cs-(Cds-O2d)(Cds-O2d)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.76,33.42,32.6,31.91,31.01,30.55,30.35],'J/(mol*K)','+|-',[5.08,5.08,5.08,5.08,5.08,5.08,5.08]),
        H298 = (14.9,'kJ/mol','+|-',4.33),
        S298 = (-146.69,'J/(mol*K)','+|-',5.92),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 532,
    label = "Cs-(Cds-O2d)(Cds-Cd)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.01,30.13,32.44,33.51,33.75,33.26,32.55],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]),
        H298 = (9.8,'kJ/mol','+|-',2.85),
        S298 = (-146.74,'J/(mol*K)','+|-',3.9),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 533,
    label = "Cs-(Cds-O2d)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 534,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 535,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 536,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 537,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 538,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.68,'kcal/mol','+|-',0.26),
        S298 = (-34.72,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CdCdCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 539,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 541,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 542,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 543,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.73,8.1,9.02,9.53,9.66,9.52,8.93],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-2.987,'kcal/mol','+|-',0.26),
        S298 = (-36.46,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""{C/C2/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 544,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-CsCsCd(CCO)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 545,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   Cs  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2007,
    label = "Cs-CsCsCd(CCO)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.48,31.89,35.19,36.68,37.19,36.66,34.96],'J/(mol*K)','+|-',[6.93,6.93,6.93,6.93,6.93,6.93,6.93]),
        H298 = (2.9,'kJ/mol','+|-',5.9),
        S298 = (-144.6,'J/(mol*K)','+|-',8.08),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 546,
    label = "Cs-CtCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 547,
    label = "Cs-(Cds-O2d)CtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 548,
    label = "Cs-(Cds-Cd)CtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 549,
    label = "Cs-(Cds-Cds)CtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.7,8.16,8.92,9.34,9.16,7.14],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.99,'kcal/mol','+|-',0.26),
        S298 = (-34.8,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCdCsCs BOZZELLI =3D Cs/Cs3/Cd + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 550,
    label = "Cs-(Cds-Cdd)CtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 551,
    label = "Cs-(Cds-Cdd-O2d)CtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-CsCsCd(CCO)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 552,
    label = "Cs-(Cds-Cdd-Cd)CtCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 553,
    label = "Cs-CbCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 554,
    label = "Cs-(Cds-O2d)CbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 555,
    label = "Cs-(Cds-Cd)CbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 556,
    label = "Cs-(Cds-Cds)CbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.7,8.16,8.92,9.34,9.16,7.14],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.99,'kcal/mol','+|-',0.26),
        S298 = (-34.8,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCdCsCs BOZZELLI =3D Cs/Cs3/Cb + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 557,
    label = "Cs-(Cds-Cdd)CbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 558,
    label = "Cs-(Cds-Cdd-O2d)CbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-CsCsCd(CCO)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 559,
    label = "Cs-(Cds-Cdd-Cd)CbCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 560,
    label = "Cs-CtCtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.16,'kcal/mol','+|-',0.26),
        S298 = (-35.26,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCtCsCs BOZZELLI =3D Cs/Cs3/Ct + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 1835,
    label = "Cs-(CtN3t)(CtN3t)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Ct  u0 {1,S} {7,T}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3t u0 {2,T}
7   N3t u0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (28.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 561,
    label = "Cs-CbCtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.16,'kcal/mol','+|-',0.26),
        S298 = (-35.26,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCsCs BOZZELLI =3D Cs/Cs3/Cb + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 562,
    label = "Cs-CbCbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.16,'kcal/mol','+|-',0.26),
        S298 = (-35.26,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 563,
    label = "Cs-CdsCdsCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 564,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   CO u0 {1,S} {8,D}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 565,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Cs u0 {1,S}
6   C  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.99,39.53,39.94,39.09,36.71,34.8,32.51],'J/(mol*K)','+|-',[5.08,5.08,5.08,5.08,5.08,5.08,5.08]),
        H298 = (19.9,'kJ/mol','+|-',4.33),
        S298 = (-150.69,'J/(mol*K)','+|-',5.92),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 566,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Cs u0 {1,S}
6   Cd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 567,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cs  u0 {1,S}
6   Cdd u0 {4,D}
7   O2d  u0 {2,D}
8   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 568,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 569,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 570,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cs u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 571,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cs u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 572,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 573,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 574,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 575,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 576,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 577,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 578,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    O2d  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 579,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 580,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.32,5.86,7.57,8.54,9.22,9.36,8.45],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.54,'kcal/mol','+|-',0.26),
        S298 = (-33.96,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CdCdCdCs BOZZELLI =3D Cs/Cs2/Cd2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 581,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cs  u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 582,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 583,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 584,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cs  u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 585,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 586,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 587,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 588,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 589,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 590,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 591,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 592,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cs  u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 593,
    label = "Cs-CtCdsCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 594,
    label = "Cs-(Cds-O2d)(Cds-O2d)CtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 595,
    label = "Cs-(Cds-O2d)(Cds-Cd)CtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 596,
    label = "Cs-(Cds-O2d)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 597,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 598,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 599,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 600,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 601,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 602,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 603,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 604,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 605,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 606,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 607,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 608,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Cs  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 609,
    label = "Cs-CbCdsCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 610,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 611,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 612,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 613,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 614,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 615,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 616,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 617,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 618,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 619,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 620,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 621,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 622,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 623,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 624,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cs  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 625,
    label = "Cs-CtCtCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 626,
    label = "Cs-(Cds-O2d)CtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 627,
    label = "Cs-(Cds-Cd)CtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 628,
    label = "Cs-(Cds-Cds)CtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCtCdCs BOZZELLI =3D Cs/Cd2/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 629,
    label = "Cs-(Cds-Cdd)CtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 630,
    label = "Cs-(Cds-Cdd-O2d)CtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 631,
    label = "Cs-(Cds-Cdd-Cd)CtCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 632,
    label = "Cs-CbCtCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 633,
    label = "Cs-(Cds-O2d)CbCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 634,
    label = "Cs-(Cds-Cd)CbCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 635,
    label = "Cs-(Cds-Cds)CbCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCdCs BOZZELLI =3D Cs/Cb/Cd/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 636,
    label = "Cs-(Cds-Cdd)CbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 637,
    label = "Cs-(Cds-Cdd-O2d)CbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 638,
    label = "Cs-(Cds-Cdd-Cd)CbCtCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCdCs BOZZELLI =3D Cs/Cb/Cd/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 639,
    label = "Cs-CbCbCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 640,
    label = "Cs-(Cds-O2d)CbCbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 641,
    label = "Cs-(Cds-Cd)CbCbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 642,
    label = "Cs-(Cds-Cds)CbCbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCdCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 643,
    label = "Cs-(Cds-Cdd)CbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 644,
    label = "Cs-(Cds-Cdd-O2d)CbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 645,
    label = "Cs-(Cds-Cdd-Cd)CbCbCs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 646,
    label = "Cs-CtCtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.23,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCtCtCs BOZZELLI =3D Cs/Cs2/Ct2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 647,
    label = "Cs-CbCtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.23,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCtCs BOZZELLI =3D Cs/Cs2/Cb/Ct + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 648,
    label = "Cs-CbCbCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.43,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCtCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 649,
    label = "Cs-CbCbCbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.23,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCbCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Cb - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 650,
    label = "Cs-CdsCdsCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 651,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   CO u0 {1,S} {8,D}
5   CO u0 {1,S} {9,D}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
9   O2d u0 {5,D}
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 652,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   CO u0 {1,S} {9,D}
5   Cd u0 {1,S} {6,D}
6   C  u0 {5,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 653,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   CO u0 {1,S} {9,D}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {5,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
9   O2d u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 654,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   CO  u0 {1,S} {9,D}
5   Cd  u0 {1,S} {6,D}
6   Cdd u0 {5,D}
7   O2d  u0 {2,D}
8   O2d  u0 {3,D}
9   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 655,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    O2d  u0 {3,D}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 656,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    O2d  u0 {3,D}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 657,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   CO u0 {1,S} {9,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {1,S} {7,D}
6   C  u0 {4,D}
7   C  u0 {5,D}
8   O2d u0 {2,D}
9   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([42.49,50.96,52.27,50.54,45.33,41.1,35.7],'J/(mol*K)','+|-',[5.08,5.08,5.08,5.08,5.08,5.08,5.08]),
        H298 = (25.2,'kJ/mol','+|-',4.33),
        S298 = (-168.67,'J/(mol*K)','+|-',5.92),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 658,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   CO u0 {1,S} {9,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {1,S} {7,D}
6   Cd u0 {4,D}
7   Cd u0 {5,D}
8   O2d u0 {2,D}
9   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 659,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cdd u0 {4,D}
7   Cd  u0 {5,D}
8   O2d  u0 {2,D}
9   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 660,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {8,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {7,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {5,D}
8    O2d  u0 {3,D}
9    O2d  u0 {4,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 661,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {8,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {7,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {5,D}
8    O2d  u0 {3,D}
9    O2d  u0 {4,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 662,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   CO  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cdd u0 {4,D}
7   Cdd u0 {5,D}
8   O2d  u0 {2,D}
9   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 663,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 664,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 665,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 666,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {9,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {1,S} {8,D}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   C  u0 {5,D}
9   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 667,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {9,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {1,S} {8,D}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   Cd u0 {5,D}
9   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 668,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   Cdd u0 {5,D}
9   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 669,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {9,D}
4    Cd  u0 {1,S} {7,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {4,D}
8    Cd  u0 {5,D}
9    O2d  u0 {3,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 670,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CO  u0 {1,S} {9,D}
4    Cd  u0 {1,S} {7,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {4,D}
8    Cd  u0 {5,D}
9    O2d  u0 {3,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 671,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cdd u0 {4,D}
8   Cdd u0 {5,D}
9   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 672,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    O2d  u0 {4,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 673,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    O2d  u0 {4,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 674,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CO  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    O2d  u0 {4,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 675,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   Cdd u0 {5,D}
9   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 676,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
12   O2d  u0 {8,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 677,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 678,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 679,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CO  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 680,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cd u0 {1,S} {9,D}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
9   C  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 681,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cd u0 {1,S} {9,D}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
9   Cd u0 {5,D}
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 682,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cd  u0 {1,S} {9,D}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   Cdd u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 683,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {3,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {3,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 684,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {3,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 685,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cd  u0 {1,S} {9,D}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
9   Cdd u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 686,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 687,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 688,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {4,D}
9    Cd  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 689,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cd  u0 {1,S} {9,D}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
9   Cdd u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 690,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
12   O2d  u0 {8,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 691,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 692,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   S2d u0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 693,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cd  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 694,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cd  u0 {1,S} {9,D}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
9   Cdd u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 695,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
12   O2d  u0 {8,D}
13   O2d  u0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 696,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
12   O2d  u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 697,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 698,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   S2d u0 {8,D}
13   S2d u0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   S2d u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 699,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    Cd  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    Cdd u0 {5,D} {13,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
13   C   u0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 700,
    label = "Cs-CtCdsCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 701,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   CO u0 {1,S} {8,D}
5   Ct u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 702,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Ct u0 {1,S}
6   C  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 703,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Ct u0 {1,S}
6   Cd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 704,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Ct  u0 {1,S}
6   Cdd u0 {4,D}
7   O2d  u0 {2,D}
8   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 705,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 706,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 707,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Ct u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 708,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Ct u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 709,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 710,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 711,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 712,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 713,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 714,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 715,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    O2d  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 716,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Ct u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 717,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 718,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Ct  u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 719,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 720,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 721,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Ct  u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 722,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 723,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 724,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 725,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 726,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 727,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 728,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 729,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Ct  u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 730,
    label = "Cs-CbCdsCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 731,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   CO u0 {1,S} {8,D}
5   Cb u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 732,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Cb u0 {1,S}
6   C  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 733,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Cb u0 {1,S}
6   Cd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 734,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cb  u0 {1,S}
6   Cdd u0 {4,D}
7   O2d  u0 {2,D}
8   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 735,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 736,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 737,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cb u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 738,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cb u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 739,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 740,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 741,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 742,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 743,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 744,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 745,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    O2d  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 746,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cb u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 747,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cb u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 748,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cb  u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 749,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 750,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 751,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cb  u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 752,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 753,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 754,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 755,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cb  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 756,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 757,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 758,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 759,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    Cb  u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 760,
    label = "Cs-CtCtCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 761,
    label = "Cs-(Cds-O2d)(Cds-O2d)CtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 762,
    label = "Cs-(Cds-O2d)(Cds-Cd)CtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 763,
    label = "Cs-(Cds-O2d)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 764,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 765,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 766,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 767,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 768,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.48,'kcal/mol','+|-',0.26),
        S298 = (-34.5,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCtCdCd BOZZELLI =3D Cs/Cs/Cd/Ct2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 769,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 770,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 771,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 772,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 773,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 774,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 775,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   Ct  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 776,
    label = "Cs-CbCtCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 777,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 778,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 779,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 780,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 781,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 782,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 783,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 784,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.48,'kcal/mol','+|-',0.26),
        S298 = (-34.5,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCdCd BOZZELLI =3D Cs/Cs/Cb/Cd2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 785,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 786,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 787,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 788,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 789,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 790,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 791,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Ct  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 792,
    label = "Cs-CbCbCdsCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 793,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 794,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 795,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 796,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 797,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 798,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 799,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 800,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.48,'kcal/mol','+|-',0.26),
        S298 = (-34.5,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCdCd BOZZELLI =3D Cs/Cs/Cb2/Cd + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index = 801,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 802,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 803,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 804,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 805,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 806,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 807,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   Cb  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 808,
    label = "Cs-CtCtCtCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   Ct      u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 809,
    label = "Cs-(Cds-O2d)CtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 810,
    label = "Cs-(Cds-Cds)CtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 811,
    label = "Cs-(Cds-Cdd)CtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 812,
    label = "Cs-(Cds-Cdd-O2d)CtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 813,
    label = "Cs-(Cds-Cdd-Cd)CtCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 814,
    label = "Cs-CbCtCtCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   Ct      u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 815,
    label = "Cs-(Cds-O2d)CbCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 816,
    label = "Cs-(Cds-Cd)CbCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 817,
    label = "Cs-(Cds-Cds)CbCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 818,
    label = "Cs-(Cds-Cdd)CbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 819,
    label = "Cs-(Cds-Cdd-O2d)CbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 820,
    label = "Cs-(Cds-Cdd-Cd)CbCtCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 821,
    label = "Cs-CbCbCtCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   Ct      u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 822,
    label = "Cs-(Cds-O2d)CbCbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 823,
    label = "Cs-(Cds-Cd)CbCbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 824,
    label = "Cs-(Cds-Cds)CbCbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 825,
    label = "Cs-(Cds-Cdd)CbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 826,
    label = "Cs-(Cds-Cdd-O2d)CbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 827,
    label = "Cs-(Cds-Cdd-Cd)CbCbCt",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 828,
    label = "Cs-CbCbCbCds",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   Cb      u0 {1,S}
5   [Cd,CO] u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 829,
    label = "Cs-(Cds-O2d)CbCbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 830,
    label = "Cs-(Cds-Cd)CbCbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 831,
    label = "Cs-(Cds-Cds)CbCbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 832,
    label = "Cs-(Cds-Cdd)CbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 833,
    label = "Cs-(Cds-Cdd-O2d)CbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 834,
    label = "Cs-(Cds-Cdd-Cd)CbCbCb",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 835,
    label = "Cs-CtCtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 836,
    label = "Cs-CbCtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 837,
    label = "Cs-CbCbCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 838,
    label = "Cs-CbCbCbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 839,
    label = "Cs-CbCbCbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {9,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {1,S} {8,D}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   C  u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cd  u0 {4,D}
8   Cdd u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {9,D}
4    Cd  u0 {1,S} {7,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {4,D}
8    Cd  u0 {5,D}
9    S2d u0 {3,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {9,D}
4    Cd  u0 {1,S} {7,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {4,D}
8    Cd  u0 {5,D}
9    S2d u0 {3,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   Cdd u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   S2d u0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    Cd  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cdd u0 {4,D} {12,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
12   C   u0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {9,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {1,S} {8,D}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   Cd u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {9,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cd  u0 {1,S} {8,D}
6   Cd  u0 {3,D}
7   Cdd u0 {4,D}
8   Cdd u0 {5,D}
9   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    S2d u0 {4,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    S2d u0 {4,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {8,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    Cd  u0 {5,D}
9    S2d u0 {4,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CtCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CtCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbCbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbCbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCtCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cs u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cs  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cs u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCtCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Ct u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1179,
    label = "Cs-C=SCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.62018927927, 7.29896802869, 8.18284274232, 8.57401625839, 9.13851640218, 9.3157719676, 9.17904774956], 'cal/(mol*K)'),
        H298 = (-4.71355346011,'kcal/mol'),
        S298 = (-24.9182063087,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCtCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=SCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   CS u0 {1,S} {8,D}
5   Ct u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=SCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   CS u0 {1,S} {8,D}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=SC=S",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   CS u0 {1,S} {8,D}
5   CS u0 {1,S} {9,D}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=SCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   CS u0 {1,S} {8,D}
5   Cb u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=S(Cds-Cd)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   CS u0 {1,S} {9,D}
5   Cd u0 {1,S} {6,D}
6   C  u0 {5,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
9   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=S(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   CS  u0 {1,S} {9,D}
5   Cd  u0 {1,S} {6,D}
6   Cdd u0 {5,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
9   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=S(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    S2d u0 {3,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=S(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    S2d u0 {3,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=S(Cds-Cds)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   CS u0 {1,S} {9,D}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {5,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
9   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Ct u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Ct  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Ct u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CbCt",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Ct u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CbCt",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CbCb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cd)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Ct u0 {1,S}
6   C  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cds)Ct",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Ct u0 {1,S}
6   Cd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Ct  u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)Ct",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Ct  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cd)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Cs u0 {1,S}
6   C  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cds)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Cs u0 {1,S}
6   Cd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cs  u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)Cs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   CS u0 {1,S} {9,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {1,S} {7,D}
6   C  u0 {4,D}
7   C  u0 {5,D}
8   S2d u0 {2,D}
9   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   CS  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cdd u0 {4,D}
7   Cd  u0 {5,D}
8   S2d u0 {2,D}
9   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cds)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {8,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {7,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {5,D}
8    S2d u0 {3,D}
9    S2d u0 {4,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    CS  u0 {1,S} {8,D}
4    CS  u0 {1,S} {9,D}
5    Cd  u0 {1,S} {7,D}
6    Cdd u0 {2,D} {10,D}
7    Cd  u0 {5,D}
8    S2d u0 {3,D}
9    S2d u0 {4,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   CS  u0 {1,S} {9,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {1,S} {7,D}
6   Cdd u0 {4,D}
7   Cdd u0 {5,D}
8   S2d u0 {2,D}
9   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2    Cd  u0 {1,S} {6,D}
3    Cd  u0 {1,S} {7,D}
4    CS  u0 {1,S} {8,D}
5    CS  u0 {1,S} {9,D}
6    Cdd u0 {2,D} {10,D}
7    Cdd u0 {3,D} {11,D}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   CS u0 {1,S} {9,D}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {1,S} {7,D}
6   Cd u0 {4,D}
7   Cd u0 {5,D}
8   S2d u0 {2,D}
9   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cd)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Cb u0 {1,S}
6   C  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   Cb  u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cds)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   Cb u0 {1,S}
6   Cd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbCtCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CbCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   Cs  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cb u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cb  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)Cb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   Cb u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   Cb  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cb",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   Cb  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbCbCb",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCbCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 840,
    label = "Cs-CCCOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 841,
    label = "Cs-CsCsCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.99,31.2,34.89,36.47,36.78,36.05,34.4],'J/(mol*K)','+|-',[3.81,3.81,3.81,3.81,3.81,3.81,3.81]),
        H298 = (-20.3,'kJ/mol','+|-',3.24),
        S298 = (-144.38,'J/(mol*K)','+|-',4.44),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 842,
    label = "Cs-CdsCsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 843,
    label = "Cs-(Cds-O2d)CsCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.15,35.17,38.11,38.72,37.49,35.88,33.45],'J/(mol*K)','+|-',[5.16,5.16,5.16,5.16,5.16,5.16,5.16]),
        H298 = (-10.9,'kJ/mol','+|-',4.39),
        S298 = (-148.7,'J/(mol*K)','+|-',6.02),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 844,
    label = "Cs-(Cds-Cd)CsCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.24,37.61,40.84,41.46,40.06,38.2,35.08],'J/(mol*K)','+|-',[3.81,3.81,3.81,3.81,3.81,3.81,3.81]),
        H298 = (-14.6,'kJ/mol','+|-',3.24),
        S298 = (-153.23,'J/(mol*K)','+|-',4.44),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 845,
    label = "Cs-(Cds-Cds)CsCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.63,6.79,7.95,8.4,8.8,8.44,8.44],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-6.6,'kcal/mol','+|-',0.4),
        S298 = (-32.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OCdCsCs BOZZELLI C/C3/O - (C/C3/H - C/Cb/C2/H), Hf-1 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 846,
    label = "Cs-(Cds-Cdd)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 847,
    label = "Cs-(Cds-Cdd-O2d)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.39,9.66,10.03,10.07,9.64,9.26,8.74],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-9.725,'kcal/mol','+|-',0.4),
        S298 = (-36.5,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""{C/CCO/O/C2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 848,
    label = "Cs-(Cds-Cdd-Cd)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 849,
    label = "Cs-OsCtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 850,
    label = "Cs-CbCsCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.63,6.79,7.95,8.4,8.8,8.44,8.44],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-6.6,'kcal/mol','+|-',0.4),
        S298 = (-32.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OCbCsCs BOZZELLI C/C3/O - (C/C3/H - C/Cb/C2/H), Hf-1 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 851,
    label = "Cs-CdsCdsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 852,
    label = "Cs-(Cds-O2d)(Cds-O2d)CsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 853,
    label = "Cs-(Cds-O2d)(Cds-Cd)CsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.75,42.15,45.09,44.95,41.74,38.55,34.46],'J/(mol*K)','+|-',[4.3,4.3,4.3,4.3,4.3,4.3,4.3]),
        H298 = (-3.9,'kJ/mol','+|-',3.66),
        S298 = (-158.3,'J/(mol*K)','+|-',5.02),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 854,
    label = "Cs-(Cds-O2d)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 855,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 856,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 857,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 858,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 859,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-8.01,'kcal/mol','+|-',0.4),
        S298 = (-34.34,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OCdCdCs Hf jwb 697 S,Cp from C/Cd2/C2""",
    longDesc = 
u"""

""",
)

entry(
    index = 860,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 861,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 862,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 863,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 864,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   O2s  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 865,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   O2s  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 866,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   O2s  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 867,
    label = "Cs-CtCdsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 868,
    label = "Cs-(Cds-O2d)CtCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 869,
    label = "Cs-(Cds-Cd)CtCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 870,
    label = "Cs-(Cds-Cds)CtCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 871,
    label = "Cs-(Cds-Cdd)CtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 872,
    label = "Cs-(Cds-Cdd-O2d)CtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 873,
    label = "Cs-(Cds-Cdd-Cd)CtCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 874,
    label = "Cs-CbCdsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 875,
    label = "Cs-(Cds-O2d)CbCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 876,
    label = "Cs-(Cds-Cd)CbCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 877,
    label = "Cs-(Cds-Cds)CbCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 878,
    label = "Cs-(Cds-Cdd)CbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 879,
    label = "Cs-(Cds-Cdd-O2d)CbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 880,
    label = "Cs-(Cds-Cdd-Cd)CbCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 881,
    label = "Cs-CtCtCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 882,
    label = "Cs-CbCtCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 883,
    label = "Cs-CbCbCsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 884,
    label = "Cs-CdsCdsCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 885,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)O2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   CO u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
8   O2d u0 {4,D}
""",
    thermo = u'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 886,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)O2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   O2s u0 {1,S}
6   C  u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 887,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   CO u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   O2s u0 {1,S}
6   Cd u0 {4,D}
7   O2d u0 {2,D}
8   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 888,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   O2s  u0 {1,S}
6   Cdd u0 {4,D}
7   O2d  u0 {2,D}
8   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 889,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 890,
    label = "Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {7,D}
4   CO  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 891,
    label = "Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)O2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   O2s u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.85,46.04,49,48.85,45.61,42.23,37.25],'J/(mol*K)','+|-',[4.09,4.09,4.09,4.09,4.09,4.09,4.09]),
        H298 = (3,'kJ/mol','+|-',3.49),
        S298 = (-160.69,'J/(mol*K)','+|-',4.77),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 892,
    label = "Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   O2s u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 893,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2s  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 894,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   O2s  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 895,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CO  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   O2s  u0 {1,S}
7   Cd  u0 {4,D}
8   O2d  u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 896,
    label = "Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   O2s  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 897,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s  u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 898,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s  u0 {1,S}
8    O2d  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 899,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CO  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s  u0 {1,S}
8    O2d  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 900,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)O2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 901,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = u'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 902,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   O2s  u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 903,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 904,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 905,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   O2s  u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 906,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 907,
    label = "Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s  u0 {1,S}
8    Cd  u0 {4,D}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 908,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    O2s  u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 909,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)O2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 910,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    O2s  u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   O2d  u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 911,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    O2s  u0 {1,S}
9    O2d  u0 {5,D}
10   O2d  u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 912,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    O2s  u0 {1,S}
9    O2d  u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 913,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    O2s  u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 914,
    label = "Cs-CtCdsCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 915,
    label = "Cs-(Cds-O2d)(Cds-O2d)CtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 916,
    label = "Cs-(Cds-O2d)(Cds-Cd)CtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 917,
    label = "Cs-(Cds-O2d)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 918,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 919,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 920,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 921,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 922,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 923,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 924,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 925,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 926,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 927,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   O2s  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 928,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   O2s  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 929,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   O2s  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 930,
    label = "Cs-CbCdsCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 931,
    label = "Cs-(Cds-O2d)(Cds-O2d)CbOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 932,
    label = "Cs-(Cds-O2d)(Cds-Cd)CbOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 933,
    label = "Cs-(Cds-O2d)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 934,
    label = "Cs-(Cds-O2d)(Cds-Cdd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 935,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 936,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 937,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 938,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 939,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 940,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 941,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 942,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 943,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   O2s  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 944,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   O2s  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 945,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   O2s  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 946,
    label = "Cs-CtCtCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 947,
    label = "Cs-(Cds-O2d)CtCtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 948,
    label = "Cs-(Cds-Cd)CtCtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 949,
    label = "Cs-(Cds-Cds)CtCtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 950,
    label = "Cs-(Cds-Cdd)CtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 951,
    label = "Cs-(Cds-Cdd-O2d)CtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 952,
    label = "Cs-(Cds-Cdd-Cd)CtCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 953,
    label = "Cs-CbCtCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 954,
    label = "Cs-(Cds-O2d)CbCtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 955,
    label = "Cs-(Cds-Cd)CbCtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 956,
    label = "Cs-(Cds-Cds)CbCtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 957,
    label = "Cs-(Cds-Cdd)CbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 958,
    label = "Cs-(Cds-Cdd-O2d)CbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 959,
    label = "Cs-(Cds-Cdd-Cd)CbCtOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 960,
    label = "Cs-CbCbCdsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 961,
    label = "Cs-(Cds-O2d)CbCbOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 962,
    label = "Cs-(Cds-Cd)CbCbOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 963,
    label = "Cs-(Cds-Cds)CbCbOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 964,
    label = "Cs-(Cds-Cdd)CbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 965,
    label = "Cs-(Cds-Cdd-O2d)CbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 966,
    label = "Cs-(Cds-Cdd-Cd)CbCbOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 967,
    label = "Cs-CtCtCtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 968,
    label = "Cs-CbCtCtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 969,
    label = "Cs-CbCbCtOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 970,
    label = "Cs-CbCbCbOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 971,
    label = "Cs-CCOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 972,
    label = "Cs-CsCsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.88,43.75,51.85,54,50.77,45.94,38.31],'J/(mol*K)','+|-',[5.77,5.77,5.77,5.77,5.77,5.77,5.77]),
        H298 = (-69.2,'kJ/mol','+|-',4.92),
        S298 = (-163.77,'J/(mol*K)','+|-',6.74),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 973,
    label = "Cs-CdsCsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   O2s      u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 974,
    label = "Cs-(Cds-O2d)CsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 975,
    label = "Cs-(Cds-Cd)CsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.95,42.92,51.33,54.81,53.92,49.73,41.11],'J/(mol*K)','+|-',[5.77,5.77,5.77,5.77,5.77,5.77,5.77]),
        H298 = (-62.8,'kJ/mol','+|-',4.92),
        S298 = (-170.44,'J/(mol*K)','+|-',6.74),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 976,
    label = "Cs-(Cds-Cds)CsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 977,
    label = "Cs-(Cds-Cdd)CsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 978,
    label = "Cs-(Cds-Cdd-O2d)CsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 979,
    label = "Cs-(Cds-Cdd-Cd)CsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 980,
    label = "Cs-CdsCdsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 981,
    label = "Cs-(Cds-O2d)(Cds-O2d)OsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 982,
    label = "Cs-(Cds-O2d)(Cds-Cd)OsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 983,
    label = "Cs-(Cds-O2d)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 984,
    label = "Cs-(Cds-O2d)(Cds-Cdd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 985,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 986,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 987,
    label = "Cs-(Cds-Cd)(Cds-Cd)OsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.08,45.85,54.7,58.39,57.78,53.65,44.31],'J/(mol*K)','+|-',[5.77,5.77,5.77,5.77,5.77,5.77,5.77]),
        H298 = (-55.7,'kJ/mol','+|-',4.92),
        S298 = (-179.76,'J/(mol*K)','+|-',6.74),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 988,
    label = "Cs-(Cds-Cds)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 989,
    label = "Cs-(Cds-Cdd)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 990,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 991,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 992,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 993,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s  u0 {1,S}
7   O2s  u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 994,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s  u0 {1,S}
7   O2s  u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 995,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s  u0 {1,S}
7   O2s  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 996,
    label = "Cs-CtCsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 997,
    label = "Cs-CtCdsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 998,
    label = "Cs-(Cds-O2d)CtOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 999,
    label = "Cs-(Cds-Cd)CtOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1000,
    label = "Cs-(Cds-Cds)CtOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1001,
    label = "Cs-(Cds-Cdd)CtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1002,
    label = "Cs-(Cds-Cdd-O2d)CtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1003,
    label = "Cs-(Cds-Cdd-Cd)CtOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1004,
    label = "Cs-CtCtOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1005,
    label = "Cs-CbCsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1006,
    label = "Cs-CbCdsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1007,
    label = "Cs-(Cds-O2d)CbOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1008,
    label = "Cs-(Cds-Cd)CbOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1009,
    label = "Cs-(Cds-Cds)CbOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1010,
    label = "Cs-(Cds-Cdd)CbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1011,
    label = "Cs-(Cds-Cdd-O2d)CbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1012,
    label = "Cs-(Cds-Cdd-Cd)CbOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1013,
    label = "Cs-CbCtOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1014,
    label = "Cs-CbCbOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1015,
    label = "Cs-COsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-CsOsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1016,
    label = "Cs-CsOsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.19,7.25,7.7,8.2,8.24,8.24],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-19,'kcal/mol','+|-',0.4),
        S298 = (-33.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OOOCs BOZZELLI est !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1017,
    label = "Cs-CdsOsOsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s      u0 {1,S}
4   O2s      u0 {1,S}
5   O2s      u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1018,
    label = "Cs-(Cds-O2d)OsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-CsOsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1019,
    label = "Cs-(Cds-Cd)OsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1020,
    label = "Cs-(Cds-Cds)OsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-CsOsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1021,
    label = "Cs-(Cds-Cdd)OsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s  u0 {1,S}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1022,
    label = "Cs-(Cds-Cdd-O2d)OsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1023,
    label = "Cs-(Cds-Cdd-Cd)OsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   O2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1024,
    label = "Cs-CtOsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1025,
    label = "Cs-CbOsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1026,
    label = "Cs-OsOsOsOs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.13,7.25,7.7,8.2,8.24,8.24],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-23,'kcal/mol','+|-',0.4),
        S298 = (-35.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OOOO BOZZELLI est !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1027,
    label = "Cs-COsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsOsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1028,
    label = "Cs-CsOsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.25,7.1,8.81,9.55,10.31,11.05,11.05],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-16,'kcal/mol','+|-',0.24),
        S298 = (-12.07,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OOCsH BENSON Hf, BOZZELLI C/C3/H - C/C2/O/H !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1029,
    label = "Cs-CdsOsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s      u0 {1,S}
4   O2s      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1030,
    label = "Cs-(Cds-O2d)OsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-CsOsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1031,
    label = "Cs-(Cds-Cd)OsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1032,
    label = "Cs-(Cds-Cds)OsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-CsOsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1033,
    label = "Cs-(Cds-Cdd)OsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s  u0 {1,S}
4   O2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1034,
    label = "Cs-(Cds-Cdd-O2d)OsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1035,
    label = "Cs-(Cds-Cdd-Cd)OsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s  u0 {1,S}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1036,
    label = "Cs-CtOsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1037,
    label = "Cs-CbOsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-COsSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   O2s u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsOsSH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1452,
    label = "Cs-CsOsSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsOsS2H',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1452,
    label = "Cs-CsOsS2H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   S2s  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.78353964374, 10.6506828182, 11.7098170286, 12.2147055402, 13.1123092159, 14.2844735055, 12.9838495838], 'cal/(mol*K)'),
        H298 = (1.07295491204,'kcal/mol'),
        S298 = (-10.1933610822,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1452,
    label = "Cs-CsOsS4H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.74020715729, 8.92538734509, 10.4754601896, 11.9536333455, 15.4684208812, 17.1055231134, 15.215403606], 'cal/(mol*K)'),
        H298 = (4.98049687625,'kcal/mol'),
        S298 = (-20.2653576731,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CdsOsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.87729881548, 11.9106022871, 12.9543576403, 13.3922933878, 14.6849318897, 15.0228272279, 13.5747441991], 'cal/(mol*K)'),
        H298 = (2.57841752802,'kcal/mol'),
        S298 = (-9.05709119317,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CtOsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbOsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.93269078548, 11.7249426271, 12.6222735103, 13.0362704378, 14.4151039797, 14.7815079179, 12.9999640891], 'cal/(mol*K)'),
        H298 = (1.81421102802,'kcal/mol'),
        S298 = (-10.6048732232,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CCOsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   O2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1453,
    label = "Cs-CsCsOsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.97826878053, 10.9241437505, 11.5599640164, 11.5061478182, 12.0104909075, 11.9946095745, 9.6936834435], 'cal/(mol*K)'),
        H298 = (3.3013838947,'kcal/mol'),
        S298 = (-35.1001213786,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1467,
    label = "Cs-COsOsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = u'Cs-CsOsOsSs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1465,
    label = "Cs-CsOsOsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.57062577733, 8.94903441152, 9.79046663179, 10.2898650912, 11.9414710878, 12.312626469, 10.120231773], 'cal/(mol*K)'),
        H298 = (-8.06384822208,'kcal/mol'),
        S298 = (-30.769653336,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1038,
    label = "Cs-CCOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsCsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1039,
    label = "Cs-CsCsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.99,29.03,34.22,37.78,41.96,44.27,47.11],'J/(mol*K)','+|-',[3.32,3.32,3.32,3.32,3.32,3.32,3.32]),
        H298 = (-25.1,'kJ/mol','+|-',2.83),
        S298 = (-52.05,'J/(mol*K)','+|-',3.88),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1040,
    label = "Cs-CdsCsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   O2s      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1041,
    label = "Cs-(Cds-O2d)CsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6,'kcal/mol','+|-',0.24),
        S298 = (-11.1,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OCOCsH BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 1042,
    label = "Cs-(Cds-Cd)CsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.84,38.86,43.83,46.37,48.34,49.06,49.94],'J/(mol*K)','+|-',[3.74,3.74,3.74,3.74,3.74,3.74,3.74]),
        H298 = (-24,'kJ/mol','+|-',3.19),
        S298 = (-61.06,'J/(mol*K)','+|-',4.36),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1043,
    label = "Cs-(Cds-Cds)CsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6,'kcal/mol','+|-',0.24),
        S298 = (-11.1,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OCdCsH BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 1044,
    label = "Cs-(Cds-Cdd)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1045,
    label = "Cs-(Cds-Cdd-O2d)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.2,8.49,9.33,9.92,10.5,10.92,11.71],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-8.37,'kcal/mol','+|-',0.24),
        S298 = (-13.04,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""{C/CCO/O/C/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 1046,
    label = "Cs-(Cds-Cdd-Cd)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1047,
    label = "Cs-CdsCdsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1048,
    label = "Cs-(Cds-O2d)(Cds-O2d)OsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    thermo = u'Cs-CsCsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1049,
    label = "Cs-(Cds-O2d)(Cds-Cd)OsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1050,
    label = "Cs-(Cds-O2d)(Cds-Cds)OsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1051,
    label = "Cs-(Cds-O2d)(Cds-Cdd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   O2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   O2d  u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cdd-Cd)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1052,
    label = "Cs-(Cds-O2d)(Cds-Cdd-O2d)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1053,
    label = "Cs-(Cds-O2d)(Cds-Cdd-Cd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CO  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1054,
    label = "Cs-(Cds-Cd)(Cds-Cd)OsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.82,38.47,43.27,45.7,47.5,48.09,48.78],'J/(mol*K)','+|-',[3.64,3.64,3.64,3.64,3.64,3.64,3.64]),
        H298 = (-17.4,'kJ/mol','+|-',3.1),
        S298 = (-64.14,'J/(mol*K)','+|-',4.24),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1055,
    label = "Cs-(Cds-Cds)(Cds-Cds)OsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.21,6.6,8.26,9.05,10.23,10.86,11.04],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6.67,'kcal/mol','+|-',0.24),
        S298 = (-10.42,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OCdCdH BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 1056,
    label = "Cs-(Cds-Cdd)(Cds-Cds)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1057,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   O2d  u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1058,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1059,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1060,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s  u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   O2d  u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1061,
    label = "Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s  u0 {1,S}
7   H   u0 {1,S}
8   O2d  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1062,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   O2s  u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1063,
    label = "Cs-CtCsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1064,
    label = "Cs-CtCdsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1065,
    label = "Cs-(Cds-O2d)CtOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1066,
    label = "Cs-(Cds-Cd)CtOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1067,
    label = "Cs-(Cds-Cds)CtOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1068,
    label = "Cs-(Cds-Cdd)CtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   O2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1069,
    label = "Cs-(Cds-Cdd-O2d)CtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1070,
    label = "Cs-(Cds-Cdd-Cd)CtOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1071,
    label = "Cs-CtCtOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1072,
    label = "Cs-CbCsOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6,'kcal/mol','+|-',0.24),
        S298 = (-11.1,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OCbCsH BOZZELLI =3D C/Cd/C/H/O Jul 91""",
    longDesc = 
u"""

""",
)

entry(
    index = 1073,
    label = "Cs-CbCdsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1074,
    label = "Cs-(Cds-O2d)CbOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = u'Cs-(Cds-O2d)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1075,
    label = "Cs-(Cds-Cd)CbOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1076,
    label = "Cs-(Cds-Cds)CbOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1077,
    label = "Cs-(Cds-Cdd)CbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   O2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1078,
    label = "Cs-(Cds-Cdd-O2d)CbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1079,
    label = "Cs-(Cds-Cdd-Cd)CbOsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   O2s  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1080,
    label = "Cs-CbCtOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1081,
    label = "Cs-CbCbOsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1082,
    label = "Cs-COsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsOsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1083,
    label = "Cs-CsOsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.01,31.9,37.45,41.88,48.53,53.31,60.53],'J/(mol*K)','+|-',[1.43,1.43,1.43,1.43,1.43,1.43,1.43]),
        H298 = (-34.3,'kJ/mol','+|-',1.22),
        S298 = (37.65,'J/(mol*K)','+|-',1.67),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1084,
    label = "Cs-CdsOsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s      u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1085,
    label = "Cs-(Cds-O2d)OsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.75,34.37,40.77,45.37,51.2,54.96,60.79],'J/(mol*K)','+|-',[4.34,4.34,4.34,4.34,4.34,4.34,4.34]),
        H298 = (-19.8,'kJ/mol','+|-',3.7),
        S298 = (31.54,'J/(mol*K)','+|-',5.06),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1086,
    label = "Cs-(Cds-Cd)OsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.42,35.65,40.62,44.31,49.79,53.92,60.6],'J/(mol*K)','+|-',[3.38,3.38,3.38,3.38,3.38,3.38,3.38]),
        H298 = (-26.6,'kJ/mol','+|-',2.88),
        S298 = (34.59,'J/(mol*K)','+|-',3.95),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1087,
    label = "Cs-(Cds-Cds)OsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-6.76,'kcal/mol','+|-',0.2),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OCdHH BOZZELLI Hf PEDLEY c*ccoh C/C/Cd/H2""",
    longDesc = 
u"""

""",
)

entry(
    index = 1088,
    label = "Cs-(Cds-Cdd)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1089,
    label = "Cs-(Cds-Cdd-O2d)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.15,8.67,9.75,10.65,11.93,12.97,14.86],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-8.68,'kcal/mol','+|-',0.2),
        S298 = (8.43,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{C/CCO/O/H2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index = 1090,
    label = "Cs-(Cds-Cdd-Cd)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   O2s  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1091,
    label = "Cs-CtOsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-6.76,'kcal/mol','+|-',0.2),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OCtHH BOZZELLI assigned C/Cd/H2/O""",
    longDesc = 
u"""

""",
)

entry(
    index = 1092,
    label = "Cs-CbOsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CCCS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   S u0 {1,S}
""",
    thermo = u'Cs-CsCsCsS',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1175,
    label = "Cs-CsCsCsS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S u0 {1,S}
""",
    thermo = u'Cs-CsCsCsS2',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1175,
    label = "Cs-CsCsCsS2",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9358692294, 6.88742650195, 7.59858975864, 8.13241874424, 10.087847921, 10.9714150153, 9.67982183311], 'cal/(mol*K)'),
        H298 = (8.2874136379,'kcal/mol'),
        S298 = (-29.0598231082,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1175,
    label = "Cs-CsCsCsS4",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   [S4s,S4d,S4b,S4t] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.62705502689, 5.51416532287, 5.7326855334, 6.11123442476, 8.54888722987, 9.78264664498, 8.8045690621], 'cal/(mol*K)'),
        H298 = (14.8769525236,'kcal/mol'),
        S298 = (-29.5854413287,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CdsCsCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CsCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CsCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CsCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-SsCtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S2s u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCsCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CdsCdsCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   S2s  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   S2s  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cs  u0 {1,S}
7   S2s  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCdsCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cd u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CtCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CtCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CtCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCdsCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cd u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CbCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CbCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CbCsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCtCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCtCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCbCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CdsCdsCdsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
4   Cd u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)S2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   S2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)S2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   S2s  u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   Cd  u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   S2s  u0 {1,S}
6   Cd  u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s  u0 {1,S}
8    Cd  u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s  u0 {1,S}
8    Cd  u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cd  u0 {1,S} {8,D}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
8   Cdd u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    S2s  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   S2d u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    S2s  u0 {1,S}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    S2s  u0 {1,S}
9    S2d u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {8,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    Cd  u0 {1,S} {7,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    Cdd u0 {4,D} {11,D}
8    S2s  u0 {1,S}
9    C   u0 {5,D}
10   C   u0 {6,D}
11   C   u0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCdsCdsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cd u0 {1,S}
4   Cd u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Ct  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   S2s  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   S2s  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Ct  u0 {1,S}
7   S2s  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCdsCdsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cd u0 {1,S}
4   Cd u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cb  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   S2s  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   S2s  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   Cb  u0 {1,S}
7   S2s  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCtCdsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Cd u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CtCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CtCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CtCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   Ct  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCtCdsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cd u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CbCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CbCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Ct  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CbCtSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Ct  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCbCdsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cd u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CbCbSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CbCbSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CbCbSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCtCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCtCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCbCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCbCbSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCsCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)(Cds-Cd)S2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   S2s u0 {1,S}
6   C  u0 {3,D}
7   C  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2s  u0 {1,S}
6   Cdd u0 {3,D}
7   Cdd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s  u0 {1,S}
8    S2d u0 {4,D}
9    C   u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   C   u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {4,S} {7,S}
2    Cd  u0 {1,S} {5,D}
3    Cd  u0 {1,S} {6,D}
4    CS  u0 {1,S} {8,D}
5    Cdd u0 {2,D} {9,D}
6    Cdd u0 {3,D} {10,D}
7    S2s  u0 {1,S}
8    S2d u0 {4,D}
9    S2d u0 {5,D}
10   S2d u0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)(Cds-Cds)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {8,D}
3   Cd  u0 {1,S} {6,D}
4   Cd  u0 {1,S} {7,D}
5   S2s  u0 {1,S}
6   Cdd u0 {3,D}
7   Cd  u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   S2s  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {7,D}
5   Cdd u0 {2,D} {9,D}
6   S2s  u0 {1,S}
7   Cd  u0 {4,D}
8   S2d u0 {3,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)(Cds-Cds)S2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {8,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,S} {7,D}
5   S2s u0 {1,S}
6   Cd u0 {3,D}
7   Cd u0 {4,D}
8   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Ct  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CtSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Ct  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCtCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SC=SSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   CS u0 {1,S} {8,D}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cd)S2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   S2s u0 {1,S}
6   C  u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cds)S2s",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   CS u0 {1,S} {8,D}
4   Cd u0 {1,S} {6,D}
5   S2s u0 {1,S}
6   Cd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   CS  u0 {1,S} {8,D}
4   Cd  u0 {1,S} {6,D}
5   S2s  u0 {1,S}
6   Cdd u0 {4,D}
7   S2d u0 {2,D}
8   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-S2d)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=S(Cds-Cdd-Cd)S2s",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {6,S}
2   Cd  u0 {1,S} {5,D}
3   CS  u0 {1,S} {7,D}
4   CS  u0 {1,S} {8,D}
5   Cdd u0 {2,D} {9,D}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbCbSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCbSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCtCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CbSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CbSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cb  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CbSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SCtSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   Ct u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)CsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)CsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)CsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   Cs  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CCSS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
    thermo = u'Cs-CsCsSS',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1202,
    label = "Cs-CsCsSS",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
    thermo = u'Cs-CsCsS2S2',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1202,
    label = "Cs-CsCsS2S2",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.82480796225, 10.3333938702, 10.7016311525, 10.8809252037, 13.4141180883, 14.2130349636, 11.0365916505], 'cal/(mol*K)'),
        H298 = (18.9312040912,'kcal/mol'),
        S298 = (-21.2341823857,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1202,
    label = "Cs-CsCsS6S2",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
5   S2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.56165272896, 8.25629731339, 9.25904689742, 10.0288700578, 13.087435264, 14.1523875448, 10.7847353045], 'cal/(mol*K)'),
        H298 = (17.4730916414,'kcal/mol'),
        S298 = (-18.8536285614,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CdsCsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CdsCdsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)(Cds-Cd)SsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)SsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cds)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s  u0 {1,S}
7   S2s  u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s  u0 {1,S}
7   S2s  u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s  u0 {1,S}
7   S2s  u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCdsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cd u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CtSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CtSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CtSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCtSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCdsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cd u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CbSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CbSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CbSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCtSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCbSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)SsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)SsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)SsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCtSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CSsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1203,
    label = "Cs-CsSsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.74531901088, 12.4681166178, 12.9627478762, 13.1321000431, 16.7186962599, 17.8643134304, 13.0656283958], 'cal/(mol*K)'),
        H298 = (29.3710078554,'kcal/mol'),
        S298 = (-15.0716751211,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CdsSsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)SsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)SsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)SsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s  u0 {1,S}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)SsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)SsSsSs",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   S2s  u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtSsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbSsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SSsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-SsSsSsSs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.38517789893, 15.086425174, 16.8829659916, 18.3122149584, 24.8788388777, 28.1042594162, 23.879887315], 'cal/(mol*K)'),
        H298 = (21.2460333112,'kcal/mol'),
        S298 = (-8.50938405129,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CSSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   S  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsSSH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1173,
    label = "Cs-CsSSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsS2S2H',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1173,
    label = "Cs-CsS2S2H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S2s  u0 {1,S}
4   S2s  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.45935862725, 10.7736328752, 11.2366693975, 11.6590227187, 14.7726553733, 16.2118303736, 14.1235228205], 'cal/(mol*K)'),
        H298 = (16.9975616422,'kcal/mol'),
        S298 = (0.776352979263,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1173,
    label = "Cs-CsS4S2H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   [S4s,S4d,S4b,S4t]  u0 {1,S}
4   S2s  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.84280255701, 11.5130677918, 12.4459893867, 13.5378372111, 17.8913288699, 19.7212800076, 16.4809277785], 'cal/(mol*K)'),
        H298 = (15.5655233989,'kcal/mol'),
        S298 = (-11.7179645498,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1173,
    label = "Cs-CsS6S2H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   [S6s,S6d,S6dd,S6t,S6td]  u0 {1,S}
4   S2s  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.74427988001, 9.57170075507, 11.8290124806, 13.2764532319, 17.2531159523, 18.9517871624, 16.09879649], 'cal/(mol*K)'),
        H298 = (15.9487360008,'kcal/mol'),
        S298 = (-3.35939337973,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CdsSsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)SsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)SsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)SsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s  u0 {1,S}
4   S2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)SsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)SsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s  u0 {1,S}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtSsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbSsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SSsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CCSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsCsSH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1169,
    label = "Cs-CsCsSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsCsS2H',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1169,
    label = "Cs-CsCsS2H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.30528446255, 7.44682815879, 8.50129944481, 9.26317805207, 11.5041454311, 12.7062158884, 12.1156322132], 'cal/(mol*K)'),
        H298 = (7.38566654163,'kcal/mol'),
        S298 = (-3.53417386536,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1169,
    label = "Cs-CsCsS4H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.50265221922, 5.10038682872, 5.66171277409, 6.45353012832, 9.66003727526, 11.6144476591, 12.5368227946], 'cal/(mol*K)'),
        H298 = (12.8401569939,'kcal/mol'),
        S298 = (-7.30205438792,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1169,
    label = "Cs-CsCsS6H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.69842816618, 5.35824318954, 6.38925112218, 7.28767864817, 9.88929632951, 11.405125142, 11.5584842643], 'cal/(mol*K)'),
        H298 = (4.15727624657,'kcal/mol'),
        S298 = (-3.33802344353,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1170,
    label = "Cs-CdsCsSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 {1,S}
3   Cs u0 {1,S}
4   S u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-(Cds-Cd)CsSsH',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 1170,
    label = "Cs-CdsCsS4H",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 {1,S}
3   Cs u0 {1,S}
4   [S4s,S4d,S4b,S4t] u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.04343335957, 9.75110445492, 9.94209393877, 10.4997656958, 13.2831747075, 14.9311306186, 14.2720671252], 'cal/(mol*K)'),
        H298 = (5.13822977388,'kcal/mol'),
        S298 = (-1.82552093996,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)CsSsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.30133190152, 11.2618901534, 12.2125295851, 12.5644228675, 13.9663336078, 14.6617640357, 13.5731942798], 'cal/(mol*K)'),
        H298 = (5.01406921298,'kcal/mol'),
        S298 = (-4.06200832986,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   S2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CdsCdsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)(Cds-Cd)SsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)(Cds-Cds)SsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cds)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cds)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   Cd  u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   S2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
7   Cdd u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   S2d u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s  u0 {1,S}
7   H   u0 {1,S}
8   S2d u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {6,S} {7,S}
2   Cd  u0 {1,S} {4,D}
3   Cd  u0 {1,S} {5,D}
4   Cdd u0 {2,D} {8,D}
5   Cdd u0 {3,D} {9,D}
6   S2s  u0 {1,S}
7   H   u0 {1,S}
8   C   u0 {4,D}
9   C   u0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1171,
    label = "Cs-CtCsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.65270886584, 7.81454146943, 8.80077736206, 9.57069745483, 11.7776615372, 13.0598760913, 11.6351420922], 'cal/(mol*K)'),
        H298 = (10.3629738865,'kcal/mol'),
        S298 = (-2.96178821527,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CtCdsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cd u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CtSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CtSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   S2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CtSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Ct  u0 {1,S}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CtCtSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1172,
    label = "Cs-CbCsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.44010952363, 8.85865200258, 9.95984521873, 10.6258115544, 12.5184309366, 13.3408578268, 12.2722585453], 'cal/(mol*K)'),
        H298 = (8.78524353812,'kcal/mol'),
        S298 = (-6.23236841037,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-CbCdsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cd u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CbSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)CbSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)CbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   S2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)CbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)CbSsH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cb  u0 {1,S}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCtSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CbCbSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCbSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=SC=SSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   CS u0 {1,S} {7,D}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1174,
    label = "Cs-C=SCsSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.63,8.58,9.55,10.04,10.49,10.68,11.16],'cal/(mol*K)'),
        H298 = (-3.61,'kcal/mol'),
        S298 = (-14.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-C=SCtSsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cd)SsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   S2s  u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-Cd)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   C   u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cdd-S2d)SsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 {1,S} {4,D}
3   CS  u0 {1,S} {7,D}
4   Cdd u0 {2,D} {8,D}
5   S2s  u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
8   S2d u0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-C=S(Cds-Cds)SsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   S2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   S2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-CSHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsSHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1163,
    label = "Cs-CsSHH",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = u'Cs-CsS2HH',
    shortDesc = u"""""",
    longDesc =
u""""

""",
)

entry(
    index = 1163,
    label = "Cs-CsS2HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.97105487034, 8.16521488142, 9.39849251857, 10.4332352113, 13.2996734018, 15.0664100743, 15.5129887976], 'cal/(mol*K)'),
        H298 = (4.18010177562,'kcal/mol'),
        S298 = (17.4217846106,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1163,
    label = "Cs-CsS4HH",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.176813218, 6.11661170125, 6.91223768838, 7.99547769869, 11.6235778285, 14.0246968132, 15.1038413438], 'cal/(mol*K)'),
        H298 = (9.15676763707,'kcal/mol'),
        S298 = (12.2672001286,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1163,
    label = "Cs-CsS6HH",
    group =
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.91691474685, 5.80834217306, 7.28720982282, 8.59968707154, 11.7958374105, 13.8211387648, 14.9095276482], 'cal/(mol*K)'),
        H298 = (1.9470921512,'kcal/mol'),
        S298 = (21.7193927897,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1164,
    label = "Cs-CdsSsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.99701097084, 10.8903732044, 11.5478901721, 12.1380970698, 14.2958450972, 15.8154019063, 16.0602090172], 'cal/(mol*K)'),
        H298 = (4.28867178147,'kcal/mol'),
        S298 = (15.5090339647,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)SsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cds)SsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd)SsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   S2s  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-S2d)SsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   S2d u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "Cs-(Cds-Cdd-Cd)SsHH",
    group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   S2s  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1165,
    label = "Cs-CtSsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.98706833584, 8.31706536443, 9.54876971706, 10.6570645698, 13.4807399372, 15.3537766663, 14.9345493622], 'cal/(mol*K)'),
        H298 = (7.01048822647,'kcal/mol'),
        S298 = (18.4257452447,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1166,
    label = "Cs-CbSsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.53359040363, 8.79729349258, 10.0676673937, 11.1378870794, 13.8173133466, 15.3662889918, 15.4255874153], 'cal/(mol*K)'),
        H298 = (3.36112478812,'kcal/mol'),
        S298 = (15.6310780196,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1168,
    label = "Cs-C=SSsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.8250980329, 12.7954785413, 13.7781372911, 14.3817207328, 16.6598536488, 18.0650619144, 17.9835242648], 'cal/(mol*K)'),
        H298 = (-1.85980131799,'kcal/mol'),
        S298 = (22.428392751,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1093,
    label = "O",
    group = 
"""
1 * O u0
""",
    thermo = u'O2s-CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2500,
    label = "Oa(S)",
    group =
"""
1 * O u0 p3 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (104.81,'kcal/mol'),
        S298 = (34.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""PrimaryTHermoLibrary""",
    longDesc =
u"""
H298: ATcT version 1.110
level of theory energy: CCSD(T)F12A/cc-pVQZ-F12//CCSD(T)/cc-pVQZ
level of theory frequency: B3LYP/6-311++g(d,p)//B3LYP/6-311++g(d,p)
""",
)

entry(
    index = 1094,
    label = "O2d",
    group = 
"""
1 * O2d u0
""",
    thermo = u'O2d-Cd',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1095,
    label = "O2d-Cd",
    group = 
"""
1 * O2d u0 {2,D}
2   CO u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""In this case the C is treated as the central atom""",
    longDesc = 
u"""

""",
)

entry(
    index = 1096,
    label = "O2d-O2d",
    group = 
"""
1 * O2d u0 {2,D}
2   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.575,3.685,3.8,3.99,4.12,4.29],'cal/(mol*K)'),
        H298 = (14.01,'kcal/mol'),
        S298 = (24.085,'cal/(mol*K)'),
    ),
    shortDesc = u"""A. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 1943,
    label = "O2d-N3d",
    group = 
"""
1 * O2d  u0 {2,D}
2   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1944,
    label = "O2d-N5dc",
    group = 
"""
1 * O2d  u0 {2,D}
2   N5dc u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1097,
    label = "O2s",
    group = 
"""
1 * O2s u0
""",
    thermo = u'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1945,
    label = "O2s-N",
    group = 
"""
1 * O2s u0 {2,S}
2   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1935,
    label = "O2s-CN",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1874,
    label = "O2s-CsN3s",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.6,4,4.3,4.7,4.8,4.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-9.2,'kcal/mol','+|-',1.3),
        S298 = (7.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1875,
    label = "O2s-CsN3d",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   N3d u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1847,
    label = "O2s-Cs(N3dOd)",
    group = 
"""
1 * O2s  u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   O2d  u0 {2,D}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.6,11.3,11.9,12.6,13.6,14.3,14.8],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (-4.8,'kcal/mol','+|-',1.1),
        S298 = (40,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1877,
    label = "O2s-CdN3d",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   N3d u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1878,
    label = "O2s-(Cd-Cd)(N3dOd)",
    group = 
"""
1   Cd  u0 {2,S} {4,D} {5,S}
2 * O2s  u0 {1,S} {3,S}
3   N3d u0 {2,S} {6,D}
4   Cd  u0 {1,D}
5   R   u0 {1,S}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.1,11.7,12.2,12.7,13.5,14.1,14.9],'cal/(mol*K)','+|-',[0.7,0.7,0.7,0.7,0.7,0.7,0.7]),
        H298 = (-5.3,'kcal/mol','+|-',0.9),
        S298 = (39.5,'cal/(mol*K)','+|-',0.9),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1876,
    label = "O2s-CsN5dc",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   N5dc u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1848,
    label = "O2s-Cs(N5dcOdOs)",
    group = 
"""
1   N5dc u0 {2,S} {3,D} {4,S}
2 * O2s  u0 {1,S} {5,S}
3   O2d  u0 {1,D}
4   O2s  u0 {1,S}
5   Cs  u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.2,13.9,15.4,16.6,18.4,19.3,19.9],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (-19.1,'kcal/mol','+|-',1.1),
        S298 = (45.3,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1879,
    label = "O2s-CdN5dc",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   N5dc u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1880,
    label = "O2s-(Cd-CdHH)(N5dcOdOs)",
    group = 
"""
1   N5dc u0 {3,S} {4,D} {5,S}
2   Cd  u0 {3,S} {6,D} {7,S}
3 * O2s  u0 {1,S} {2,S}
4   O2d  u0 {1,D}
5   O2s  u0 {1,S}
6   Cd  u0 {2,D}
7   R   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.4,14.2,15.7,16.9,18.5,19.3,20.1],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (-18.4,'kcal/mol','+|-',1.1),
        S298 = (45.4,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1936,
    label = "O2s-ON",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1881,
    label = "O2s-OsN3s",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   O2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.9,5.6,6.3,7,7.1,6.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (5.3,'kcal/mol','+|-',1.3),
        S298 = (6.9,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1882,
    label = "O2s-OsN3d",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   O2s  u0 {1,S}
3   N3d u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1883,
    label = "O2s-O2s(N3dOd)",
    group = 
"""
1 * O2s  u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   O2d  u0 {2,D}
4   O2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.7,12.9,13.6,14.2,15,15.5,16],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (15.2,'kcal/mol','+|-',1.3),
        S298 = (40.7,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1937,
    label = "O2s-NN",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1884,
    label = "O2s-N3sN3s",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8,4.6,5.1,5.2,5.2,4.9,4.3],'cal/(mol*K)','+|-',[1.6,1.6,1.6,1.6,1.6,1.6,1.6]),
        H298 = (5.7,'kcal/mol','+|-',2.2),
        S298 = (6.8,'cal/(mol*K)','+|-',2.1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1885,
    label = "O2s-N3sN3d",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   N3d u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1886,
    label = "O2s-N3s(N3dOd)",
    group = 
"""
1 * O2s  u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   O2d  u0 {2,D}
4   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.2,11.5,12.4,13,13.9,14.3,14.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (10.8,'kcal/mol','+|-',1.3),
        S298 = (40.8,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1098,
    label = "O2s-HH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.03,8.19,8.42,8.68,9.26,9.86,11.26],'cal/(mol*K)'),
        H298 = (-57.8,'kcal/mol','+|-',0.01),
        S298 = (46.51,'cal/(mol*K)','+|-',0.002),
    ),
    shortDesc = u"""O-HH WATER. !!!Using NIST value for H2O, S(group) = S(H2O) + Rln(2)""",
    longDesc = 
u"""

""",
)

entry(
    index = 1099,
    label = "O2s-OsH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.21,5.72,6.17,6.66,7.15,7.61,8.43],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (-16.3,'kcal/mol','+|-',0.14),
        S298 = (27.83,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""O-OH SANDIA 1/2*H2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 1100,
    label = "O2s-OsOs",
    group =
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.2,3.64,4.2,4.34,4.62,4.9,4.9],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.85,'kcal/mol','+|-',0.16),
        S298 = (9.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-OO LAY 1997=20 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc =
u"""

""",
)

entry(
    index = 1100,
    label = "O2s-SsOs",
    group =
"""
1 * O2s u0 {2,S} {3,S}
2   S   u0 {1,S}
3   O2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.23501508538, 3.81646072154, 4.086407263, 4.22204283211, 4.78817153826, 4.90802403895, 4.88871371802], 'cal/(mol*K)'),
        H298 = (-3.33921943066,'kcal/mol'),
        S298 = (8.69896260294,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 1101,
    label = "O2s-CH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = u'O2s-CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1102,
    label = "O2s-CtH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-37.9,'kcal/mol','+|-',0.16),
        S298 = (29.1,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CtH BENSON (Assigned O-CsH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 1103,
    label = "O2s-CdsH",
    group = 
"""
1 * O2s      u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
""",
    thermo = u'O2s-(Cds-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1104,
    label = "O2s-(Cds-O2d)H",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   H  u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.07,19.8,20.85,22.07,24.57,26.95,31.66],'J/(mol*K)','+|-',[2.54,2.54,2.54,2.54,2.54,2.54,2.54]),
        H298 = (-165.2,'kJ/mol','+|-',2.16),
        S298 = (125.32,'J/(mol*K)','+|-',2.96),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1105,
    label = "O2s-(Cds-Cd)H",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   H  u0 {1,S}
4   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.6,30.3,32.52,33.15,33.29,33.55,34.97],'J/(mol*K)','+|-',[4.18,4.18,4.18,4.18,4.18,4.18,4.18]),
        H298 = (-188.1,'kJ/mol','+|-',3.56),
        S298 = (106.3,'J/(mol*K)','+|-',4.87),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1106,
    label = "O2s-CsH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.07,19.8,20.85,22.07,24.57,26.95,31.66],'J/(mol*K)','+|-',[2.54,2.54,2.54,2.54,2.54,2.54,2.54]),
        H298 = (-165.2,'kJ/mol','+|-',2.16),
        S298 = (125.32,'J/(mol*K)','+|-',2.96),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc =
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1107,
    label = "O2s-CbH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-37.9,'kcal/mol','+|-',0.16),
        S298 = (29.1,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CbH BENSON (Assigned O-CsH)""",
    longDesc = 
u"""

""",
)

entry(
    index = 1460,
    label = "O2s-CSH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CS u0 {1,S} {4,D}
3   H  u0 {1,S}
4   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.37509714471, 3.80993071627, 4.71931696357, 5.55947387879, 6.82899017016, 7.74558507626, 9.16700739329], 'cal/(mol*K)'),
        H298 = (-51.2948420389,'kcal/mol'),
        S298 = (31.2732634287,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1108,
    label = "O2s-OsC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = u'O2s-OsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1109,
    label = "O2s-OsCt",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.31,4.6,4.84,5.32,5.8,5.8],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (7,'kcal/mol','+|-',0.3),
        S298 = (10.8,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""O-OCb Hf JWB plot S,Cp assigned O/O/Cd !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1110,
    label = "O2s-OsCds",
    group = 
"""
1 * O2s      u0 {2,S} {3,S}
2   O2s      u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    thermo = u'O2s-O2s(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1111,
    label = "O2s-O2s(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   O2s u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.53,5.02,5.79,6.08,6.54,6.49,6.49],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-23.22,'kcal/mol','+|-',0.3),
        S298 = (9.11,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""O-OCO jwl cbsQ 99 cqcho=20 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1112,
    label = "O2s-O2s(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   O2s u0 {1,S}
4   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.87,3.95,4.15,4.73,4.89,4.89],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (1.64,'kcal/mol','+|-',0.3),
        S298 = (10.12,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""O-OCd WESTMORELAND S,Cp LAY'9405 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1113,
    label = "O2s-OsCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.31,4.6,4.84,5.32,5.8,5.8],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-5.4,'kcal/mol','+|-',0.3),
        S298 = (8.54,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""O-OCs LAY 1997 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1114,
    label = "O2s-OsCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Cb u0 {1,S}
""",
    thermo = u'O2s-O2s(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1115,
    label = "O2s-CC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = u'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1116,
    label = "O2s-CtCt",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
""",
    thermo = u'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1117,
    label = "O2s-CtCds",
    group = 
"""
1 * O2s      u0 {2,S} {3,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    thermo = u'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1118,
    label = "O2s-Ct(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   Ct u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = u'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1119,
    label = "O2s-Ct(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Ct u0 {1,S}
4   C  u0 {2,D}
""",
    thermo = u'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1120,
    label = "O2s-CtCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
""",
    thermo = u'O2s-Cs(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1873,
    label = "O2s-Cs(CtN3t)",
    group = 
"""
1 * O2s  u0 {2,S} {4,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.1,9.8,10.6,11.2,12.3,13,13.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (10,'kcal/mol','+|-',1.3),
        S298 = (39.1,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1121,
    label = "O2s-CtCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct u0 {1,S}
3   Cb u0 {1,S}
""",
    thermo = u'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1122,
    label = "O2s-CdsCds",
    group = 
"""
1 * O2s      u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    thermo = u'O2s-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1123,
    label = "O2s-(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   CO u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.4,11.55,6.97,3.72,-0.53,-2.57,-1.41],'J/(mol*K)','+|-',[6.51,6.51,6.51,6.51,6.51,6.51,6.51]),
        H298 = (-46.4,'kJ/mol','+|-',5.54),
        S298 = (80.8,'J/(mol*K)','+|-',7.59),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1124,
    label = "O2s-(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {5,D}
3   Cd u0 {1,S} {4,D}
4   C  u0 {3,D}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.02,19.61,18.5,17.71,17.02,16.49,15.33],'J/(mol*K)','+|-',[8.17,8.17,8.17,8.17,8.17,8.17,8.17]),
        H298 = (-100.6,'kJ/mol','+|-',6.96),
        S298 = (38.43,'J/(mol*K)','+|-',9.53),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1125,
    label = "O2s-(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-19.61,'kcal/mol','+|-',0.19),
        S298 = (10,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CdCd BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index = 1126,
    label = "O2s-CdsCs",
    group = 
"""
1 * O2s      u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
""",
    thermo = u'O2s-Cs(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1127,
    label = "O2s-Cs(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   Cs u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.49,9.94,9.96,10.7,12.71,14.71,18],'J/(mol*K)','+|-',[3.15,3.15,3.15,3.15,3.15,3.15,3.15]),
        H298 = (-102.2,'kJ/mol','+|-',2.69),
        S298 = (45.71,'J/(mol*K)','+|-',3.68),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1128,
    label = "O2s-Cs(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cs u0 {1,S}
4   C  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.07,23.32,25.26,25.92,25.5,24.52,22.72],'J/(mol*K)','+|-',[3.47,3.47,3.47,3.47,3.47,3.47,3.47]),
        H298 = (-123.9,'kJ/mol','+|-',2.96),
        S298 = (18.91,'J/(mol*K)','+|-',4.05),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = -1,
    label = "O2s-CdsCb",
    group = 
"""
1 * O2s      u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   Cb      u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "O2s-Cb(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   Cb u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "O2s-Cb(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cb u0 {1,S}
4   C  u0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1129,
    label = "O2s-CsCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.7,13.4,13.58,14.54,16.71,18.29,20.17],'J/(mol*K)','+|-',[2.44,2.44,2.44,2.44,2.44,2.44,2.44]),
        H298 = (-98.6,'kJ/mol','+|-',2.08),
        S298 = (38.61,'J/(mol*K)','+|-',2.85),
    ),
    shortDesc = u"""\Derived from CBS-QB3 calculation with 1DHR treatment""",
    longDesc = 
u"""
Derived using calculations at B3LYP/6-311G(d,p)/CBS-QB3 level of theory. 1DH-rotors
optimized at the B3LYP/6-31G(d).Paraskevas et al, Chem. Eur. J. 2013, 19, 16431-16452,
DOI: 10.1002/chem.201301381
""",
)

entry(
    index = 1130,
    label = "O2s-CsCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.6],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-22.6,'kcal/mol','+|-',0.19),
        S298 = (9.7,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CbCs REID, PRAUSNITZ and SHERWOOD !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 1131,
    label = "O2s-CbCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19,-0.24,-0.72,-0.51,0.43,1.36,1.75],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-18.77,'kcal/mol','+|-',0.19),
        S298 = (13.59,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CbCb CHERN 1/97 Hf PEDLEY, Mopac""",
    longDesc = 
u"""

""",
)

entry(
    index = 1461,
    label = "O2s-Cs(Cds-S2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   CS u0 {1,S} {4,D}
4   S2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.01016915331, 1.85601360252, 2.34306888626, 2.92650771427, 3.9101554919, 4.6197868587, 5.58990042609], 'cal/(mol*K)'),
        H298 = (-34.1353220711,'kcal/mol'),
        S298 = (9.0769267427,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = 1600,
    label = "Si",
    group = 
"""
1 * Si u0
""",
    thermo = u'Cs-HHHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2504,
    label = "SiJ2(S)",
    group =
"""
1 * Si u0 p1
""",
    thermo = u'CJ2_singlet',
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 1400,
    label = "S",
    group = 
"""
1 * S u0
""",
    thermo = u'S2s-CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "S2d",
    group = 
"""
1 * S2d u0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2501,
    label = "Sa(S)",
    group =
"""
1 * S u0 p3 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,4.97,4.97,4.97,4.97,5.13,5.06],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (66.2,'kcal/mol','+|-',1),
        S298 = (40.11,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""SulfurLibrary""",
    longDesc =
u"""
H298, S298, Cp1000, Cp1500 from [10], rest from AGV
Singlet sulfur, thermo data copied from triplet sulfur, likely very incorrect (taken from SulfurLibrary).
""",
)

entry(
    index = 1160,
    label = "S2d-C",
    group = 
"""
1 * S2d u0 {2,D}
2   C u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1161,
    label = "S2d-S",
    group = 
"""
1 * S2d u0 {2,D}
2   S u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.19716395226, 2.23141203381, 2.10060564926, 1.9236602295, 1.72523487459, 1.5415821619, 1.37558758592], 'cal/(mol*K)'),
        H298 = (45.0698684027,'kcal/mol'),
        S298 = (14.4929177111,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc = 
u"""

""",
)

entry(
    index = 1161,
    label = "S2d-O",
    group =
"""
1 * S2d u0 {2,D}
2   O u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.267, 7.55, 7.84, 8.077, 8.389, 8.573, 8.773], 'cal/(mol*K)'),
        H298 = (0.26064,'kcal/mol'),
        S298 = (50.866,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = -1,
    label = "S2s",
    group = 
"""
1 * S2s u0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1132,
    label = "S2s-HH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.150095602, 8.484703633, 8.843212237, 9.249521989, 10.08604207, 10.82695985, 12.09369025], 'cal/(mol*K)'),
        H298 = (-5.377629063,'kcal/mol'),
        S298 = (50.52581262,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "S2s-CH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1133,
    label = "S2s-CsH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.73698416637, 5.23668260742, 5.51579532127, 5.74489590563, 4.96122489336, 4.87237353319, 6.96133610475], 'cal/(mol*K)'),
        H298 = (-5.13157240812,'kcal/mol'),
        S298 = (25.9818713104,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1134,
    label = "S2s-CdH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.57256617375, 6.00667614039, 6.92562207143, 7.55994614146, 7.22292032999, 7.17278036786, 9.65907008137], 'cal/(mol*K)'),
        H298 = (-11.2360647656,'kcal/mol'),
        S298 = (32.5588731097,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1135,
    label = "S2s-CtH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.75478429461, 7.89219812568, 9.13371867733, 9.79438154969, 9.09544545446, 8.66113989654, 10.5469911807], 'cal/(mol*K)'),
        H298 = (-16.4630239469,'kcal/mol'),
        S298 = (28.4680082041,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1136,
    label = "S2s-CbH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.14232953135, 7.36600010511, 8.62188241976, 9.33885021287, 8.73631528625, 8.48280627133, 10.8946670185], 'cal/(mol*K)'),
        H298 = (-13.645387113,'kcal/mol'),
        S298 = (29.5804660471,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1462,
    label = "S2s-(C=O)H",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   H  u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.60421593673, 5.70454124893, 6.50652259237, 7.1706335281, 7.10206591007, 7.06637903561, 8.954074827], 'cal/(mol*K)'),
        H298 = (-14.6483659608,'kcal/mol'),
        S298 = (22.1771310177,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1153,
    label = "S2s-(C=S2d)H",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CS u0 {1,S} {4,D}
3   H  u0 {1,S}
4   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.8191893134, 7.97060346872, 9.10323298521, 9.70005291657, 9.01331959238, 8.69287424158, 10.8606740162], 'cal/(mol*K)'),
        H298 = (-19.5172757868,'kcal/mol'),
        S298 = (42.3077229963,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1147,
    label = "S2s-S2sH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.81566141978, 6.59131198331, 7.14568242211, 7.50431550416, 8.02105105115, 8.39446348109, 8.97646790308], 'cal/(mol*K)'),
        H298 = (2.23490129729,'kcal/mol'),
        S298 = (32.6296918447,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 11488,
    label = "S2s-S_DeH",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   [S4d,S6d,S6dd]  u0 {1,S}
3   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.27295538946, 6.84959222202, 6.94231736097, 7.33902362195, 7.76760886673, 8.07656475568, 8.49362410941], 'cal/(mol*K)'),
        H298 = (2.08364970862,'kcal/mol'),
        S298 = (28.4688615788,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1148,
    label = "S2s-SH",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   S  ux {1,S}
3   H  u0 {1,S}
""",
    thermo = u'S2s-S2sH',
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 1152,
    label = "S2s-SsSs",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.18608786344, 6.33041988715, 6.28243741299, 6.44963826821, 6.56830143931, 6.50676603543, 5.9535264127], 'cal/(mol*K)'),
        H298 = (2.35039744965,'kcal/mol'),
        S298 = (8.66425865962,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1152,
    label = "S2s-SS",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   S ux {1,S}
3   S ux {1,S}
""",
    thermo = u'S2s-SsSs',
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 1152,
    label = "S2s-SO",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   S ux {1,S}
3   O ux {1,S}
""",
    thermo = u'S2s-S2O',
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 1152,
    label = "S2s-S2O",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   S2s ux {1,S}
3   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.91386255834, 6.8213093274, 6.88365699469, 6.90589914261, 6.63391426614, 6.47697892332, 5.91079003009], 'cal/(mol*K)'),
        H298 = (5.49319983176,'kcal/mol'),
        S298 = (10.0543125885,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 1152,
    label = "S2s-S4O",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   [S4s,S4d,S4b,S4t] ux {1,S}
3   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.55629482228, 7.20964820399, 7.14779247652, 7.80120801456, 7.88631973358, 7.76799406866, 7.0830008553], 'cal/(mol*K)'),
        H298 = (6.4176767089,'kcal/mol'),
        S298 = (5.38528707731,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 1152,
    label = "S2s-S6O",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   [S6s,S6d,S6dd,S6t,S6td] ux {1,S}
3   O ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.40812668423, 8.97337642109, 9.12705514021, 9.24790849285, 9.12882390201, 8.79440881794, 7.11127351378], 'cal/(mol*K)'),
        H298 = (3.25326643195,'kcal/mol'),
        S298 = (1.92879144439,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = -1,
    label = "S2s-SC",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   S ux {1,S}
3   C ux {1,S}
""",
    thermo = u'S2s-S2sC',
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = -1,
    label = "S2s-S2sC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = u'S2s-S2sCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = -1,
    label = "S2s-S46C",
    group =
"""
1 * S2s u0 {2,S} {3,S}
2   [S4s,S4d,S4b,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.1691431915, 4.58843892617, 4.40137151384, 4.56776137391, 3.32401686698, 2.65698899774, 3.9958567635], 'cal/(mol*K)'),
        H298 = (-4.61562860071,'kcal/mol'),
        S298 = (2.97970536535,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u"""

""",
)

entry(
    index = 1148,
    label = "S2s-S2sCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.02379705921, 4.61355555637, 4.8046960243, 4.84849770916, 3.68191779325, 3.06475319884, 4.26478018592], 'cal/(mol*K)'),
        H298 = (-2.90505631993,'kcal/mol'),
        S298 = (4.63681187439,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1149,
    label = "S2s-S2sCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.98567585631, 5.4355436579, 6.15006333029, 6.55194342493, 5.50581519638, 4.8687042787, 6.30032768405], 'cal/(mol*K)'),
        H298 = (-9.17172524384,'kcal/mol'),
        S298 = (14.5610790986,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1150,
    label = "S2s-S2sCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.02063470709, 7.05615996784, 8.08494429801, 8.50002758712, 7.28290642236, 6.34325752821, 7.38861794858], 'cal/(mol*K)'),
        H298 = (-12.0793869937,'kcal/mol'),
        S298 = (11.585640054,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1151,
    label = "S2s-S2sCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.08987147795, 6.40666947075, 7.1543417046, 7.63041403263, 6.88163834128, 6.17219357109, 7.39049132427], 'cal/(mol*K)'),
        H298 = (-13.1085922892,'kcal/mol'),
        S298 = (8.95539786032,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = -1,
    label = "S2s-CC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1137,
    label = "S2s-CsCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.06621355466, 3.16753276973, 3.45726747132, 3.42727798451, 0.981247403048, -0.444614829575, 2.1842392677], 'cal/(mol*K)'),
        H298 = (-7.09022818705,'kcal/mol'),
        S298 = (-3.94684833795,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1138,
    label = "S2s-CsCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cd u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.43905917499, 4.92735808798, 5.49352062946, 5.67053437777, 3.32194360513, 2.06343166008, 4.9839687075], 'cal/(mol*K)'),
        H298 = (-15.0003121145,'kcal/mol'),
        S298 = (3.6594672162,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1463,
    label = "S2s-Cs(C=O)",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   CO u0 {1,S} {4,D}
4   O2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.86779836287, 2.22560223524, 3.20326216439, 4.02058636224, 2.84988068957, 2.08251937638, 4.71733686041], 'cal/(mol*K)'),
        H298 = (-19.722300141,'kcal/mol'),
        S298 = (-8.71940593717,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1139,
    label = "S2s-CsCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.31865788732, 5.50343142168, 6.53759049404, 6.94255837948, 4.59542056533, 3.16065843277, 5.79818534766], 'cal/(mol*K)'),
        H298 = (-20.6895077492,'kcal/mol'),
        S298 = (2.34649107599,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1140,
    label = "S2s-CsCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.44329681406, 4.80992938111, 5.90625136647, 6.39142474267, 4.16458867713, 2.95842423756, 6.12196061545], 'cal/(mol*K)'),
        H298 = (-17.0353508353,'kcal/mol'),
        S298 = (2.45512482902,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1141,
    label = "S2s-CdCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.79691685853, 4.96906442227, 6.14001509903, 6.74016808417, 4.85856842002, 3.82151579628, 7.24066009346], 'cal/(mol*K)'),
        H298 = (-19.8931410144,'kcal/mol'),
        S298 = (13.4070199415,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1142,
    label = "S2s-CdCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd u0 {1,S}
3   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.31434225566, 6.24097282124, 7.79362268424, 8.47888617158, 6.36857938774, 5.01233422885, 7.51972999138], 'cal/(mol*K)'),
        H298 = (-25.0606138678,'kcal/mol'),
        S298 = (9.48927106164,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1143,
    label = "S2s-CdCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd u0 {1,S}
3   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.15436775066, 6.06672489124, 7.62174251091, 8.35746806991, 6.37937926441, 5.13120931218, 8.34860188805], 'cal/(mol*K)'),
        H298 = (-23.1470447178,'kcal/mol'),
        S298 = (10.328793045,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1144,
    label = "S2s-CtCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.59289555588, 10.0523503547, 12.609642578, 13.9501142727, 12.3975575756, 11.2181880231, 14.3290365414], 'cal/(mol*K)'),
        H298 = (-9.23265086052,'kcal/mol'),
        S298 = (10.7776990182,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1145,
    label = "S2s-CtCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct u0 {1,S}
3   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.79533022588, 7.28480414469, 9.07776239466, 9.88344760604, 7.70381635226, 6.22493117642, 9.1953462981], 'cal/(mol*K)'),
        H298 = (-27.4334793805,'kcal/mol'),
        S298 = (6.49544280157,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1146,
    label = "S2s-CbCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.82042901588, 6.51506545469, 8.47484333799, 9.3612041327, 7.33063598559, 5.98396245308, 9.07091034143], 'cal/(mol*K)'),
        H298 = (-25.7957483405,'kcal/mol'),
        S298 = (7.93353074824,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1154,
    label = "S2s-(C=S2d)Cs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   CS u0 {1,S} {4,D}
4   S2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.04799684221, 4.39763410812, 5.66349748174, 6.34575395163, 4.34909478063, 3.19006147083, 6.10890275386], 'cal/(mol*K)'),
        H298 = (-24.1755794692,'kcal/mol'),
        S298 = (12.2752776027,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)



entry(
    index = 1158,
    label = "S2s-(C=S2d)(C=S2d)",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CS u0 {1,S} {4,D}
3   CS u0 {1,S} {5,D}
4   S2d u0 {2,D}
5   S2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.6189251388, 6.52833494438, 8.13836977086, 9.11679738123, 7.41796769332, 6.23163203627, 8.76834554571], 'cal/(mol*K)'),
        H298 = (-26.4696800566,'kcal/mol'),
        S298 = (25.3828532162,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 1155,
    label = "S2s-(C=S2d)Cmb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   [Cd,Cb,Ct,CO] u0 {1,S}
3   CS u0 {1,S} {4,D}
4   S2d u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.17187593234, 6.52170020454, 8.24685512442, 9.04779616697, 6.94409151446, 5.59393488967, 8.54916905357], 'cal/(mol*K)'),
        H298 = (-27.0887371436,'kcal/mol'),
        S298 = (17.0764520172,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)


entry(
    index = 1887,
    label = "N",
    group = 
"""
1 * N u0
""",
    thermo = u'N3s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10001,
    label = "N0sc",
    group = 
"""
1 * N0sc u0 p3 c-2 {2,S}
2   R    ux px     {1,S}
""",
    thermo = u'N1s',
    shortDesc = u"""""",
    longDesc = 
u"""
Nitrogen with three lone pairs and a single bond (e.g., [NH+]#[N+][N-2])
""",
)

entry(
    index = 10002,
    label = "N1s",
    group = 
"""
1 * N1s u0 p2
""",
    thermo = u'N1s-H',
    shortDesc = u"""""",
    longDesc = 
u"""
Nitrogen with two lone pairs and a single bond
""",
)

entry(
    index = 10003,
    label = "N1s-H",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   H   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.9764,6.9777,6.9982,7.0454,7.2242,7.4742,8.0656],'cal/(mol*K)'),
        H298 = (85.2952,'kcal/mol'),
        S298 = (43.3053,'cal/(mol*K)'),
    ),
    shortDesc = u"""NH(S)""",
    longDesc = 
u"""
Data base on species NH(S), source: GRIMech3.0-N
""",
)

entry(
    index = 10004,
    label = "N1s-N1s",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   N1s u0 p2 {1,S}
""",
    thermo = u'N1s-H',
    shortDesc = u"""[N][N](S)""",
    longDesc = 
u"""
Pointing to NH(S), so far no better alternative
""",
)

entry(
    index = 10005,
    label = "N1s-Cs",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   C   u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.00,2.65,2.50,2.49,2.65,2.65,2.57],'cal/(mol*K)'),
        H298 = (120.94,'kcal/mol'),
        S298 = (24.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""[N]-CH3(S)""",
    longDesc = 
u"""
Data base on species CH3N(S), source: thermo_DFT_CCSDTF12_BAC
level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
subtracting the Cs-N2sHHH group
[N1s-CH3 (N-CH3 species) from thermo_DFT_CCSDTF12_BAC] - [Cs-N2sHHH from group.py]
""",
)

entry(
    index = 10006,
    label = "N1s-N3s",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   N   u0 px {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.97,2.07,2.25,2.50,3.05,3.48,5.50],'cal/(mol*K)'),
        H298 = (61.00,'kcal/mol'),
        S298 = (23.00,'cal/(mol*K)'),
    ),
    shortDesc = u"""[N]-NH2(S)""",
    longDesc = 
u"""
Data base on species H2NN(S), source: Curran thermo library
subtracting the N3s-N3sFF group
[N1s-NH2 (N-NH2 species) from Curran] - [N3s-N3sHH from group.py]
""",
)

entry(
    index = 10007,
    label = "N1s-O2s",
    group = 
"""
1 * N1s u0 p2 {2,S}
2   O   u0 px {1,S}
""",
    thermo = u'N1s-H',
    shortDesc = u"""[N]-OH(S)""",
    longDesc = 
u"""
Pointing to NH(S), so far no better alternative
""",
)

entry(
    index = 1922,
    label = "N1dc",
    group = 
"""
1 * N1dc u0 p2 {2,D}
2   R!H ux px {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10001,
    label = "N1sc",
    group = 
"""
1 * N1sc u0 p2 {2,S} (3,S}
2   R   ux px {1,S}
3   R   ux px {1,S}
""",
    thermo = u'N1s',
    shortDesc = u"""""",
    longDesc = 
u"""
Nitrogen with two lone pairs and two single bonds
""",
)

entry(
    index = 1888,
    label = "N3s",
    group = 
"""
1 * N3s u0
""",
    thermo = u'N3s-CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1938,
    label = "N3s-CHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1808,
    label = "N3s-CsHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.72,6.51,7.32,8.07,9.41,10.47,12.28],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (29.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1817,
    label = "N3s-CbHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.72,6.51,7.32,8.07,9.41,10.47,12.28],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (29.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1825,
    label = "N3s-(CO)HH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.07,5.74,7.13,8.29,9.96,11.22,14.37],'cal/(mol*K)'),
        H298 = (-14.9,'kcal/mol'),
        S298 = (-24.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1889,
    label = "N3s-CdHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.7,6.5,7.3,8.1,9.4,10.5,12.3],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (29.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1938,
    label = "N3s-CCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1809,
    label = "N3s-CsCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.2,5.21,6.13,6.83,7.9,8.65,9.55],'cal/(mol*K)'),
        H298 = (15.4,'kcal/mol'),
        S298 = (8.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1818,
    label = "N3s-CbCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (14.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1820,
    label = "N3s-CbCbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (16.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1826,
    label = "N3s-(CO)CsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-4.4,'kcal/mol'),
        S298 = (3.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1828,
    label = "N3s-(CO)CbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1829,
    label = "N3s-(CO)(CO)H",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d  u0 {2,D}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-18.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1894,
    label = "N3s-(CtN3t)CsH",
    group = 
"""
1 * N3s u0 {2,S} {4,S} {5,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,11.6,12.8,13.9,15.5,16.7,18.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (44.1,'kcal/mol','+|-',1.3),
        S298 = (40.7,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1899,
    label = "N3s-(CdCd)CsH",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.8,6.1,6.4,6.7,7.5,8.1,9.1],'cal/(mol*K)','+|-',[1.3,1.3,1.3,1.3,1.3,1.3,1.3]),
        H298 = (15.3,'kcal/mol','+|-',1.9),
        S298 = (8.7,'cal/(mol*K)','+|-',1.7),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1939,
    label = "N3s-CCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1810,
    label = "N3s-CsCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.48,4.56,5.43,5.97,6.56,6.67,6.5],'cal/(mol*K)'),
        H298 = (24.4,'kcal/mol'),
        S298 = (-13.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1819,
    label = "N3s-CbCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (26.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1827,
    label = "N3s-(CO)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1830,
    label = "N3s-(CO)(CO)Cs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-5.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1831,
    label = "N3s-(CO)(CO)Cb",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cb  u0 {1,S}
5   O2d  u0 {2,D}
6   O2d  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1895,
    label = "N3s-(CtN3t)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {4,S} {5,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.6,9.6,10.5,11.4,12.9,13.8,14.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (53.3,'kcal/mol','+|-',1.3),
        S298 = (21,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1898,
    label = "N3s-(CdCd)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,2.9,3.3,3.7,4.6,5,5.5],'cal/(mol*K)','+|-',[1.3,1.3,1.3,1.3,1.3,1.3,1.3]),
        H298 = (25.9,'kcal/mol','+|-',1.9),
        S298 = (-11,'cal/(mol*K)','+|-',1.7),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1811,
    label = "N3s-N3sHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.1,7.38,8.43,9.27,10.54,11.52,13.19],'cal/(mol*K)'),
        H298 = (11.4,'kcal/mol'),
        S298 = (29.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1812,
    label = "N3s-N3dHH",
    group =
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
4   N3d u0 {1,S}
""",
    thermo = u'N3s-N3sHH',
    shortDesc = u"""""",
    longDesc =
u"""
Currently points to N3s-N3sHH with no better estimate available
""",
)

entry(
    index = 1940,
    label = "N3s-NCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1812,
    label = "N3s-N3sCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.82,5.8,6.5,7,7.8,8.3,9],'cal/(mol*K)'),
        H298 = (20.9,'kcal/mol'),
        S298 = (9.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1814,
    label = "N3s-N3sCbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3s u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (22.1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1897,
    label = "N3s-CsH(N3dOd)",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   N3d u0 {1,S} {5,D}
5   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.4,11.9,13.4,14.7,16.6,17.9,19.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (25.2,'kcal/mol','+|-',1.3),
        S298 = (41.7,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1902,
    label = "N3s-CsH(N5dcOdOs)",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   N5dc u0 {1,S} {5,D} {6,S}
5   O2d  u0 {4,D}
6   O2s  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.1,15.5,17.6,19.2,21.4,22.8,24.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (8.4,'kcal/mol','+|-',1.3),
        S298 = (45.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1901,
    label = "N3s-(CdCd)HN3s",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.5,5.4,6.5,7.3,8.5,9.1,9.9],'cal/(mol*K)','+|-',[1.1,1.1,1.1,1.1,1.1,1.1,1.1]),
        H298 = (20.5,'kcal/mol','+|-',1.5),
        S298 = (6.6,'cal/(mol*K)','+|-',1.4),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1940,
    label = "N3s-NCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1893,
    label = "N3s-NCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (29.2,'kcal/mol'),
        S298 = (-13.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1813,
    label = "N3s-CsCsN3s",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.7,4.9,5.8,6.3,6.8,6.8,6.7],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (26.8,'kcal/mol','+|-',1.3),
        S298 = (-14.5,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1896,
    label = "N3s-CsCs(N3dOd)",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   N3d u0 {1,S} {5,D}
5   O2d  u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.4,10.5,11.5,12.4,13.8,14.6,15.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (32.6,'kcal/mol','+|-',1.3),
        S298 = (19.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1903,
    label = "N3s-CsCs(N5dcOdOs)",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   N5dc u0 {1,S} {5,D} {6,S}
5   O2d  u0 {4,D}
6   O2s  u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.5,13.4,15.2,16.7,18.8,20,21.1],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (16.7,'kcal/mol','+|-',1.3),
        S298 = (25.8,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1941,
    label = "N3s-NCdCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   Cd  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1900,
    label = "N3s-(CdCd)CsN3s",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.2,4.2,4.4,4.8,5.4,5.7,6],'cal/(mol*K)','+|-',[1.1,1.1,1.1,1.1,1.1,1.1,1.1]),
        H298 = (30.3,'kcal/mol','+|-',1.5),
        S298 = (-13.2,'cal/(mol*K)','+|-',1.4),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1891,
    label = "N3s-CsHOs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   O2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2,6.2,7,7.7,8.7,9.4,10.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (20.4,'kcal/mol','+|-',1.4),
        S298 = (8.1,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1892,
    label = "N3s-CsCsOs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,5.1,5.7,6.2,7,7.3,7.5],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (26.6,'kcal/mol','+|-',1.2),
        S298 = (-12.7,'cal/(mol*K)','+|-',1.1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1890,
    label = "N3s-OsHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   O2s  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.1,7.4,8.4,9.3,10.5,11.5,13.2],'cal/(mol*K)'),
        H298 = (11.4,'kcal/mol'),
        S298 = (29.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1904,
    label = "N3d",
    group = 
"""
1 * N3d u0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1906,
    label = "N3d-CdH",
    group = 
"""
1 * N3d      u0 {2,D} {3,S}
2   [Cd,Cdd] u0 {1,D}
3   H        u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3,3.5,3.9,4.3,5,5.5,6.4],'cal/(mol*K)'),
        H298 = (16.3,'kcal/mol'),
        S298 = (13.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1907,
    label = "N3d-CdN3s",
    group =
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   N3s  u0 {1,S}
""",
    thermo = u'N3d-CdH',
    shortDesc = u"""""",
    longDesc =
u"""
Currently references to N3d-CdH with no better data
""",
)

entry(
    index = 1815,
    label = "N3d-N3dH",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   H   u0 {1,S}
3   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.38,4.89,5.44,5.94,6.77,7.42,8.44],'cal/(mol*K)'),
        H298 = (25.1,'kcal/mol'),
        S298 = (26.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1822,
    label = "N3d-N3dN3s",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   N3d u0 {1,D}
3   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (23,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1909,
    label = "N3d-OdOs",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d  u0 {1,D}
3   O2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1910,
    label = "N3d-OdN3s",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d  u0 {1,D}
3   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1911,
    label = "N3d-CsR",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   Cs  u0 {1,S}
3   R!H u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (21.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1908,
    label = "N3d-OdC",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d  u0 {1,D}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1905,
    label = "N3d-CdCs",
    group = 
"""
1 * N3d      u0 {2,D} {3,S}
2   [Cd,Cdd] u0 {1,D}
3   Cs       u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2,2.2,2.2,2.3,2.5,2.7,2.9],'cal/(mol*K)'),
        H298 = (21.3,'kcal/mol'),
        S298 = (-6.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1907,
    label = "N3d-N3dCs",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.6,3.7,3.9,4.3,4.6,4.9],'cal/(mol*K)'),
        H298 = (27,'kcal/mol'),
        S298 = (7.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1912,
    label = "N3d-CbR",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   Cb  u0 {1,S}
3   R!H u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (16.7,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1913,
    label = "N5dc",
    group = 
"""
1 * N5dc u0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1914,
    label = "N5dc-OdOsCs",
    group = 
"""
1 * N5dc u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O2s  u0 {1,S}
4   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1915,
    label = "N5dc-OdOsCd",
    group = 
"""
1 * N5dc u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O2s  u0 {1,S}
4   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1916,
    label = "N5dc-OdOsOs",
    group = 
"""
1 * N5dc u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O2s  u0 {1,S}
4   O2s  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1917,
    label = "N5dc-OdOsN3s",
    group = 
"""
1 * N5dc u0 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O2s  u0 {1,S}
4   N3s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1918,
    label = "N5ddc",
    group = 
"""
1 * N5ddc u0 p0 c+1
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1919,
    label = "N3t",
    group =
"""
1 * N3t  u0 p1 {2,T}
2   R!H  u0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 1920,
    label = "N3t-CtH",
    group =
"""
1 * N3t  u0 p1 {2,T}
2   Ct   u0 {1,T} {3,S}
3   H    u0 (2,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28,5.68,5.97,6.22,6.6,6.97,6.66],'cal/(mol*K)'),
        H298 = (3.17,'kcal/mol'),
        S298 = (41.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Calculated by subtracting the data for the Ct-CtCs group (Ct-Cs STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714) from respective values from thermo_DFT_CCSDTF12_BAC data for the HCN species.
""",
)
    
entry(
    index = 2000,
    label = "S2s-OH",
    group =
"""
1 * S2s  u0 p2 {2,S} {3,S}
2   O    ux {1,S}
3   H    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.22093319549, 7.54935333849, 7.82390396332, 8.07268391528, 8.23928311342, 8.45317536895, 8.71527692416], 'cal/(mol*K)'),
        H298 = (9.66747779653,'kcal/mol'),
        S298 = (30.7645885392,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2000,
    label = "S2s-OC",
    group =
"""
1 * S2s  u0 p2 {2,S} {3,S}
2   O    ux {1,S}
3   C    ux (1,S)
""",
    thermo = u'S2s-OCs',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2000,
    label = "S2s-OCs",
    group =
"""
1 * S2s  u0 p2 {2,S} {3,S}
2   O    ux {1,S}
3   Cs    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.35266544606, 5.56317749795, 5.66792320645, 5.68861491902, 4.22803118429, 3.44249262325, 4.30451094661], 'cal/(mol*K)'),
        H298 = (0.904478033274,'kcal/mol'),
        S298 = (4.59117356714,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2000,
    label = "S2s-OO",
    group =
"""
1 * S2s  u0 p2 {2,S} {3,S}
2   O    ux {1,S}
3   O    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.21969280872, 7.64472820307, 8.26015454598, 8.56407038896, 8.27455213649, 7.98934141798, 7.07376660442], 'cal/(mol*K)'),
        H298 = (6.46836489835,'kcal/mol'),
        S298 = (8.06914403392,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2001,
    label = "S4d-OdCC",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   C    ux (1,S)
4   C    ux (1,S)
""",
    thermo = u'S4d-OdCsCs',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2001,
    label = "S4d-OdCsCs",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cs    ux (1,S)
4   Cs    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.5486513906, 11.6681656991, 12.6429281853, 12.8082597191, 9.33067593678, 7.22615342028, 8.6202390094], 'cal/(mol*K)'),
        H298 = (-48.0555864489,'kcal/mol'),
        S298 = (9.92679425077,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2001,
    label = "S4d-OdCdCd",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cd    ux (1,S)
4   Cd    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.73760096406, 6.9851684459, 9.53073683007, 9.59762283408, 7.25606043409, 6.05459975197, 9.23120662191], 'cal/(mol*K)'),
        H298 = (-53.0934793012,'kcal/mol'),
        S298 = (17.3139922441,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2002,
    label = "S4d-OdCO",
    group =
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   C   ux (1,S)
4   O   ux (1,S)
""",
    thermo = u'S4d-OdOsCs',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2002,
    label = "S4d-OdOsCs",
    group =
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   Cs   ux (1,S)
4   O   ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.9862817504, 12.102662985, 12.8679965785, 13.1598454352, 11.2357493115, 10.017358453, 10.4909185837], 'cal/(mol*K)'),
        H298 = (-46.9299278847,'kcal/mol'),
        S298 = (12.7803266783,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2002,
    label = "S4d-OdOsCd",
    group =
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   Cd   ux (1,S)
4   O   ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.11588763952, 9.63956299027, 11.3484509965, 11.5823242938, 10.3244893453, 9.62510999212, 10.8757185335], 'cal/(mol*K)'),
        H298 = (-48.0285148121,'kcal/mol'),
        S298 = (15.9861465324,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2003,
    label = "S4d-OdCS",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   C    ux (1,S)
4   S    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.52862521615, 10.093110299, 11.0219184341, 11.1180696101, 9.73528000347, 8.92610715958, 10.2321118639], 'cal/(mol*K)'),
        H298 = (-33.1383056155,'kcal/mol'),
        S298 = (16.0375324232,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2004,
    label = "S4d-OdSS",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   S    ux (1,S)
4   S    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.83909723018, 10.0772868426, 10.607140546, 10.4365099469, 10.5418111282, 10.6679836683, 10.6137777163], 'cal/(mol*K)'),
        H298 = (-17.986238387,'kcal/mol'),
        S298 = (23.3153317494,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2005,
    label = "S4d-OdHH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   H    ux (1,S)
4   H    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.94,4.77,5.73,6.51,7.67,8.38,9.30],'cal/(mol*K)'),
        H298 = (21.19,'kcal/mol'),
        S298 = (39.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2006,
    label = "S4d-OdCH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   C    ux (1,S)
4   H    ux (1,S)
""",
    thermo = u'S4d-OdCsH',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2006,
    label = "S4d-OdCsH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   Cs    ux (1,S)
4   H    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.6683084997, 10.4678406338, 12.0330738535, 12.8734494126, 12.3396437947, 12.042197759, 13.5753075844], 'cal/(mol*K)'),
        H298 = (-27.76282433,'kcal/mol'),
        S298 = (32.4919379613,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2006,
    label = "S4d-OdCdH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   Cd    ux (1,S)
4   H    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.50730048203, 9.67458422295, 11.879868415, 12.318811417, 11.677530217, 11.426799876, 13.520603311], 'cal/(mol*K)'),
        H298 = (-31.1925496506,'kcal/mol'),
        S298 = (37.6519961221,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2007,
    label = "S4d-OdSH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   S    ux (1,S)
4   H    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.12679482409, 10.2502495145, 11.6003036201, 11.978619315, 13.1784809366, 13.9739952786, 14.8224937444], 'cal/(mol*K)'),
        H298 = (-13.9701407961,'kcal/mol'),
        S298 = (39.8645241414,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2008,
    label = "S4d-OdOH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   O    ux (1,S)
4   H    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.8847773082, 12.1379111003, 12.9637388375, 13.5432717949, 14.0723803098, 14.4609032284, 14.8559186092], 'cal/(mol*K)'),
        H298 = (-25.1564558821,'kcal/mol'),
        S298 = (34.986764952,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2009,
    label = "S4d-OdOO",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   O    ux (1,S)
4   O    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.985771936, 13.0608267723, 13.6425527297, 13.9895578451, 13.7162675253, 13.4281958031, 12.6275996868], 'cal/(mol*K)'),
        H298 = (-50.4865111933,'kcal/mol'),
        S298 = (11.0800456149,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2010,
    label = "S4d-OdOS",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   O    ux (1,S)
4   S    ux (1,S)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.8612599733, 12.1952029407, 13.0121080253, 13.2359004673, 13.153185451, 12.9359431073, 12.0312081384], 'cal/(mol*K)'),
        H298 = (-29.9519117689,'kcal/mol'),
        S298 = (17.5758973404,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2011,
    label = "S4dd-OdOd",
    group =
"""
1 * S4dd  u0 p1 {2,D} {3,D}
2   O2d   ux p2 {1,D}
3   O2d   ux p2 (1,D)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.567, 10.437, 11.163, 11.704, 12.443, 12.922, 13.447], 'cal/(mol*K)'),
        H298 = (-71.22272,'kcal/mol'),
        S298 = (60.733,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2012,
    label = "S4dd-CdOd",
    group =
"""
1 * S4dd  u0 p1 {2,D} {3,D}
2   C     ux {1,D}
3   O2d   ux (1,D)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.41518098405, 9.65940028401, 9.45005998966, 9.76425039625, 11.8032280982, 13.0152974609, 12.1188912684], 'cal/(mol*K)'),
        H298 = (-7.69961883061,'kcal/mol'),
        S298 = (35.6732876601,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2012,
    label = "S4dd-CdCd",
    group =
"""
1 * S4dd  u0 p1 {2,D} {3,D}
2   C     ux {1,D}
3   C     ux (1,D)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.0093619681, 9.23480056802, 8.00111997933, 8.02350079249, 11.1704561964, 13.0025949218, 10.6497825368], 'cal/(mol*K)'),
        H298 = (55.1084823388,'kcal/mol'),
        S298 = (10.1065753202,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2012,
    label = "S4dd-OdSd",
    group =
"""
1 * S4dd  u0 p1 {2,D} {3,D}
2   O     ux {1,D}
3   S     ux (1,D)
""",
    thermo = u'S4dd-OdS4d',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2012,
    label = "S4dd-OdS4d",
    group =
"""
1 * S4dd  u0 p1 {2,D} {3,D}
2   O     ux {1,D}
3   [S4d,S4dd]     ux (1,D)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.66624911488, 7.89619427289, 10.1949071039, 11.1756957715, 10.3345847197, 10.1223517673, 11.4370639139], 'cal/(mol*K)'),
        H298 = (-61.8152962936,'kcal/mol'),
        S298 = (33.8232466134,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2012,
    label = "S4dd-OdS6d",
    group =
"""
1 * S4dd  u0 p1 {2,D} {3,D}
2   O     ux {1,D}
3   [S6d,S6dd,S6ddd,S6td]     ux (1,D)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.377, 6.286, 6.174, 6.114, 6.032, 6.021, 6.077], 'cal/(mol*K)'),
        H298 = (34.876,'kcal/mol'),
        S298 = (12.496,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2012,
    label = "S4dd-SdCd",
    group =
"""
1 * S4dd  u0 p1 {2,D} {3,D}
2   C     ux {1,D}
3   S     ux (1,D)
""",
    thermo = u'S4dd-S46dCd',
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2012,
    label = "S4dd-S46dCd",
    group =
"""
1 * S4dd  u0 p1 {2,D} {3,D}
2   C     ux {1,D}
3   [S4d,S4dd,S6d,S6dd,S6ddd,S6td]     ux (1,D)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.62851570348, 7.20789176918, 6.25771239894, 6.1137114943, 7.28106919999, 7.6397304507, 5.90719038815], 'cal/(mol*K)'),
        H298 = (58.4382823739,'kcal/mol'),
        S298 = (5.03234420883,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2012,
    label = "S4dd-S2dCd",
    group =
"""
1 * S4dd  u0 p1 {2,D} {3,D}
2   C     ux {1,D}
3   S2d     ux (1,D)
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.07,-1.49,-1.34,-1.37,-1.46,-1.60,-2.06],'cal/(mol*K)'),
        H298 = (-1.36,'kcal/mol'),
        S298 = (-49.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2013,
    label = "S6dd-OdOdCC",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    thermo = u'S6dd-OdOdCsCs',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2013,
    label = "S6dd-OdOdCsCs",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.6512813149, 14.5746057623, 14.9566022384, 15.1750282633, 13.411254586, 12.5464271278, 14.5402631413], 'cal/(mol*K)'),
        H298 = (-86.3661588983,'kcal/mol'),
        S298 = (-3.31208822383,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2013,
    label = "S6dd-OdOdCdCd",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cd   ux {1,S}
5   Cd   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.6297099912, 14.8696902898, 15.2595219643, 15.4753179628, 13.5608446121, 12.590037068, 14.6794373577], 'cal/(mol*K)'),
        H298 = (-85.7159765287,'kcal/mol'),
        S298 = (-0.550485709671,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)


entry(
    index = 2014,
    label = "S6dd-OdOdCH",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   C       ux {1,S}
5   H       ux {1,S}
""",
    thermo = u'S6dd-OdOdCsH',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2014,
    label = "S6dd-OdOdCsH",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   Cs       ux {1,S}
5   H       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.5426093203, 13.8001651607, 14.9504905981, 15.8569993486, 16.0669780149, 16.4175155338, 18.7092354124], 'cal/(mol*K)'),
        H298 = (-71.84009005,'kcal/mol'),
        S298 = (30.7274926506,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2014,
    label = "S6dd-OdOdCdH",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   Cs       ux {1,S}
5   H       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.48,5.70,6.90,8.14,10.39,11.99,14.32],'cal/(mol*K)'),
        H298 = (12.20,'kcal/mol'),
        S298 = (7.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2015,
    label = "S6dd-OdOdSH",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   S       ux {1,S}
5   H       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.8746752659, 12.8264739239, 14.592949981, 15.687741807, 17.5622502136, 18.7766927164, 20.045491447], 'cal/(mol*K)'),
        H298 = (-58.1631240351,'kcal/mol'),
        S298 = (44.5024636989,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2016,
    label = "S6dd-OdOdCO",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   C       ux {1,S}
5   O       ux {1,S}
""",
    thermo = u'S6dd-OdOdCsOs',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)

entry(
    index = 2016,
    label = "S6dd-OdOdCsOs",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   Cs       ux {1,S}
5   O       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.5700775322, 14.3963345792, 15.2713166921, 15.9406090043, 15.487256314, 15.2739876387, 16.3373946029], 'cal/(mol*K)'),
        H298 = (-93.636221312,'kcal/mol'),
        S298 = (7.80872344346,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2016,
    label = "S6dd-OdOdCdOs",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   Cd      ux {1,S}
5   O       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.45,6.12,6.72,7.70,9.42,10.25,12.04],'cal/(mol*K)'),
        H298 = (-17.56,'kcal/mol'),
        S298 = (-18.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2017,
    label = "S6dd-OdOdCS",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   C       ux {1,S}
5   S       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.6583164802, 14.3671662651, 15.2708485862, 15.5952960941, 15.1572344154, 14.9007718931, 15.7936212623], 'cal/(mol*K)'),
        H298 = (-74.1125755208,'kcal/mol'),
        S298 = (10.7770240403,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2018,
    label = "S6dd-OdOdSS",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   S       ux {1,S}
5   S       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.6903505318, 15.0084478478, 16.0018999619, 15.7769836139, 15.9050004272, 16.3308854328, 16.734982894], 'cal/(mol*K)'),
        H298 = (-60.1512680701,'kcal/mol'),
        S298 = (24.8134273978,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2019,
    label = "S6dd-OdOdHH",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   H       ux {1,S}
5   H       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.025, 13.124, 15.113, 16.805, 19.275, 20.995, 23.294], 'cal/(mol*K)'),
        H298 = (-55.94098,'kcal/mol'),
        S298 = (61.757,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2020,
    label = "S6dd-OdOdOO",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   O       ux {1,S}
5   O       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.6112524009, 16.2053721384, 17.1486340054, 17.8123712619, 17.9148251365, 18.0469579399, 17.7742015856], 'cal/(mol*K)'),
        H298 = (-97.9167270317,'kcal/mol'),
        S298 = (14.93754742,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2021,
    label = "S6dd-OdOdOH",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   O       ux {1,S}
5   H       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.9509346516, 13.7713201353, 15.3310495535, 16.7065592093, 18.8022821397, 19.6857427228, 20.751109055], 'cal/(mol*K)'),
        H298 = (-79.657566083,'kcal/mol'),
        S298 = (40.7344388565,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2022,
    label = "S6dd-OdOdOS",
    group =
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   O       ux {1,S}
5   S       ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.1560982255, 15.3263925113, 16.3454361126, 16.7550864009, 17.1309624054, 17.4490781219, 17.5993265978], 'cal/(mol*K)'),
        H298 = (-77.3246574136,'kcal/mol'),
        S298 = (21.935437155,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2023,
    label = "S6ddd-OdOdOd",
    group =
"""
1 * S6ddd   u0 p0 {2,D} {3,D} {4,D}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   O2d     ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.4018360477, 13.0365879662, 14.2593943507, 15.1653397705, 16.3907651254, 17.1874178381, 17.9104124141], 'cal/(mol*K)'),
        H298 = (-87.3675884027,'kcal/mol'),
        S298 = (53.8370822889,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2023,
    label = "S6ddd-OdXdXd",
    group =
"""
1 * S6ddd   u0 p0 {2,D} {3,D} {4,D}
2   O2d     ux {1,D}
3   [C,S2d,S4d,S4dd,S6ddd,S6td,S6dd,S6d]     ux {1,D}
4   [C,S2d,S4d,S4dd,S6ddd,S6td,S6dd,S6d]     ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.89,-4.87,-4.95,-5.29,-5.80,-6.24,-6.98],'cal/(mol*K)'),
        H298 = (2.62,'kcal/mol'),
        S298 = (-25.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2023,
    label = "S6ddd-OdOdXd",
    group =
"""
1 * S6ddd   u0 p0 {2,D} {3,D} {4,D}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   [C,S2d,S4d,S4dd,S6ddd,S6td,S6dd,S6d]     ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.89,-4.87,-4.95,-5.29,-5.80,-6.24,-6.98],'cal/(mol*K)'),
        H298 = (2.62,'kcal/mol'),
        S298 = (-25.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2024,
    label = "O2d-Sd",
    group =
"""
1 * O2d   u0 {2,D}
2   S     ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""
Inferred from a least squares fit from 40 species mostly calculated at cbsqb3, 4/2017, Ryan Gillis
""",
)


entry(
    index = 2025,
    label = "O2s-CS6",
    group =
"""
1 * O2s   u0 {2,S} {3,S}
2   [S6s,S6d,S6dd,S6t,S6td]  ux {1,S}
3   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.42971439719, 2.25830517685, 2.31935766946, 2.47798980441, 3.23310298115, 3.57246311694, 4.00510357088], 'cal/(mol*K)'),
        H298 = (-23.8703348644,'kcal/mol'),
        S298 = (10.8045014188,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2032,
    label = "O2s-CS4",
    group =
"""
1 * O2s   u0 {2,S} {3,S}
2   [S4s,S4d,S4b,S4t]   ux {1,S}
3   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.75533705307, 1.71344820173, 1.93782852266, 2.26082163081, 3.23031481295, 3.84408383086, 4.42757875546], 'cal/(mol*K)'),
        H298 = (-22.0930371217,'kcal/mol'),
        S298 = (10.5104329759,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2032,
    label = "O2s-CS2",
    group =
"""
1 * O2s   u0 {2,S} {3,S}
2   S2s   ux {1,S}
3   Cs    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.90173148863, 3.58186813837, 3.92789558129, 4.26135245535, 5.12571786601, 5.51825627946, 5.99331240899], 'cal/(mol*K)'),
        H298 = (-23.4356187885,'kcal/mol'),
        S298 = (8.02529731048,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2026,
    label = "O2s-S_nonDeH",
    group =
"""
1 * O2s   u0 {2,S} {3,S}
2   [S2s,S4s,S6s]   ux {1,S}
3   H     ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.88195009374, 4.91122424074, 5.44551646196, 5.85859107002, 6.65315417123, 7.13015137151, 7.80829372934], 'cal/(mol*K)'),
        H298 = (-36.4350754466,'kcal/mol'),
        S298 = (29.2230165119,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2026,
    label = "O2s-S_DeH",
    group =
"""
1 * O2s   u0 {2,S} {3,S}
2   [S4d,S6d,S6dd]   ux {1,S}
3   H     ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.87489248954, 4.39868912688, 4.7209308737, 4.95329033113, 5.7227986301, 6.28220439877, 7.2304926307], 'cal/(mol*K)'),
        H298 = (-37.7711044736,'kcal/mol'),
        S298 = (29.8901106401,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2027,
    label = "O2s-SH",
    group =
"""
1 * O2s   u0 {2,S} {3,S}
2   S     ux {1,S}
3   H     ux {1,S}
""",
    thermo = u'O2s-S_nonDeH',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2028,
    label = "O2s-CS",
    group =
"""
1 * O2s   u0 {2,S} {3,S}
2   S     ux {1,S}
3   C     ux {1,S}
""",
    thermo = u'O2s-CS4',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2029,
    label = "S4dd",
    group =
"""
1 * S4dd  u0
""",
    thermo = u'S4dd-OdOd',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2030,
    label = "S4d",
    group =
"""
1 * S4d  u0
""",
    thermo = u'S4d-Od',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2030,
    label = "S6ddd",
    group =
"""
1 * S6ddd  u0
""",
    thermo = u'S6ddd-XdXdXd',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2031,
    label = "S6dd",
    group =
"""
1 * S6dd   u0
""",
    thermo = u'S6dd-OdOd',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2032,
    label = "S4s",
    group =
"""
1 * S4s   u0
""",
    thermo = u'S4s-CCCH',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
Couldn't converge these geometries to calculate values and so I copied the S6s values that seem similarly unfavorable
""",
)

entry(
    index = 2033,
    label = "S4s-CCCH",
    group =
"""
1 * S4s   u0 p1 {2,S} {3,S} {4,S} {5,S}
2   C     ux {1,S}
3   C     ux {1,S}
4   C     ux {1,S}
5   H     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.4512308758, 12.5513874524, 13.6839436092, 14.05294988, 14.2772033575, 14.2723440176, 13.3796806405], 'cal/(mol*K)'),
        H298 = (29.0605153234,'kcal/mol'),
        S298 = (-10.3316758854,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2034,
    label = "S6s",
    group =
"""
1 * S6s   u0
""",
    thermo = u'S6s-CCCCCH',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2035,
    label = "S6s-CCCCCH",
    group =
"""
1 * S6s   u0 p0 {2,S} {3,S} {4,S} {5,S} {6,S} {7,S}
2   C     ux {1,S}
3   C     ux {1,S}
4   C     ux {1,S}
5   C     ux {1,S}
6   C     ux {1,S}
7   H     u0 {1,S}
""",
        thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.4609614982, 12.1242151759, 12.497144081, 12.4811811675, 7.65871566455, 5.33239813112, 10.1419872076], 'cal/(mol*K)'),
        H298 = (84.8913334059,'kcal/mol'),
        S298 = (-121.028287929,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""
Calculated at CBS-QB3, June 2017
""",
)

entry(
    index = 2035,
    label = "S6s-SOOCCH",
    group =
"""
1 * S6s   u0 p0 {2,S} {3,S} {4,S} {5,S} {6,S} {7,S}
2   S     ux {1,S}
3   O     ux {1,S}
4   O     ux {1,S}
5   C     ux {1,S}
6   C     ux {1,S}
7   H     u0 {1,S}
""",
        thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.1676076338, 10.856236927, 11.5798531063, 12.1145907641, 10.6769998501, 10.36249632, 13.8580401812], 'cal/(mol*K)'),
        H298 = (45.8597682703,'kcal/mol'),
        S298 = (-71.7643561516,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""
Calculated at CBS-QB3, June 2017
""",
)


entry(
    index = 2036,
    label = "S4s-OCCH",
    group =
"""
1 * S4s   u0 p1 {2,S} {3,S} {4,S} {5,S}
2   O     ux {1,S}
3   C     ux {1,S}
4   C     ux {1,S}
5   H     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.58,11.43,12.51,13.49,14.96,15.33,16.12],'cal/(mol*K)'),
        H298 = (45.75,'kcal/mol'),
        S298 = (-21.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2036,
    label = "S4s-OOCC",
    group =
"""
1 * S4s   u0 p1 {2,S} {3,S} {4,S} {5,S}
2   O     ux {1,S}
3   O     ux {1,S}
4   C     ux {1,S}
5   C     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.68,10.98,11.54,12.28,13.55,13.51,13.81],'cal/(mol*K)'),
        H298 = (7.83,'kcal/mol'),
        S298 = (-46.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2036,
    label = "S4s-SOCH",
    group =
"""
1 * S4s   u0 p1 {2,S} {3,S} {4,S} {5,S}
2   S     ux {1,S}
3   O     ux {1,S}
4   C     ux {1,S}
5   H     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.4555420376, 13.4235439837, 13.1112245982, 13.1763450134, 11.7477962692, 10.8584575957, 11.1271559748], 'cal/(mol*K)'),
        H298 = (12.9404529866,'kcal/mol'),
        S298 = (-10.6173364215,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2036,
    label = "S4s-SOOH",
    group =
"""
1 * S4s   u0 p1 {2,S} {3,S} {4,S} {5,S}
2   S     ux {1,S}
3   O     ux {1,S}
4   O     ux {1,S}
5   H     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.68,10.98,11.54,12.28,13.55,13.51,13.81],'cal/(mol*K)'),
        H298 = (7.83,'kcal/mol'),
        S298 = (-46.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2037,
    label = "S6s-OCCCCH",
    group =
"""
1 * S6s   u0 p0 {2,S} {3,S} {4,S} {5,S} {6,S} {7,S}
2   O     ux {1,S}
3   C     ux {1,S}
4   C     ux {1,S}
5   C     ux {1,S}
6   C     ux {1,S}
7   H     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.1162191048, 12.4013479, 12.5693988029, 12.550953864, 8.66641836041, 6.96956713338, 11.0920960367], 'cal/(mol*K)'),
        H298 = (61.8452871713,'kcal/mol'),
        S298 = (-98.2350468551,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2038,
    label = "S6d-OdOCCH",
    group =
"""
1 * S6d   u0 p0 {2,S} {3,S} {4,S} {5,D} {6,S}
2   O     ux {1,S}
3   C     ux {1,S}
4   C     ux {1,S}
5   O     ux {1,D}
6   H     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.7146921097, 13.0795969435, 14.4165267587, 15.4939821359, 14.8144876357, 14.6931548537, 17.3417022523], 'cal/(mol*K)'),
        H298 = (-1.74182916403,'kcal/mol'),
        S298 = (-29.2906258117,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2039,
    label = "S6d-OdCCCH",
    group =
"""
1 * S6d   u0 p0 {2,S} {3,S} {4,S} {5,D} {6,S}
2   C     ux {1,S}
3   C     ux {1,S}
4   C     ux {1,S}
5   O     ux {1,D}
6   H     u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.79,8.88,10.35,11.48,13.31,14.04,14.47],'cal/(mol*K)'),
        H298 = (79.31,'kcal/mol'),
        S298 = (-37.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2018""",
    longDesc =
u""""

""",
)

entry(
    index = 2040,
    label = "S6d",
    group =
"""
1 * S6d   u0
""",
    thermo = u'S6d-OdCCCH',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2041,
    label = "S4d-Od",
    group =
"""
1 * S4d u0 p1 {2,D}
2   O2d ux    {1,D}
""",
    thermo = u'S4d-OdCC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2042,
    label = "S4d-Cd",
    group =
"""
1 * S4d u0 p1 {2,D}
2   C   ux    {1,D}
""",
    thermo = u'S4d-CdCC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2042,
    label = "S4d-Sd",
    group =
"""
1 * S4d u0 p1 {2,D}
2   S   ux    {1,D}
""",
    thermo = u'S4d-SdOC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2053,
    label = "S4d-SdOC",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   S    ux {1,D}
3   O    ux {1,S}
4   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.49716961112, 10.2941725845, 11.1769286028, 11.7525154257, 10.1386706571, 9.15551038305, 9.76337727015], 'cal/(mol*K)'),
        H298 = (-41.2520701425,'kcal/mol'),
        S298 = (1.74687762153,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2053,
    label = "S4d-SdOH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   S    ux {1,D}
3   O    ux {1,S}
4   H    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.026263813, 12.5032258065, 13.2801853309, 13.8319254055, 14.0281042322, 14.1124162252, 13.9870879607], 'cal/(mol*K)'),
        H298 = (-22.3168442006,'kcal/mol'),
        S298 = (23.0932401352,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2053,
    label = "S4d-SdCH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   S    ux {1,D}
3   H    ux {1,S}
4   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.6805310142, 8.29005784425, 7.2684747663, 6.35191885347, 6.38970325568, 6.4329626236, 7.62014725028], 'cal/(mol*K)'),
        H298 = (55.6717760079,'kcal/mol'),
        S298 = (15.9290105592,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2053,
    label = "S4d-SdSC",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   S    ux {1,D}
3   S    ux {1,S}
4   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.9392298926, 10.314296611, 9.90254243143, 9.8304909246, 7.62562294301, 6.48577006168, 7.88133730908], 'cal/(mol*K)'),
        H298 = (-38.7183996452,'kcal/mol'),
        S298 = (3.44624876755,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2043,
    label = "S4t",
    group =
"""
1 * S4t   u0
""",
    thermo = u'S4t-CtC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2044,
    label = "S6dd-OdOd",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
""",
    thermo = u'S6dd-OdOdCC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2045,
    label = "S6dd-OdCd",
    group =
"""
1 * S6dd   u0 p0 {2,D} {3,D}
2   O2d    u0 {1,D}
3   C      ux {1,D}
""",
    thermo = u'S6dd-OdCdCC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2045,
    label = "S6dd-OdSd",
    group =
"""
1 * S6dd   u0 p0 {2,D} {3,D}
2   O2d    u0 {1,D}
3   S      ux {1,D}
""",
    thermo = u'S6dd-OdSdOC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2063,
    label = "S6dd-OdSdOC",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   S    ux {1,D}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.1663210367, 15.241663473, 16.1482347791, 16.6666477699, 15.8029329024, 15.34407405, 15.7193441364], 'cal/(mol*K)'),
        H298 = (-75.1368456855,'kcal/mol'),
        S298 = (-6.0852795204,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2063,
    label = "S6dd-OdSdOH",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   S    ux {1,D}
4   H    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.2014150136, 14.0131338354, 15.3165598306, 16.4149033356, 17.6286412796, 18.5816251892, 19.5882414643], 'cal/(mol*K)'),
        H298 = (-60.2616946935,'kcal/mol'),
        S298 = (27.9265716705,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2063,
    label = "S6dd-OdSdCH",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   S    ux {1,D}
4   C    ux {1,S}
5   H    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.9281283474, 12.9482310014, 14.1176231669, 15.073976004, 15.4579082583, 15.9035974643, 17.8435098556], 'cal/(mol*K)'),
        H298 = (-54.7409657215,'kcal/mol'),
        S298 = (17.7788247031,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2046,
    label = "S6dd-CdCd",
    group =
"""
1 * S6dd   u0 p0 {2,D} {3,D}
2   C      ux {1,D}
3   C      ux {1,D}
""",
    thermo = u'S6dd-CdCdCC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2047,
    label = "S6t",
    group =
"""
1 * S6t   u0
""",
    thermo = u'S6t-CtCCC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2048,
    label = "S6td",
    group =
"""
1 * S6td   u0
""",
    thermo = u'S6td-CtCdC',
    shortDesc = u"""Sulfur/Oxygen Extension, Ryan Gillis""",
    longDesc =
u""""
""",
)

entry(
    index = 2050,
    label = "S4d-CdCC",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   C    ux {1,D}
3   C    ux {1,S}
4   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.6498409405, 10.6449770594, 10.3842773498, 10.7334360036, 12.5551011776, 13.6154405236, 12.7455666025], 'cal/(mol*K)'),
        H298 = (44.3549170373,'kcal/mol'),
        S298 = (1.52593180361,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2051,
    label = "S4d-CdCH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   C    ux {1,D}
3   C    ux {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.381407037, 10.6536740292, 10.6805251154, 11.1027163826, 11.43593226, 11.7365944046, 12.1523487552], 'cal/(mol*K)'),
        H298 = (42.7395339559,'kcal/mol'),
        S298 = (10.9791936329,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2052,
    label = "S4d-CdHH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   C    ux {1,D}
3   H    u0 {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.10218098405, 8.38940028401, 8.61005998966, 9.43025039625, 12.3042280982, 14.2222974609, 14.5658912684], 'cal/(mol*K)'),
        H298 = (59.1524811694,'kcal/mol'),
        S298 = (31.9072876601,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2053,
    label = "S4d-CdOC",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   C    ux {1,D}
3   O    ux {1,S}
4   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.547794804, 11.2110188993, 10.6688213603, 10.547275593, 9.65118217422, 9.1493106984, 8.58919007235], 'cal/(mol*K)'),
        H298 = (25.5285289994,'kcal/mol'),
        S298 = (-10.2086742526,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2054,
    label = "S4d-CdOH",
    group =
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   C    ux {1,D}
3   O    ux {1,S}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.5778698349, 10.9115877957, 10.8980959471, 11.3880559518, 13.2878632881, 14.4811630896, 13.7562541564], 'cal/(mol*K)'),
        H298 = (37.7962850068,'kcal/mol'),
        S298 = (13.2939211667,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2055,
    label = "S4t-CtC",
    group =
"""
1 * S4t  u0 p1 {2,T} {3,S}
2   C    ux {1,T}
3   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.12519500259, 6.88984288948, 7.39353538752, 7.63106310794, 7.02196951821, 6.66543955281, 7.40502253635], 'cal/(mol*K)'),
        H298 = (-18.0938494054,'kcal/mol'),
        S298 = (25.2624118419,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2056,
    label = "S4t-CtH",
    group =
"""
1 * S4t  u0 p1 {2,T} {3,S}
2   C    ux {1,T}
3   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.79496894967, 7.54256914433, 8.15407026174, 8.70059712156, 10.4812653564, 11.6411426091, 12.1475650496], 'cal/(mol*K)'),
        H298 = (-3.83390219194,'kcal/mol'),
        S298 = (46.6765058692,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2057,
    label = "S4t-CtO",
    group =
"""
1 * S4t  u0 p1 {2,T} {3,S}
2   C    ux {1,T}
3   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.94637848647, 8.99938129317, 8.90217108986, 8.74672642579, 9.22377192417, 9.52536318451, 8.76026773922], 'cal/(mol*K)'),
        H298 = (-19.4556644534,'kcal/mol'),
        S298 = (25.7281313351,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2058,
    label = "S6dd-CdCdCC",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   C    ux {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.53698810856, 4.35173559111, 3.53170762574, 3.23687541095, 1.03530573075, -0.127455942462, 1.72624884291], 'cal/(mol*K)'),
        H298 = (47.0934030735,'kcal/mol'),
        S298 = (-94.8543601352,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2059,
    label = "S6dd-CdCdCH",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   C    ux {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.74919580892, 3.07609255593, 3.23647880953, 3.73923917744, 3.74916259784, 3.93086443131, 5.9806514014], 'cal/(mol*K)'),
        H298 = (57.1923803924,'kcal/mol'),
        S298 = (-62.0861025494,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2060,
    label = "S6dd-CdCdOC",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   C    ux {1,D}
3   C    ux {1,D}
4   O    ux {1,S}
5   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.14330331939, 5.07440342906, 5.29654793583, 5.5469488463, 4.58536396774, 3.88566003254, 4.16115877069], 'cal/(mol*K)'),
        H298 = (34.321385866,'kcal/mol'),
        S298 = (-86.8162131895,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2061,
    label = "S6dd-OdCdCC",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3131282029, 9.12081217972, 9.17593793337, 9.22541817636, 7.99502338241, 7.3440920956, 8.79929732236], 'cal/(mol*K)'),
        H298 = (-7.53939667329,'kcal/mol'),
        S298 = (-26.2667562423,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2062,
    label = "S6dd-OdCdCH",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.41456485931, 8.39024483957, 9.00628277798, 9.75303550852, 10.1133495751, 10.5343313246, 12.7859555707], 'cal/(mol*K)'),
        H298 = (-6.32413237769,'kcal/mol'),
        S298 = (-15.3236652308,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2063,
    label = "S6dd-OdCdOC",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.765922676, 10.2128358924, 10.480494496, 10.9059747568, 10.057494741, 9.4586989189, 10.0391483981], 'cal/(mol*K)'),
        H298 = (-24.239052471,'kcal/mol'),
        S298 = (-39.405421278,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2063,
    label = "S6dd-OdCdOH",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   H    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.67297887806, 10.1054856309, 11.3840876247, 12.4661118732, 13.5182402425, 14.1134150097, 14.442613127], 'cal/(mol*K)'),
        H298 = (-8.17036520247,'kcal/mol'),
        S298 = (-8.13880339626,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2063,
    label = "S6dd-OdCdOS",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   S    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.72729318139, 9.78543919158, 10.1267496414, 10.3672495484, 10.4499176324, 10.4718255312, 10.731938673], 'cal/(mol*K)'),
        H298 = (-11.5044355178,'kcal/mol'),
        S298 = (-22.6958678894,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2063,
    label = "S6dd-OdCdSH",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   H    ux {1,S}
5   S    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.1443934604, 8.56729516095, 9.55431334688, 10.2609975413, 11.5653072354, 12.434390215, 13.5215957556], 'cal/(mol*K)'),
        H298 = (4.86606454492,'kcal/mol'),
        S298 = (0.955404094809,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2063,
    label = "S6dd-OdCdOO",
    group =
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 {1,D}
3   C    ux {1,D}
4   O    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.606302597, 12.3337864908, 12.7576486635, 13.1246363948, 12.6291116096, 12.4203306047, 11.7393284424], 'cal/(mol*K)'),
        H298 = (-30.4756472551,'kcal/mol'),
        S298 = (-30.858243675,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2064,
    label = "S6t-CtCCC",
    group =
"""
1 * S6t  u0 p0 {2,T} {3,S} {4,S} {5,S}
2   C    ux {1,T}
3   C    ux {1,S}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.6183458486, 13.3934982499, 12.3657567104, 11.5875058221, 8.62669475511, 7.12418148776, 8.94735737413], 'cal/(mol*K)'),
        H298 = (37.1399058516,'kcal/mol'),
        S298 = (15.3597331118,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2065,
    label = "S6t-CtHHH",
    group =
"""
1 * S6t  u0 p0 {2,T} {3,S} {4,S} {5,S}
2   C    ux {1,T}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.88196894967, 8.13456914433, 9.49807026174, 10.9345971216, 14.2662653564, 16.4511426091, 18.4535650496], 'cal/(mol*K)'),
        H298 = (71.0548378081,'kcal/mol'),
        S298 = (47.3535058692,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2066,
    label = "S6t-CtOCC",
    group =
"""
1 * S6t  u0 p0 {2,T} {3,S} {4,S} {5,S}
2   C    ux {1,T}
3   C    ux {1,S}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.8936034552, 11.8386309739, 11.7650114322, 11.6562785186, 10.322397451, 9.68635049002, 10.7084662033], 'cal/(mol*K)'),
        H298 = (11.801859617,'kcal/mol'),
        S298 = (-37.9890258143,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2067,
    label = "S6t-CtOCH",
    group =
"""
1 * S6t  u0 p0 {2,T} {3,S} {4,S} {5,S}
2   C    ux {1,T}
3   C    ux {1,S}
4   O    ux {1,S}
5   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.8868111556, 11.0749879388, 11.773782616, 12.4006422851, 13.1932543181, 13.8536708638, 15.0108687618], 'cal/(mol*K)'),
        H298 = (21.4768369359,'kcal/mol'),
        S298 = (-4.87076822851,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2068,
    label = "S6td-CtCdC",
    group =
"""
1 * S6td u0 p0 {2,T} {3,D} {4,S}
2   C    ux {1,T}
3   C    ux {1,D}
4   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.537597297, 10.4718001457, 10.5826934287, 10.7825731256, 11.0631736147, 11.3532400734, 12.0535749052], 'cal/(mol*K)'),
        H298 = (-5.98574791342,'kcal/mol'),
        S298 = (10.6973305723,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)


entry(
    index = 2069,
    label = "S6td-CtOdC",
    group =
"""
1 * S6td u0 p0 {2,T} {3,D} {4,S}
2   C    ux {1,T}
3   O    u0 {1,D}
4   C    ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3407612493, 10.6182121795, 11.043299078, 11.3912333551, 11.8964084893, 12.2738222353, 13.1171624911], 'cal/(mol*K)'),
        H298 = (-32.9112395108,'kcal/mol'),
        S298 = (20.2972482834,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)

entry(
    index = 2070,
    label = "S6td-CtOdH",
    group =
"""
1 * S6td u0 p0 {2,T} {3,D} {4,S}
2   C    ux {1,T}
3   O    u0 {1,D}
4   H    u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.86796894967, 11.2415691443, 12.2750702617, 13.1305971216, 15.3902653564, 16.8291426091, 17.5985650496], 'cal/(mol*K)'),
        H298 = (-23.6932621919,'kcal/mol'),
        S298 = (52.2545058692,'cal/(mol*K)'),
    ),
    shortDesc = u"""RMG-type entries for Sulfur Groups, based on quantum calculations perfomred by Vandeputte (2011), Gillis, Class (2013), and Bozzelli, refit by Ryan Gillis in 2019""",
    longDesc =
u""""

""",
)


entry(
    index = 1919,
    label = "CJ2_singlet",
    group =
"""
1 * C u0 p1
""",
    thermo = u'CsJ2_singlet-CsH',
    shortDesc = u"""Branch for singlet carbenes""",
    longDesc =
u"""

""",
)

entry(
    index = 1920,
    label = "CsJ2_singlet-HH",
    group =
"""
1 * C2s u0 p1 {2,S} {3,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.069, 8.313, 8.631, 8.994, 9.768, 10.497, 11.825],'cal/(mol*K)'),
        H298 = (102.462,'kcal/mol'),
        S298 = (45.144,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to DFT_QCI_thermo library""",
    longDesc =
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)


entry(
    index = 1921,
    label = "CsJ2_singlet-OsH",
    group =
"""
1 * C2s u0 p1 {2,S} {3,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.075, 5.312, 6.211, 6.926, 8.355, 9.557, 10.212],'cal/(mol*K)'),
        H298 = (65.592,'kcal/mol'),
        S298 = (23.749,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to DFT_QCI_thermo library""",
    longDesc =
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 2502,
    label = "CdJ2_singlet-Od",
    group =
"""
1 * C2d u0 p1 {2,D}
2   O2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-2.38,-3.32,-4.24,-5.75,-6.88,-8.59],'cal/(mol*K)'),
        H298 = (103.73,'kcal/mol'),
        S298 = (-6.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to formaldehyde from NIST values""",
    longDesc =
u"""

""",
)

entry(
    index = 2503,
    label = "CdJ2_singlet-Sd",
    group =
"""
1 * C2d u0 p1 {2,D}
2   S2d u0 p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97,-2.97,-3.85,-4.6,-5.82,-6.79,-8.44],'cal/(mol*K)'),
        H298 = (143.53,'kcal/mol'),
        S298 = (-6.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc =
u"""

""",
)

entry(
    index = 1922,
    label = "CdJ2_singlet-(Cdd-Od)",
    group =
"""
1   Cdd u0 {2,D} {3,D}
2 * C2d u0 p1 {1,D}
3   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.135, 11.201, 11.749, 12.051, 12.813, 13.581, 14.122],'cal/(mol*K)'),
        H298 = (110.367,'kcal/mol'),
        S298 = (53.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to DFT_QCI_thermo library""",
    longDesc =
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 1923,
    label = "CsJ2_singlet-CH",
    group =
"""
1   C   u0 {2,S}
2 * C2s u0 p1 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = u'CsJ2_singlet-CsH',
    shortDesc = u"""Branch for singlet carbenes single-bonded to one carbon and one hydrogen""",
    longDesc =
u"""

""",
)

entry(
    index = 1924,
    label = "CsJ2_singlet-CsH",
    group =
"""
1   Cs  u0 {2,S}
2 * C2s u0 p1 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.255, 5.932, 6.136, 6.192, 6.77, 7.73, 8.134],'cal/(mol*K)'),
        H298 = (97.669,'kcal/mol'),
        S298 = (29.684,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to DFT_QCI_thermo library""",
    longDesc =
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 1925,
    label = "CsJ2_singlet-CtH",
    group =
"""
1   Ct  u0 {2,S}
2 * C2s u0 p1 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.675, 6.472, 6.776, 6.9, 7.469, 8.156, 7.58],'cal/(mol*K)'),
        H298 = (88.247,'kcal/mol'),
        S298 = (28.407,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to DFT_QCI_thermo library""",
    longDesc =
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 1926,
    label = "CdJ2_singlet-Cd",
    group =
"""
1   C   u0 {2,D}
2 * C2d u0 p1 {1,D}
""",
    thermo = u'CdJ2_singlet-Cds',
    shortDesc = u"""Branch for singlet carbenes double-bonded to one carbon""",
    longDesc =
u"""

""",
)

entry(
    index = 1927,
    label = "CdJ2_singlet-Cds",
    group =
"""
1   Cd  u0 {2,D}
2 * C2d u0 p1 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.372, 5.272, 4.916, 4.506, 4.219, 4.263, 3.97],'cal/(mol*K)'),
        H298 = (92.157,'kcal/mol'),
        S298 = (26.864,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to DFT_QCI_thermo library""",
    longDesc =
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 1928,
    label = "CdJ2_singlet-(Cdd-Cds)",
    group =
"""
1   Cdd u0 {2,D} {3,D)
2 * C2d u0 p1 {1,D}
3   C   u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.406, 3.333, 3.175, 3.019, 3.156, 3.468, 3.593],'cal/(mol*K)'),
        H298 = (91.676,'kcal/mol'),
        S298 = (26.434,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to DFT_QCI_thermo library""",
    longDesc =
u"""
Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
J. Phys. Chem. A 2012, 116, 9033-9057.
""",
)

entry(
    index = 1929,
    label = "CsJ2_singlet-(Cds-Cds-Cds-C)C",
    group =
"""
1   C   u0 {2,D}
2   Cd  u0 {1,D} {6,S}
3   C   u0 {4,S}
4 * C2s u0 p1 {3,S} {5,S}
5   Cd  u0 {6,D} {4,S}
6   Cd  u0 {2,S} {5,D}
""",
    thermo = u'CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_6_ring',
    shortDesc = u"""Branch for singlet carbenes delocalized over two conjugated carbon double bonds""",
    longDesc =
u"""

""",
)

entry(
    index = 1930,
    label = "CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_5_ring",
    group =
"""
1   Cd  u0 {2,D}
2   Cd  u0 {1,D} {6,S} {3,S}
3   Cs  u0 {4,S} {2,S}
4 * C2s u0 p1 {3,S} {5,S}
5   Cd  u0 {6,D} {4,S}
6   Cd  u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.025, 5.12, 5.268, 4.917, 4.799, 5.731, 5.087],'cal/(mol*K)'),
        H298 = (82.041,'kcal/mol'),
        S298 = (10.325,'cal/(mol*K)'),
    ),
    shortDesc=u"""Fitted to DFT_QCI_thermo library""",
    longDesc=
    u"""
    Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
    """,
)

entry(
    index = 1931,
    label = "CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_6_ring",
    group =
"""
1   Cd  u0 {2,D} {3,S}
2   Cd  u0 {1,D} {6,S}
3   Cs  u0 {4,S} {1,S}
4 * C2s u0 p1 {3,S} {5,S}
5   Cd  u0 {6,D} {4,S}
6   Cd  u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.322, 5.406, 5.554, 5.182, 5.008, 5.927, 5.232],'cal/(mol*K)'),
        H298 = (80.263,'kcal/mol'),
        S298 = (12.963,'cal/(mol*K)'),
    ),
    shortDesc=u"""Fitted to DFT_QCI_thermo library""",
    longDesc=
    u"""
    Fitted to RQCISD(T)/cc-PV(infinity)(Q)Z calculations of:

    Goldsmith, C. F.; Magoon, G. R.; Green, W. H., Database of Small Molecule Thermochemistry for Combustion.
    J. Phys. Chem. A 2012, 116, 9033-9057.
    """,
)

entry(
    index = 1932,
    label = "Cds-(Cds-Os)CbH",
    group =
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D} {5,S}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   O2s u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28, 6.83, 7.245, 7.264, 8.226, 9.901, 10.176],'cal/(mol*K)'),
        H298 = (10.329,'kcal/mol'),
        S298 = (2.958,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
Fitted to CBS-QB3 calculations for OC=Cc1ccccc1
""",
)

tree(
"""
L1: R
    L2: C
        L3: CJ2_singlet
            L4: CsJ2_singlet-HH
            L4: CsJ2_singlet-OsH
            L4: CdJ2_singlet-Od
            L4: CdJ2_singlet-Sd
            L4: CdJ2_singlet-(Cdd-Od)
            L4: CsJ2_singlet-CH
                L5: CsJ2_singlet-CsH
                L5: CsJ2_singlet-CtH
            L4: CdJ2_singlet-Cd
                L5: CdJ2_singlet-Cds
                L5: CdJ2_singlet-(Cdd-Cds)
            L4: CsJ2_singlet-(Cds-Cds-Cds-C)C
                L5: CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_5_ring
                L5: CsJ2_singlet-(Cds-Cds-Cds-Cds)Cs_6_ring
        L3: Cbf
            L4: Cbf-CbCbCbf
            L4: Cbf-CbCbfCbf
            L4: Cbf-CbfCbfCbf
        L3: Cb
            L4: Cb-H
            L4: Cb-O2s
            L4: Cb-S
            L4: Cb-N3s
            L4: Cb-C
                L5: Cb-Cs
                L5: Cb-Cds
                    L6: Cb-(Cds-O2d)
                    L6: Cb-(Cds-Cd)
                        L7: Cb-(Cds-Cds)
                        L7: Cb-(Cds-Cdd)
                            L8: Cb-(Cds-Cdd-O2d)
                            L8: Cb-(Cds-Cdd-S2d)
                            L8: Cb-(Cds-Cdd-Cd)
                L5: Cb-Ct
                    L6: Cb-(CtN3t)
                L5: Cb-Cb
        L3: Ct
            L4: Ct-CtN3s
            L4: Ct-N3tN3s
            L4: Ct-CtH
            L4: Ct-StH
            L4: Ct-CtOs
            L4: Ct-N3tOs
            L4: Ct-CtS
                L5: Ct-CtS2
                L5: Ct-CtS4
                L5: Ct-CtS6
            L4: Ct-N3tC
                L5: Ct-N3tCs
                L5: Ct-N3tCd
            L4: Ct-CtC
                L5: Ct-CtCs
                L5: Ct-CtCds
                    L6: Ct-Ct(Cds-O2d)
                    L6: Ct-Ct(Cds-Cd)
                        L7: Ct-Ct(Cds-Cds)
                        L7: Ct-Ct(Cds-Cdd)
                            L8: Ct-Ct(Cds-Cdd-O2d)
                            L8: Ct-Ct(Cds-Cdd-S2d)
                            L8: Ct-Ct(Cds-Cdd-Cd)
                L5: Ct-CtCt
                    L6: Ct-Ct(CtN3t)
                L5: Ct-CtCb
        L3: Cdd
            L4: Cdd-N3dCd
            L4: Cdd-OdOd
            L4: Cdd-OdSd
            L4: Cdd-SdSd
                L5: Cdd-S2dS2d
                L5: Cdd-S4S4
                L5: Cdd-S2S4
            L4: Cdd-CdOd
                L5: Cdd-CdsOd
                L5: Cdd-CddOd
                    L6: Cdd-(Cdd-O2d)O2d
                    L6: Cdd-(Cdd-Cd)O2d
            L4: Cdd-CdSd
                L5: Cdd-CdsSd
                    L6: Cdd-CdsS2d
                    L6: Cdd-CdsS4d
                    L6: Cdd-CdsS6d
                L5: Cdd-CddSd
                    L6: Cdd-(Cdd-S2d)S2d
                    L6: Cdd-(Cdd-Cd)S2d
            L4: Cdd-CdCd
                L5: Cdd-CddCdd
                    L6: Cdd-(Cdd-O2d)(Cdd-O2d)
                    L6: Cdd-(Cdd-S2d)(Cdd-S2d)
                    L6: Cdd-(Cdd-O2d)(Cdd-Cd)
                    L6: Cdd-(Cdd-S2d)(Cdd-Cd)
                    L6: Cdd-(Cdd-Cd)(Cdd-Cd)
                L5: Cdd-CddCds
                    L6: Cdd-(Cdd-O2d)Cds
                    L6: Cdd-(Cdd-S2d)Cds
                    L6: Cdd-(Cdd-Cd)Cds
                L5: Cdd-CdsCds
        L3: Cds
            L4: Cds-OdN3sH
            L4: Cds-OdN3sCs
            L4: Cd-N3dCsCs
            L4: Cd-N3dCsH
            L4: Cd-N3dHH
            L4: Cds-OdHH
            L4: Cds-OdOsH
            L4: CO-SH
                L5: CO-S2H
                L5: CO-S4H
                L5: CO-S6H
            L4: Cds-OdOsOs
            L4: CO-CsSs
            L4: CO-OsSs
            L4: Cds-OdCH
                L5: Cds-OdCsH
                L5: Cds-OdCdsH
                    L6: Cds-O2d(Cds-O2d)H
                    L6: Cds-O2d(Cds-Cd)H
                        L7: Cds-O2d(Cds-Cds)H
                        L7: Cds-O2d(Cds-Cdd)H
                            L8: Cds-O2d(Cds-Cdd-O2d)H
                            L8: Cds-O2d(Cds-Cdd-Cd)H
                L5: Cds-OdCtH
                L5: Cds-OdCbH
            L4: Cds-OdCOs
                L5: Cds-OdCsOs
                L5: Cds-OdCdsOs
                    L6: Cds-O2d(Cds-O2d)O2s
                    L6: Cds-O2d(Cds-Cd)O2s
                        L7: Cds-O2d(Cds-Cds)O2s
                        L7: Cds-O2d(Cds-Cdd)O2s
                            L8: Cds-O2d(Cds-Cdd-O2d)O2s
                            L8: Cds-O2d(Cds-Cdd-Cd)O2s
                L5: Cds-OdCtOs
                L5: Cds-OdCbOs
            L4: Cds-OdCC
                L5: Cds-OdCsCs
                L5: Cds-OdCdsCs
                    L6: Cds-O2d(Cds-O2d)Cs
                    L6: Cds-O2d(Cds-Cd)Cs
                        L7: Cds-O2d(Cds-Cds)Cs
                        L7: Cds-O2d(Cds-Cdd)Cs
                            L8: Cds-O2d(Cds-Cdd-O2d)Cs
                            L8: Cds-O2d(Cds-Cdd-Cd)Cs
                L5: Cds-OdCdsCds
                    L6: Cds-O2d(Cds-O2d)(Cds-O2d)
                    L6: Cds-O2d(Cds-Cd)(Cds-O2d)
                        L7: Cds-O2d(Cds-Cds)(Cds-O2d)
                        L7: Cds-O2d(Cds-Cdd)(Cds-O2d)
                            L8: Cds-O2d(Cds-Cdd-O2d)(Cds-O2d)
                            L8: Cds-O2d(Cds-Cdd-Cd)(Cds-O2d)
                    L6: Cds-O2d(Cds-Cd)(Cds-Cd)
                        L7: Cds-O2d(Cds-Cds)(Cds-Cds)
                        L7: Cds-O2d(Cds-Cdd)(Cds-Cds)
                            L8: Cds-O2d(Cds-Cdd-O2d)(Cds-Cds)
                            L8: Cds-O2d(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-O2d(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-O2d(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-O2d)
                            L8: Cds-O2d(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cds-OdCtCs
                L5: Cds-OdCtCds
                    L6: Cds-OdCt(Cds-O2d)
                    L6: Cds-OdCt(Cds-Cd)
                        L7: Cds-OdCt(Cds-Cds)
                        L7: Cds-OdCt(Cds-Cdd)
                            L8: Cds-OdCt(Cds-Cdd-O2d)
                            L8: Cds-OdCt(Cds-Cdd-Cd)
                L5: Cds-OdCtCt
                L5: Cds-OdCbCs
                L5: Cds-OdCbCds
                    L6: Cds-OdCb(Cds-O2d)
                    L6: Cds-OdCb(Cds-Cd)
                        L7: Cds-OdCb(Cds-Cds)
                        L7: Cds-OdCb(Cds-Cdd)
                            L8: Cds-OdCb(Cds-Cdd-O2d)
                            L8: Cds-OdCb(Cds-Cdd-Cd)
                L5: Cds-OdCbCt
                L5: Cds-OdCbCb
            L4: Cds-CdHH
                L5: Cds-CdsHH
                L5: Cds-CddHH
                    L6: Cds-(Cdd-O2d)HH
                    L6: Cds-(Cdd-S2d)HH
                    L6: Cds-(Cdd-Cd)HH
            L4: Cds-CdOsH
                L5: Cds-CdsOsH
                L5: Cds-CddOsH
                    L6: Cds-(Cdd-O2d)OsH
                    L6: Cds-(Cdd-Cd)OsH
            L4: Cds-CdSH
                L5: Cds-CdsSH
                    L6: Cds-CdsS2H
                    L6: Cds-CdsS4H
                    L6: Cds-CdsS6H
                L5: Cds-CddSsH
                    L6: Cds-(Cdd-S2d)SsH
                    L6: Cds-(Cdd-Cd)SsH
            L4: Cds-CdOsOs
                L5: Cds-CdsOsOs
                L5: Cds-CddOsOs
                    L6: Cds-(Cdd-O2d)OsOs
                    L6: Cds-(Cdd-Cd)OsOs
            L4: Cds-CdSsSs
                L5: Cds-CdsSsSs
                L5: Cds-CddSsSs
                    L6: Cds-(Cdd-S2d)SsSs
                    L6: Cds-(Cdd-Cd)SsSs
            L4: Cds-CdCH
                L5: Cds-CdsCsH
                L5: Cds-CdsCdsH
                    L6: Cd-Cd(CO)H
                    L6: Cds-Cds(Cds-Cd)H
                        L7: Cds-Cds(Cds-Cds)H
                        L7: Cds-Cds(Cds-Cdd)H
                            L8: Cd-Cd(CCO)H
                            L8: Cds-Cds(Cds-Cdd-S2d)H
                            L8: Cds-Cds(Cds-Cdd-Cd)H
                L5: Cds-CdsCtH
                    L6: Cds-CdsH(CtN3t)
                L5: Cds-CdsCbH
                    L6: Cds-(Cds-Os)CbH
                L5: Cds-CddCsH
                    L6: Cds-(Cdd-O2d)CsH
                    L6: Cds-(Cdd-S2d)CsH
                    L6: Cds-(Cdd-Cd)CsH
                L5: Cds-CddCdsH
                    L6: Cds-(Cdd-O2d)(Cds-O2d)H
                    L6: Cds-(Cdd-O2d)(Cds-Cd)H
                        L7: Cds-(Cdd-O2d)(Cds-Cds)H
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)H
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)H
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)H
                    L6: Cds-(Cdd-S2d)(Cds-Cd)H
                        L7: Cds-(Cdd-S2d)(Cds-Cds)H
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)H
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)H
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)H
                    L6: Cds-(Cdd-Cd)(Cds-O2d)H
                    L6: Cds-(Cdd-Cd)(Cds-Cd)H
                        L7: Cds-(Cdd-Cd)(Cds-Cds)H
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)H
                L5: Cds-CddCtH
                    L6: Cds-(Cdd-O2d)CtH
                    L6: Cds-(Cdd-S2d)CtH
                    L6: Cds-(Cdd-Cd)CtH
                L5: Cds-CddCbH
                    L6: Cds-(Cdd-O2d)CbH
                    L6: Cds-(Cdd-S2d)CbH
                    L6: Cds-(Cdd-Cd)CbH
                L5: Cds-(Cdd-Cd)C=SH
                L5: Cds-(Cdd-S2d)C=SH
                L5: Cds-CdsC=SH
            L4: Cds-CdCO
                L5: Cds-CdsCdsOs
                    L6: Cds-Cds(Cds-O2d)O2s
                    L6: Cds-Cds(Cds-Cd)O2s
                        L7: Cds-Cds(Cds-Cds)O2s
                        L7: Cds-Cds(Cds-Cdd)O2s
                            L8: Cds-Cds(Cds-Cdd-O2d)O2s
                            L8: Cds-Cds(Cds-Cdd-Cd)O2s
                L5: Cds-CdsCtOs
                L5: Cds-CdsCbOs
                L5: Cds-CddCdsOs
                    L6: Cds-(Cdd-O2d)(Cds-O2d)O2s
                    L6: Cds-(Cdd-O2d)(Cds-Cd)O2s
                        L7: Cds-(Cdd-O2d)(Cds-Cds)O2s
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)O2s
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)O2s
                    L6: Cds-(Cdd-Cd)(Cds-Cd)O2s
                        L7: Cds-(Cdd-Cd)(Cds-Cds)O2s
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)O2s
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)O2s
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)O2s
                L5: Cds-CddCtOs
                    L6: Cds-(Cdd-O2d)CtOs
                    L6: Cds-(Cdd-Cd)CtOs
                L5: Cds-CddCbOs
                    L6: Cds-(Cdd-O2d)CbOs
                    L6: Cds-(Cdd-Cd)CbOs
                L5: Cd-CdCsOs
                    L6: Cds-CdsCsOs
                    L6: Cds-CddCsOs
                        L7: Cds-(Cdd-O2d)CsOs
                        L7: Cds-(Cdd-Cd)CsOs
            L4: Cds-CdCS
                L5: Cds-CdsCsSs
                    L6: Cds-CdsCsS2
                    L6: Cds-CdsCsS4
                    L6: Cds-CdsCsS6
                L5: Cds-CdsCdsSs
                    L6: Cds-Cds(Cds-Cd)S2s
                        L7: Cds-Cds(Cds-Cds)S2s
                        L7: Cds-Cds(Cds-Cdd)S2s
                            L8: Cds-Cds(Cds-Cdd-S2d)S2s
                            L8: Cds-Cds(Cds-Cdd-Cd)S2s
                L5: Cds-CdsCtSs
                L5: Cds-CdsCbSs
                L5: Cds-CddCsSs
                    L6: Cds-(Cdd-S2d)CsSs
                    L6: Cds-(Cdd-Cd)CsSs
                L5: Cds-CddCdsSs
                    L6: Cds-(Cdd-S2d)(Cds-Cd)S2s
                        L7: Cds-(Cdd-S2d)(Cds-Cds)S2s
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)S2s
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)S2s
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)S2s
                    L6: Cds-(Cdd-Cd)(Cds-Cd)S2s
                        L7: Cds-(Cdd-Cd)(Cds-Cds)S2s
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)S2s
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)S2s
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)S2s
                L5: Cds-CddCtSs
                    L6: Cds-(Cdd-S2d)CtSs
                    L6: Cds-(Cdd-Cd)CtSs
                L5: Cds-CddCbSs
                    L6: Cds-(Cdd-S2d)CbSs
                    L6: Cds-(Cdd-Cd)CbSs
                L5: Cds-(Cdd-S2d)C=SSs
                L5: Cds-CdsC=SSs
            L4: Cds-CdCC
                L5: Cds-CdsCsCs
                L5: Cds-CdsCdsCs
                    L6: Cd-CdCs(CO)
                    L6: Cds-Cds(Cds-Cd)Cs
                        L7: Cds-Cds(Cds-Cds)Cs
                        L7: Cds-Cds(Cds-Cdd)Cs
                            L8: Cd-CdCs(CCO)
                            L8: Cds-Cds(Cds-Cdd-S2d)Cs
                            L8: Cds-Cds(Cds-Cdd-Cd)Cs
                L5: Cds-CdsCdsCds
                    L6: Cds-Cds(Cds-O2d)(Cds-O2d)
                    L6: Cds-Cds(Cds-O2d)(Cds-Cd)
                        L7: Cds-Cds(Cds-O2d)(Cds-Cds)
                        L7: Cds-Cds(Cds-O2d)(Cds-Cdd)
                            L8: Cds-Cds(Cds-O2d)(Cds-Cdd-O2d)
                            L8: Cds-Cds(Cds-O2d)(Cds-Cdd-Cd)
                    L6: Cds-Cds(Cds-Cd)(Cds-Cd)
                        L7: Cds-Cds(Cds-Cds)(Cds-Cds)
                        L7: Cds-Cds(Cds-Cds)(Cds-Cdd)
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-O2d)
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-S2d)
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cds-Cds(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cds-Cds(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cds-Cds(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cds-Cds(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cds-CdsCtCs
                    L6: Cd-CdCs(CtN3t)
                L5: Cds-CdsCtCds
                    L6: Cds-CdsCt(Cds-O2d)
                    L6: Cds-CdsCt(Cds-Cd)
                        L7: Cds-Cds(Cds-Cds)Ct
                        L7: Cds-Cds(Cds-Cdd)Ct
                            L8: Cds-Cds(Cds-Cdd-O2d)Ct
                            L8: Cds-Cds(Cds-Cdd-S2d)Ct
                            L8: Cds-Cds(Cds-Cdd-Cd)Ct
                L5: Cds-CdsCtCt
                    L6: Cds-Cd(CtN3t)(CtN3t)
                L5: Cds-CdsCbCs
                L5: Cds-CdsCbCds
                    L6: Cds-CdsCb(Cds-O2d)
                    L6: Cds-Cds(Cds-Cd)Cb
                        L7: Cds-Cds(Cds-Cds)Cb
                        L7: Cds-Cds(Cds-Cdd)Cb
                            L8: Cds-Cds(Cds-Cdd-O2d)Cb
                            L8: Cds-Cds(Cds-Cdd-S2d)Cb
                            L8: Cds-Cds(Cds-Cdd-Cd)Cb
                L5: Cds-CdsCbCt
                L5: Cds-CdsCbCb
                L5: Cds-CddCsCs
                    L6: Cds-(Cdd-O2d)CsCs
                    L6: Cds-(Cdd-S2d)CsCs
                    L6: Cds-(Cdd-Cd)CsCs
                L5: Cds-CddCdsCs
                    L6: Cds-(Cdd-O2d)(Cds-O2d)Cs
                    L6: Cds-(Cdd-O2d)(Cds-Cd)Cs
                        L7: Cds-(Cdd-O2d)(Cds-Cds)Cs
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cs
                    L6: Cds-(Cdd-S2d)(Cds-Cd)Cs
                        L7: Cds-(Cdd-S2d)(Cds-Cds)Cs
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)Cs
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)Cs
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Cs
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Cs
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs
                L5: Cds-CddCdsCds
                    L6: Cds-(Cdd-O2d)(Cds-O2d)(Cds-O2d)
                    L6: Cds-(Cdd-O2d)(Cds-Cd)(Cds-O2d)
                        L7: Cds-(Cdd-O2d)(Cds-Cds)(Cds-O2d)
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)(Cds-O2d)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-O2d)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-O2d)
                    L6: Cds-(Cdd-O2d)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-O2d)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cds)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-Cd)(Cds-O2d)(Cds-O2d)
                    L6: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cd)
                        L7: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd)
                            L8: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-O2d)
                            L8: Cds-(Cdd-Cd)(Cds-O2d)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-S2d)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-S2d)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cds)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cds-CddCtCs
                    L6: Cds-(Cdd-O2d)CtCs
                    L6: Cds-(Cdd-S2d)CtCs
                    L6: Cds-(Cdd-Cd)CtCs
                L5: Cds-CddCtCds
                    L6: Cds-(Cdd-O2d)(Cds-O2d)Ct
                    L6: Cds-(Cdd-O2d)(Cds-Cd)Ct
                        L7: Cds-(Cdd-O2d)(Cds-Cds)Ct
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)Ct
                    L6: Cds-(Cdd-S2d)(Cds-Cd)Ct
                        L7: Cds-(Cdd-S2d)(Cds-Cds)Ct
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)Ct
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)Ct
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Ct
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Ct
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct
                L5: Cds-CddCtCt
                    L6: Cds-(Cdd-O2d)CtCt
                    L6: Cds-(Cdd-S2d)CtCt
                    L6: Cds-(Cdd-Cd)CtCt
                L5: Cds-CddCbCs
                    L6: Cds-(Cdd-O2d)CbCs
                    L6: Cds-(Cdd-S2d)CbCs
                    L6: Cds-(Cdd-Cd)CbCs
                L5: Cds-CddCbCds
                    L6: Cds-(Cdd-O2d)(Cds-O2d)Cb
                    L6: Cds-(Cdd-O2d)(Cds-Cd)Cb
                        L7: Cds-(Cdd-O2d)(Cds-Cds)Cb
                        L7: Cds-(Cdd-O2d)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cds-(Cdd-O2d)(Cds-Cdd-Cd)Cb
                    L6: Cds-(Cdd-S2d)(Cds-Cd)Cb
                        L7: Cds-(Cdd-S2d)(Cds-Cds)Cb
                        L7: Cds-(Cdd-S2d)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-S2d)Cb
                            L8: Cds-(Cdd-S2d)(Cds-Cdd-Cd)Cb
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Cb
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Cb
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-O2d)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-S2d)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb
                L5: Cds-CddCbCt
                    L6: Cds-(Cdd-O2d)CbCt
                    L6: Cds-(Cdd-S2d)CbCt
                    L6: Cds-(Cdd-Cd)CbCt
                L5: Cds-CddCbCb
                    L6: Cds-(Cdd-O2d)CbCb
                    L6: Cds-(Cdd-S2d)CbCb
                    L6: Cds-(Cdd-Cd)CbCb
                L5: Cds-CdsC=SC=S
                L5: Cds-(Cdd-Cd)C=S(Cds-Cd)
                    L6: Cds-(Cdd-Cd)C=S(Cds-Cds)
                    L6: Cds-(Cdd-Cd)C=S(Cds-Cdd)
                        L7: Cds-(Cdd-Cd)C=S(Cds-Cdd-Cd)
                        L7: Cds-(Cdd-Cd)C=S(Cds-Cdd-S2d)
                L5: Cds-(Cdd-S2d)C=SCs
                L5: Cds-(Cdd-S2d)C=SCt
                L5: Cds-(Cdd-S2d)C=SCb
                L5: Cds-(Cdd-Cd)C=SC=S
                L5: Cds-(Cdd-S2d)(Cds-Cd)C=S
                    L6: Cds-(Cdd-S2d)(Cds-Cds)C=S
                    L6: Cds-(Cdd-S2d)(Cds-Cdd)C=S
                        L7: Cds-(Cdd-S2d)(Cds-Cdd-S2d)C=S
                        L7: Cds-(Cdd-S2d)(Cds-Cdd-Cd)C=S
                L5: Cds-CdsCbC=S
                L5: Cds-CdsCtC=S
                L5: Cds-CdsC=SCs
                L5: Cds-CdsC=S(Cds-Cd)
                    L6: Cds-CdsC=S(Cds-Cds)
                    L6: Cds-CdsC=S(Cds-Cdd)
                        L7: Cds-CdsC=S(Cds-Cdd-Cd)
                        L7: Cds-CdsC=S(Cds-Cdd-S2d)
                L5: Cds-(Cdd-S2d)C=SC=S
            L4: Cds-CNH
                L5: Cd-CdHN3s
                L5: Cd-CdH(N5dcOdOs)
            L4: Cds-CCN
                L5: Cd-CdCsN3s
                L5: Cd-CdCs(N5dcOdOs)
            L4: C=S-SsSs
            L4: C=S-CH
                L5: C=S-CsH
                    L6: C=S2-CsH
                    L6: C=S4-CsH
                L5: C=S-CdsH
                    L6: C=S-(Cds-Cd)H
                        L7: C=S-(Cds-Cdd)H
                            L8: C=S-(Cds-Cdd-Cd)H
                            L8: C=S-(Cds-Cdd-S2d)H
                        L7: C=S-(Cds-Cds)H
                L5: C=S-CtH
                L5: C=S-C=SH
            L4: C=S-CC
                L5: C=S-CbCds
                    L6: C=S-Cb(Cds-Cd)
                        L7: C=S-Cb(Cds-Cds)
                        L7: C=S-Cb(Cds-Cdd)
                            L8: C=S-Cb(Cds-Cdd-S2d)
                            L8: C=S-Cb(Cds-Cdd-Cd)
                L5: C=S-CtCt
                L5: C=S-CbCb
                L5: C=S-CdsCds
                    L6: C=S-(Cds-Cd)(Cds-Cd)
                        L7: C=S-(Cds-Cdd)(Cds-Cds)
                            L8: C=S-(Cds-Cdd-Cd)(Cds-Cds)
                            L8: C=S-(Cds-Cdd-S2d)(Cds-Cds)
                        L7: C=S-(Cds-Cds)(Cds-Cds)
                        L7: C=S-(Cds-Cdd)(Cds-Cdd)
                            L8: C=S-(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: C=S-(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: C=S-(Cds-Cdd-Cd)(Cds-Cdd-S2d)
                L5: C=S-CtCds
                    L6: C=S-Ct(Cds-Cd)
                        L7: C=S-Ct(Cds-Cds)
                        L7: C=S-Ct(Cds-Cdd)
                            L8: C=S-Ct(Cds-Cdd-Cd)
                            L8: C=S-Ct(Cds-Cdd-S2d)
                L5: C=S-CbCt
                L5: C=S-CsCs
                L5: C=S-CdsCs
                    L6: C=S-(Cds-Cd)Cs
                        L7: C=S-(Cds-Cds)Cs
                        L7: C=S-(Cds-Cdd)Cs
                            L8: C=S-(Cds-Cdd-S2d)Cs
                            L8: C=S-(Cds-Cdd-Cd)Cs
                L5: C=S-CtCs
                L5: C=S-CbCs
                L5: C=S-C=SCs
                L5: C=S-CtC=S
                L5: C=S-(Cds-Cd)C=S
                    L6: C=S-(Cds-Cdd)C=S
                        L7: C=S-(Cds-Cdd-Cd)C=S
                        L7: C=S-(Cds-Cdd-S2d)C=S
                    L6: C=S-(Cds-Cds)C=S
                L5: C=S-C=SC=S
                L5: C=S-CbC=S
            L4: C=S-HH
                L5: C=S2d-HH
                L5: C=S4d-HH
                L5: C=S6dd-HH
                L5: C=S6ddd-HH
            L4: C=S-SH
                L5: C=S-S2H
                L5: C=S-S4H
                L5: C=S-S6H
                L5: C=S6-S2H
            L4: C=S-CSs
                L5: C=S-CbSs
                L5: C=S-CdsSs
                    L6: C=S-(Cds-Cd)S2s
                        L7: C=S-(Cds-Cds)S2s
                        L7: C=S-(Cds-Cdd)S2s
                            L8: C=S-(Cds-Cdd-Cd)S2s
                            L8: C=S-(Cds-Cdd-S2d)S2s
                L5: C=S-CtSs
                L5: C=S-CsSs
                L5: C=S-C=SSs
                L5: C=S-S(CO)
            L4: C=S-OsH
                L5: C=S2-OsH
                L5: C=S4-OsH
            L4: C=S-CsOs
            L4: C=S-OsOs
            L4: C=S-OsS
        L3: Cs
            L4: Cs-NHHH
                L5: Cs-N3sHHH
                L5: Cs-N3dHHH
                    L6: Cs-(N3dCd)HHH
                    L6: Cs-(N3dN3d)HHH
            L4: Cs-NCsHH
                L5: Cs-N3sCsHH
                L5: Cs-N3dCHH
                    L6: Cs-(N3dN3d)CsHH
                    L6: Cs-(N3dOd)CHH
                    L6: Cs-(N3dCd)CsHH
                L5: Cs-N5dcCsHH
                    L6: Cs-(N5dcOdOs)CsHH
            L4: Cs-NCsCsH
                L5: Cs-N3sCsCsH
                L5: Cs-N3dCsCsH
                    L6: Cs-(N3dOd)CsCsH
                    L6: Cs-(N3dN3d)CsCsH
                L5: Cs-N5dcCsCsH
                    L6: Cs-(N5dcOdOs)CsCsH
            L4: Cs-NCsCsCs
                L5: Cs-N3sCsCsCs
                L5: Cs-N3dCsCsCs
                    L6: Cs-(N3dOd)CsCsCs
                    L6: Cs-(N3dN3d)CsCsCs
                L5: Cs-N5dcCsCsCs
                    L6: Cs-(N5dcOdOs)CsCsCs
            L4: Cs-NNCsCs
                L5: Cs-N5dcN5dcCsCs
            L4: Cs-NNCsH
                L5: Cs-(N5dcOdOs)(N5dcOdOs)CsH
            L4: Cs-HHHH
            L4: Cs-CHHH
                L5: Cs-CsHHH
                L5: Cs-CdsHHH
                    L6: Cs-(Cds-O2d)HHH
                    L6: Cs-(Cds-Cd)HHH
                        L7: Cs-(Cds-Cds)HHH
                        L7: Cs-(Cds-Cdd)HHH
                            L8: Cs-(Cds-Cdd-O2d)HHH
                            L8: Cs-(Cds-Cdd-S2d)HHH
                            L8: Cs-(Cds-Cdd-Cd)HHH
                    L6: Cs-(CdN3d)HHH
                L5: Cs-CtHHH
                    L6: Cs-(CtN3t)HHH
                L5: Cs-CbHHH
                L5: Cs-C=SHHH
            L4: Cs-OsHHH
            L4: Cs-OsOsHH
            L4: Cs-OsOsOsH
            L4: Cs-OsSHH
                L5: Cs-OsS2HH
                L5: Cs-OsS4HH
            L4: Cs-OsSSH
                L5: Cs-OsS2S2H
                L5: Cs-OsS4S2H
            L4: Cs-OsOsSH
                L5: Cs-OsOsS2H
                L5: Cs-OsOsS4H
            L4: Cs-SsHHH
                L5: Cs-S2sHHH
                L5: Cs-S4HHH
                L5: Cs-S6HHH
            L4: Cs-SsSsHH
            L4: Cs-SsSsSsH
            L4: Cs-CCHH
                L5: Cs-CsCsHH
                L5: Cs-CdsCsHH
                    L6: Cs-(Cds-O2d)CsHH
                    L6: Cs-(Cds-Cd)CsHH
                        L7: Cs-(Cds-Cds)CsHH
                        L7: Cs-(Cds-Cdd)CsHH
                            L8: Cs-(Cds-Cdd-O2d)CsHH
                            L8: Cs-(Cds-Cdd-S2d)CsHH
                            L8: Cs-(Cds-Cdd-Cd)CsHH
                    L6: Cs-(CdN3d)CsHH
                L5: Cs-CdsCdsHH
                    L6: Cs-(Cds-O2d)(Cds-O2d)HH
                    L6: Cs-(Cds-O2d)(Cds-Cd)HH
                        L7: Cs-(Cds-O2d)(Cds-Cds)HH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)HH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)HH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)HH
                    L6: Cs-(Cds-Cd)(Cds-Cd)HH
                        L7: Cs-(Cds-Cds)(Cds-Cds)HH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)HH
                            L8: Cs-Cd(CCO)HH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)HH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)HH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)HH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)HH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)HH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)HH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)HH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH
                L5: Cs-CtCsHH
                    L6: Cs-(CtN3t)CsHH
                L5: Cs-CtCdsHH
                    L6: Cs-(Cds-O2d)CtHH
                    L6: Cs-(Cds-Cd)CtHH
                        L7: Cs-(Cds-Cds)CtHH
                        L7: Cs-(Cds-Cdd)CtHH
                            L8: Cs-(Cds-Cdd-O2d)CtHH
                            L8: Cs-(Cds-Cdd-S2d)CtHH
                            L8: Cs-(Cds-Cdd-Cd)CtHH
                L5: Cs-CtCtHH
                L5: Cs-CbCsHH
                L5: Cs-CbCdsHH
                    L6: Cs-(Cds-O2d)CbHH
                    L6: Cs-(Cds-Cd)CbHH
                        L7: Cs-(Cds-Cds)CbHH
                        L7: Cs-(Cds-Cdd)CbHH
                            L8: Cs-(Cds-Cdd-O2d)CbHH
                            L8: Cs-(Cds-Cdd-S2d)CbHH
                            L8: Cs-(Cds-Cdd-Cd)CbHH
                L5: Cs-CbCtHH
                L5: Cs-CbCbHH
                L5: Cs-C=SCtHH
                L5: Cs-C=SCsHH
                L5: Cs-C=S(Cds-Cd)HH
                    L6: Cs-C=S(Cds-Cdd)HH
                        L7: Cs-C=S(Cds-Cdd-Cd)HH
                        L7: Cs-C=S(Cds-Cdd-S2d)HH
                    L6: Cs-C=S(Cds-Cds)HH
                L5: Cs-C=SC=SHH
                L5: Cs-C=SCbHH
            L4: Cs-CCCH
                L5: Cs-CsCsCsH
                L5: Cs-CdsCsCsH
                    L6: Cs-(Cds-O2d)CsCsH
                    L6: Cs-(Cds-Cd)CsCsH
                        L7: Cs-(Cds-Cds)CsCsH
                        L7: Cs-(Cds-Cdd)CsCsH
                            L8: Cs-(Cds-Cdd-O2d)CsCsH
                            L8: Cs-(Cds-Cdd-S2d)CsCsH
                            L8: Cs-(Cds-Cdd-Cd)CsCsH
                    L6: Cs-(CdN3d)CsCsH
                L5: Cs-CtCsCsH
                    L6: Cs-(CtN3t)CsCsH
                L5: Cs-CbCsCsH
                L5: Cs-CdsCdsCsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)CsH
                    L6: Cs-(Cds-O2d)(Cds-Cd)CsH
                        L7: Cs-(Cds-O2d)(Cds-Cds)CsH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CsH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CsH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CsH
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsH
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsH
                            L8: Cs-CsCd(CCO)H
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH
                L5: Cs-CtCdsCsH
                    L6: Cs-(Cds-O2d)CtCsH
                    L6: Cs-(Cds-Cd)CtCsH
                        L7: Cs-(Cds-Cds)CtCsH
                        L7: Cs-(Cds-Cdd)CtCsH
                            L8: Cs-(Cds-Cdd-O2d)CtCsH
                            L8: Cs-(Cds-Cdd-S2d)CtCsH
                            L8: Cs-(Cds-Cdd-Cd)CtCsH
                L5: Cs-CbCdsCsH
                    L6: Cs-(Cds-O2d)CbCsH
                    L6: Cs-(Cds-Cd)CbCsH
                        L7: Cs-(Cds-Cds)CbCsH
                        L7: Cs-(Cds-Cdd)CbCsH
                            L8: Cs-(Cds-Cdd-O2d)CbCsH
                            L8: Cs-(Cds-Cdd-Cd)CbCsH
                L5: Cs-CtCtCsH
                L5: Cs-CbCtCsH
                L5: Cs-CbCbCsH
                L5: Cs-CdsCdsCdsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)H
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)H
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)H
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)H
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)H
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)H
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)H
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)H
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)H
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)H
                            L8: Cs-CdCd(CCO)H
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)H
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)H
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)H
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                L5: Cs-CtCdsCdsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)CtH
                    L6: Cs-(Cds-O2d)(Cds-Cd)CtH
                        L7: Cs-(Cds-O2d)(Cds-Cds)CtH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CtH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CtH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CtH
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtH
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CtH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CtH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH
                L5: Cs-CbCdsCdsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbH
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbH
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbH
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbH
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH
                L5: Cs-CtCtCdsH
                    L6: Cs-CtCt(Cds-O2d)H
                    L6: Cs-CtCt(Cds-Cd)H
                        L7: Cs-CtCt(Cds-Cds)H
                        L7: Cs-CtCt(Cds-Cdd)H
                            L8: Cs-CtCt(Cds-Cdd-O2d)H
                            L8: Cs-CtCt(Cds-Cdd-S2d)H
                            L8: Cs-CtCt(Cds-Cdd-Cd)H
                L5: Cs-CbCtCdsH
                    L6: Cs-CbCt(Cds-O2d)H
                    L6: Cs-CbCt(Cds-Cd)H
                        L7: Cs-CbCt(Cds-Cds)H
                        L7: Cs-CbCt(Cds-Cdd)H
                            L8: Cs-CbCt(Cds-Cdd-O2d)H
                            L8: Cs-CbCt(Cds-Cdd-S2d)H
                            L8: Cs-CbCt(Cds-Cdd-Cd)H
                L5: Cs-CbCbCdsH
                    L6: Cs-CbCb(Cds-O2d)H
                    L6: Cs-CbCb(Cds-Cd)H
                        L7: Cs-CbCb(Cds-Cds)H
                        L7: Cs-CbCb(Cds-Cdd)H
                            L8: Cs-CbCb(Cds-Cdd-O2d)H
                            L8: Cs-CbCb(Cds-Cdd-S2d)H
                            L8: Cs-CbCb(Cds-Cdd-Cd)H
                L5: Cs-CtCtCtH
                L5: Cs-CbCtCtH
                L5: Cs-CbCbCtH
                L5: Cs-CbCbCbH
                L5: Cs-C=SC=SCbH
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)H
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)H
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)H
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)H
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)H
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)H
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)H
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)H
                L5: Cs-C=S(Cds-Cd)CtH
                    L6: Cs-C=S(Cds-Cdd)CtH
                        L7: Cs-C=S(Cds-Cdd-S2d)CtH
                        L7: Cs-C=S(Cds-Cdd-Cd)CtH
                    L6: Cs-C=S(Cds-Cds)CtH
                L5: Cs-C=SC=SCtH
                L5: Cs-C=SCtCsH
                L5: Cs-C=SC=SCsH
                L5: Cs-C=S(Cds-Cd)CbH
                    L6: Cs-C=S(Cds-Cds)CbH
                    L6: Cs-C=S(Cds-Cdd)CbH
                        L7: Cs-C=S(Cds-Cdd-S2d)CbH
                        L7: Cs-C=S(Cds-Cdd-Cd)CbH
                L5: Cs-C=S(Cds-Cd)CsH
                    L6: Cs-C=S(Cds-Cds)CsH
                    L6: Cs-C=S(Cds-Cdd)CsH
                        L7: Cs-C=S(Cds-Cdd-Cd)CsH
                        L7: Cs-C=S(Cds-Cdd-S2d)CsH
                L5: Cs-CbCtC=SH
                L5: Cs-C=SC=SC=SH
                L5: Cs-C=SCsCsH
                L5: Cs-CtCtC=SH
                L5: Cs-CbCbC=SH
                L5: Cs-C=SC=S(Cds-Cd)H
                    L6: Cs-C=SC=S(Cds-Cds)H
                    L6: Cs-C=SC=S(Cds-Cdd)H
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)H
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)H
            L4: Cs-CCCC
                L5: Cs-CsCsCsCs
                L5: Cs-CdsCsCsCs
                    L6: Cs-(Cds-O2d)CsCsCs
                    L6: Cs-(Cds-Cd)CsCsCs
                        L7: Cs-(Cds-Cds)CsCsCs
                        L7: Cs-(Cds-Cdd)CsCsCs
                            L8: Cs-(Cds-Cdd-O2d)CsCsCs
                            L8: Cs-(Cds-Cdd-S2d)CsCsCs
                            L8: Cs-(Cds-Cdd-Cd)CsCsCs
                    L6: Cs-(CdN3d)CsCsCs
                L5: Cs-CtCsCsCs
                    L6: Cs-(CtN3t)CsCsCs
                L5: Cs-CbCsCsCs
                L5: Cs-CdsCdsCsCs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CsCs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CsCs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CsCs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CsCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CsCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CsCs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsCs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsCs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsCs
                            L8: Cs-CsCsCd(CCO)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CsCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs
                L5: Cs-CtCdsCsCs
                    L6: Cs-(Cds-O2d)CtCsCs
                    L6: Cs-(Cds-Cd)CtCsCs
                        L7: Cs-(Cds-Cds)CtCsCs
                        L7: Cs-(Cds-Cdd)CtCsCs
                            L8: Cs-(Cds-Cdd-O2d)CtCsCs
                            L8: Cs-(Cds-Cdd-S2d)CtCsCs
                            L8: Cs-(Cds-Cdd-Cd)CtCsCs
                L5: Cs-CbCdsCsCs
                    L6: Cs-(Cds-O2d)CbCsCs
                    L6: Cs-(Cds-Cd)CbCsCs
                        L7: Cs-(Cds-Cds)CbCsCs
                        L7: Cs-(Cds-Cdd)CbCsCs
                            L8: Cs-(Cds-Cdd-O2d)CbCsCs
                            L8: Cs-(Cds-Cdd-S2d)CbCsCs
                            L8: Cs-(Cds-Cdd-Cd)CbCsCs
                L5: Cs-CtCtCsCs
                    L6: Cs-(CtN3t)(CtN3t)CsCs
                L5: Cs-CbCtCsCs
                L5: Cs-CbCbCsCs
                L5: Cs-CdsCdsCdsCs
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cs
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Cs
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cs
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Cs
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cs
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Cs
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                L5: Cs-CtCdsCdsCs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CtCs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CtCs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CtCs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CtCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CtCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtCs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtCs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CtCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs
                L5: Cs-CbCdsCdsCs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbCs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbCs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbCs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbCs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbCs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs
                L5: Cs-CtCtCdsCs
                    L6: Cs-(Cds-O2d)CtCtCs
                    L6: Cs-(Cds-Cd)CtCtCs
                        L7: Cs-(Cds-Cds)CtCtCs
                        L7: Cs-(Cds-Cdd)CtCtCs
                            L8: Cs-(Cds-Cdd-O2d)CtCtCs
                            L8: Cs-(Cds-Cdd-S2d)CtCtCs
                            L8: Cs-(Cds-Cdd-Cd)CtCtCs
                L5: Cs-CbCtCdsCs
                    L6: Cs-(Cds-O2d)CbCtCs
                    L6: Cs-(Cds-Cd)CbCtCs
                        L7: Cs-(Cds-Cds)CbCtCs
                        L7: Cs-(Cds-Cdd)CbCtCs
                            L8: Cs-(Cds-Cdd-O2d)CbCtCs
                            L8: Cs-(Cds-Cdd-S2d)CbCtCs
                            L8: Cs-(Cds-Cdd-Cd)CbCtCs
                L5: Cs-CbCbCdsCs
                    L6: Cs-(Cds-O2d)CbCbCs
                    L6: Cs-(Cds-Cd)CbCbCs
                        L7: Cs-(Cds-Cds)CbCbCs
                        L7: Cs-(Cds-Cdd)CbCbCs
                            L8: Cs-(Cds-Cdd-O2d)CbCbCs
                            L8: Cs-(Cds-Cdd-S2d)CbCbCs
                            L8: Cs-(Cds-Cdd-Cd)CbCbCs
                L5: Cs-CtCtCtCs
                L5: Cs-CbCtCtCs
                L5: Cs-CbCbCtCs
                L5: Cs-CbCbCbCs
                L5: Cs-CdsCdsCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-O2d)
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cd)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cds)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)(Cds-Cd)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)(Cds-Cds)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)(Cds-Cds)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cds)
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cs-CtCdsCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Ct
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Ct
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Ct
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Ct
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Ct
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Ct
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Ct
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Ct
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Ct
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                L5: Cs-CbCdsCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)Cb
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)Cb
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)Cb
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)Cb
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)Cb
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)Cb
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)Cb
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)Cb
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)Cb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                L5: Cs-CtCtCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)CtCt
                    L6: Cs-(Cds-O2d)(Cds-Cd)CtCt
                        L7: Cs-(Cds-O2d)(Cds-Cds)CtCt
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CtCt
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CtCt
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CtCt
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtCt
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtCt
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CtCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CtCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt
                L5: Cs-CbCtCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbCt
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbCt
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbCt
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbCt
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCt
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCt
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbCt
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbCt
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCt
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCt
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt
                L5: Cs-CbCbCdsCds
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbCb
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbCb
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbCb
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbCb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbCb
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbCb
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbCb
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbCb
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbCb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbCb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbCb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbCb
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbCb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbCb
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbCb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb
                L5: Cs-CtCtCtCds
                    L6: Cs-(Cds-O2d)CtCtCt
                    L6: Cs-(Cds-Cd)CtCtCt
                        L7: Cs-(Cds-Cds)CtCtCt
                        L7: Cs-(Cds-Cdd)CtCtCt
                            L8: Cs-(Cds-Cdd-O2d)CtCtCt
                            L8: Cs-(Cds-Cdd-S2d)CtCtCt
                            L8: Cs-(Cds-Cdd-Cd)CtCtCt
                L5: Cs-CbCtCtCds
                    L6: Cs-(Cds-O2d)CbCtCt
                    L6: Cs-(Cds-Cd)CbCtCt
                        L7: Cs-(Cds-Cds)CbCtCt
                        L7: Cs-(Cds-Cdd)CbCtCt
                            L8: Cs-(Cds-Cdd-O2d)CbCtCt
                            L8: Cs-(Cds-Cdd-S2d)CbCtCt
                            L8: Cs-(Cds-Cdd-Cd)CbCtCt
                L5: Cs-CbCbCtCds
                    L6: Cs-(Cds-O2d)CbCbCt
                    L6: Cs-(Cds-Cd)CbCbCt
                        L7: Cs-(Cds-Cds)CbCbCt
                        L7: Cs-(Cds-Cdd)CbCbCt
                            L8: Cs-(Cds-Cdd-O2d)CbCbCt
                            L8: Cs-(Cds-Cdd-S2d)CbCbCt
                            L8: Cs-(Cds-Cdd-Cd)CbCbCt
                L5: Cs-CbCbCbCds
                    L6: Cs-(Cds-O2d)CbCbCb
                    L6: Cs-(Cds-Cd)CbCbCb
                        L7: Cs-(Cds-Cds)CbCbCb
                        L7: Cs-(Cds-Cdd)CbCbCb
                            L8: Cs-(Cds-Cdd-O2d)CbCbCb
                            L8: Cs-(Cds-Cdd-S2d)CbCbCb
                            L8: Cs-(Cds-Cdd-Cd)CbCbCb
                L5: Cs-CtCtCtCt
                L5: Cs-CbCtCtCt
                L5: Cs-CbCbCtCt
                L5: Cs-CbCbCbCt
                L5: Cs-CbCbCbCb
                L5: Cs-C=SCbCtCt
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)(Cds-Cd)
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cds)
                    L6: Cs-C=S(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cs-C=S(Cds-Cd)CtCt
                    L6: Cs-C=S(Cds-Cds)CtCt
                    L6: Cs-C=S(Cds-Cdd)CtCt
                        L7: Cs-C=S(Cds-Cdd-S2d)CtCt
                        L7: Cs-C=S(Cds-Cdd-Cd)CtCt
                L5: Cs-C=S(Cds-Cd)CtCs
                    L6: Cs-C=S(Cds-Cds)CtCs
                    L6: Cs-C=S(Cds-Cdd)CtCs
                        L7: Cs-C=S(Cds-Cdd-S2d)CtCs
                        L7: Cs-C=S(Cds-Cdd-Cd)CtCs
                L5: Cs-C=SCbCbCt
                L5: Cs-C=SCbCsCs
                L5: Cs-C=SCbCbCs
                L5: Cs-C=SCtCtCt
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)Cs
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)Cs
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cs
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cs
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)Cs
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)Cs
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Cs
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cs
                L5: Cs-C=SC=SCtCt
                L5: Cs-C=SCsCsCs
                L5: Cs-C=SCtCtCs
                L5: Cs-C=SC=SC=SCt
                L5: Cs-C=SC=SC=SCs
                L5: Cs-C=SC=SC=SC=S
                L5: Cs-C=SCtCsCs
                L5: Cs-C=SC=SC=SCb
                L5: Cs-C=SC=SC=S(Cds-Cd)
                    L6: Cs-C=SC=SC=S(Cds-Cdd)
                        L7: Cs-C=SC=SC=S(Cds-Cdd-Cd)
                        L7: Cs-C=SC=SC=S(Cds-Cdd-S2d)
                    L6: Cs-C=SC=SC=S(Cds-Cds)
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)Ct
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)Ct
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Ct
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Ct
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)Ct
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)Ct
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Ct
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Ct
                L5: Cs-C=SC=SCtCs
                L5: Cs-C=SC=SCbCb
                L5: Cs-C=S(Cds-Cd)CsCs
                    L6: Cs-C=S(Cds-Cds)CsCs
                    L6: Cs-C=S(Cds-Cdd)CsCs
                        L7: Cs-C=S(Cds-Cdd-Cd)CsCs
                        L7: Cs-C=S(Cds-Cdd-S2d)CsCs
                L5: Cs-C=SC=SCbCt
                L5: Cs-C=S(Cds-Cd)CbCt
                    L6: Cs-C=S(Cds-Cds)CbCt
                    L6: Cs-C=S(Cds-Cdd)CbCt
                        L7: Cs-C=S(Cds-Cdd-S2d)CbCt
                        L7: Cs-C=S(Cds-Cdd-Cd)CbCt
                L5: Cs-C=SC=SCsCs
                L5: Cs-C=S(Cds-Cd)CbCb
                    L6: Cs-C=S(Cds-Cds)CbCb
                    L6: Cs-C=S(Cds-Cdd)CbCb
                        L7: Cs-C=S(Cds-Cdd-S2d)CbCb
                        L7: Cs-C=S(Cds-Cdd-Cd)CbCb
                L5: Cs-C=SC=S(Cds-Cd)Ct
                    L6: Cs-C=SC=S(Cds-Cds)Ct
                    L6: Cs-C=SC=S(Cds-Cdd)Ct
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)Ct
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)Ct
                L5: Cs-C=SC=S(Cds-Cd)Cs
                    L6: Cs-C=SC=S(Cds-Cds)Cs
                    L6: Cs-C=SC=S(Cds-Cdd)Cs
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)Cs
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)Cs
                L5: Cs-C=SC=S(Cds-Cd)(Cds-Cd)
                    L6: Cs-C=SC=S(Cds-Cdd)(Cds-Cds)
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cds)
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cds)
                    L6: Cs-C=SC=S(Cds-Cdd)(Cds-Cdd)
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-C=SC=S(Cds-Cds)(Cds-Cds)
                L5: Cs-C=SC=S(Cds-Cd)Cb
                    L6: Cs-C=SC=S(Cds-Cdd)Cb
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)Cb
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)Cb
                    L6: Cs-C=SC=S(Cds-Cds)Cb
                L5: Cs-C=SCbCtCs
                L5: Cs-C=S(Cds-Cd)CbCs
                    L6: Cs-C=S(Cds-Cds)CbCs
                    L6: Cs-C=S(Cds-Cdd)CbCs
                        L7: Cs-C=S(Cds-Cdd-S2d)CbCs
                        L7: Cs-C=S(Cds-Cdd-Cd)CbCs
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)Cb
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)Cb
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)Cb
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)Cb
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)Cb
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)Cb
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)Cb
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cb
                L5: Cs-C=SCbCbCb
                L5: Cs-C=SC=SCbCs
            L4: Cs-CCCOs
                L5: Cs-CsCsCsOs
                L5: Cs-CdsCsCsOs
                    L6: Cs-(Cds-O2d)CsCsOs
                    L6: Cs-(Cds-Cd)CsCsOs
                        L7: Cs-(Cds-Cds)CsCsOs
                        L7: Cs-(Cds-Cdd)CsCsOs
                            L8: Cs-(Cds-Cdd-O2d)CsCsOs
                            L8: Cs-(Cds-Cdd-Cd)CsCsOs
                L5: Cs-OsCtCsCs
                L5: Cs-CbCsCsOs
                L5: Cs-CdsCdsCsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CsOs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CsOs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CsOs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CsOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CsOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CsOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs
                L5: Cs-CtCdsCsOs
                    L6: Cs-(Cds-O2d)CtCsOs
                    L6: Cs-(Cds-Cd)CtCsOs
                        L7: Cs-(Cds-Cds)CtCsOs
                        L7: Cs-(Cds-Cdd)CtCsOs
                            L8: Cs-(Cds-Cdd-O2d)CtCsOs
                            L8: Cs-(Cds-Cdd-Cd)CtCsOs
                L5: Cs-CbCdsCsOs
                    L6: Cs-(Cds-O2d)CbCsOs
                    L6: Cs-(Cds-Cd)CbCsOs
                        L7: Cs-(Cds-Cds)CbCsOs
                        L7: Cs-(Cds-Cdd)CbCsOs
                            L8: Cs-(Cds-Cdd-O2d)CbCsOs
                            L8: Cs-(Cds-Cdd-Cd)CbCsOs
                L5: Cs-CtCtCsOs
                L5: Cs-CbCtCsOs
                L5: Cs-CbCbCsOs
                L5: Cs-CdsCdsCdsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-O2d)O2s
                    L6: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cd)O2s
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cds)O2s
                        L7: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd)O2s
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-O2d)(Cds-O2d)(Cds-Cdd-Cd)O2s
                    L6: Cs-(Cds-O2d)(Cds-Cd)(Cds-Cd)O2s
                        L7: Cs-(Cds-O2d)(Cds-Cds)(Cds-Cds)O2s
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cds)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cds)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cds)O2s
                        L7: Cs-(Cds-O2d)(Cds-Cdd)(Cds-Cdd)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)O2s
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)O2s
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)O2s
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)O2s
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-O2d)O2s
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)(Cds-Cdd-Cd)O2s
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)O2s
                L5: Cs-CtCdsCdsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CtOs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CtOs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CtOs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CtOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CtOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CtOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CtOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CtOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CtOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs
                L5: Cs-CbCdsCdsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)CbOs
                    L6: Cs-(Cds-O2d)(Cds-Cd)CbOs
                        L7: Cs-(Cds-O2d)(Cds-Cds)CbOs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)CbOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)CbOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)CbOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)CbOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)CbOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)CbOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs
                L5: Cs-CtCtCdsOs
                    L6: Cs-(Cds-O2d)CtCtOs
                    L6: Cs-(Cds-Cd)CtCtOs
                        L7: Cs-(Cds-Cds)CtCtOs
                        L7: Cs-(Cds-Cdd)CtCtOs
                            L8: Cs-(Cds-Cdd-O2d)CtCtOs
                            L8: Cs-(Cds-Cdd-Cd)CtCtOs
                L5: Cs-CbCtCdsOs
                    L6: Cs-(Cds-O2d)CbCtOs
                    L6: Cs-(Cds-Cd)CbCtOs
                        L7: Cs-(Cds-Cds)CbCtOs
                        L7: Cs-(Cds-Cdd)CbCtOs
                            L8: Cs-(Cds-Cdd-O2d)CbCtOs
                            L8: Cs-(Cds-Cdd-Cd)CbCtOs
                L5: Cs-CbCbCdsOs
                    L6: Cs-(Cds-O2d)CbCbOs
                    L6: Cs-(Cds-Cd)CbCbOs
                        L7: Cs-(Cds-Cds)CbCbOs
                        L7: Cs-(Cds-Cdd)CbCbOs
                            L8: Cs-(Cds-Cdd-O2d)CbCbOs
                            L8: Cs-(Cds-Cdd-Cd)CbCbOs
                L5: Cs-CtCtCtOs
                L5: Cs-CbCtCtOs
                L5: Cs-CbCbCtOs
                L5: Cs-CbCbCbOs
            L4: Cs-CCOsOs
                L5: Cs-CsCsOsOs
                L5: Cs-CdsCsOsOs
                    L6: Cs-(Cds-O2d)CsOsOs
                    L6: Cs-(Cds-Cd)CsOsOs
                        L7: Cs-(Cds-Cds)CsOsOs
                        L7: Cs-(Cds-Cdd)CsOsOs
                            L8: Cs-(Cds-Cdd-O2d)CsOsOs
                            L8: Cs-(Cds-Cdd-Cd)CsOsOs
                L5: Cs-CdsCdsOsOs
                    L6: Cs-(Cds-O2d)(Cds-O2d)OsOs
                    L6: Cs-(Cds-O2d)(Cds-Cd)OsOs
                        L7: Cs-(Cds-O2d)(Cds-Cds)OsOs
                        L7: Cs-(Cds-O2d)(Cds-Cdd)OsOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)OsOs
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)OsOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)OsOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)OsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)OsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)OsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)OsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)OsOs
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)OsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs
                L5: Cs-CtCsOsOs
                L5: Cs-CtCdsOsOs
                    L6: Cs-(Cds-O2d)CtOsOs
                    L6: Cs-(Cds-Cd)CtOsOs
                        L7: Cs-(Cds-Cds)CtOsOs
                        L7: Cs-(Cds-Cdd)CtOsOs
                            L8: Cs-(Cds-Cdd-O2d)CtOsOs
                            L8: Cs-(Cds-Cdd-Cd)CtOsOs
                L5: Cs-CtCtOsOs
                L5: Cs-CbCsOsOs
                L5: Cs-CbCdsOsOs
                    L6: Cs-(Cds-O2d)CbOsOs
                    L6: Cs-(Cds-Cd)CbOsOs
                        L7: Cs-(Cds-Cds)CbOsOs
                        L7: Cs-(Cds-Cdd)CbOsOs
                            L8: Cs-(Cds-Cdd-O2d)CbOsOs
                            L8: Cs-(Cds-Cdd-Cd)CbOsOs
                L5: Cs-CbCtOsOs
                L5: Cs-CbCbOsOs
            L4: Cs-COsOsOs
                L5: Cs-CsOsOsOs
                L5: Cs-CdsOsOsOs
                    L6: Cs-(Cds-O2d)OsOsOs
                    L6: Cs-(Cds-Cd)OsOsOs
                        L7: Cs-(Cds-Cds)OsOsOs
                        L7: Cs-(Cds-Cdd)OsOsOs
                            L8: Cs-(Cds-Cdd-O2d)OsOsOs
                            L8: Cs-(Cds-Cdd-Cd)OsOsOs
                L5: Cs-CtOsOsOs
                L5: Cs-CbOsOsOs
            L4: Cs-OsOsOsOs
            L4: Cs-COsOsH
                L5: Cs-CsOsOsH
                L5: Cs-CdsOsOsH
                    L6: Cs-(Cds-O2d)OsOsH
                    L6: Cs-(Cds-Cd)OsOsH
                        L7: Cs-(Cds-Cds)OsOsH
                        L7: Cs-(Cds-Cdd)OsOsH
                            L8: Cs-(Cds-Cdd-O2d)OsOsH
                            L8: Cs-(Cds-Cdd-Cd)OsOsH
                L5: Cs-CtOsOsH
                L5: Cs-CbOsOsH
            L4: Cs-COsSH
                L5: Cs-CsOsSH
                    L6: Cs-CsOsS2H
                    L6: Cs-CsOsS4H
                L5: Cs-CdsOsSsH
                L5: Cs-CtOsSsH
                L5: Cs-CbOsSsH
            L4: Cs-CCOsSs
                L5: Cs-CsCsOsSs
            L4: Cs-COsOsSs
                L5: Cs-CsOsOsSs
            L4: Cs-CCOsH
                L5: Cs-CsCsOsH
                L5: Cs-CdsCsOsH
                    L6: Cs-(Cds-O2d)CsOsH
                    L6: Cs-(Cds-Cd)CsOsH
                        L7: Cs-(Cds-Cds)CsOsH
                        L7: Cs-(Cds-Cdd)CsOsH
                            L8: Cs-(Cds-Cdd-O2d)CsOsH
                            L8: Cs-(Cds-Cdd-Cd)CsOsH
                L5: Cs-CdsCdsOsH
                    L6: Cs-(Cds-O2d)(Cds-O2d)OsH
                    L6: Cs-(Cds-O2d)(Cds-Cd)OsH
                        L7: Cs-(Cds-O2d)(Cds-Cds)OsH
                        L7: Cs-(Cds-O2d)(Cds-Cdd)OsH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-O2d)OsH
                            L8: Cs-(Cds-O2d)(Cds-Cdd-Cd)OsH
                    L6: Cs-(Cds-Cd)(Cds-Cd)OsH
                        L7: Cs-(Cds-Cds)(Cds-Cds)OsH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)OsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cds)OsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)OsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-O2d)OsH
                            L8: Cs-(Cds-Cdd-O2d)(Cds-Cdd-Cd)OsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH
                L5: Cs-CtCsOsH
                L5: Cs-CtCdsOsH
                    L6: Cs-(Cds-O2d)CtOsH
                    L6: Cs-(Cds-Cd)CtOsH
                        L7: Cs-(Cds-Cds)CtOsH
                        L7: Cs-(Cds-Cdd)CtOsH
                            L8: Cs-(Cds-Cdd-O2d)CtOsH
                            L8: Cs-(Cds-Cdd-Cd)CtOsH
                L5: Cs-CtCtOsH
                L5: Cs-CbCsOsH
                L5: Cs-CbCdsOsH
                    L6: Cs-(Cds-O2d)CbOsH
                    L6: Cs-(Cds-Cd)CbOsH
                        L7: Cs-(Cds-Cds)CbOsH
                        L7: Cs-(Cds-Cdd)CbOsH
                            L8: Cs-(Cds-Cdd-O2d)CbOsH
                            L8: Cs-(Cds-Cdd-Cd)CbOsH
                L5: Cs-CbCtOsH
                L5: Cs-CbCbOsH
            L4: Cs-COsHH
                L5: Cs-CsOsHH
                L5: Cs-CdsOsHH
                    L6: Cs-(Cds-O2d)OsHH
                    L6: Cs-(Cds-Cd)OsHH
                        L7: Cs-(Cds-Cds)OsHH
                        L7: Cs-(Cds-Cdd)OsHH
                            L8: Cs-(Cds-Cdd-O2d)OsHH
                            L8: Cs-(Cds-Cdd-Cd)OsHH
                L5: Cs-CtOsHH
                L5: Cs-CbOsHH
            L4: Cs-CCCS
                L5: Cs-CsCsCsS
                    L6: Cs-CsCsCsS2
                    L6: Cs-CsCsCsS4
                L5: Cs-CdsCsCsSs
                    L6: Cs-(Cds-Cd)CsCsSs
                        L7: Cs-(Cds-Cds)CsCsSs
                        L7: Cs-(Cds-Cdd)CsCsSs
                            L8: Cs-(Cds-Cdd-S2d)CsCsSs
                            L8: Cs-(Cds-Cdd-Cd)CsCsSs
                L5: Cs-SsCtCsCs
                L5: Cs-CbCsCsSs
                L5: Cs-CdsCdsCsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsSs
                L5: Cs-CtCdsCsSs
                    L6: Cs-(Cds-Cd)CtCsSs
                        L7: Cs-(Cds-Cds)CtCsSs
                        L7: Cs-(Cds-Cdd)CtCsSs
                            L8: Cs-(Cds-Cdd-S2d)CtCsSs
                            L8: Cs-(Cds-Cdd-Cd)CtCsSs
                L5: Cs-CbCdsCsSs
                    L6: Cs-(Cds-Cd)CbCsSs
                        L7: Cs-(Cds-Cds)CbCsSs
                        L7: Cs-(Cds-Cdd)CbCsSs
                            L8: Cs-(Cds-Cdd-S2d)CbCsSs
                            L8: Cs-(Cds-Cdd-Cd)CbCsSs
                L5: Cs-CtCtCsSs
                L5: Cs-CbCtCsSs
                L5: Cs-CbCbCsSs
                L5: Cs-CdsCdsCdsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)S2s
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)S2s
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-S2d)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)S2s
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)S2s
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s
                L5: Cs-CtCdsCdsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CtSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CtSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CtSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtSs
                L5: Cs-CbCdsCdsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)CbSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)CbSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)CbSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbSs
                L5: Cs-CtCtCdsSs
                    L6: Cs-(Cds-Cd)CtCtSs
                        L7: Cs-(Cds-Cds)CtCtSs
                        L7: Cs-(Cds-Cdd)CtCtSs
                            L8: Cs-(Cds-Cdd-S2d)CtCtSs
                            L8: Cs-(Cds-Cdd-Cd)CtCtSs
                L5: Cs-CbCtCdsSs
                    L6: Cs-(Cds-Cd)CbCtSs
                        L7: Cs-(Cds-Cds)CbCtSs
                        L7: Cs-(Cds-Cdd)CbCtSs
                            L8: Cs-(Cds-Cdd-S2d)CbCtSs
                            L8: Cs-(Cds-Cdd-Cd)CbCtSs
                L5: Cs-CbCbCdsSs
                    L6: Cs-(Cds-Cd)CbCbSs
                        L7: Cs-(Cds-Cds)CbCbSs
                        L7: Cs-(Cds-Cdd)CbCbSs
                            L8: Cs-(Cds-Cdd-S2d)CbCbSs
                            L8: Cs-(Cds-Cdd-Cd)CbCbSs
                L5: Cs-CtCtCtSs
                L5: Cs-CbCtCtSs
                L5: Cs-CbCbCtSs
                L5: Cs-CbCbCbSs
                L5: Cs-C=SCbCsSs
                L5: Cs-C=SCsCsSs
                L5: Cs-C=S(Cds-Cd)(Cds-Cd)S2s
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cdd)S2s
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)S2s
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-Cd)S2s
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cdd-S2d)S2s
                    L6: Cs-C=S(Cds-Cdd)(Cds-Cds)S2s
                        L7: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)S2s
                        L7: Cs-C=S(Cds-Cdd-S2d)(Cds-Cds)S2s
                    L6: Cs-C=S(Cds-Cds)(Cds-Cds)S2s
                L5: Cs-C=S(Cds-Cd)CtSs
                    L6: Cs-C=S(Cds-Cds)CtSs
                    L6: Cs-C=S(Cds-Cdd)CtSs
                        L7: Cs-C=S(Cds-Cdd-S2d)CtSs
                        L7: Cs-C=S(Cds-Cdd-Cd)CtSs
                L5: Cs-C=SCtCsSs
                L5: Cs-C=SC=SC=SSs
                L5: Cs-C=SC=S(Cds-Cd)S2s
                    L6: Cs-C=SC=S(Cds-Cds)S2s
                    L6: Cs-C=SC=S(Cds-Cdd)S2s
                        L7: Cs-C=SC=S(Cds-Cdd-S2d)S2s
                        L7: Cs-C=SC=S(Cds-Cdd-Cd)S2s
                L5: Cs-C=SCbCbSs
                L5: Cs-C=SC=SCbSs
                L5: Cs-C=SC=SCsSs
                L5: Cs-C=SCtCtSs
                L5: Cs-C=S(Cds-Cd)CbSs
                    L6: Cs-C=S(Cds-Cdd)CbSs
                        L7: Cs-C=S(Cds-Cdd-Cd)CbSs
                        L7: Cs-C=S(Cds-Cdd-S2d)CbSs
                    L6: Cs-C=S(Cds-Cds)CbSs
                L5: Cs-C=SCbCtSs
                L5: Cs-C=SC=SCtSs
                L5: Cs-C=S(Cds-Cd)CsSs
                    L6: Cs-C=S(Cds-Cds)CsSs
                    L6: Cs-C=S(Cds-Cdd)CsSs
                        L7: Cs-C=S(Cds-Cdd-S2d)CsSs
                        L7: Cs-C=S(Cds-Cdd-Cd)CsSs
            L4: Cs-CCSS
                L5: Cs-CsCsSS
                    L6: Cs-CsCsS2S2
                    L6: Cs-CsCsS6S2
                L5: Cs-CdsCsSsSs
                    L6: Cs-(Cds-Cd)CsSsSs
                        L7: Cs-(Cds-Cds)CsSsSs
                        L7: Cs-(Cds-Cdd)CsSsSs
                            L8: Cs-(Cds-Cdd-S2d)CsSsSs
                            L8: Cs-(Cds-Cdd-Cd)CsSsSs
                L5: Cs-CdsCdsSsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)SsSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)SsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)SsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)SsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)SsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)SsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)SsSs
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)SsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsSs
                L5: Cs-CtCsSsSs
                L5: Cs-CtCdsSsSs
                    L6: Cs-(Cds-Cd)CtSsSs
                        L7: Cs-(Cds-Cds)CtSsSs
                        L7: Cs-(Cds-Cdd)CtSsSs
                            L8: Cs-(Cds-Cdd-S2d)CtSsSs
                            L8: Cs-(Cds-Cdd-Cd)CtSsSs
                L5: Cs-CtCtSsSs
                L5: Cs-CbCsSsSs
                L5: Cs-CbCdsSsSs
                    L6: Cs-(Cds-Cd)CbSsSs
                        L7: Cs-(Cds-Cds)CbSsSs
                        L7: Cs-(Cds-Cdd)CbSsSs
                            L8: Cs-(Cds-Cdd-S2d)CbSsSs
                            L8: Cs-(Cds-Cdd-Cd)CbSsSs
                L5: Cs-CbCtSsSs
                L5: Cs-CbCbSsSs
                L5: Cs-C=SCsSsSs
                L5: Cs-C=S(Cds-Cd)SsSs
                    L6: Cs-C=S(Cds-Cdd)SsSs
                        L7: Cs-C=S(Cds-Cdd-Cd)SsSs
                        L7: Cs-C=S(Cds-Cdd-S2d)SsSs
                    L6: Cs-C=S(Cds-Cds)SsSs
                L5: Cs-C=SC=SSsSs
                L5: Cs-C=SCbSsSs
                L5: Cs-C=SCtSsSs
            L4: Cs-CSsSsSs
                L5: Cs-CsSsSsSs
                L5: Cs-CdsSsSsSs
                    L6: Cs-(Cds-Cd)SsSsSs
                        L7: Cs-(Cds-Cds)SsSsSs
                        L7: Cs-(Cds-Cdd)SsSsSs
                            L8: Cs-(Cds-Cdd-S2d)SsSsSs
                            L8: Cs-(Cds-Cdd-Cd)SsSsSs
                L5: Cs-CtSsSsSs
                L5: Cs-CbSsSsSs
                L5: Cs-C=SSsSsSs
            L4: Cs-SsSsSsSs
            L4: Cs-CSSH
                L5: Cs-CsSSH
                    L6: Cs-CsS2S2H
                    L6: Cs-CsS4S2H
                    L6: Cs-CsS6S2H
                L5: Cs-CdsSsSsH
                    L6: Cs-(Cds-Cd)SsSsH
                        L7: Cs-(Cds-Cds)SsSsH
                        L7: Cs-(Cds-Cdd)SsSsH
                            L8: Cs-(Cds-Cdd-S2d)SsSsH
                            L8: Cs-(Cds-Cdd-Cd)SsSsH
                L5: Cs-CtSsSsH
                L5: Cs-CbSsSsH
                L5: Cs-C=SSsSsH
            L4: Cs-CCSH
                L5: Cs-CsCsSH
                    L6: Cs-CsCsS2H
                    L6: Cs-CsCsS4H
                    L6: Cs-CsCsS6H
                L5: Cs-CdsCsSH
                    L6: Cs-CdsCsS4H
                    L6: Cs-(Cds-Cd)CsSsH
                        L7: Cs-(Cds-Cds)CsSsH
                        L7: Cs-(Cds-Cdd)CsSsH
                            L8: Cs-(Cds-Cdd-S2d)CsSsH
                            L8: Cs-(Cds-Cdd-Cd)CsSsH
                L5: Cs-CdsCdsSsH
                    L6: Cs-(Cds-Cd)(Cds-Cd)SsH
                        L7: Cs-(Cds-Cds)(Cds-Cds)SsH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)SsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cds)SsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)SsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)SsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-S2d)SsH
                            L8: Cs-(Cds-Cdd-S2d)(Cds-Cdd-Cd)SsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsH
                L5: Cs-CtCsSsH
                L5: Cs-CtCdsSsH
                    L6: Cs-(Cds-Cd)CtSsH
                        L7: Cs-(Cds-Cds)CtSsH
                        L7: Cs-(Cds-Cdd)CtSsH
                            L8: Cs-(Cds-Cdd-S2d)CtSsH
                            L8: Cs-(Cds-Cdd-Cd)CtSsH
                L5: Cs-CtCtSsH
                L5: Cs-CbCsSsH
                L5: Cs-CbCdsSsH
                    L6: Cs-(Cds-Cd)CbSsH
                        L7: Cs-(Cds-Cds)CbSsH
                        L7: Cs-(Cds-Cdd)CbSsH
                            L8: Cs-(Cds-Cdd-S2d)CbSsH
                            L8: Cs-(Cds-Cdd-Cd)CbSsH
                L5: Cs-CbCtSsH
                L5: Cs-CbCbSsH
                L5: Cs-C=SCbSsH
                L5: Cs-C=SC=SSsH
                L5: Cs-C=SCsSsH
                L5: Cs-C=SCtSsH
                L5: Cs-C=S(Cds-Cd)SsH
                    L6: Cs-C=S(Cds-Cdd)SsH
                        L7: Cs-C=S(Cds-Cdd-Cd)SsH
                        L7: Cs-C=S(Cds-Cdd-S2d)SsH
                    L6: Cs-C=S(Cds-Cds)SsH
            L4: Cs-CSHH
                L5: Cs-CsSHH
                    L6: Cs-CsS2HH
                    L6: Cs-CsS4HH
                    L6: Cs-CsS6HH
                L5: Cs-CdsSsHH
                    L6: Cs-(Cds-Cd)SsHH
                        L7: Cs-(Cds-Cds)SsHH
                        L7: Cs-(Cds-Cdd)SsHH
                            L8: Cs-(Cds-Cdd-S2d)SsHH
                            L8: Cs-(Cds-Cdd-Cd)SsHH
                L5: Cs-CtSsHH
                L5: Cs-CbSsHH
                L5: Cs-C=SSsHH
    L2: O
        L3: Oa(S)
        L3: O2d
            L4: O2d-Cd
            L4: O2d-O2d
            L4: O2d-N3d
            L4: O2d-N5dc
            L4: O2d-Sd
        L3: O2s
            L4: O2s-N
                L5: O2s-CN
                    L6: O2s-CsN3s
                    L6: O2s-CsN3d
                        L7: O2s-Cs(N3dOd)
                    L6: O2s-CdN3d
                        L7: O2s-(Cd-Cd)(N3dOd)
                    L6: O2s-CsN5dc
                        L7: O2s-Cs(N5dcOdOs)
                    L6: O2s-CdN5dc
                        L7: O2s-(Cd-CdHH)(N5dcOdOs)
                L5: O2s-ON
                    L6: O2s-OsN3s
                    L6: O2s-OsN3d
                        L7: O2s-O2s(N3dOd)
                L5: O2s-NN
                    L6: O2s-N3sN3s
                    L6: O2s-N3sN3d
                        L7: O2s-N3s(N3dOd)
            L4: O2s-HH
            L4: O2s-OsH
            L4: O2s-OsOs
            L4: O2s-SsOs
            L4: O2s-CH
                L5: O2s-CtH
                L5: O2s-CdsH
                    L6: O2s-(Cds-O2d)H
                    L6: O2s-(Cds-Cd)H
                L5: O2s-CsH
                L5: O2s-CbH
                L5: O2s-CSH
            L4: O2s-OsC
                L5: O2s-OsCt
                L5: O2s-OsCds
                    L6: O2s-O2s(Cds-O2d)
                    L6: O2s-O2s(Cds-Cd)
                L5: O2s-OsCs
                L5: O2s-OsCb
            L4: O2s-CC
                L5: O2s-CtCt
                L5: O2s-CtCds
                    L6: O2s-Ct(Cds-O2d)
                    L6: O2s-Ct(Cds-Cd)
                L5: O2s-CtCs
                    L6: O2s-Cs(CtN3t)
                L5: O2s-CtCb
                L5: O2s-CdsCds
                    L6: O2s-(Cds-O2d)(Cds-O2d)
                    L6: O2s-(Cds-O2d)(Cds-Cd)
                    L6: O2s-(Cds-Cd)(Cds-Cd)
                L5: O2s-CdsCs
                    L6: O2s-Cs(Cds-O2d)
                    L6: O2s-Cs(Cds-Cd)
                L5: O2s-CdsCb
                    L6: O2s-Cb(Cds-O2d)
                    L6: O2s-Cb(Cds-Cd)
                L5: O2s-CsCs
                L5: O2s-CsCb
                L5: O2s-CbCb
                L5: O2s-Cs(Cds-S2d)
            L4: O2s-CS
                L5: O2s-CS2
                L5: O2s-CS4
                L5: O2s-CS6
            L4: O2s-SH
                L5: O2s-S_nonDeH
                L5: O2s-S_DeH
    L2: Si
        L3: SiJ2(S)
    L2: S
        L3: Sa(S)
        L3: S2d
            L4: S2d-C
            L4: S2d-S
            L4: S2d-O
        L3: S2s
            L4: S2s-HH
            L4: S2s-CH
                L5: S2s-CsH
                L5: S2s-CdH
                L5: S2s-CtH
                L5: S2s-CbH
                L5: S2s-(C=O)H
                L5: S2s-(C=S2d)H
            L4: S2s-SH
                L5: S2s-S2sH
                L5: S2s-S_DeH
            L4: S2s-SS
                L5: S2s-SsSs
            L4: S2s-SO
                L5: S2s-S2O
                L5: S2s-S4O
                L5: S2s-S6O
            L4: S2s-SC
                L5: S2s-S2sC
                    L6: S2s-S2sCs
                    L6: S2s-S2sCd
                    L6: S2s-S2sCt
                    L6: S2s-S2sCb
                L5: S2s-S46C
            L4: S2s-CC
                L5: S2s-CsCs
                L5: S2s-CsCd
                L5: S2s-Cs(C=O)
                L5: S2s-CsCt
                L5: S2s-CsCb
                L5: S2s-CdCd
                L5: S2s-CdCt
                L5: S2s-CdCb
                L5: S2s-CtCt
                L5: S2s-CtCb
                L5: S2s-CbCb
                L5: S2s-(C=S2d)Cs
                L5: S2s-(C=S2d)(C=S2d)
                L5: S2s-(C=S2d)Cmb
            L4: S2s-OH
            L4: S2s-OO
            L4: S2s-OC
                L5: S2s-OCs
        L3: S4dd
            L4: S4dd-OdOd
            L4: S4dd-CdOd
            L4: S4dd-CdCd
            L4: S4dd-OdSd
                L5: S4dd-OdS4d
                L5: S4dd-OdS6d
            L4: S4dd-SdCd
                L5: S4dd-S2dCd
                L5: S4dd-S46dCd
        L3: S4d
            L4: S4d-Od
                L5: S4d-OdHH
                L5: S4d-OdCC
                    L6:S4d-OdCsCs
                    L6:S4d-OdCdCd
                L5: S4d-OdCH
                    L6:S4d-OdCsH
                    L6:S4d-OdCdH
                L5: S4d-OdCS
                L5: S4d-OdCO
                    L6: S4d-OdOsCs
                    L6: S4d-OdOsCd
                L5: S4d-OdOO
                L5: S4d-OdOH
                L5: S4d-OdOS
                L5: S4d-OdSS
                L5: S4d-OdSH
            L4: S4d-Cd
                L5: S4d-CdCC
                L5: S4d-CdCH
                L5: S4d-CdHH
                L5: S4d-CdOC
                L5: S4d-CdOH
            L4: S4d-Sd
                L5: S4d-SdOC
                L5: S4d-SdOH
                L5: S4d-SdCH
                L5: S4d-SdSC
        L3: S4s
            L4: S4s-OCCH
            L4: S4s-CCCH
            L4: S4s-OOCC
            L4: S4s-SOCH
            L4: S4s-SOOH
        L3: S4t
            L4: S4t-CtC
            L4: S4t-CtH
            L4: S4t-CtO
        L3: S6s
            L4: S6s-CCCCCH
            L4: S6s-OCCCCH
            L4: S6s-SOOCCH
        L3: S6d
            L4: S6d-OdOCCH
            L4: S6d-OdCCCH
        L3: S6dd
            L4: S6dd-OdOd
                L5: S6dd-OdOdHH
                L5: S6dd-OdOdCC
                    L6: S6dd-OdOdCsCs
                    L6: S6dd-OdOdCdCd
                L5: S6dd-OdOdCH
                    L6: S6dd-OdOdCsH
                    L6: S6dd-OdOdCdH
                L5: S6dd-OdOdCS
                L5: S6dd-OdOdCO
                    L6: S6dd-OdOdCsH
                    L6: S6dd-OdOdCdH
                L5: S6dd-OdOdOO
                L5: S6dd-OdOdOH
                L5: S6dd-OdOdOS
                L5: S6dd-OdOdSS
                L5: S6dd-OdOdSH
            L4: S6dd-OdCd
                L5: S6dd-OdCdCC
                L5: S6dd-OdCdCH
                L5: S6dd-OdCdOC
                L5: S6dd-OdCdOO
                L5: S6dd-OdCdOH
                L5: S6dd-OdCdSH
                L5: S6dd-OdCdOS
            L4: S6dd-CdCd
                L5: S6dd-CdCdCC
                L5: S6dd-CdCdCH
                L5: S6dd-CdCdOC
            L4: S6dd-OdSd
                L5: S6dd-OdSdOC
                L5: S6dd-OdSdOH
                L5: S6dd-OdSdCH
        L3: S6ddd
            L4: S6ddd-OdOdOd
            L4: S6ddd-OdOdXd
            L4: S6ddd-OdXdXd
        L3: S6t
            L4: S6t-CtCCC
            L4: S6t-CtHHH
            L4: S6t-CtOCC
            L4: S6t-CtOCH
        L3: S6td
            L4: S6td-CtCdC
            L4: S6td-CtOdC
            L4: S6td-CtOdH
    L2: N
        L3: N0sc
        L3: N1s
            L4: N1s-H
            L4: N1s-N1s
            L4: N1s-Cs
            L4: N1s-N3s
            L4: N1s-O2s
        L3: N1dc
        L3: N1sc
        L3: N3s
            L4: N3s-CHH
                L5: N3s-CsHH
                L5: N3s-CbHH
                L5: N3s-(CO)HH
                L5: N3s-CdHH
            L4: N3s-CCH
                L5: N3s-CsCsH
                L5: N3s-CbCsH
                L5: N3s-CbCbH
                L5: N3s-(CO)CsH
                L5: N3s-(CO)CbH
                L5: N3s-(CO)(CO)H
                L5: N3s-(CtN3t)CsH
                L5: N3s-(CdCd)CsH
            L4: N3s-CCC
                L5: N3s-CsCsCs
                L5: N3s-CbCsCs
                L5: N3s-(CO)CsCs
                L5: N3s-(CO)(CO)Cs
                L5: N3s-(CO)(CO)Cb
                L5: N3s-(CtN3t)CsCs
                L5: N3s-(CdCd)CsCs
            L4: N3s-N3sHH
            L4: N3s-N3dHH
            L4: N3s-NCH
                L5: N3s-N3sCsH
                L5: N3s-N3sCbH
                L5: N3s-CsH(N3dOd)
                L5: N3s-CsH(N5dcOdOs)
                L5: N3s-(CdCd)HN3s
            L4: N3s-NCC
                L5: N3s-NCsCs
                    L6: N3s-CsCsN3s
                    L6: N3s-CsCs(N3dOd)
                    L6: N3s-CsCs(N5dcOdOs)
                L5: N3s-NCdCs
                    L6: N3s-(CdCd)CsN3s
            L4: N3s-CsHOs
            L4: N3s-CsCsOs
            L4: N3s-OsHH
        L3: N3d
            L4: N3d-CdH
            L4: N3d-CdN3s
            L4: N3d-N3dH
            L4: N3d-N3dN3s
            L4: N3d-OdOs
            L4: N3d-OdN3s
            L4: N3d-CsR
                L5: N3d-OdC
                L5: N3d-CdCs
                L5: N3d-N3dCs
            L4: N3d-CbR
        L3: N3t
            L4: N3t-CtH
        L3: N5dc
            L4: N5dc-OdOsCs
            L4: N5dc-OdOsCd
            L4: N5dc-OdOsOs
            L4: N5dc-OdOsN3s
        L3: N5ddc
"""
)

