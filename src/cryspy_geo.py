import cryspy_numbers as nb
import cryspy_fromstr as fs
import blockprint as bp

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
            raise(BaseException(\
                "I cannot add objects of types %s and %s"% \
                (type(self), type(right))))
        return 0

    def __sub__(self, right):
        if isinstance(right, Dif):
            return Pos(self.value - right.value)
        elif isinstance(right, Pos):
            return Dif(self.value - right.value)
        else:
            raise(BaseException(\
                "I cannot subtract objects of type %s and %s"% \
                (typen(self), type(right))))

class Dif:
    def __init__(self, value):
        assert isinstance(value, nb.Matrix), \
            "Must be created by an object of type Matrix."
        assert (value.shape() == (4, 1)), \
            "Must be created by a 4x1-Matrix."
        assert (value.liste[3].liste[0] == 0), \
            "Must be created by a 4x1-Matrix with a 0 as last entry."
        self.value = value

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
            raise(BaseException("I cannot add objects of type %s and %s"\
                %(type(self), type(right))))

    def __sub__(self, right):
        if isinstance(right, Dif):
            return Dif(self.value - right.value)
        else:
            raise(BaseException("I cannot subtract objects of type"\
                "%s and %s"%(type(self), type(right))))

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

    def __pow__(self, right):
        if isinstance(right, Pos):
            return Pos(self.value * right.value)
        elif isinstance(right, Dif):
            return Dif(self.value * right.value)
        elif isinstance(right, Symmetry):
            return Symmetry(self.value * right.value * self.value.inv())
        elif isinstance(right, Transformation):
            return Transformation(self.value * right.value * \
                self.value.inv())
        elif isinstance(right, Transgen):
            return Transgen(self.value * right.value)
        elif isinstance(right, Operator):
            return Operator(self.value * right.value * self.value.inv())
        else:
            return NotImplemented
            #"I cannot apply object of type Operator"\
            #    " to object of type %s."%(type(right))))

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
        if (number == 0):
            return ''
        elif (number.value > 0):
            if (number == 1) and (variablestr != ''):
                return '+' + variablestr
            else:
                return '+' + number.__str__() + variablestr
        elif (number.value < 0):
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


def str2linearterm(string, liste_variables):
    assert isinstance(string, str), \
        "Argument must be of type str."
    assert isinstance(liste_variables, list), \
        "Argument must be of type list."
    for item in liste_variables:
        assert isinstance(item, str), \
            "Argument must be a list of objects of type str."
    string = string.replace('-', '+-')
    string = string.replace(' ', '')
    words = string.split('+')
    liste_numbers = [0 for i in range(len(liste_variables) + 1)]
    for word in words:
        has_variable = False
        index = -1
        for a in word:
            if a.isalpha():
                word = word.replace(a, '')
                index = liste_variables.index(a)
                has_variable = True
        if word == '' or word == '-':
            if has_variable:
                word += '1'
            else:
                word += '0'
        liste_numbers[index] += fs.fromstr(word)
    return liste_numbers


class Symmetry(Operator):
    def __str__(self):
        result = ''
        for i in range(3):
            result +=  linearterm2str(self.value.liste[i].liste,
                ["x", "y", "z", '']) + ','
        result = result[:-1]
        return result
            

class Transformation(Operator):
    def __str__(self):
        result = ''
        m = self.value.inv()
        matrix = nb.Matrix( \
            [nb.Row([m.liste[0].liste[0], m.liste[1].liste[0], m.liste[2].liste[0], m.liste[0].liste[3]]), \
             nb.Row([m.liste[0].liste[1], m.liste[1].liste[1], m.liste[2].liste[1], m.liste[1].liste[3]]), \
             nb.Row([m.liste[0].liste[2], m.liste[1].liste[2], m.liste[2].liste[2], m.liste[2].liste[3]]), \
             nb.Row([m.liste[3].liste[0], m.liste[3].liste[1], m.liste[3].liste[2], m.liste[3].liste[3]])])
        for i in range(3):
            result += linearterm2str(matrix.liste[i].liste, 
                ["a", "b", "c", '']) + "\n"
        result = result[:-1]
        return bp.block([["Transformation ", "a' = \nb' = \nc' = ", result],])


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

    
    def dot(self, vector1, vector2):
        assert  isinstance(vector1, Dif) \
            and isinstance(vector2, Dif), \
            "Arguments must be both of type Dif."
        if (isinstance(vector1, Pos) or isinstance(vector1, Dif)):
            matrix = vector1.value.transpose() * self.value * vector2.value
            return matrix.liste[0].liste[0]

    def length(self, vector):
        assert isinstance(vector, Dif), \
            "Argument must be of type Dif."
        return nb.sqrt(self.dot(vector, vector))

    def angle(self, vector1, vector2):
        assert  isinstance(vector1, Dif) \
            and isinstance(vector2, Dif), \
            "Both arguments must be of type Dif."
        len1 = self.length(vector1)
        len2 = self.length(vector2)
        return nb.arccos(self.dot(vector1, vector2) \
            / (len1 * len2))

    def to_Cellparameters(self):
        e1 = Dif(fs.fromstr("1 \n 0 \n 0 \n 0"))
        e2 = Dif(fs.fromstr("0 \n 1 \n 0 \n 0"))
        e3 = Dif(fs.fromstr("0 \n 0 \n 1 \n 0"))
        a = self.length(e1)
        b = self.length(e2)
        c = self.length(e3)
        alpha = nb.rad2deg(self.angle(e2, e3))
        beta  = nb.rad2deg(self.angle(e3, e1))
        gamma = nb.rad2deg(self.angle(e1, e2))
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
        aa = a*a
        bb = b*b
        cc = c*c
        ab = a * b * nb.cos(nb.deg2rad(gamma))
        ac = a * c * nb.cos(nb.deg2rad(beta))
        bc = b * c * nb.cos(nb.deg2rad(alpha))
        return Metric(nb.Matrix([nb.Row([aa, ab, ac, 0]), \
                                 nb.Row([ab, bb, bc, 0]), \
                                 nb.Row([ac, bc, cc, 0]), \
                                 nb.Row([0,  0,  0,  1])]))

    def __str__(self):
        return "Cellparameters\n" + \
               bp.block([["a", " b", " c", " alpha", " beta", " gamma"], \
                         [self.a.__str__(), \
                          " " + self.b.__str__(), \
                          " " + self.c.__str__(), \
                          " " + self.alpha.__str__(), \
                          " " + self.beta.__str__(), \
                          " " + self.gamma.__str__()]])

class Transgen(Operator):
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
        assert  (value.liste[0].liste[3] == 0) \
            and (value.liste[1].liste[3] == 0) \
            and (value.liste[2].liste[3] == 0), \
            "Must be created by a 4x4-Matrix without translation part."
        self.value = value
        
    def __str__(self):
        if self == canonical:
            return "canonical"
        else:
            return bp.block([["Transgen", \
                self.value.block(0, 3, 0, 1).__str__(), ' ', \
                self.value.block(0, 3, 1, 2).__str__(), ' ', \
                self.value.block(0, 3, 2, 3).__str__()],])

    def __rmod__(self, left):
        assert isinstance(left, Pos), \
            "Argument must be of type Pos."
        left = Pos(self.value.inv() * left.value)
        left.value.liste[0].liste[0] %= 1
        left.value.liste[1].liste[0] %= 1
        left.value.liste[2].liste[0] %= 1
        return Pos(self.value * left.value)


canonical = Transgen(nb.Matrix.onematrix(4))

class Coset():
    def __init__(self, symmetry, transgen):
        assert isinstance(symmetry, Symmetry), \
            "First argument must be of type Symmetry."
        assert isinstance(transgen, Transgen), \
            "Second argument must be of type Transgen."
        self.symmetry = symmetry
        self.transgen = transgen
        self.gohome()
    
    def __str__(self):
        if self.transgen == canonical:
            return "{"+self.symmetry.__str__()+"}"
        else:
            transgenblock = bp.block( \
                [[self.transgen.value.liste[i].liste[j].__str__() + "  " \
                    for j in range(3)] for i in range(3)])
            return bp.block([["{"+self.symmetry.__str__()+"}",],\
                             [transgenblock,]])

    def gohome(self):
       self.symmetry = self.transgen.inv() ** self.symmetry
       self.symmetry.value.liste[0].liste[3] %= 1
       self.symmetry.value.liste[1].liste[3] %= 1
       self.symmetry.value.liste[2].liste[3] %= 1
       self.symmetry = self.transgen ** self.symmetry

    def __pow__(self, right):
        if isinstance(right, Pos):
            return (self.symmetry ** right) % self.transgen
        else:
            return NotImplemented

    def __rpow__(self, left):
        if isinstance(left, Operator):
            return Coset(left ** self.symmetry, left ** self.transgen)
        else:
            return NotImplemented

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
                "as the Spacegroup."
        self.transgen = transgen
        self.liste_cosets = liste_cosets

    def __str__(self):
        liste_strings = [["Spacegroup", ''], \
                         ["----------", ''], \
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

    def __rpow__(self, left):
        assert isinstance(left, Transformation), \
            "Argument must be of type Transformation."
        return Spacegroup(left ** self.transgen, \
                          [left ** coset for coset in self.liste_cosets])
    
