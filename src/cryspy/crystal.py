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
        return bp.block([["Atom", " " + self.name,
                          " " + self.typ, " " + self.pos.__str__()], ])

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
            "to an object of type Atom." % (type(left))
        return Atom(self.name, self.typ, left ** self.pos)

    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "I cannot take an object of type Atom " \
            "modulo an object of type %s" % (type(right))
        return Atom(self.name, self.typ, self.pos % right)

    def __hash__(self):
        string = "%s%s%s%s%s" % (
            self.name, self.typ,
            str(hash(self.pos.x())),
            str(hash(self.pos.y())),
            str(hash(self.pos.z())))
        return int(hashlib.sha1(string.encode()).hexdigest(), 16)


class Momentum():
    def __init__(self, pos, direction):
        assert isinstance(pos, geo.Pos), \
            "First argument of crystal.Momentum(pos, dir) must be of type " \
            " geo.Pos ."
        assert isinstance(direction, geo.Dif), \
            "Second argument of crystal.Momentum(pos, dir) must be of type" \
            " geo.Dif ."
        self.pos = pos
        self.direction = direction
        self.has_color = False
        self.color = None
        self.has_plotlength = False
        self.plotlength = None

    def set_color(self, color):
        assert isinstance(color, tuple), \
            "Argument of crystal.Momentum.set_color(color) must be of type " \
            " tuple."
        assert (len(color) == 3), \
            "Argument of crystal.Momentum.set_color(color) must be of type "\
            "tuple and must have three items."
        for item in color:
            assert isinstance(item, float) or isinstance(item, int) \
                or isinstance(item, nb.Mixed), \
                "Argument of crystal.Momentum.set_color(color) must be of " \
                "type tuple with three numbers in it."
        self.has_color = True
        self.color = (float(color[0]), float(color[1]), float(color[2]))

    def set_plotlength(self, plotlength):
        assert isinstance(plotlength, float) or isinstance(plotlength, int) \
            or isinstance(plotlength, nb.Mixed), \
            "Argument of crystal.Momentum.set_plotlength(plotlength) must " \
            "be of type float or int or numbers.Mixed."
        self.has_plotlength = True
        self.plotlength = float(plotlength)

    def __str__(self):
        return "Momentum"

    def __eq__(self, right):
        if isinstance(right, Momentum):
            if (self.pos == right.pos) and (self.direction == right.direction):
                return True
            else:
                return False
        else:
            return False

    def __add__(self, right):
        if isinstance(right, geo.Dif):
            result = Momentum(self.pos + right, self.direction)
            if self.has_color:
                result.set_color(self.color)
            if self.has_plotlength:
                result.set_plotlength(self.plotlength)
            return result
        else:
            return NotImplemented

    def __rpow__(self, left):
        if isinstance(left, geo.Operator) \
            or isinstance(left, geo.Coset):
            result = Momentum(left ** self.pos, self.direction)
            if self.has_color:
                result.set_color(self.color)
            if self.has_plotlength:
                result.set_plotlength(self.plotlength)
            return result

    def __hash__(self):
        string = "x%sy%sz%sdx%sdy%sdz%s" \
            % (str(hash(self.pos.x())),
               str(hash(self.pos.y())),
               str(hash(self.pos.z())),
               str(hash(self.direction.x())),
               str(hash(self.direction.y())),
               str(hash(self.direction.z())))
        return int(hashlib.sha1(string.encode()).hexdigest(), 16)


class Atomset():
    def __init__(self, menge):
        assert isinstance(menge, set), \
            "Argument must be of type set."
        for item in menge:
            assert isinstance(item, Atom) or isinstance(item, Momentum), \
                "Argument must be a set of "\
                "objects of type Atom or of type Momentum."
        self.menge = menge

    def __eq__(self, right):
        if isinstance(right, Atomset):
            return (self.menge == right.menge)
        else:
            return False

    def __str__(self):
        # The Atoms are printed in alphabetically order with regard to
        # the name, and if name is equal, with regard to the type.
        strings = [["Atomset\n"
                    "-------"], ]
        liste = [atom for atom in self.menge]
        atomliste = []
        momentumliste = []
        for item in self.menge:
            if isinstance(item, Atom):
                atomliste.append(item)
            elif isinstance(item, Momentum):
                momentumliste.append(item)
        types = [atom.typ for atom in atomliste]
        indexes = [i for (j, i) in sorted(zip(types, range(len(atomliste))))]
        names = [atomliste[i].name for i in indexes]
        indexes = [i for (j, i) in sorted(zip(names, indexes))]
        print(indexes)
        for i in indexes:
            strings.append(["", atomliste[i].__str__()])
            strings.append([""])
        for momentum in momentumliste:
            strings.append(["", str(momentum)])
        return bp.block(strings)

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
            menge = set([])
            return Atomset({left ** item for item in self.menge})
        if isinstance(left, geo.Spacegroup):
            atoms = set([])
            for atom in self.menge:
                for coset in left.liste_cosets:
                    atoms |= set([coset ** atom])
            return Atomset(atoms)

    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "I cannot take an object of type Atomset " \
            "modulo an object of type" % (type(right))
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
