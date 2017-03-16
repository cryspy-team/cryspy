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
        string = "%s%s%s%s" % (
            self.typ,
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
        else:
            return NotImplemented

    def __hash__(self):
        string = "x%sy%sz%sdx%sdy%sdz%s" \
            % (str(hash(self.pos.x())),
               str(hash(self.pos.y())),
               str(hash(self.pos.z())),
               str(hash(self.direction.x())),
               str(hash(self.direction.y())),
               str(hash(self.direction.z())))
        return int(hashlib.sha1(string.encode()).hexdigest(), 16)


class Bond():
    def __init__(self, start, target):
        assert isinstance(start, geo.Pos), \
            "The start position of an object of type Bond " \
            "must be of type geo.Position."
        assert isinstance(target, geo.Pos), \
            "The target position of an object of type Bond " \
            "must be of type geo.Position."
        self.start = start
        self.target = target
        self.has_color = False
        self.color = None
        self.has_thickness = False
        self.thickness = None

    def set_color(self, color):
        assert isinstance(color, tuple), \
            "Argument of crystal.Bond.set_color(color) must be of type " \
            " tuple."
        assert (len(color) == 3), \
            "Argument of crystal.Bond.set_color(color) must be of type "\
            "tuple and must have three items."
        for item in color:
            assert isinstance(item, float) or isinstance(item, int) \
                or isinstance(item, nb.Mixed), \
                "Argument of crystal.Bond.set_color(color) must be of " \
                "type tuple with three numbers in it."
        self.has_color = True
        self.color = (float(color[0]), float(color[1]), float(color[2]))

    def set_thickness(self, thickness):
        assert isinstance(thickness, float) or isinstance(thickness, int) \
            or isinstance(thickness, nb.Mixed), \
            "Argument of crystal.Bond.set_thickness(...) must be of type " \
            "float, int or Mixed."

    def __str__(self):
        return "Bond"

    def __eq__(self, right):
        if isinstance(right, Bond):
            if (self.start == right.start) and (self.target == right.target):
                return True
            else:
                return False
        else:
            return False

    def __add__(self, right):
        if isinstance(right, geo.Dif):
            result = Bond(self.start + right, self.target + right)
            if self.has_color:
                result.set_color(self.color)
            if self.has_thickness:
                result.set_thickness(self.thickness)
            return result
        else:
            return NotImplemented

    def __rpow__(self, left):
        if isinstance(left, geo.Operator) \
            or isinstance(left, geo.Coset):
            result = Bond(left ** self.start, left ** self.target)
            if self.has_color:
                result.set_color(self.color)
            if self.has_thickness:
                result.set_thickness(self.thickness)
            return result
        else:
            return NotImplemented

    def __hash__(self):
        string = "x%sy%sz%sdx%sdy%sdz%s" \
            % (str(hash(self.start.x())),
               str(hash(self.start.y())),
               str(hash(self.start.z())),
               str(hash(self.target.x())),
               str(hash(self.target.y())),
               str(hash(self.target.z())))
        return int(hashlib.sha1(string.encode()).hexdigest(), 16)


class Face():
    def __init__(self, corners):
        assert isinstance(corners, list), \
            "Face must be created by a list of objects of type geo.Pos."
        for corner in corners:
            assert isinstance(corner, geo.Pos), \
                "Face must be created by a list of objects of type geo.Pos."
        self.corners = corners
        self.has_color = False
        self.color = None
        self.has_opacity = False
        self.opacity = None
 
    def set_color(self, color):
        assert isinstance(color, tuple), \
            "Argument of crystal.Bond.set_color(color) must be of type " \
            " tuple."
        assert (len(color) == 3), \
            "Argument of crystal.Bond.set_color(color) must be of type "\
            "tuple and must have three items."
        for item in color:
            assert isinstance(item, float) or isinstance(item, int) \
                or isinstance(item, nb.Mixed), \
                "Argument of crystal.Bond.set_color(color) must be of " \
                "type tuple with three numbers in it."
        self.has_color = True
        self.color = (float(color[0]), float(color[1]), float(color[2]))

    def set_opacity(self, opacity):
        assert isinstance(opacity, Mixe) or isinstance(opacity, float) \
            or isinstance(opacity, int), \
            "Opacity must be a number."
        assert 0 <= float(opacity) <= 1, \
            "Opacity must be between 0 and 1."
        self.has_opacity = True
        self.opacity = opacity 

    def __str__(self):
        return "Face"

    def __eq__(self, right):
        if isinstance(right, Face):
            if len(self.corners) == len(right.corners):
                result = True
                for i in range(len(self.corners)):
                    if self.corners[i] != right.corners[i]:
                        result = False
                return result
            else:
                return False
        else:
            return False

    def __add__(self, right):
        if isinstance(right, geo.Dif):
            liste = []
            for corner in self.corners:
                liste.append(corner + right)
            result = Face(liste)
            if self.has_color:
                result.set_color(self.color)
            return result
        else:
            return NotImplemented

    def __rpow__(self, left):
        if isinstance(left, geo.Operator) \
            or isinstance(left, geo.Coset):
            result = Face([left ** corner for corner in self.corners])
            if self.has_color:
                result.set_color(self.color)
            return result
        else:
            return NotImplemented

    def __hash__(self):
        string = ""
        for corner in self.corners:
            string += "x%sy%sz%s" \
               %(str(hash(corner.x())),
               str(hash(corner.y())),
               str(hash(corner.z())))
        return int(hashlib.sha1(string.encode()).hexdigest(), 16)

      



class Atomset():
    def __init__(self, menge):
        assert isinstance(menge, set), \
            "Argument must be of type set."
        for item in menge:
            assert isinstance(item, Atom) or isinstance(item, Momentum) \
                or isinstance(item, Bond) or isinstance(item, Face), \
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
        bondliste = []
        faceliste = []
        for item in self.menge:
            if isinstance(item, Atom):
                atomliste.append(item)
            elif isinstance(item, Momentum):
                momentumliste.append(item)
            elif isinstance(item, Bond):
                bondliste.append(item)
            elif isinstance(item, Face):
                faceliste.append(item)
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
        for bond in bondliste:
            strings.append(["", str(bond)])
        for face in faceliste:
            strings.append(["", str(face)])
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
                i = 0
                for coset in left.liste_cosets:
                    i += 1
                    new_atom = coset ** atom
                    if isinstance(atom, Atom):
                        new_atom.name = new_atom.name + "_%i"%(i)
                    atoms |= set([new_atom])
            return Atomset(atoms)

    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "I cannot take an object of type Atomset " \
            "modulo an object of type" % (type(right))
        atoms = set([])
        for atom in self.menge:
            atoms |= set([atom % right])
        return Atomset(atoms)

    def get_atom(self, atomname):
        for atom in self.menge:
            if atom.name == atomname:
                return atom
        return None

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
