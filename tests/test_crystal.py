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
    assert atom1.has_color == False
    assert atom1.__str__() == \
        "Atom Cs1 Cs Pos /  0  \ \n" \
        "               |   0   |\n" \
        "                \  0  / "
    assert (atom1 + "hallo").name == atom1.name + "hallo"
    atom2 = cr.Atom("Cs2", "Cs", fs("p 0 0 0"))
    assert atom2 == atom1
    assert hash(atom2) == hash(atom1)
    assert {atom2} == {atom1}
    atom3 = cr.Atom("Cs3", "Cs", fs("p0.1 0 0"))
    assert atom3 != atom1
    atom4 = cr.Atom("Cs1", "Fe", fs("p 0 0 0"))
    assert atom4 != atom1

    atom = cr.Atom("Cl1", "Cl", fs("p 1/2 1/2 1/2"))
    transformation = fs("O->(0,0,0) \n"
                        "then\n"
                        "a' = a \n"
                        "b' = 2b \n"
                        "c' = c")
    atom_trans = cr.Atom("Cl1", "Cl", fs("p 1/2 1/4 1/2"))
    assert (transformation ** atom).__str__() == atom_trans.__str__()

    sym = fs("-x+1/2,-y+1/2, z")
    atom_sym = cr.Atom("Cl1", "Cl", fs("p0 0 1/2"))
    assert (sym ** atom).__str__() == atom_sym.__str__()

    coset = fs("{x, -y, z+1}")
    atom = cr.Atom("Cl1", "Cl", fs("p 1/2 1/4 1/2"))
    atom1 = coset ** atom
    atom2 = cr.Atom("Cl1", "Cl", fs("p 1/2 3/4 1/2"))
    assert atom1.__str__() == atom2.__str__()

    transgen = geo.Transgen(fs("d 1 0 0"),
                            fs("d 0 1 0"),
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
    m = cr.Momentum("M", fs("p 0 0 0"), fs("d 0 0 1"))
    assert isinstance(m, cr.Momentum)
    m.set_color((0, 0, 1))
    m.set_color((fs("0.3"), 0.1, 1))
    m.set_plotlength(1)
    m.set_plotlength(0.5)
    m.set_plotlength(fs("1/2"))
    d = fs("d 0 0 1/2")
    m1 = cr.Momentum("M", fs("p 0 0 0"), fs("d 0 0 1"))
    m2 = cr.Momentum("M", fs("p 1 2 3"), fs("d 0 0 1"))
    m3 = cr.Momentum("M", fs("p 0 0 0"), fs("d 1 2 3"))
    assert m == m1
    assert (m == m2) == False
    assert (m == m3) == False
    assert m + d == cr.Momentum("M", fs("p 0 0 1/2"), fs("d 0 0 1"))
    assert fs("x+1/2,y,z") ** m == cr.Momentum("M", fs("p 1/2 0 0"), fs("d 0 0 1"))
    assert fs("{x+3/2,y,z}") ** m == cr.Momentum("M", fs("p 1/2 0 0"), fs("d 0 0 1"))
    m1 = cr.Momentum("M", fs("p 0 0 1/2"), fs("d 0 0 1"))
    assert (m1 + "test").name == "Mtest"


def test_Bond():
    b = cr.Bond("B", fs("p 0 0 0"), fs("p 0 0 1/2"))
    assert isinstance(b, cr.Bond)
    b.set_color((0, 0, 1))
    b.set_color((fs("0.3"), 0.1, 1))
    b.set_thickness(1)
    b.set_thickness(0.5)
    b.set_thickness(fs("1/2"))
    d = fs("d 0 0 1/2")
    b1 = cr.Bond("Bblabla", fs("p 0 0 0"), fs("p 0 0 1/2"))
    b2 = cr.Bond("B", fs("p 1 2 3"), fs("p 0 0 1/2"))
    b3 = cr.Bond("B", fs("p 0 0 0"), fs("p 1 2 3"))
    assert b == b1
    assert (b == b2) == False
    assert (b == b3) == False
    assert b + d == cr.Bond("B", fs("p 0 0 1/2"), fs("p 0 0 1"))
    assert fs("x+1/2,y,z") ** b == cr.Bond("B", fs("p 1/2 0 0"), fs("p 1/2 0 1/2"))
    assert fs("{x+3/2,y,z}") ** b == cr.Bond("B", fs("p 1/2 0 0"), fs("p 1/2 0 1/2"))
    b = cr.Bond("B", fs("p 0 0 0"), fs("p 0 0 1/2"))
    assert (b + "test").name == "Btest"


def test_Face():
    f = cr.Face("F", [fs("p 0 0 0"), fs("p 1 0 0"), fs("p 0 1 0")])
    assert isinstance(f, cr.Face)
    f.set_color((0, 0, 1))
    f.set_color((fs("0.3"), 0.1, 1))
    f.set_opacity(0.5)
    d = fs("d 0 0 1/2")
    f1 = cr.Face("Fblabla", [fs("p 0 0 0"), fs("p 1 0 0"), fs("p 0 1 0")])
    f2 = cr.Face("F", [fs("p 0 0 0"), fs("p 0.7 0 0"), fs("p 0 1 0")])
    f3 = cr.Face("F", [fs("p 0 0 0"), fs("p 1 0 0"), fs("p 0 2 0")])
    assert f == f1
    assert (f == f2) == False
    assert (f == f3) == False
    assert f + d == cr.Face("F", [fs("p 0 0 1/2"), fs("p 1 0 1/2"), fs("p 0 1 1/2")])
    assert fs("x+1/2,y,z") ** f == cr.Face("F", [fs("p 1/2 0 0"), fs("p 3/2 0 0"), fs("p 1/2 1 0")])
    assert fs("{x+3/2,y,z}") ** f == cr.Face("F", [fs("p 1/2 0 0"), fs("p 1/2 0 0"), fs("p 1/2 0 0")])
    f = cr.Face("F", [fs("p 0 0 0"), fs("p 1 0 0"), fs("p 0 1 0")])
    assert (f + "test").name == "Ftest"

def test_Atomset():
    atom1 = cr.Atom("Cs1", "Cs", fs("p 0 0 0"))
    atom2 = cr.Atom("Cs2", "Cs", fs("p 1/4 1/4 0"))
    momentum = cr.Momentum("M", fs("p 0 0 0"), fs("d 0 0 1"))
    bond = cr.Bond("B", fs("p 0 0 0"), fs("p 1/2 1/2 1/2"))
    face = cr.Face("F", [fs("p 0 0 0"), fs("p 1 0 0"), fs("p 0 1 0")])
    atomset = cr.Atomset({atom1, atom2, momentum, bond, face})
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
        "                         Momentum\n" \
        "                             Bond\n" \
        "                             Face"

    transformation = fs("O->(0,0,1/4) \n"
                        "then\n"
                        "a' = a+b \n"
                        "b' = b   \n"
                        "c' = c")
    atomset1 = transformation**atomset
    atomset2 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 -1/4")), \
                           cr.Atom("Cs2", "Cs", fs("p 1/4 0 -1/4")), \
                           cr.Momentum("M", fs("p 0 0 -1/4"), fs("d 0 0 1")), \
                           cr.Bond("B", fs("p 0 0 -1/4"), fs("p 1/2 0 1/4")), \
                           cr.Face("F", [fs("p 0 0 -1/4"), fs("p 1 -1 -1/4"), fs("p 0 1 -1/4")])})
    assert (transformation ** bond) == cr.Bond("B", fs("p 0 0 -1/4"), fs("p 1/2 0 1/4"))
    assert (transformation ** face) == cr.Face("F", [fs("p 0 0 -1/4"), fs("p 1 -1 -1/4"), fs("p 0 1 -1/4")])
    assert atomset1 == atomset2

    spacegroup = geo.Spacegroup(geo.canonical, [fs("{x, y, z}"),
                                                fs("{-x, -y, -z}")])

    atomset1 = spacegroup ** atomset
    atomset2 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 0")), \
                           cr.Atom("Cs2", "Cs", fs("p 1/4 1/4 0")), \
                           cr.Atom("Cs2_1", "Cs", fs("p 3/4 3/4 0")), \
                           momentum, \
                           bond, \
                           cr.Face("F", [fs("p 0 0 0"), fs("p 0 0 0"), fs("p 0 0 0")])})
    assert atomset1 == atomset2
    assert atomset1.names == atomset2.names

    atomset1 = spacegroup ** (atomset + "_1")
    atomset2 = cr.Atomset({cr.Atom("Cs1_1", "Cs", fs("p 0 0 0")), \
                           cr.Atom("Cs2_1", "Cs", fs("p 1/4 1/4 0")), \
                           cr.Atom("Cs2_2", "Cs", fs("p 3/4 3/4 0")), \
                           momentum, \
                           bond, \
                           cr.Face("F", [fs("p 0 0 0"), fs("p 0 0 0"), fs("p 0 0 0")])})
    assert atomset1 == atomset2
    assert atomset1.names == atomset2.names


    atomset = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 -1/4")),
                          cr.Atom("Cs2", "Cs", fs("p 1/4 0 -1/4"))})
    atomset1 = atomset % geo.canonical
    atomset2 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 3/4")),
                          cr.Atom("Cs2", "Cs", fs("p 1/4 0 3/4"))})

    assert atomset1 == atomset2

    atomset1 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 0"))})
    atomset2 = cr.Atomset({cr.Atom("Cu1", "Cu", fs("p 1/2 1/2 1/2"))})
    atomset3 = atomset1 + atomset2
    atomset4 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 0")),
                           cr.Atom("Cu1", "Cu", fs("p 1/2 1/2 1/2"))})
    assert atomset3 == atomset4

    d = fs("d 1/2 0 0")
    atomset5 = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 1/2 0 0"))})
    atomset6 = atomset1 + d
    atomset7 = d + atomset1
    assert atomset5 == atomset6
    assert atomset5 == atomset7

    atomset = cr.Atomset({cr.Atom("Cs1", "Cs", fs("p 0 0 -1/4")),
                          cr.Atom("Cs2", "Cs", fs("p 1/4 0 -1/4"))})
    assert atomset.nextname("Cs1") == "Cs1_1"
    assert atomset.nextname("Cs3") == "Cs3"

    atomset = cr.Atomset({cr.Atom("Cs_1", "Cs", fs("p 0 0 -1/4")),
                          cr.Atom("Ar_1", "Cs", fs("p 1/4 0 -1/4")),
                          cr.Atom("Ar_2", "Ar", fs("p 0 1/2 0"))})
    assert atomset.nextname("Cs_1") == "Cs_2"
    assert atomset.nextname("Ar_2") == "Ar_3"
    assert atomset.nextname("Ar_1") == "Ar_3"

    atomset = cr.Atomset({cr.Subset("S_1", fs("p 0 0 0"), {
                                        cr.Atom("Fe1", "Fe", fs("p -0.1 0 0")),
                                        cr.Atom("Fe2", "Fe", fs("p  0.1 0 0"))
                                    }
                          )
    })
    sg = geo.Spacegroup(geo.canonical, [fs("{x, y, z}"), fs("{x, -y+1/2, z}")])
    assert sg.is_really_a_spacegroup()
    atomset1 = cr.Atomset({cr.Subset("S_1", fs("p 0 0 0"), {
                                        cr.Atom("Fe1", "Fe", fs("p -0.1 0 0")),
                                        cr.Atom("Fe2", "Fe", fs("p  0.1 0 0"))
                                    }
                          ),
                           cr.Subset("S_2", fs("p 0 1/2 0"), {
                                        cr.Atom("Fe1", "Fe", fs("p -0.1 1/2 0")),
                                        cr.Atom("Fe2", "Fe", fs("p  0.1 1/2 0"))
                                    }
                          )

    })
    
    assert sg ** atomset == atomset1
    
    atomset_unpacked = cr.Atomset({
        cr.Atom("S_1:Fe1", "Fe", fs("p -0.1  0  0")),
        cr.Atom("S_1:Fe2", "Fe", fs("p  0.1  0  0")),
        cr.Atom("S_2:Fe1", "Fe", fs("p -0.1 1/2 0")),
        cr.Atom("S_2:Fe2", "Fe", fs("p  0.1 1/2 0"))
    })
    for subset in (sg ** atomset).menge:
        print(subset.name)
    assert (sg ** atomset).unpack_subsets() == atomset_unpacked
    assert (sg ** atomset).names \
        == atomset1.names
    assert ((sg ** atomset).unpack_subsets()).names \
        == atomset_unpacked.names
   
def test_Subset():
    a1 = cr.Atom("Fe1", "Fe", fs("p 0 0 0"))
    a2 = cr.Atom("Fe2", "Fe", fs("p 0 0 1/4"))
    subset = cr.Subset("Sub", fs("p 0 0 1/8"), {a1, a2})
    subset1 = cr.Subset("Sub1", fs("p 0 0 1/8"), {a1, a2})
    subset2 = cr.Subset("Sub", fs("p 0 0 0"), {a1, a2})
    subset3 = cr.Subset("Sub", fs("p 0 0 1/8"), {a1})
    assert subset == subset1
    assert (subset == subset2) == False
    assert (subset == subset3) == False
    assert str(subset) == "Subset"
    subset4 = cr.Subset("Sub", fs("p 7/8 0 1/8"),
                        {cr.Atom("Fe1", "Fe", fs("p 7/8 0 0")), 
                         cr.Atom("Fe2", "Fe", fs("p 7/8 0 1/4"))})
    assert fs("x+7/8, y, z") ** subset == subset4
    assert fs("{x-1/8, y, z}") ** subset == subset4
    subset5 = cr.Subset("Sub", fs("p 1/2 0 1/8"),
                        {cr.Atom("Fe1", "Fe", fs("p 1/2 0 0")), 
                         cr.Atom("Fe2", "Fe", fs("p 1/2 0 1/4"))})
    assert subset + fs("d 1/2 0 0") == subset5
    


def test_structurefactor():
    asyunit = cr.Atomset({cr.Atom("Ca1", "Ca", fs("p 0     0     0")),
                          cr.Atom("Mn1", "Mn", fs("p 1/2   0     0")),
                          cr.Atom("Mn2", "Mn", fs("p 1/2   0     0")),
                          cr.Atom("Mn3", "Mn", fs("p 0     0     1/2")),
                          cr.Atom("O1",  "O",  fs("p 0.223 0.274 0.081")),
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

    cell = cr.Atomset({cr.Atom("Au1", "Au", fs("p 0   0   0  ")),
                       cr.Atom("Cu1", "Cu", fs("p 0   1/2 1/2")),
                       cr.Atom("Cu2", "Cu", fs("p 1/2 0   1/2")),
                       cr.Atom("Cu3", "Cu", fs("p 1/2 1/2 0  "))})
    cellparameters = geo.Cellparameters(3.71, 3.71, 3.71, 90, 90, 90)
    metric = cellparameters.to_Metric()
    q = fs("q 1 0 0")
    sintl = 0.5 * metric.length(q)
