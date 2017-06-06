import sys
sys.path.append("../src")
from cryspy.fromstr import fromstr as fs
import cryspy.geo as geo
import cryspy.crystal as cr
import cryspy.niceprint


def test_print_atomtable():
    atomset = \
        cr.Atomset({cr.Atom("Dy1", "Dy", fs("p 0.982(0)    0.082(0)  1/4        ")),
                cr.Atom("Mn1", "Mn", fs("p 1/2         0         0          ")),
                cr.Atom("O1", "O", fs("p 0.108(2)    0.471(2)  1/4        ")),
                cr.Atom("O2", "O", fs("p 0.707(1)    0.328(1)  0.052(1)   "))})

    liste = ["Dy1", "Mn1", "O1", "O2"]
    assert cryspy.niceprint.atomtable(liste, atomset) == \
        "  name  type          x           y           z \n" \
        "  ----  ----         ---         ---         ---\n" \
        "   Dy1    Dy    0.982(0)    0.082(0)         1/4\n" \
        "   Mn1    Mn         1/2           0           0\n" \
        "    O1     O  0.1080(20)  0.4710(20)         1/4\n" \
        "    O2     O  0.7070(10)  0.3280(10)  0.0520(10)"


def test_print_cif():
    atomset = \
        cr.Atomset({cr.Atom("Dy1", "Dy", fs("p 0.982(0)    0.082(0)  1/4        ")),
                cr.Atom("Mn1", "Mn", fs("p 1/2         0         0          ")),
                cr.Atom("O1", "O", fs("p 0.108(2)    0.471(2)  1/4        ")),
                cr.Atom("O2", "O", fs("p 0.707(1)    0.328(1)  0.052(1)   "))})

    sg = geo.Spacegroup(geo.canonical, [fs("{x,y,z}"), fs("{-x,-y,-z}")])
    liste = ["Dy1", "Dy1_1", "Mn1", "O1", "O1_1", "O2", "O2_1"]

    atomset_all = (sg ** atomset) % geo.canonical
    metric = geo.Cellparameters(5.0, 5.0, 5.0, 90, 90, 90).to_Metric()
    print(cryspy.niceprint.print_cif_without_symmetries(liste, atomset_all, metric))
    assert cryspy.niceprint.print_cif_without_symmetries(liste, atomset_all, metric) == \
    "data_global _chemical_name 'noname' \n" \
    "_cell_length_a 5.0\n" \
    "_cell_length_b 5.0\n" \
    "_cell_length_c 5.0\n" \
    "_cell_angle_alpha 90\n" \
    "_cell_angle_beta 90\n" \
    "_cell_angle_gamma 90\n" \
    "_symmetry_space_group_name_H-M 'P 1'\n" \
    "loop_ \n" \
    " _atom_site_label \n" \
    " _atom_site_type_symbol \n" \
    " _atom_site_fract_x \n" \
    " _atom_site_fract_y \n" \
    " _atom_site_fract_z \n" \
    "  Dy1_1 Dy 0.982000 0.082000 0.250000\n" \
    "  Dy1_1_1 Dy 0.018000 0.918000 0.750000\n" \
    "  Mn1_1 Mn 0.500000 0.000000 0.000000\n" \
    "  O1_1 O 0.108000 0.471000 0.250000\n" \
    "  O1_1_1 O 0.892000 0.529000 0.750000\n" \
    "  O2_1 O 0.707000 0.328000 0.052000\n" \
    "  O2_1_1 O 0.293000 0.672000 0.948000\n"
