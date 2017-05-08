from rmgpy.molecule.molecule import Molecule
from rmgpy.molecule.group import Group
from rmgpy.molecule.atomtype import getAtomType

test1 = Group().fromAdjacencyList("""
1 * S2s u1 {2,S}
2   H   u0 {1,S}
""")

test2 = test1.makeSampleMolecule()

print test2.toAdjacencyList()
print getAtomType(test2.atoms[1],test2.atoms[1].bonds)
