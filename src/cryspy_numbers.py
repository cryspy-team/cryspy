import quicktions as fr
import uncertainties as uc


class Mixed(object):
    """ Mixed
       Class for Numbers, which can be either an exact rational fraction, \
       or a float with error.

       >>> a = Mixed(fr.Fraction(1, 3))
       >>> type(a)
       <class 'cryspy_numbers.Mixed'>
       >>> print(a)
       1/3
       >>> b = Mixed(uc.ufloat(1.2, 0.1))
       >>> type(b)
       <class 'cryspy_numbers.Mixed'>
       >>> print(b)
       1.20+/-0.10
    """

    def __init__(self, value):
        assert isinstance(value, fr.Fraction) or \
            isinstance(value, uc.UFloat),\
            "Instance of Mixed must be created either by a "\
            "qicktion.Fraction or an uncertainties.core.Variable."

        self.value = value

    def __str__(self):
        return self.value.__str__()

    def __add__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 2))
            >>> c = Mixed(uc.ufloat(1.0, 0.3))
            >>> d = Mixed(uc.ufloat(1.0, 0.4))
            >>> print(a + b)
            3/4
            >>> print(c + d)
            2.0+/-0.5
            >>> print(a + c)
            1.25+/-0.30
            >>> print(c + a)
            1.25+/-0.30
        """
        if isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value + right.value)
            if isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) + right.value)
        if isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value + float(right.value))
            if isinstance(right.value, uc.UFloat):
                return Mixed(self.value + right.value)
       
    def __sub__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 2))
            >>> c = Mixed(uc.ufloat(1.0, 0.3))
            >>> d = Mixed(uc.ufloat(1.0, 0.4))
            >>> print(a - b)
            -1/4
            >>> print(c - d)
            0.0+/-0.5
            >>> print(a - c)
            -0.75+/-0.30
            >>> print(c - a)
            0.75+/-0.30
        """
        if isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value - right.value)
            if isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) - right.value)
        if isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value - float(right.value))
            if isinstance(right.value, uc.UFloat):
                return Mixed(self.value - right.value)
       
    def __mul__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(2, 1))
            >>> c = Mixed(uc.ufloat(1.0, 0.3))
            >>> d = Mixed(uc.ufloat(3.0, 0.0))
            >>> print(a * b)
            1/2
            >>> print(c * d)
            3.0+/-0.9
            >>> print(b * c)
            2.0+/-0.6
            >>> print(c * b)
            2.0+/-0.6
        """
        if isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value * right.value)
            if isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) * right.value)
        if isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value * float(right.value))
            if isinstance(right.value, uc.UFloat):
                return Mixed(self.value * right.value)

    def __truediv__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 3))
            >>> c = Mixed(uc.ufloat(1.0, 0.3))
            >>> d = Mixed(uc.ufloat(2.0, 0.0))
            >>> print(a / b)
            3/4
            >>> print(c / d)
            0.50+/-0.15
            >>> print(a / d)
            0.125+/-0
            >>> print(c / a)
            4.0+/-1.2
        """
        if isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value / right.value)
            if isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) / right.value)
        if isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value / float(right.value))
            if isinstance(right.value, uc.UFloat):
                return Mixed(self.value / right.value)


class Matrix(object):
    def __init__(self, liste):
        """
            >>> a = Mixed(fr.Fraction(1, 3))
            >>> b = Mixed(fr.Fraction(1, 4))
            >>> c = Mixed(fr.Fraction(2, 5))
            >>> d = Mixed(fr.Fraction(3, 4))
            >>> x = Mixed(uc.ufloat(1.2, 0.1))
            >>> y = Mixed(uc.ufloat(1.003, 0.001))
            >>> M = Matrix([[a, b], [c, d]])
            >>> type(M)
            <class 'cryspy_numbers.Matrix'>
            >>> print(M)
             /  1/3  1/4  \ 
             \  2/5  3/4  / 
            >>> N = Matrix([[a, b, c, d], [a, d, x, y], [b, x, d, x]])
            >>> print(N)
             /  1/3          1/4          2/5              3/4  \ 
            |   1/3          3/4  1.20+/-0.10  1.0030+/-0.0010   |
             \  1/4  1.20+/-0.10          3/4      1.20+/-0.10  / 

        """
        assert isinstance(liste, list), \
            "Object of type Matrix must be created by a list."
        for row in liste:
            assert isinstance(row, list), \
             "Object of type Matrix must be created by a list of lists"
        rowlength = len(liste[0])
        for row in liste:
            assert (len(row) == rowlength), \
              "Object of type Matrix must be created by a list of lists"\
              " of the same length each."
        for row in liste:
            for item in row:
                assert isinstance(item, Mixed), \
                    "Object of type Matrix must be created by a list "\
                    "of lists of objects of type Mixed."
        Matrix.liste = liste

    def __str__(self):
        str = ''
        length = [0]*len(self.liste[0])
        for row in self.liste:
            for (i, item) in zip(range(len(row)), row):
                length[i] = max(length[i], len(item.__str__()))

        for (j, row) in zip(range(len(self.liste)), self.liste):
            if j == 0:
                str += ' /  '
            elif j == len(self.liste) - 1:
                str += ' \\  '
            else:
                str += '|   '
            for (i, item) in zip(range(len(row)), row):
                codestr = '%' + '%i'%(length[i]) + 's  '
                str += codestr%(item.__str__())
            if j == 0:
                str += '\\ '
            elif j == len(self.liste) - 1:
                str += '/ '
            else:
                str += ' |'
            str += '\n'
        str = str[:-1]
        return str         


