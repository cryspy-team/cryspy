#  File:         ==== cryspy.numbers.py ====
#  Description:  Contains the number class Mixed which is used
#                by all cryspy classes.
#                Mixed can represent one of the following types:
#                
#                    * an exact fraction of two integers
#                    * a float with error
#                    * an integer
#                    * a float
#
#                In calculations with different types, the result
#                will have a reasonable type, for example
#                
#                    (float with error) + (exact fraction)
#                    = (float with error) .
#
#                It is recommended, that cryspy classes using Mixed-numbers
#                as arguments can use integers or floats instead, e.g.
#                
#                    >>> m = cryspy.numbers.Matrix([[1, 2], [3, 4]])
#           
#                is possible, the numbers need not to be converted
#                to Mixed-objects by the user.
#
#                Furthermore, the numbers-module exhibits a type
#                cryspy.numbers.Matrix ,
#                which represents a matrix of elements of type Mixed.

import hashlib
from copy import deepcopy
import quicktions as fr
import uncertainties as uc
from uncertainties import unumpy
import numpy as np


class Mixed(object):
    def __init__(self, value):
        assert isinstance(value, fr.Fraction) or \
            isinstance(value, uc.UFloat) or \
            isinstance(value, float) or \
            isinstance(value, int) or \
            isinstance(value, Mixed), \
            "Instance of Mixed must be created either by a "\
            "quicktion.Fraction or "\
            "an uncertainties.core.Variable "\
            "or float or int or Mixed."
        if isinstance(value, int):
            self.value = value
        elif isinstance(value, float):
            self.value = value
        elif isinstance(value, Mixed):
            self.value = value.value
        elif isinstance(value, fr.Fraction):
            if value.denominator == 1:
                self.value = value.numerator
            else:
                self.value = value
        elif isinstance(value, uc.UFloat):
            self.value = uc.ufloat(value.n, value.s)

    def __float__(self):
        if isinstance(self.value, fr.Fraction):
            return float(self.value)
        elif isinstance(self.value, uc.UFloat):
            return float(self.value.n)
        elif isinstance(self.value, int):
            return float(self.value)
        elif isinstance(self.value, float):
            return self.value

    def __str__(self):
        if isinstance(self.value, fr.Fraction):
            return self.value.__str__()
        elif isinstance(self.value, uc.UFloat):
            return self.value.format('S')
        elif isinstance(self.value, int):
            return self.value.__str__()
        elif isinstance(self.value, float):
            return self.value.__str__()
        else:
            raise(BaseException("Something is wrong with value of Mixed."))
            return ''

    def __hash__(self):
        if isinstance(self.value, fr.Fraction):
            string = 'fr'
        elif isinstance(self.value, uc.UFloat):
            string = 'uf'
        elif isinstance(self.value, int):
            string = 'in'
        elif isinstance(self.value, float):
            string = 'fl'
        string += str(hash(self.value))
        return int(hashlib.sha1(string.encode()).hexdigest(), 16) 

    def __eq__(self, right):
        right = Mixed(right)
        if isinstance(right, Mixed):
            if type(self.value) == type(right.value):
                if isinstance(self.value, fr.Fraction):
                    return self.value == right.value
                if isinstance(self.value, uc.UFloat):
                    return (self.value.n == right.value.n) \
                        and (self.value.s == right.value.s)
                if isinstance(self.value, int):
                    return self.value == right.value
                if isinstance(self.value, float):
                    return self.value == right.value
            else:
                return False
        else:
            return False

    def __abs__(self):
        if self.value < 0:
            return -self
        else:
            return self

    def __add__(self, right):
        if isinstance(right, fr.Fraction):
            right = Mixed(right)
        elif isinstance(right, uc.UFloat):
            right = Mixed(right)
        elif isinstance(right, int):
            right = Mixed(right)
        elif isinstance(right, float):
            right = Mixed(right)
        assert isinstance(right, Mixed), \
            "Cannot add object of type %s " \
            "to object of type Mixed." % (type(right))
        if isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value + right.value)
            elif isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) + right.value)
            elif isinstance(right.value, int):
                return Mixed(self.value + right.value)
            elif isinstance(right.value, float):
                return Mixed(float(self.value) + right.value)
        elif isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(deepcopy(self.value) + float(right.value))
            elif isinstance(right.value, uc.UFloat):
                return Mixed(deepcopy(self.value) + deepcopy(right.value))
            elif isinstance(right.value, int):
                return Mixed(uc.ufloat(self.value.n + right.value, self.value.s))
            elif isinstance(right.value, float):
                return Mixed(uc.ufloat(self.value.n + right.value, self.value.s))
        elif isinstance(self.value, int):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value + right.value)
            elif isinstance(right.value, uc.UFloat):
                return Mixed(self.value + deepcopy(right.value))
            elif isinstance(right.value, int):
                return Mixed(self.value + right.value)
            elif isinstance(right.value, float):
                return Mixed(self.value + right.value)
        elif isinstance(self.value, float):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value + right.value)
            if isinstance(right.value, uc.UFloat):
                return Mixed(
                    uc.ufloat(self.value + right.value.n, right.value.s))
            if isinstance(right.value, int):
                return Mixed(self.value + right.value)
            if isinstance(right.value, float):
                return Mixed(self.value + right.value)

    def __radd__(self, left):
        if isinstance(left, fr.Fraction):
            left = Mixed(left)
        elif isinstance(left, uc.UFloat):
            left = Mixed(left)
        elif isinstance(left, int):
            left = Mixed(left)
        elif isinstance(left, float):
            left = Mixed(left)
        assert isinstance(left, Mixed), \
            "Cannot add object of type Mixed to object " \
            "of type %s." % (type(left))
        return self + left

    def __sub__(self, right):
        if isinstance(right, fr.Fraction):
            right = Mixed(right)
        elif isinstance(right, uc.UFloat):
            right = Mixed(right)
        elif isinstance(right, int):
            right = Mixed(right)
        elif isinstance(right, float):
            right = Mixed(right)
        assert isinstance(right, Mixed), \
            "Cannot subtract object of type %s " \
            "from object of type Mixed." % (type(right))
        if isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value - right.value)
            elif isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) - right.value)
            elif isinstance(right.value, int):
                return Mixed(self.value - right.value)
            elif isinstance(right.value, float):
                return Mixed(float(self.value) - right.value)
        elif isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value - float(right.value))
            if isinstance(right.value, uc.UFloat):
                return Mixed(self.value - right.value)
            if isinstance(right.value, int):
                return Mixed(self.value - right.value)
            if isinstance(right.value, float):
                return Mixed(self.value - right.value)
        elif isinstance(self.value, int):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value - right.value)
            elif isinstance(right.value, uc.UFloat):
                return Mixed(self.value - right.value)
            elif isinstance(right.value, int):
                return Mixed(self.value - right.value)
            elif isinstance(right.value, float):
                return Mixed(self.value - right.value)
        elif isinstance(self.value, float):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value - right.value)
            elif isinstance(right.value, uc.UFloat):
                return Mixed(self.value - right.value)
            elif isinstance(right.value, int):
                return Mixed(self.value - right.value)
            elif isinstance(right.value, float):
                return Mixed(self.value - right.value)

    def __rsub__(self, left):
        if isinstance(left, fr.Fraction):
            left = Mixed(left)
        elif isinstance(left, uc.UFloat):
            left = Mixed(left)
        elif isinstance(left, int):
            left = Mixed(left)
        elif isinstance(left, float):
            left = Mixed(left)
        if isinstance(left, Mixed):
            return left - self
        else:
            return NotImplemented

    def __mul__(self, right):
        if isinstance(right, fr.Fraction):
            right = Mixed(right)
        elif isinstance(right, uc.UFloat):
            right = Mixed(right)
        elif isinstance(right, int):
            right = Mixed(right)
        elif isinstance(right, float):
            right = Mixed(right)
        if not(isinstance(right, Mixed)):
            return NotImplemented
        if isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value * right.value)
            elif isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) * right.value)
            elif isinstance(right.value, int):
                if right.value == 0:
                    return Mixed(0)
                else:
                    return Mixed(self.value * right.value)
            elif isinstance(right.value, float):
                return Mixed(float(self.value) * right.value)
        elif isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value * float(right.value))
            elif isinstance(right.value, uc.UFloat):
                return Mixed(self.value * right.value)
            elif isinstance(right.value, int):
                if right.value == 0:
                    return Mixed(0)
                else:
                    return Mixed(self.value * right.value)
            elif isinstance(right.value, float):
                return Mixed(self.value * right.value)
        elif isinstance(self.value, int):
            if self.value == 0:
                return Mixed(0)
            else:
                if isinstance(right.value, fr.Fraction):
                    return Mixed(self.value * right.value)
                elif isinstance(right.value, uc.UFloat):
                    return Mixed(self.value * right.value)
                elif isinstance(right.value, int):
                    if right.value == 0:
                        return Mixed(0)
                    else:
                        return Mixed(self.value * right.value)
                elif isinstance(right.value, float):
                    return Mixed(self.value * right.value)
        elif isinstance(self.value, float):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value * float(right.value))
            elif isinstance(right.value, uc.UFloat):
                return Mixed(self.value * right.value)
            elif isinstance(right.value, int):
                if right.value == 0:
                    return Mixed(0)
                else:
                    return Mixed(self.value * right.value)
            elif isinstance(right.value, float):
                return Mixed(self.value * right.value)


    def __rmul__(self, left):
        if isinstance(left, fr.Fraction):
            left = Mixed(left)
        elif isinstance(left, uc.UFloat):
            left = Mixed(left)
        elif isinstance(left, int):
            left = Mixed(left)
        elif isinstance(left, float):
            left = Mixed(left)
        if isinstance(left, Mixed):
            return left * self
        else:
            return NotImplemented

    def __truediv__(self, right):
        if isinstance(right, fr.Fraction):
            right = Mixed(right)
        elif isinstance(right, uc.UFloat):
            right = Mixed(right)
        elif isinstance(right, int):
            right = Mixed(right)
        elif isinstance(right, float):
            right = Mixed(right)
        if not isinstance(right, Mixed):
            return NotImplemented
        if isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value / right.value)
            elif isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) / right.value)
            elif isinstance(right.value, int):
                return Mixed(self.value / right.value)
            elif isinstance(right.value, float):
                return Mixed(float(self.value) / right.value)
        elif isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value / float(right.value))
            elif isinstance(right.value, uc.UFloat):
                return Mixed(self.value / right.value)
            elif isinstance(right.value, int):
                return Mixed(self.value / right.value)
            elif isinstance(right.value, float):
                return Mixed(self.value / right.value)
        elif isinstance(self.value, int):
            if self.value == 0:
                return Mixed(0)
            else:
                if isinstance(right.value, fr.Fraction):
                    return Mixed(self.value / right.value)
                elif isinstance(right.value, uc.UFloat):
                    return Mixed(self.value / right.value)
                elif isinstance(right.value, int):
                    return Mixed(fr.Fraction(self.value, right.value))
                elif isinstance(right.value, float):
                    return Mixed(self.value / right.value)
        elif isinstance(self.value, float):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value / float(right.value))
            elif isinstance(right.value, uc.UFloat):
                return Mixed(self.value / right.value)
            elif isinstance(right.value, int):
                return Mixed(self.value / right.value)
            elif isinstance(right.value, float):
                return Mixed(self.value / right.value)

    def __rtruediv__(self, left):
        if isinstance(left, fr.Fraction):
            left = Mixed(left)
        elif isinstance(left, uc.UFloat):
            left = Mixed(left)
        elif isinstance(left, float):
            left = Mixed(left)
        elif isinstance(left, int):
            left = Mixed(left)
        if isinstance(left, Mixed):
            return left / self
        else:
            return NotImplemented

    def __neg__(self):
        return (-1) * self


    def __mod__(self, right):
        if isinstance(right, int):
            right = Mixed(right)
        if isinstance(right, Mixed):
            if isinstance(right.value, int):
                if isinstance(self.value, fr.Fraction):
                    return Mixed(self.value % right.value)
                elif isinstance(self.value, uc.UFloat):
                    return Mixed(self.value % right.value)
                elif isinstance(self.value, int):
                    return Mixed(self.value % right.value)
                elif isinstance(self.value, float):
                    return Mixed(self.value % right.value)
            else:
                return NotImplemented
        else:
            return NotImplemented

pi = Mixed(3.141592653589793)


def sqrt(number):
    number = Mixed(number)
    if isinstance(number.value, fr.Fraction):
        p = np.sqrt(number.value.numerator)
        q = np.sqrt(number.value.denominator)
        if (p % 1 == 0) and (q % 1 == 0):
            return Mixed(fr.Fraction(int(p), int(q)))
        else:
            return Mixed(np.sqrt(float(number.value)))
    elif isinstance(number.value, uc.UFloat):
        return Mixed(unumpy.sqrt(number.value).item())
    elif isinstance(number.value, int):
        s = np.sqrt(number.value)
        if s % 1 == 0:
            return Mixed(int(s))
        else:
            return Mixed(s)
    elif isinstance(number.value, float):
        return Mixed(float(np.sqrt(number.value)))


def deg2rad(number):
    assert isinstance(number, Mixed) \
        or isinstance(number, fr.Fraction) \
        or isinstance(number, uc.UFloat) \
        or isinstance(number, int) \
        or isinstance(number, float), \
        "Argument must be of type Mixed, quicktions.Fraction, " \
        "uncertainties.UFloat, int or float."
    return number * pi / 180


def rad2deg(number):
    assert isinstance(number, Mixed) \
        or isinstance(number, fr.Fraction) \
        or isinstance(number, uc.UFloat) \
        or isinstance(number, int) \
        or isinstance(number, float), \
        "Argument must be of type Mixed, quicktions.Fraction, " \
        "uncertainties.UFloat, int or float."
    return number / pi * 180


def sin(number):
    if isinstance(number, fr.Fraction):
        number = Mixed(number)
    elif isinstance(number, uc.UFloat):
        number = Mixed(number)
    elif isinstance(number, float):
        number = Mixed(number)
    elif isinstance(number, int):
        number = Mixed(number)
    assert isinstance(number, Mixed), \
        "Connot calculate cos of an object of type %s." % (type(number))
    if isinstance(number.value, fr.Fraction):
        return Mixed(np.sin(float(number.value)))
    elif isinstance(number.value, uc.UFloat):
        return Mixed(unumpy.sin(number.value).item())
    elif isinstance(number.value, float):
        return Mixed(np.sin(number.value))
    elif isinstance(number.value, int):
        return Mixed(np.sin(number.value))


def cos(number):
    if isinstance(number, fr.Fraction):
        number = Mixed(number)
    elif isinstance(number, uc.UFloat):
        number = Mixed(number)
    elif isinstance(number, float):
        number = Mixed(number)
    elif isinstance(number, int):
        number = Mixed(number)
    assert isinstance(number, Mixed), \
        "Connot calculate cos of an object of type %s." % (type(number))
    if isinstance(number.value, fr.Fraction):
        return Mixed(np.cos(float(number.value)))
    elif isinstance(number.value, uc.UFloat):
        return Mixed(unumpy.cos(number.value).item())
    elif isinstance(number.value, float):
        return Mixed(np.cos(number.value))
    elif isinstance(number.value, int):
        return Mixed(np.cos(number.value))


def arccos(number):
    if isinstance(number, fr.Fraction):
        number = Mixed(number)
    elif isinstance(number, uc.UFloat):
        number = Mixed(number)
    elif isinstance(number, int):
        number = Mixed(number)
    elif isinstance(number, float):
        number = Mixed(number)
    assert isinstance(number, Mixed), \
        "Cannot calculate arccos of object of type %s." % (type(number))
    if isinstance(number.value, uc.UFloat):
        return Mixed(unumpy.arccos(number.value).item())
    elif isinstance(number.value, fr.Fraction):
        return Mixed(np.arccos(float(number.value)))
    elif isinstance(number.value, int):
        return Mixed(np.arccos(number.value))
    elif isinstance(number.value, float):
        return Mixed(np.arccos(number.value))


class Row(object):
    def __init__(self, liste):
        assert isinstance(liste, list), \
            "Object of type Row must be created by a list."
        length = len(liste)
        assert (length > 0), \
            "Object of type Row must be created by a non-empty list."
        self.liste = deepcopy(liste)
        for i in range(len(liste)):
            if isinstance(self.liste[i], fr.Fraction):
                self.liste[i] = Mixed(self.liste[i])
            elif isinstance(self.liste[i], uc.UFloat):
                self.liste[i] = Mixed(self.liste[i])
            elif isinstance(self.liste[i], int):
                self.liste[i] = Mixed(self.liste[i])
            elif isinstance(self.liste[i], float):
                self.liste[i] = Mixed(self.liste[i])
        for item in self.liste:
            assert isinstance(item, Mixed), \
                "Object of type Row cannot be created by an object of type " \
                "%s in the list" % (type(item))

    def __len__(self):
        return len(self.liste)

    def __eq__(self, right):
        if isinstance(right, Row):
            if len(self) == len(right):
                return min([(self.liste[i] == right.liste[i])
                    for i in range(len(self))])
            else:
                return False
        else:
            return False

    def __str__(self):
        str = "(  "
        for item in self.liste:
            str += item.__str__()
            str += "  "
        str += ")"
        return str

    def canonical(dim, i):
        assert isinstance(dim, int), \
            "Canonical Row must be created by a dimension of type int."
        assert isinstance(i, int), \
            "Canonical Row must be cretated by an index of type int."
        assert (dim > 0), \
            "Canonical Row must be cretated by a dimension > 0."
        assert (i >= 0) and (i < dim), \
            "Canonical Row must be created by an index i with 0 <= i < dim."
        def kronecker(i, j):
            if (i == j):
                return Mixed(fr.Fraction(1, 1))
            else:
                return Mixed(fr.Fraction(0, 1))
        return Row([kronecker(i, j) for j in range(dim)])

    def block(self, i1, i2):
        length = len(self)
        assert isinstance(i1, int) and isinstance(i2, int), \
            "For cutting a block out of a Row, use integers of type int!"
        assert (i1 >= 0) and (i2 >= 0) and (i1 <= length) and (i2 <= length), \
            "For cutting a block out of a Row, use integers between "\
            "0 and the length of the Row!"
        assert (i1 < i2), \
            "For cutting a block out of a Row, use integers (i1, i2) with "\
            "i1 < i2 !"
        return Row([self.liste[i] for i in range(i1, i2)])

    def __add__(self, right):
        assert isinstance(right, Row), \
            "Only object of type Row can be added to object of type Row."
        assert (len(self) == len(right)), \
            "Two rows must have the same length to be added."
        return Row([self.liste[i] + right.liste[i] for i in range(len(self))])

    def __sub__(self, right):
        assert isinstance(right, Row), \
            "Only object of type Row can be added to object of type Row."
        assert (len(self) == len(right)), \
            "Two rows must have the same length to be added."
        return Row([self.liste[i] - right.liste[i] for i in range(len(self))])

    def __mul__(self, right):
        right = Mixed(right)
        return Row([self.liste[i] * right for i in range(len(self))])

    def __rmul__(self, left):
        left = Mixed(left)
        if isinstance(left, Mixed):
            return self * left
        else:
            return NotImplemented

    def __neg__(self):
        return Row([-number for number in self.liste])


class Matrix(object):
    def __init__(self, liste):
        assert isinstance(liste, list), \
            "Object of type Matrix must be created by a list."
        for i in range(len(liste)):
            if isinstance(liste[i], list):
                liste[i] = Row(liste[i])
        rowlength = len(liste[0])
        for row in liste:
            assert (len(row) == rowlength), \
              "Object of type Matrix must be created by a list of objects of type "\
              "Row of the same length each."
        self.liste = deepcopy(liste)

    def shape(self):
        return (len(self.liste), len(self.liste[0]))

    def __eq__(self, right):
        if isinstance(right, Matrix):
            if (self.shape() == right.shape()):
                return min([(self.liste[i] == right.liste[i])
                    for i in range(self.shape()[0])])
            else:
                return False
        else:
            return False

    def __str__(self):
        str = ''
        length = [0]*self.shape()[1]
        for row in self.liste:
            for (i, item) in zip(range(len(row)), row.liste):
                length[i] = max(length[i], len(item.__str__()))
        for (i, row) in zip(range(len(self.liste)), self.liste):
            if self.shape()[0] == 1:
                str += ' <  '
            elif i == 0:
                str += ' /  '
            elif i == len(self.liste) - 1:
                str += ' \\  '
            else:
                str += '|   '
            for (j, item) in zip(range(len(row)), row.liste):
                codestr = '%' + '%i' % (length[j]) + 's  '
                str += codestr % (item.__str__())
            if self.shape()[0] == 1:
                str += '> '
            elif i == 0:
                str += '\\ '
            elif i == len(self.liste) - 1:
                str += '/ '
            else:
                str += ' |'
            str += '\n'
        str = str[:-1]
        return str


    def __add__(self, right):
        if isinstance(right, Matrix):
            assert self.shape() == right.shape(), \
                "Two Matrices must have the same shape for Operator +"
            (numrows, numcolumns) = self.shape()
            return Matrix([
                Row([self.liste[i].liste[j] + right.liste[i].liste[j]
                for j in range(numcolumns)])
                for i in range(numrows)])
        else:
            return NotImplemented

    def __sub__(self, right):
        if isinstance(right, Matrix):
            assert self.shape() == right.shape(), \
                "Two Matrices must have the same shape for Operator +"
            (numrows, numcolumns) = self.shape()
            return Matrix([
                Row([self.liste[i].liste[j] - right.liste[i].liste[j]
                for j in range(numcolumns)])
                for i in range(numrows)])
        else:
            return NotImplemented


    def __mul__(self, right):
        if isinstance(right, fr.Fraction):
            right = Mixed(right)
        elif isinstance(right, uc.UFloat):
            right = Mixed(right)
        elif isinstance(right, int):
            right = Mixed(right)
        elif isinstance(right, float):
            right = Mixed(right)
        if isinstance(right, Mixed):
            (numrows, numcols) = self.shape()
            return Matrix(
                [
                    Row([self.liste[i].liste[j] * right for j in range(numcols)])
                    for i in range(numrows)
                ]
            )
        elif isinstance(right, Matrix):
            (numrows1, numcols1) = self.shape()
            (numrows2, numcols2) = right.shape()
            assert (numcols1 == numrows2), \
                "Matrix-Multiplication needs two matrices, with "\
                " width of first matrix equals height of second matrix."
            def matrixitem(i, j):
                s = Mixed(fr.Fraction(0, 1))
                for k in range(numcols1):
                    s += self.liste[i].liste[k] * right.liste[k].liste[j]
                return s
            return Matrix(
                [
                   Row([matrixitem(i, j) for j in range(numcols2)])
                   for i in range(numrows1)
                ]
            )
        else:
            return NotImplemented

    def __rmul__(self, left):
        if isinstance(left, fr.Fraction):
            left = Mixed(left)
        elif isinstance(left, uc.UFloat):
            left = Mixed(left)
        elif isinstance(left, int):
            left = Mixed(left)
        elif isinstance(left, float):
            left = Mixed(left)
        if isinstance(left, Mixed):
            return self * left
        else:
            return NotImplemented

    def __neg__(self):
        return Matrix([-row for row in self.liste])

    def onematrix(dim):
        assert isinstance(dim, int), \
            "Onematrix must be created via a dimension of type int."
        assert (dim > 0), \
            "Dimension for creating onematrix must be > 0."
        return Matrix([Row.canonical(dim, i) for i in range(dim)])

    def block(self, i1, i2, j1, j2):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> eins = Mixed(fr.Fraction(1, 1))
            >>> null = Mixed(fr.Fraction(0, 1))
            >>> x = Mixed(uc.ufloat(3.75, 0.23))
            >>> z = Mixed(fr.Fraction(5, 1))
            >>> M = Matrix([Row([a, b]), Row([c, x]), Row([eins, z])])
            >>> print(M.block(0, 2, 0, 1))
             /  1/4  \ 
             \  3/7  / 
        """
        assert isinstance(i1, int) and isinstance(i2, int) \
            and isinstance(j1, int) and isinstance(j2, int), \
            "For cutting a block out of a matrix, use indexes of type integer!"
        (numrows, numcols) = self.shape()
        assert (i1 <= numrows) and (i2 <= numrows)\
            and (j1 <= numcols) and (j2 <= numcols), \
            "For cutting a block out of a matrix, use integers, which are between "\
            "0 and num of rows / num of cols"
        assert (i1 < i2) and (j1 < j2), \
            "For cutting a block out of a matrix, use integers (i1, i2, j1, j2) "\
            "with i1 < i2 and j1 < j2."
        return Matrix([self.liste[i].block(j1, j2) for i in range(i1, i2)])

    def swap_rows(self, i, j):
        assert isinstance(i, int) and isinstance(j, int), \
            "The indices for swapping rows must be of type integer."
        (numrows, numcols) = self.shape()
        assert (i >= 0) and (i < numrows) and (j >= 0) and (j < numrows), \
            "The index for swapping rows must be >= 0 and < num of rows."
        if (i == j):
            return self
        else:
            indexes = list(range(numrows))
            (indexes[i], indexes[j]) = (j, i)
            return Matrix([self.liste[index] for index in indexes])

    def vglue(left, right):
        (numrows1, numcols1) = left.shape()
        (numrows2, numcols2) = right.shape()
        assert (numcols1 == numcols2), \
            "I cannot vglue (vertical glue) Matrices with different numbers " \
            "of cols."
        def row(i):
            if i < numrows1:
                return left.liste[i]
            else:
                return right.liste[i - numrows1]
        return Matrix([row(i) for i in range(numrows1 + numrows2)])


    def subtract_x_times_rowj_from_rowi(self, x, i, j):
        new = deepcopy(self)
        new.liste[i] = self.liste[i] + self.liste[j] * (Mixed(-1) * x)
        return new

    def inv(self):
        (numrows, numcols) = self.shape()
        assert (numrows == numcols), \
            "I can invert square matrices only (num of rows == num of cols)."
        dim = numrows
        right = Matrix.onematrix(dim) 
        def make_triangle(self, right):
            (dim, dim) = self.shape()
            for rownumber in range(dim - 1):
                i = rownumber
                while (self.liste[i].liste[rownumber] == Mixed(0)) \
                    and (i < dim):
                    i += 1

                assert (i < dim), \
                    "Cannot transform matrix to triangle matrix."

                self = self.swap_rows(rownumber, i)
                right = right.swap_rows(rownumber, i)


                for i in range(rownumber + 1, dim):
                    x = self.liste[i].liste[rownumber] \
                    / self.liste[rownumber].liste[rownumber]
                    self = self.subtract_x_times_rowj_from_rowi(x, i, rownumber)
                    right = right.subtract_x_times_rowj_from_rowi(x, i, rownumber)
            return (self, right)
        def make_diagonal(self, right):
            (dim, dim) = self.shape()
            for rownumber in range(1, dim):
                for i in range(0, rownumber):
                    x = self.liste[i].liste[rownumber] \
                    / self.liste[rownumber].liste[rownumber]
                    self = self.subtract_x_times_rowj_from_rowi(x, i, rownumber)
                    right = right.subtract_x_times_rowj_from_rowi(x, i, rownumber)
            return(self, right)
        def make_one(self, right):
            new = deepcopy(self)
            (dim, dim) = self.shape()
            for rownumber in range(0, dim):
                x = self.liste[rownumber].liste[rownumber]
                new.liste[rownumber] = self.liste[rownumber] * (Mixed(1) / x)
                right.liste[rownumber] = right.liste[rownumber] * (Mixed(1) / x)
            return (new, right)
        (self, right) = make_triangle(self, right)
        (self, right) = make_diagonal(self, right)
        (self, right) = make_one(self, right)
        return right   

    def transpose(self):
        shape = self.shape()
        return Matrix([
                   Row([
                       self.liste[j].liste[i]
                       for j in range(shape[0])
                   ])
                   for i in range(shape[1])
               ])

    def delete_ith_row_and_first_column(self, i):
        assert isinstance(i, int), \
            "Index of Row must be an integer."
        assert (0 <= i < self.shape()[0]), \
            "Index of Row must be between 0 and " \
            "number of Row - 1."

        liste = []
        count = 0
        for row in self.liste:
            if count != i:
                liste.append(Row(row.liste[1:]))
            count += 1

        return Matrix(liste)



    def det(self):
        # Returns the determinant.
        shape = self.shape()
        assert shape[0] == shape[1], \
            "Matrix must be a square matrix" \
            "for taking the determinant."

        if shape[0] == 1:
            return self.liste[0].liste[0]
        else:
            result = 0
            for i in range(0, shape[0]):
                M = self.delete_ith_row_and_first_column(i)
                result += self.liste[i].liste[0] * (-1)**i * M.det()

            return result


    def delete_translation(self):
        # If a 4x4-Matrix has the shape
        #
        #  / *  *  *  * \
        # |  *  *  *  *  |
        # |  *  *  *  *  |
        #  \ 0  0  0  1 / ,
        #
        # it is reduced to
        #
        #  / *  *  *  0 \
        # |  *  *  *  0  |
        # |  *  *  *  0  |
        #  \ 0  0  0  1 / .

        assert self.shape() == (4, 4), \
            "Matrix must be a 4x4-Matrix"

        assert self.block(3, 4, 0, 4) == Matrix([[0, 0, 0, 1]]), \
            "Matrix must be of the form\n" \
            "  / * * * * \  \n" \
            " |  * * * *  | \n" \
            " |  * * * *  | \n" \
            "  \ 0 0 0 1 /  "

        a = self.liste[0].liste[0]
        b = self.liste[0].liste[1]
        c = self.liste[0].liste[2]
        d = self.liste[1].liste[0]
        e = self.liste[1].liste[1]
        f = self.liste[1].liste[2]
        g = self.liste[2].liste[0]
        h = self.liste[2].liste[1]
        i = self.liste[2].liste[2]

        return Matrix([[a, b, c, 0],
                       [d, e, f, 0],
                       [g, h, i, 0],
                       [0, 0, 0, 1]])

