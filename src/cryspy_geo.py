import cryspy_numbers as nb
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
            return Pos(self.value * right.value)
        elif isinstance(right, Operator):
            return Operator(self.value * right.value * self.value.inv())
        else:
            raise(BaseException("I cannot apply object of type Operator"\
                " to object of type %s."%(type(right))))




class Symmetry(Operator):
    def __str__(self):
        def row2term(row):
            assert isinstance(row, nb.Row), \
                "Argument must be of type Row."
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
            result =  prefactor(row.liste[0], 'x') \
                    + prefactor(row.liste[1], 'y') \
                    + prefactor(row.liste[2], 'z') \
                    + prefactor(row.liste[3], '')
            if result[0] == '+':
                result = result[1:]
            return result
        result =  row2term(self.value.liste[0]) + ',' \
                + row2term(self.value.liste[1]) + ',' \
                + row2term(self.value.liste[2])
        return result
            

