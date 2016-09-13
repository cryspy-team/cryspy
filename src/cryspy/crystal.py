import hashlib
from cryspy import numbers as nb
from cryspy import geo as geo
from cryspy import blockprint as bp

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
        return bp.block([["Atom", " " + self.name, \
                          " " + self.typ, " " +  self.pos.__str__()],])

    def __eq__(self, right):
        if (self.typ == right.typ) and (self.pos == right.pos):
            return True
        else:
            return False

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
        strings = [["Atomset\n" \
                    "-------"],]
        for atom in self.menge:
            strings.append(["", atom.__str__() + "\n "])
        return bp.block(strings)


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

