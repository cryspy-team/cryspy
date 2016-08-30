# This is a collection of different formatted prints.
# This must not be tested, but it must not be used in other
# modules.

from fromstr import fromstr as fs
import blockprint as bp
import cryspy_numbers as nb
import geo as geo
import crystal as cr

def atomtable(liste, atomset):
    assert isinstance(liste, list), \
        "First Argument must be of type list."
    for atomname in liste:
        assert isinstance(atomname, str), \
            "First Argument must be a list " \
            "of str."
    assert isinstance(atomset, cr.Atomset), \
        "Second argument must by of type Atomset."

    for atom in atomset.menge:
        assert (atom.name in liste), \
            "The list does not contain an atom " \
            "named %s ."%atom.name

    stringliste = [["  name", "  type", "   x ", "   y ", "   z "], \
                   ["  ----", "  ----", "  ---", "  ---", "  ---"]]
    for atomname in liste:
        how_often = 0
        for atom in atomset.menge:
            if (atom.name == atomname):
                how_often += 1
                stringliste.append( \
                    ["  " + atom.name, \
                     "  " + atom.typ, \
                     "  " + atom.pos.x().__str__(), \
                     "  " + atom.pos.y().__str__(), \
                     "  " + atom.pos.z().__str__()])
        assert (how_often == 1), \
            "There are %i atoms named "\
            "%s in the atomset" \
            %(how_often, atomname)
    string = bp.block(stringliste)
    return string
       

def atomtable_equalnames(liste, atomset):
    assert isinstance(liste, list), \
        "First Argument must be of type list."
    for atomname in liste:
        assert isinstance(atomname, str), \
            "First Argument must be a list " \
            "of str."
    assert isinstance(atomset, cr.Atomset), \
        "Second argument must by of type Atomset."

    for atom in atomset.menge:
        assert (atom.name in liste), \
            "The list does not contain an atom " \
            "named %s ."%atom.name

    stringliste = [["  name", "  type", "   x ", "   y ", "   z "], \
                   ["  ----", "  ----", "  ---", "  ---", "  ---"]]
    for atomname in liste:
        how_often = 0
        for atom in atomset.menge:
            if (atom.name == atomname):
                how_often += 1
                stringliste.append( \
                    ["  " + atom.name, \
                     "  " + atom.typ, \
                     "  " + atom.pos.x().__str__(), \
                     "  " + atom.pos.y().__str__(), \
                     "  " + atom.pos.z().__str__()])
#        assert (how_often == 1), \
#            "There are %i atoms named "\
#            "%s in the atomset" \
#            %(how_often, atomname)
    string = bp.block(stringliste)
    return string


def print_cif_without_symmetries(liste, atomset, metric):
    assert isinstance(liste, list), \
        "First Argument must be of type list."
    for atomname in liste:
        assert isinstance(atomname, str), \
            "First Argument must be a list " \
            "of str."
    assert isinstance(atomset, cr.Atomset), \
        "Second argument must by of type Atomset."

    for atom in atomset.menge:
        assert (atom.name in liste), \
            "The list does not contain an atom " \
            "named %s ."%atom.name

    cell = metric.to_Cellparameters()
    string = "data_global _chemical_name 'noname' \n"
    string += "_cell_length_a " + cell.a.__str__() + "\n"
    string += "_cell_length_b " + cell.b.__str__() + "\n"
    string += "_cell_length_c " + cell.c.__str__() + "\n"
    string += "_cell_angle_alpha " + cell.alpha.__str__() + "\n"
    string += "_cell_angle_beta " + cell.beta.__str__() + "\n"
    string += "_cell_angle_gamma " + cell.gamma.__str__() + "\n"
    string += "_symmetry_space_group_name_H-M 'P 1'"
    string += "\n"
    string += "loop_ \n" \
             " _atom_site_label \n" \
             " _atom_site_type_symbol \n" \
             " _atom_site_fract_x \n" \
             " _atom_site_fract_y \n" \
             " _atom_site_fract_z \n"
    for atomname in liste:
        how_often = 0
        for atom in atomset.menge:
            if (atom.name == atomname):
                how_often += 1
                atomname_extended = "%s_%i"%(atomname, how_often)
                string += "  " + atomname_extended
                string += " " + atom.typ
                string += " %f"%(float(atom.pos.x()))
                string += " %f"%(float(atom.pos.y()))
                string += " %f"%(float(atom.pos.z()))
                string += "\n"

    return string
