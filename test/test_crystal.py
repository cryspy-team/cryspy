import pytest
import sys
sys.path.append("../src/")
import geo as geo
from fromstr import fromstr as fs
import crystal as cr

def test_Atom():
    atom1 = cr.Atom("Cs1", "Cs", fs("p 0 0 0"))
    assert atom1.__str__() == \
    "Atom Cs1 Cs Pos /  0  \ \n" \
    "               |   0   |\n" \
    "                \  0  / "

    atom2 = cr.Atom("Cs2", "Cs", fs("p 0 0 0"))
    assert atom2 == atom1
    atom3 = cr.Atom("Cs3", "Cs", fs("p0.1 0 0"))
    assert atom3 != atom1
    atom4 = cr.Atom("Cs1", "Fe", fs("p 0 0 0"))
    assert atom4 != atom1

    atom = cr.Atom("Cl1", "Cl", fs("p 1/2 1/2 1/2"))
    transformation = fs("O->(0,0,0) \n" \
                        "then\n" \
                        "a' = a \n" \
                        "b' = 2b \n" \
                        "c' = c")
    atom_trans = cr.Atom("Cl1", "Cl", fs("p 1/2 1/4 1/2"))
    assert (transformation**atom).__str__() == atom_trans.__str__()

    sym = fs("-x+1/2,-y+1/2, z")
    atom_sym = cr.Atom("Cl1", "Cl", fs("p0 0 1/2"))
    assert (sym**atom).__str__() == atom_sym.__str__()

    coset = fs("{x, -y, z+1}")
    atom = cr.Atom("Cl1", "Cl", fs("p 1/2 1/4 1/2"))
    atom1 = coset ** atom
    atom2 = cr.Atom("Cl1", "Cl", fs("p 1/2 3/4 1/2"))
    assert atom1.__str__() == atom2.__str__()


    transgen = geo.Transgen(fs("d 1 0 0"), \
                            fs("d 0 1 0"), \
                            fs("d 0 0 2"))
    atom = cr.Atom("Cl1", "Cl", fs("p 1/2 5/4 -1/2"))
    atom1 = atom % transgen
    atom2 = cr.Atom("Cl1", "Cl", fs("p 1/2 1/4 3/2"))
    assert atom1 == atom2


def test_Atomset():
    atom1 = cr.Atom("Cs1", "Cs", fs("p 0 0 0"))
    atom2 = cr.Atom("Cs2", "Cs", fs("p 1/4 1/4 0"))
    atomset = cr.Atomset({atom1, atom2})
    assert atomset.__str__() == \
        "Atomset                          \n" \
        "-------                          \n" \
        "         Atom Cs1 Cs Pos /  0  \ \n" \
        "                        |   0   |\n" \
        "                         \  0  / \n" \
        "                                 \n" \
        "       Atom Cs2 Cs Pos /  1/4  \ \n" \
        "                      |   1/4   |\n" \
        "                       \    0  / \n" \
        "                                 "

    transformation = fs("O->(0,0,1/4) \n" \
                        "then\n" \
                        "a' = a+b \n" \
                        "b' = b   \n" \
                        "c' = c")
    atomset1 = transformation**atomset
    atomset2 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 -1/4")), \
                           cr.Atom("Cs2", "Cs", fs("p 1/4 0 -1/4"))})
    assert atomset1 == atomset2

    spacegroup = geo.Spacegroup(geo.canonical, [fs("{x, y, z}"), \
                                                fs("{-x, -y, -z}")])
    atomset1 = spacegroup ** atomset
    atomset2 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 0")), \
                           cr.Atom("Cs2", "Cs", fs("p 1/4 1/4 0")), \
                           cr.Atom("Cs2", "Cs", fs("p 3/4 3/4 0"))})
    assert atomset1 == atomset2

    
    atomset = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 -1/4")), \
                          cr.Atom("Cs2", "Cs", fs("p 1/4 0 -1/4"))})
    atomset1 = atomset % geo.canonical
    atomset2 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 3/4")), \
                          cr.Atom("Cs2", "Cs", fs("p 1/4 0 3/4"))})
