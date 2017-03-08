# File:         ======== geo.py ========
# Description:  This module includes all the basic objects nedded
#               for calculations in 3D-Space (direct or reciprocal).
#
#               In direct space there exist the classes Pos and Dif:
#               Pos is a position and Dif is the difference-vector between
#               two positions. So you can calculate in the following way:
#
#               Dif + Dif = Dif
#               Dif - Dif = Dif
#               Pos - Pos = Dif
#               Pos + Dif = Pos
#               Pos - Dif = Pos
#               Pos + Pos: not defined
#
#               In reciprocal space, there is the type Rec, which represents
#               a reciprocal vector.
#
#               You can calculate Rec * Dif = Mixed, which in independent
#               from the metric you caclulate with.
#
#               For other scalar products (and thus length and angles),
#               you need to specify a metric of type Metric.
#               It can be easy created from an object of type
#               Cellparameters in the following way (example is orthorhombic):
#
#                   >>> metric = cryspy.geo.Cellparameters( \
#                           1.23, 3.45, 5.67, 90, 90, 90 \
#                       ).to_Metric()
#
#               This metric can now be used to calculate scalarproduct:
#
#               Metric.dot(Dif, Dif) = Mixed
#               Metric.dot(Rec, Rec) = Mixed
#               similar for Metric.angle and Metric.length .
#
#
#

from cryspy import numbers as nb
from cryspy import blockprint as bp

# **** class Pos ****
# An object of this class represents a position in 3D direct space.
# It is constructed via a 4x1-numbers.Matrix, wherein the last entry
# must be 1.


class Pos:
    def __init__(self, value):
        assert isinstance(value, nb.Matrix), \
            "Must be created by an object of type Matrix."
        assert (value.shape() == (4, 1)), \
            "Must be createy by a 4x1-Matrix."
        assert (value.liste[3].liste[0] == 1), \
            "Must be created by a 4x1-Matrix with a 1 as last entry."
        self.value = value

    def __str__(self):
        return bp.block([["Pos", self.value.block(0, 3, 0, 1).__str__()],])

    def x(self):
        return self.value.liste[0].liste[0]

    def y(self):
        return self.value.liste[1].liste[0]

    def z(self):
        return self.value.liste[2].liste[0]

    def __eq__(self, right):
        if isinstance(right, Pos):
            return (self.value == right.value)
        else:
            return False

    def __add__(self, right):
        if isinstance(right, Dif):
            return Pos(self.value + right.value)
        else:
            raise(BaseException(
                "I cannot add objects of types %s and %s" %
                (type(self), type(right))))
        return 0

    def __sub__(self, right):
        if isinstance(right, Dif):
            return Pos(self.value - right.value)
        elif isinstance(right, Pos):
            return Dif(self.value - right.value)
        else:
            raise(BaseException(
                "I cannot subtract objects of type %s and %s" %
                (typen(self), type(right))))

origin = Pos(nb.Matrix([[0], [0], [0], [1]]))


# **** class Dif ****
# An object of this class represents a difference vector in 3D
# direct space.
# It is constructed via a 4x1-numbers.Matrix, wherein the last
# entry must be a 0.
class Dif:
    def __init__(self, value):
        assert isinstance(value, nb.Matrix), \
            "Must be created by an object of type Matrix."
        assert (value.shape() == (4, 1)), \
            "Must be created by a 4x1-Matrix."
        assert (value.liste[3].liste[0] == 0), \
            "Must be created by a 4x1-Matrix with a 0 as last entry."
        self.value = value

    def x(self):
        return self.value.liste[0].liste[0]

    def y(self):
        return self.value.liste[1].liste[0]

    def z(self):
        return self.value.liste[2].liste[0]

    def __str__(self):
        return bp.block([["Dif", self.value.block(0, 3, 0, 1).__str__()],])

    def __eq__(self, right):
        if isinstance(right, Dif):
            return (self.value == right.value)
        else:
            return False

    def __add__(self, right):
        if isinstance(right, Dif):
            return Dif(self.value + right.value)
        elif isinstance(right, Pos):
            return Pos(self.value + right.value)
        else:
            return NotImplemented

    def __sub__(self, right):
        if isinstance(right, Dif):
            return Dif(self.value - right.value)
        else:
            raise(BaseException("I cannot subtract objects of type"
                                "%s and %s" % (type(self), type(right))))

    def __neg__(self):
        return Dif(-self.value)

    def __mul__(self, right):
        if isinstance(right, nb.Mixed):
            return Dif(nb.Matrix([[right * self.x()],
                                  [right * self.y()],
                                  [right * self.z()],
                                  [0               ]]))
        else:
            return NotImplemented

canonical_e0 = Dif(nb.Matrix([nb.Row([1]),
                              nb.Row([0]),
                              nb.Row([0]),
                              nb.Row([0])]))

canonical_e1 = Dif(nb.Matrix([nb.Row([0]),
                              nb.Row([1]),
                              nb.Row([0]),
                              nb.Row([0])]))

canonical_e2 = Dif(nb.Matrix([nb.Row([0]),
                              nb.Row([0]),
                              nb.Row([1]),
                              nb.Row([0])]))


# **** class Rec ****
# An object of this class represents a vector in 3D reciprocal space.
# It is constructed via a 1x4-numbers.Matrix, wherein the last
# entry must be a 0.
class Rec:
    def __init__(self, value):
        assert isinstance(value, nb.Matrix), \
            "Must be created by an object of type Matrix."
        assert value.shape() == (1, 4), \
            "Must be created by a 1x4-Matrix."
        assert value.liste[0].liste[3] == 0, \
            "Must be created by a 1x4-Matrix of this shape: \n" \
            "  < *  *  *  0 > "
        self.value = value

    def __str__(self):
        return bp.block([["Rec", self.value.block(0, 1, 0, 3).__str__()],])

    def __eq__(self, right):
        if isinstance(right, Rec):
            return (self.value == right.value)
        else:
            return False

    def __add__(self, right):
        if isinstance(right, Rec):
            return Rec(self.value + right.value)
        else:
            return NotImplemented

    def __sub__(self, right):
        if isinstance(right, Rec):
            return Rec(self.value - right.value)
        else:
            return NotImplemented

    def __neg__(self):
        return Rec(-self.value)

    def __mul__(self, right):
        if isinstance(right, Dif):
            return (self.value * right.value).liste[0].liste[0]
        else:
            return NotImplemented

    def h(self):
        return self.value.liste[0].liste[0]

    def k(self):
        return self.value.liste[0].liste[1]

    def l(self):
        return self.value.liste[0].liste[2]


# **** class Operator ****
# This class is the basic class for the following classes:
#
#     * Symmetry
#     * Transformation
#     * Metric
#
# It is constructed via a 4x4-Matrix of the following form:
#
#     * * * *
#     * * * *
#     * * * *
#     0 0 0 1
#
class Operator:
    def __init__(self, value):
        assert isinstance(value, nb.Matrix), \
            "Must be created by an object of type Matrix."
        assert value.shape() == (4, 4), \
            "Must be created by a 4x4-Matrix."
        assert value.liste[3] == nb.Row([0, 0, 0, 1]), \
            "Must be created by a 4x4-Matrix of this shape: \n"\
            "   * * * * \n"\
            "   * * * * \n"\
            "   * * * * \n"\
            "   0 0 0 1 \n"
        self.value = value

    def __str__(self):
        return bp.block([["Operator", self.value.__str__()],])

    def __eq__(self, right):
        if isinstance(right, Operator):
            return (self.value == right.value)
        else:
            return False

    def inv(self):
        return Operator(self.value.inv())


def linearterm2str(liste_numbers, liste_variables):
    assert isinstance(liste_numbers, list), \
        "Argument must be of type list."
    for item in liste_numbers:
        assert isinstance(item, nb.Mixed) or \
            isinstance(item, int) or \
            isinstance(item, float), \
            "Argument must be a list of Mixed, int or flot."
    assert isinstance(liste_variables, list), \
        "Argument must be of type list."
    for item in liste_variables:
        assert isinstance(item, str), \
            "Argument must be a list of str."
    assert len(liste_numbers) == len(liste_variables), \
        "Arguments must have the same length."
    def prefactor(number, variablestr):
        assert isinstance(number, nb.Mixed), \
            "Argument must be of type Mixed."
        if (float(number) == 0):
            return ''
        elif (float(number.value) > 0):
            if (number == 1) and (variablestr != ''):
                return '+' + variablestr
            else:
                return '+' + number.__str__() + variablestr
        elif (float(number.value) < 0):
            if (number == -1) and (variablestr != ''):
                return '-' + variablestr
            else:
                return '-' + (-number).__str__() + variablestr
    result =  ''
    for i in range(len(liste_numbers)):
        result += prefactor(liste_numbers[i], liste_variables[i])
    if result[0] == '+':
        result = result[1:]
    return result


class Symmetry(Operator):
    def __str__(self):
        result = ''
        for i in range(3):
            result +=  linearterm2str(self.value.liste[i].liste,
                                      ["x", "y", "z", '']) + ','
        result = result[:-1]
        return result

    def inv(self):
        return Symmetry(self.value.inv())

    def __mul__(self, right):
        if isinstance(right, Symmetry):
            return Symmetry(self.value * right.value)
        else:
            return NotImplemented

    def __pow__(self, right):
        if isinstance(right, Pos):
            return Pos(self.value * right.value)
        elif isinstance(right, Dif):
            return Dif(self.value * right.value)
        else:
            return NotImplemented


# **** class Pointgroup ****
# An object of this class represents a point group.
# It is essentially a list of objects of type Symmetry.
# It is constructed via a list of objects of type Symmetry.
class Pointgroup:
    def __init__(self, liste):
        assert isinstance(liste, list), \
            "Object of type geo.Pointgroup must be constructed " \
            "via a list of object of type Symmetry."

        for symmetry in liste:
            assert isinstance(symmetry, Symmetry), \
                "Object of type geo.Pointgroup must be constructed " \
                "via a list of object of type Symmetry."

        self.liste = liste

    def __str__(self):
        string  = "Pointgroup\n"
        string += "==========\n"
        for symmetry in self.liste:
            string += symmetry.__str__() + "\n"
        return string

    def __eq__(self, right):
        if isinstance(right, Pointgroup):
            if len(self.liste) == len(right.liste):
                result = True
                for i in range(len(self.liste)):
                    if not self.liste[i] == right.liste[i]:
                        result = False
                return result
            else:
                return False
        else:
            return False

    def is_really_a_pointgroup(self):
        result = True
        for s1 in self.liste:
            for s2 in self.liste:
                if not((s1 * s2) in self.liste):
                    result = False
        return result

    def sort(self):
        # This is the sorting of algorithm A of:
        #     H. D. Flack
        #     "The Derivation of Twin Laws for
        #      (Pseudo-)Merohedry by Coset
        #      Decomposition"
        #     Acta Cryst. (1987) A43, 564-568
        #
        identity = []
        twofold_rotations = []
        non_twofold_rotations = []
        inversion = []
        mirror_reflections = []
        non_twofold_second_kind = []

        id = Symmetry(nb.Matrix([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 1]]))
        I = Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                [0, -1, 0, 0],
                                [0, 0, -1, 0],
                                [0, 0, 0, 1]]))

        for symmetry in self.liste:
            if symmetry == id:
                identity.append(symmetry)
            elif symmetry.value.det() == 1:
                if symmetry *symmetry == id:
                    twofold_rotations.append(symmetry)
                else:
                    non_twofold_rotations.append(symmetry)
            else:
                if symmetry == I:
                    inversion.append(symmetry)
                elif symmetry *symmetry == id:
                    mirror_reflections.append(symmetry)
                else:
                    non_twofold_second_kind.append(symmetry)

        return Pointgroup(
            identity +
            twofold_rotations +
            non_twofold_rotations +
            inversion +
            mirror_reflections +
            non_twofold_second_kind
        )

    def coset_decomposition_with_respect_to(self, subgroup):
        # This is the algorithm A of:
        #     H. D. Flack
        #     "The Derivation of Twin Laws for
        #      (Pseudo-)Merohedry by Coset
        #      Decomposition"
        #     Acta Cryst. (1987) A43, 564-568
        assert isinstance(subgroup, Pointgroup), \
            "I can only calculate a coset decomposition with respect " \
            "to a pointgroup (an object of type geo.Pointgroup)."

        G = self.sort()
        H = subgroup.sort()

        n = len(G.liste)
        m = len(H.liste)
        flags = [True,] * n
        for i in range(n):
            if flags[i]:
                for j in range(1, m):
                    for k in range(i +1, n):
                        if G.liste[k] == G.liste[i] *H.liste[j]:
                            flags[k] = False
        string = ""
        for i in range(n):
            if flags[i]:
                string += G.liste[i].__str__() + "\n"

        return string


class Transformation(Operator):
    def __str__(self):
        result = 'Transformation '
        m = self.value.inv()
        Ox = m.liste[0].liste[3]
        Oy = m.liste[1].liste[3]
        Oz = m.liste[2].liste[3]
        matrix = nb.Matrix([[1, 0, 0, Ox],
                            [0, 1, 0, Oy],
                            [0, 0, 1, Oz],
                            [0, 0, 0, 1]])
        result = "Transformation O -> (%s, %s, %s)\n" \
                 "               then\n" % \
        (Ox.__str__(), Oy.__str__(), Oz.__str__())
        matrix = nb.Matrix(
            [nb.Row([m.liste[0].liste[0], m.liste[1].liste[0], m.liste[2].liste[0], 0]),
             nb.Row([m.liste[0].liste[1], m.liste[1].liste[1], m.liste[2].liste[1], 0]),
             nb.Row([m.liste[0].liste[2], m.liste[1].liste[2], m.liste[2].liste[2], 0]),
             nb.Row([m.liste[3].liste[0], m.liste[3].liste[1], m.liste[3].liste[2], 1])])
        terms = []
        for i in range(3):
            print(matrix.liste[i].liste[0], matrix.liste[i].liste[1], matrix.liste[i].liste[2], matrix.liste[i].liste[3])
            terms.append(linearterm2str(matrix.liste[i].liste,
                                        ["a", "b", "c", '']))
        return result + "               a' = " + terms[0] + "\n" \
                      + "               b' = " + terms[1] + "\n" \
                      + "               c' = " + terms[2]

    def inv(self):
        return Transformation(self.value.inv())

    def __mul__(self, right):
        if isinstance(right, Transformation):
            return Transformation(self.value * right.value)
        else:
            return NotImplemented

    def __pow__(self, right):
        if isinstance(right, Symmetry):
            return Symmetry(self.value * right.value * self.value.inv())
        elif isinstance(right, Transgen):
            return Transgen(self ** right.liste[0],
                            self ** right.liste[1],
                            self ** right.liste[2])
        elif isinstance(right, Pos):
            return Pos(self.value * right.value)
        elif isinstance(right, Dif):
            return Dif(self.value * right.value)
        elif isinstance(right, Metric):
            M = self.value.delete_translation()
            Minv = M.inv()
            Minvtr = Minv.transpose()
            return Metric(Minvtr * right.value * Minv)
        elif isinstance(right, Spacegroup):
            return Spacegroup(self ** right.transgen,
                              [self ** coset for coset in right.liste_cosets])
        elif isinstance(right, Rec):
            return Rec(right.value * self.inv().value.delete_translation())
        else:
            return NotImplemented


class Metric(Operator):
    def __init__(self, value):
        assert isinstance(value, nb.Matrix), \
            "Must be created by an object of type Matrix."
        assert value.shape() == (4, 4), \
            "Must be created by a 4x4-Matrix."
        assert  (value.liste[3] == nb.Row([0, 0, 0, 1])) \
            and (value.liste[0].liste[3] == 0) \
            and (value.liste[1].liste[3] == 0) \
            and (value.liste[2].liste[3] == 0), \
            "Argument must be a Matrix of this shape:\n" \
            "     * * * 0\n" \
            "     * * * 0\n" \
            "     * * * 0\n" \
            "     0 0 0 1"
        self.value = value
        self.valueinv = value.inv()
        self.schmidttransformation = self.calculate_schmidttransformation()

    def dot(self, vector1, vector2):
        assert  (isinstance(vector1, Dif) and isinstance(vector2, Dif) ) \
            or (isinstance(vector1, Rec) and isinstance(vector2, Rec)), \
            "Arguments must be both of type Dif of both of type Rec."
        if isinstance(vector1, Dif):
            matrix = vector1.value.transpose() * self.value * vector2.value
            return matrix.liste[0].liste[0]
        if isinstance(vector1, Rec):
            matrix = vector1.value * self.valueinv * vector2.value.transpose()
            return matrix.liste[0].liste[0]

    def length(self, vector):
        assert isinstance(vector, Dif) or isinstance(vector, Rec), \
            "Argument must be of type Dif or Rec."
        return nb.sqrt(self.dot(vector, vector))

    def angle(self, vector1, vector2):
        assert (isinstance(vector1, Dif) and isinstance(vector2, Dif)) \
            or (isinstance(vector1, Rec) and isinstance(vector2, Rec)), \
            "Both arguments must be of type Dif."
        len1 = self.length(vector1)
        len2 = self.length(vector2)
        return nb.arccos(self.dot(vector1, vector2)
                         / (len1 * len2))

    def calculate_schmidttransformation(self):
        a1 = canonical_e0
        b1 = canonical_e1
        c1 = canonical_e2

        a2 = a1
        a3 = a2 * (1 /self.length(a2))

        b2 = b1 - a3 *self.dot(a3, b1)
        b3 = b2 * (1 /self.length(b2))

        c2 = c1 - a3 *self.dot(a3, c1) - b3 *self.dot(b3, c1)
        c3 = c2 * (1 /self.length(c2))

        M = nb.Matrix([[a3.x(), b3.x(), c3.x()],
                       [a3.y(), b3.y(), c3.y()],
                       [a3.z(), b3.z(), c3.z()]]).inv()
        transformation = Transformation(
            nb.Matrix([[M.liste[0].liste[0], M.liste[0].liste[1], M.liste[0].liste[2], 0],
                       [M.liste[1].liste[0], M.liste[1].liste[1], M.liste[1].liste[2], 0],
                       [M.liste[2].liste[0], M.liste[2].liste[1], M.liste[2].liste[2], 0],
                       [0   , 0   , 0   , 1]])
            )

        return transformation

#    def cartesian(self, pos):

    def to_Cellparameters(self):
        e0 = canonical_e0
        e1 = canonical_e1
        e2 = canonical_e2
        a = self.length(e0)
        b = self.length(e1)
        c = self.length(e2)
        alpha = nb.rad2deg(self.angle(e1, e2))
        beta  = nb.rad2deg(self.angle(e2, e0))
        gamma = nb.rad2deg(self.angle(e0, e1))
        return Cellparameters(a, b, c, alpha, beta, gamma)

    def __str__(self):
        return bp.block([["Metric", self.value.__str__()]])


class Cellparameters():
    def __init__(self, a, b, c, alpha, beta, gamma):
        for number in [a, b, c, alpha, beta, gamma]:
            assert isinstance(number, nb.Mixed) \
                or isinstance(number, int) \
                or isinstance(number, float), \
                "Arguments must be of type Mixed, int or float."
        self.a = nb.Mixed(a)
        self.b = nb.Mixed(b)
        self.c = nb.Mixed(c)
        self.alpha = nb.Mixed(alpha)
        self.beta = nb.Mixed(beta)
        self.gamma = nb.Mixed(gamma)

    def to_Metric(self):
        a = self.a
        b = self.b
        c = self.c
        alpha = self.alpha
        beta  = self.beta
        gamma = self.gamma
        aa = a *a
        bb = b *b
        cc = c *c
        ab = a * b * nb.cos(nb.deg2rad(gamma))
        ac = a * c * nb.cos(nb.deg2rad(beta))
        bc = b * c * nb.cos(nb.deg2rad(alpha))
        return Metric(nb.Matrix([nb.Row([aa, ab, ac, 0]),
                                 nb.Row([ab, bb, bc, 0]),
                                 nb.Row([ac, bc, cc, 0]),
                                 nb.Row([0, 0, 0, 1])]))

    def __str__(self):
        return "Cellparameters\n" + \
               bp.block([["a", " b", " c", " alpha", " beta", " gamma"],
                         [self.a.__str__(),
                          " " + self.b.__str__(),
                          " " + self.c.__str__(),
                          " " + self.alpha.__str__(),
                          " " + self.beta.__str__(),
                          " " + self.gamma.__str__()]])


class Transgen():
    def __init__(self, b1, b2, b3):
        assert  isinstance(b1, Dif) \
            and isinstance(b2, Dif) \
            and isinstance(b3, Dif), \
            "Arguments must be of type Dif."
        self.liste = [b1, b2, b3]
        m00 = b1.value.liste[0].liste[0]
        m01 = b2.value.liste[0].liste[0]
        m02 = b3.value.liste[0].liste[0]
        m10 = b1.value.liste[1].liste[0]
        m11 = b2.value.liste[1].liste[0]
        m12 = b3.value.liste[1].liste[0]
        m20 = b1.value.liste[2].liste[0]
        m21 = b2.value.liste[2].liste[0]
        m22 = b3.value.liste[2].liste[0]
        self.transformation = Transformation(nb.Matrix(
            [nb.Row([m00, m01, m02, 0]),
             nb.Row([m10, m11, m12, 0]),
             nb.Row([m20, m21, m22, 0]),
             nb.Row([  0, 0, 0, 1])]))
        self.transformationinv = self.transformation.inv()

    def __str__(self):
        if self == canonical:
            return "canonical"
        else:
            return bp.block([["Transgen",
                              self.liste[0].value.block(0,3,0,1).__str__(), ' ',
                              self.liste[1].value.block(0,3,0,1).__str__(), ' ',
                              self.liste[2].value.block(0,3,0,1).__str__()],])

    def __rmod__(self, left):
        if isinstance(left, Pos):
            result = self.transformation.inv() ** left
            result.value.liste[0].liste[0] %= 1
            result.value.liste[1].liste[0] %= 1
            result.value.liste[2].liste[0] %= 1
            return self.transformation ** result
        elif isinstance(left, Dif):
            result = self.transformation.inv() ** left
            result.value.liste[0].liste[0] %= 1
            result.value.liste[1].liste[0] %= 1
            result.value.liste[2].liste[0] %= 1
            return self.transformation ** result
        elif isinstance(left, Symmetry):
            result = self.transformationinv ** left
            result.value.liste[0].liste[3] %= 1
            result.value.liste[1].liste[3] %= 1
            result.value.liste[2].liste[3] %= 1
            return self.transformation ** result
        elif isinstance(left, Coset):
            if left.transgen == self:
                return Coset(left.symmetry % self, self)
            else:
                raise(BaseException("If you try to calculate "
                                    "Coset % Transgen, but the coset has another "
                                    "transgen, then you come into devil's kitchen!"))
        elif isinstance(left, Spacegroup):
            if left.transgen == self:
                return Spacegroup(self, [coset % self
                                         for coset in left.liste_cosets])
            else:
                raise(BaseException("If you try to calculate "
                                    "Spacegroup % Transgen, but the spacegroup has "
                                    "another transgen, then you come into "
                                    "devil's kitchen!"))
        else:
            return NotImplemented

    def __eq__(self, right):
        # Returns True even when the order is different.
        assert isinstance(right, Transgen), \
            "Cannot compare Object of type Transgen " \
            "with object of type %s." % (type(right))
        return  (self.liste[0] in right.liste) \
            and (self.liste[1] in right.liste) \
            and (self.liste[2] in right.liste)


canonical = Transgen(
    Dif(nb.Matrix(
    [nb.Row([1]), nb.Row([0]), nb.Row([0]), nb.Row([0])])),
    Dif(nb.Matrix(
    [nb.Row([0]), nb.Row([1]), nb.Row([0]), nb.Row([0])])),
    Dif(nb.Matrix(
    [nb.Row([0]), nb.Row([0]), nb.Row([1]), nb.Row([0])])))


class Coset():
    def __init__(self, symmetry, transgen):
        assert isinstance(symmetry, Symmetry), \
            "First argument must be of type Symmetry."
        assert isinstance(transgen, Transgen), \
            "Second argument must be of type Transgen."
        self.symmetry = symmetry % transgen
        self.transgen = transgen

    def __str__(self):
        if self.transgen == canonical:
            return "{" +self.symmetry.__str__() +"}"
        else:
            transgenblock = bp.block(
                [[self.transgen.liste[j].value.liste[i].liste[0].__str__() + "  "
                    for j in range(3)] for i in range(3)])
            return bp.block([["{" +self.symmetry.__str__() +"}",],
                             [transgenblock,]])

    def __eq__(self, right):
        if isinstance(right, Coset):
            return (self.transgen == right.transgen) \
                and (self.symmetry == right.symmetry)
        else:
            return False

    def gohome(self):
        return Coset(self.symmetry % self.transgen, self.transgen)
    def __pow__(self, right):
        if isinstance(right, Pos):
            return (self.symmetry ** right) % self.transgen
        elif isinstance(right, Dif):
            return(self.symmetry ** right) % self.transgen
        else:
            return NotImplemented

    def __rpow__(self, left):
        if isinstance(left, Operator):
            return Coset(left ** self.symmetry, left ** self.transgen)
        else:
            return NotImplemented

    def __mul__(self, right):
        assert isinstance(right, Coset), \
            "Cannot multiply Coset with %s ." % (type(right))
        assert self.transgen == right.transgen, \
            "Can only multiply two Cosets with the same Transgen, "\
            "but " + bp.block([[self.transgen.__str__(),
                                " != ",
                                right.transgen.__str__()]])
        return Coset(self.symmetry * right.symmetry, self.transgen)


class Spacegroup():
    def __init__(self, transgen, liste_cosets):
        assert isinstance(transgen, Transgen), \
            "First argument must be of type Transgen."
        assert type(liste_cosets) == list, \
            "Second argument must be a list."
        for coset in liste_cosets:
            assert isinstance(coset, Coset), \
                "Second argument must be a list " \
                "of objects of type Coset."
            assert transgen == coset.transgen, \
                "All cosets must have the same transgen "\
                "as the Spacegroup. At the moment they are" \
                "different: \n%s \n\n%s" %\
                (transgen.__str__(), liste_cosets[0].transgen.__str__())
        self.transgen = transgen
        self.liste_cosets = liste_cosets

    def is_really_a_spacegroup(self):
        for coset1 in self.liste_cosets:
            for coset2 in self.liste_cosets:
                coset3 = coset1 *coset2
                if not (coset3 in self.liste_cosets):
                    print("%s * %s = %s" % (
                        coset1.__str__(),
                        coset2.__str__(),
                        coset3.__str__()
                    ))
                    return False
        return True

    def __str__(self):
        liste_strings = [["Spacegroup", ''],
                         ["----------", ''],
                         [self.transgen.__str__(), '']]
        for coset in self.liste_cosets:
            liste_strings.append(['', coset.symmetry.__str__()])

        return bp.block(liste_strings)

    def __eq__(self, right):
        assert isinstance(right, Spacegroup), \
            "Can compare object of type Spacegroup " \
            "to object of type Spacegroup only."
        return (self.transgen == right.transgen) and \
               (self.liste_cosets == right.liste_cosets)



