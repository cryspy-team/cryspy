import pytest
import sys
sys.path.append("../src/")
import numpy as np
import test_numbers_Mixed
from cryspy import geo as geo
from cryspy.fromstr import fromstr as fs
from cryspy import crystal as cr
from cryspy import tables

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

    d = fs("d 1/2 0 0")
    atom1 = cr.Atom("Cl1", "Cl", fs("p 0 0 0"))
    atom2 = cr.Atom("Cl1", "Cl", fs("p 1/2 0 0"))
    atom3 = atom1 + d
    assert atom2 == atom3

def test_Momentum():
    m = cr.Momentum(fs("p 0 0 0"), fs("d 0 0 1"))
    assert isinstance(m, cr.Momentum)
    m.set_color((0, 0, 1))
    m.set_color((fs("0.3"), 0.1, 1))
    m.set_plotlength(1)
    m.set_plotlength(0.5)
    m.set_plotlength(fs("1/2"))
    d = fs("d 0 0 1/2")
    m1 = cr.Momentum(fs("p 0 0 0"), fs("d 0 0 1"))
    m2 = cr.Momentum(fs("p 1 2 3"), fs("d 0 0 1"))
    m3 = cr.Momentum(fs("p 0 0 0"), fs("d 1 2 3"))
    assert m == m1
    assert (m == m2) == False
    assert (m == m3) == False
    assert m + d == cr.Momentum(fs("p 0 0 1/2"), fs("d 0 0 1"))
    assert fs("x+1/2,y,z") ** m == cr.Momentum(fs("p 1/2 0 0"), fs("d 0 0 1"))
    assert fs("{x+3/2,y,z}") ** m == cr.Momentum(fs("p 1/2 0 0"), fs("d 0 0 1"))

def test_Atomset():
    atom1 = cr.Atom("Cs1", "Cs", fs("p 0 0 0"))
    atom2 = cr.Atom("Cs2", "Cs", fs("p 1/4 1/4 0"))
    momentum = cr.Momentum(fs("p 0 0 0"), fs("d 0 0 1"))
    atomset = cr.Atomset({atom1, atom2, momentum})
    print(atomset)
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
        "                                 \n" \
        "                         Momentum"

    transformation = fs("O->(0,0,1/4) \n" \
                        "then\n" \
                        "a' = a+b \n" \
                        "b' = b   \n" \
                        "c' = c")
    atomset1 = transformation**atomset
    atomset2 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 -1/4")), \
                           cr.Atom("Cs2", "Cs", fs("p 1/4 0 -1/4")), \
                           cr.Momentum(fs("p 0 0 -1/4"), fs("d 0 0 1"))})
    assert atomset1 == atomset2

    spacegroup = geo.Spacegroup(geo.canonical, [fs("{x, y, z}"), \
                                                fs("{-x, -y, -z}")])
    atomset1 = spacegroup ** atomset
    atomset2 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 0")), \
                           cr.Atom("Cs2", "Cs", fs("p 1/4 1/4 0")), \
                           cr.Atom("Cs2", "Cs", fs("p 3/4 3/4 0")), \
                           momentum})
    assert atomset1 == atomset2

    
    atomset = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 -1/4")), \
                          cr.Atom("Cs2", "Cs", fs("p 1/4 0 -1/4"))})
    atomset1 = atomset % geo.canonical
    atomset2 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 3/4")), \
                          cr.Atom("Cs2", "Cs", fs("p 1/4 0 3/4"))})

    assert atomset1 == atomset2

    atomset1 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 0"))})
    atomset2 = cr.Atomset({cr.Atom("Cu1", "Cu", fs("p 1/2 1/2 1/2"))})
    atomset3 = atomset1 + atomset2
    atomset4 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 0")), \
                           cr.Atom("Cu1", "Cu", fs("p 1/2 1/2 1/2"))})
    assert atomset3 == atomset4

    d = fs("d 1/2 0 0")
    atomset5 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 1/2 0 0"))})
    atomset6 = atomset1 + d
    atomset7 = d + atomset1
    assert atomset5 == atomset6
    assert atomset5 == atomset7
    



def test_structurefactor():
    asyunit = cr.Atomset({cr.Atom("Ca1", "Ca", fs("p 0     0     0")), \
                          cr.Atom("Mn1", "Mn", fs("p 1/2   0     0")), \
                          cr.Atom("Mn2", "Mn", fs("p 1/2   0     0")), \
                          cr.Atom("Mn3", "Mn", fs("p 0     0     1/2")), \
                          cr.Atom("O1",  "O",  fs("p 0.223 0.274 0.081")), \
                          cr.Atom("O2",  "O",  fs("p 0.342 0.522 0.341"))})
    sg = tables.spacegroup(148)
    cell = sg ** asyunit
    cellparameters = geo.Cellparameters(10.46, 10.46, 6.35, 90, 90, 120)
    metric = cellparameters.to_Metric()
    q = fs("q 3 0 0")
    wavelength = 0.71073
    F = cr.structurefactor(cell, metric, q, wavelength)
#    assert test_numbers_Mixed.approx(-6.540191224, F.real)
#    assert test_numbers_Mixed.approx(0.0, F.imag)

    cell = cr.Atomset({cr.Atom("Au1", "Au", fs("p 0   0   0  ")), \
                       cr.Atom("Cu1", "Cu", fs("p 0   1/2 1/2")), \
                       cr.Atom("Cu2", "Cu", fs("p 1/2 0   1/2")), \
                       cr.Atom("Cu3", "Cu", fs("p 1/2 1/2 0  "))})
    cellparameters = geo.Cellparameters(3.71, 3.71, 3.71, 90, 90, 90)
    metric = cellparameters.to_Metric()
    q = fs("q 1 0 0")
    sintl = 0.5 * metric.length(q)


