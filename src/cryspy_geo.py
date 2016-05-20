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
        elif isinstance(right, Operator):
            return Operator(self.value * right.value * self.value.inv())
        else:
            raise(BaseException("I cannot apply object of type Operator"\
                " to object of type %s."%(type(right))))


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
        print("word : %s"%(word))
        has_variable = False
        index = -1
        for a in word:
            print("buchstabe: %s"%(a))
            if a.isalpha():
                word = word.replace(a, '')
                index = liste_variables.index(a)
                has_variable = True
        if word == '' or word == '-':
            if has_variable:
                word += '1'
            else:
                word += '0'
        print("soll zahl sein: %s"%(word))
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
        for i in range(3):
            result += linearterm2str(self.value.liste[i].liste, 
                ["a", "b", "c", '']) + "\n"
        result = result[:-1]
        return bp.block([["Transformation ", "a' = \nb' = \nc' = ", result],])

