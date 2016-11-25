import hashlib
import numpy as np
from cryspy import numbers as nb
from cryspy import geo as geo
from cryspy import blockprint as bp
from cryspy import tables

class Atom():
    def __init__(self, name, typ, pos):
        assert isinstance(name, str), \
            "First argument must be of type str."
        assert isinstance(typ, str), \
            "Second argument must be of type str."
        assert isinstance(pos, geo.Pos), \
            "Third argument must be of type Pos."
        self.name = name
        self.typ = typ
        self.pos = pos
    
    def __str__(self):
        return "# Atom\n" \
               "# ====\n" \
               "_atom_site_label\n" \
               "_atom_site_type_symbol\n" \
               "_atom_site_fract_x\n" \
               "_atom_site_fract_y\n" \
               "_atom_site_fract_z\n" + \
               self.name + " " \
               + self.typ + "  " \
               + self.pos.x().__str__()  + "  " \
               + self.pos.y().__str__() + "  " \
               + self.pos.z().__str__()

    def __eq__(self, right):
        if (self.typ == right.typ) and (self.pos == right.pos):
            return True
        else:
            return False

    def __add__(self, right):
        if isinstance(right, geo.Dif):
            return Atom(self.name, self.typ, self.pos + right)
        else:
            return NotImplemented

    def __rpow__(self, left):
        assert isinstance(left, geo.Operator) \
            or isinstance(left, geo.Coset), \
            "I cannot apply an object of type %s " \
            "to an object of type Atom."%(type(left))
        return Atom(self.name, self.typ, left ** self.pos)

    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "I cannot take an object of type Atom " \
            "modulo an object of type %s"%(type(right))
        return Atom(self.name, self.typ, self.pos % right)

    def __hash__(self):
        return int(hashlib.sha1(self.__str__().encode()).hexdigest(), 16)


class Atomset():
    def __init__(self, menge):
        assert isinstance(menge, set), \
            "Argument must be of type set."
        for item in menge:
            assert isinstance(item, Atom), \
                "Argument must be a set of "\
                "objects of type Atom"
        self.menge = menge


    def __eq__(self, right):
        if isinstance(right, Atomset):
            return (self.menge == right.menge)
        else:
            return False

    def __str__(self):
        string = "# Atomset\n" \
                 "# =======\n" \
                 "loop_\n" \
                 " _atom_site_label\n" \
                 " _atom_site_type_symbol\n" \
                 " _atom_type_fract_x\n" \
                 " _atom_type_fract_y\n" \
                 " _atom_type_fract_z"
        lines = []
        for atom in self.menge:
            lines.append( \
                atom.name + " " + \
                atom.typ + "  " + \
                atom.pos.x().__str__() + "  " + \
                atom.pos.y().__str__() + "  " + \
                atom.pos.z().__str__()
            )
        lines = sorted(lines)
        for line in lines:
            string += "\n" + line
        return string
    def __add__(self, right):
        if isinstance(right, geo.Dif):
            return Atomset({atom + right for atom in self.menge})
        elif isinstance(right, Atomset):
            return Atomset(self.menge.union(right.menge))
        else:
            return NotImplemented
            
           
    def __radd__(self, left):
        if isinstance(left, geo.Dif):
            return self + left
        else:
            return NotImplemented


    def __rpow__(self, left):
        assert isinstance(left, geo.Operator) \
            or isinstance(left, geo.Spacegroup), \
            "Argument must be of type Operator."
        if isinstance(left, geo.Operator):
            return Atomset({left**atom for atom in self.menge})
        if isinstance(left, geo.Spacegroup):
            atoms = set([])
            for atom in self.menge:
                for coset in left.liste_cosets:
                    atoms |= set([coset ** atom])
            return Atomset(atoms)

    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "I cannot take an object of type Atomset " \
            "modulo an object of type"%(type(right))
        atoms = set([])
        for atom in self.menge:
            atoms |= set([atom % right])
        return Atomset(atoms)


def structurefactor(atomset, metric, q, wavelength):
    assert isinstance(atomset, Atomset), \
        "atomset must be of type Atomset."
    assert isinstance(metric, geo.Metric), \
        "metric must be of type geo.Metric."
    assert isinstance(q, geo.Rec), \
        "q (scattering vector) must be of type geo.Rec."
    wavelength = nb.Mixed(wavelength)
    assert isinstance(wavelength, nb.Mixed), \
        "wavelength must be of type numbers.Mixed or a type " \
        "that can be converted to this."

    sintl = 0.5 * metric.length(q)
    i2pi = np.complex(0, 1) * 2.0 * np.pi
    F = 0
    for atom in atomset.menge:
        F += tables.formfactor(atom.typ, sintl) \
           * np.exp(i2pi * float(q * (atom.pos - geo.origin)))

    return F
