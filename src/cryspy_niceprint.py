# This is a collection of different formatted prints.
# This must not be tested, but it must not be used in other
# modules.

from cryspy_fromstr import fromstr as fs
import blockprint as bp
import cryspy_numbers as nb
import cryspy_geo as geo
import cryspy_crystal as cr

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
       

