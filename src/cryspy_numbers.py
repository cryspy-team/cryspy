from copy import deepcopy
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
       1.20(10)
    """

    def __init__(self, value):
        assert isinstance(value, fr.Fraction) or \
            isinstance(value, uc.UFloat) or \
            isinstance(value, float) or \
            isinstance(value, int), \
            "Instance of Mixed must be created either by a "\
            "qicktion.Fraction or an uncertainties.core.Variable or float or int."
        if isinstance(value, int):
            self.value = fr.Fraction(value, 1)
        elif isinstance(value, float):
            self.value = uc.ufloat(value, 0.0)
        else:
            self.value = value

    def __str__(self):
        if isinstance(self.value, fr.Fraction):
            return self.value.__str__()
        elif isinstance(self.value, uc.UFloat):
            return self.value.format('S')
        else:
            raise(BaseException("Something is wrong with value of Mixed."))
            return ''

    def __add__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 2))
            >>> c = Mixed(uc.ufloat(1.0, 0.3))
            >>> d = Mixed(uc.ufloat(1.0, 0.4))
            >>> print(a + b)
            3/4
            >>> print(c + d)
            2.0(5)
            >>> print(a + c)
            1.25(30)
            >>> print(c + a)
            1.25(30)
            >>> print(a + 0.5)
            0.75(0)
            >>> print(a + 1)
            5/4
        """
        if isinstance(right, int):
            return Mixed(self.value + right)
        elif isinstance(right, float):
            return Mixed(self.value + right)
        elif isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value + right.value)
            if isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) + right.value)
        elif isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value + float(right.value))
            if isinstance(right.value, uc.UFloat):
                return Mixed(self.value + right.value)
       
    def __radd__(self, left):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> print(0.5 + a)
            0.75(0)
            >>> print(1 + a)
            5/4
        """
        if isinstance(left, int):
            return Mixed(self.value + left)
        elif isinstance(left, float):
            return Mixed(self.value + left)
        else:
            raise(BaseException("Error in __radd__."))

    def __sub__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 2))
            >>> c = Mixed(uc.ufloat(1.0, 0.3))
            >>> d = Mixed(uc.ufloat(1.0, 0.4))
            >>> print(a - b)
            -1/4
            >>> print(c - d)
            0.0(5)
            >>> print(a - c)
            -0.75(30)
            >>> print(c - a)
            0.75(30)
            >>> print(a - 0.5)
            -0.25(0)
            >>> print(a - 1)
            -3/4
        """
        if isinstance(right, int):
            return Mixed(self.value - right)
        elif isinstance(right, float):
            return Mixed(self.value - right)
        elif isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value - right.value)
            if isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) - right.value)
        elif isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value - float(right.value))
            if isinstance(right.value, uc.UFloat):
                return Mixed(self.value - right.value)
       
    def __rsub__(self, left):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> print(0.5 - a)
            0.25(0)
            >>> print(1 - a)
            3/4
        """
        if isinstance(left, int):
            return Mixed(left - self.value)
        elif isinstance(left, float):
            return Mixed(left - self.value)
        else:
            raise(BaseException("Error in __rsub__."))

    def __mul__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(2, 1))
            >>> c = Mixed(uc.ufloat(1.0, 0.3))
            >>> d = Mixed(uc.ufloat(3.0, 0.0))
            >>> print(a * b)
            1/2
            >>> print(c * d)
            3.0(9)
            >>> print(b * c)
            2.0(6)
            >>> print(c * b)
            2.0(6)
            >>> print(a * 0.5)
            0.125(0)
            >>> print(a * 2)
            1/2
        """
        if isinstance(right, int):
            return Mixed(self.value * right)
        elif isinstance(right, float):
            return Mixed(self.value * right)
        elif isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value * right.value)
            if isinstance(right.value, uc.UFloat):
                if self.value == fr.Fraction(0, 1):
                    return Mixed(fr.Fraction(0, 1))
                else:
                    return Mixed(float(self.value) * right.value)
        elif isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                if right.value == fr.Fraction(0, 1):
                    return Mixed(fr.Fraction(0, 1))
                else:
                    return Mixed(self.value * float(right.value))
            if isinstance(right.value, uc.UFloat):
                return Mixed(self.value * right.value)

    def __rmul__(self, left):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(2, 1))
            >>> c = Mixed(uc.ufloat(1.0, 0.3))
            >>> d = Mixed(uc.ufloat(3.0, 0.0))
            >>> print(0.5 * a)
            0.125(0)
            >>> print(2 * a)
            1/2
        """
        if isinstance(left, int):
            if left == 0:
                return Mixed(fr.Fraction(0, 1))
            else:
                return Mixed(left * self.value)
        elif isinstance(left, float):
            return Mixed(left * self.value)
        else:
            raise(BaseException("Error in __rmul__."))

    def __truediv__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 3))
            >>> c = Mixed(uc.ufloat(1.0, 0.3))
            >>> d = Mixed(uc.ufloat(2.0, 0.0))
            >>> print(a / b)
            3/4
            >>> print(c / d)
            0.50(15)
            >>> print(a / d)
            0.125(0)
            >>> print(c / a)
            4.0(1.2)
            >>> print(a/0.5)
            0.5(0)
            >>> print(a/2)
            1/8
        """
        if isinstance(right, int):
            return Mixed(self.value / right)
        elif isinstance(right, float):
            return Mixed(self.value / right)
        elif isinstance(self.value, fr.Fraction):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value / right.value)
            if isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) / right.value)
        elif isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                return Mixed(self.value / float(right.value))
            if isinstance(right.value, uc.UFloat):
                return Mixed(self.value / right.value)

    def __rtruediv__(self, left):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> print(0.5/a)
            2.0(0)
            >>> print(2/a)
            8
        """
        if isinstance(left, int):
            return Mixed(left / self.value)
        elif isinstance(left, float):
            return Mixed(left / self.value)
        else:
            raise(BaseException("Error in __rtruediv__."))

    def __pos__(self):
        return self

    def __neg__(self):
        """
            >>> a = Mixed(fr.Fraction(1, 2))
            >>> print(-a)
            -1/2
        """
        return (-1) * self

    def __eq__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1,2))
            >>> b = Mixed(uc.ufloat(1.2, 0.1))
            >>> c = Mixed(uc.ufloat(1.2, 0.1))
            >>> a == b
            False
            >>> a == a
            True
            >>> b == b
            True
            >>> b == c
            True
            >>> a == 0.5
            True
            >>> b == 1.2
            False
            >>> 0.5 == a
            True
        """
        if isinstance(right, Mixed):
            if isinstance(self.value, uc.UFloat):
                if isinstance(right.value, uc.UFloat):
                    return ((self.value.n, self.value.s) \
                        == (right.value.n, right.value.s))
                else:
                    return False
            else:
                return (self.value == right.value)
        else:
            try:
                return (self.value == right)
            except:
                raise(BaseException("Object of this type cannot"\
                                    "be compared with object of tpye"\
                                    "Mixed."))

    def __mod__(self, right):
        """
           >>> a = Mixed(fr.Fraction(5, 2))
           >>> b = Mixed(fr.Fraction(9, 4))
           >>> c = Mixed(uc.ufloat(1.2, 0.1))
           >>> d = Mixed(uc.ufloat(2.5, 0.3))
           >>> print(a % b)
           1/4
           >>> print("%8f"%((a % c).value.n))
           0.100000
           >>> print(c % a)
           1.2(0)
           >>> print(c % d)
           1.20(10)
           >>> print(a % 1)
           1/2
           >>> print(a % 0.5)
           0.0(0)
           >>> print(c % 1)
           0.20(10)
           >>> print(c % 0.5)
           0.20(10)
        """    
        assert isinstance(right, Mixed) \
            or isinstance(right, int) \
            or isinstance(right, float), \
            "Cannot calculate modulo of objects of type %s and %s"%\
            (type(self), type(right))
        if isinstance(right, Mixed):
            if isinstance(self.value, uc.UFloat) \
                and isinstance(right.value, fr.Fraction):
                return Mixed(self.value.n % float(right.value))
            elif isinstance(self.value, fr.Fraction) \
                and isinstance(right.value, uc.UFloat):
                return Mixed(float(self.value) % right.value.n)
            else:
                return Mixed(self.value % right.value)
        elif isinstance(right, int) or isinstance(right, float):
            return Mixed(self.value % right)

class Row(object):
    """
        >>> A = Row([Mixed(fr.Fraction(2, 3)), Mixed(fr.Fraction(3, 4))])
        >>> print(A)
        (  2/3  3/4  )
        >>> A = Row([0.1, 5])
        >>> print(A)
        (  0.1(0)  5  )
    """
    def __init__(self, liste):
        assert isinstance(liste, list), \
            "Object of type Row must be created by a list."
        length = len(liste)
        assert (length > 0), \
            "Object of type Row must be created by a non-empty list."
        for item in liste:
            assert isinstance(item, Mixed) or \
                isinstance(item, int) or \
                isinstance(item, float), \
                "Object of type Row must be created by a list of " \
                "objects of type Mixed or int or float."
        self.liste = deepcopy(liste)
        for i in range(len(self.liste)):
            if isinstance(self.liste[i], int):
                self.liste[i] = Mixed(fr.Fraction(self.liste[i]))
            if isinstance(self.liste[i], float):
                self.liste[i] = Mixed(uc.ufloat(self.liste[i], 0.0))
    
    def len(self):
        return len(self.liste)
    
    def __str__(self):
        str = "(  "
        for item in self.liste:
            str += item.__str__()
            str += "  "
        str += ")"
        return str
    
    def canonical(dim, i):
        """
            >>> print(Row.canonical(5, 3))
            (  0  0  0  1  0  )
        """
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
        """
            >>> a = Mixed(fr.Fraction(1, 3))
            >>> b = Mixed(fr.Fraction(1, 4))
            >>> c = Mixed(fr.Fraction(2, 5))
            >>> d = Mixed(uc.ufloat(1.2, 0.1))
            >>> R = Row([a, b, c, d])
            >>> print(R.block(1, 3))
            (  1/4  2/5  )
        """
        length = self.len()
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
        """
            >>> A = Row([Mixed(fr.Fraction(1, 2)), Mixed(fr.Fraction(2, 3))])
            >>> B = Row([Mixed(fr.Fraction(3, 4)), Mixed(fr.Fraction(4, 5))])
            >>> print(A + B)
            (  5/4  22/15  )
        """
        assert isinstance(right, Row), \
            "Only object of type Row can be added to object of type Row."
        assert (self.len() == right.len()), \
            "Two rows must have the same length to be added."
        return Row([self.liste[i] + right.liste[i] for i in range(self.len())])

    def __sub__(self, right):
        """
            >>> A = Row([Mixed(fr.Fraction(1, 2)), Mixed(fr.Fraction(2, 3))])
            >>> B = Row([Mixed(fr.Fraction(3, 4)), Mixed(fr.Fraction(4, 5))])
            >>> print(A - B)
            (  -1/4  -2/15  )
        """
        assert isinstance(right, Row), \
            "Only object of type Row can be added to object of type Row."
        assert (self.len() == right.len()), \
            "Two rows must have the same length to be added."
        return Row([self.liste[i] - right.liste[i] for i in range(self.len())])

    def __mul__(self, right):
        assert isinstance(right, Mixed), \
            "Only object of type Mixed can be multiplied with object of type Row."
        
        return Row([self.liste[i] * right for i in range(self.len())])

    def __eq__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 3))
            >>> b = Mixed(fr.Fraction(1, 4))
            >>> c = Mixed(fr.Fraction(2, 5))
            >>> R1 = Row([a, b, c])
            >>> R2 = Row([a, b, c])
            >>> R3 = Row([a, b, b])
            >>> R4 = Row([a, b])
            >>> R1 == R2
            True
            >>> R1 == R3
            False
            >>> R1 == R4
            False
            >>> R1 == a
            False
        """
        if isinstance(right, Row):
            if self.len() == right.len():
                return min([(self.liste[i] == right.liste[i]) \
                    for i in range(self.len())])
            else:
                return False
        else:
            return False


class Matrix(object):
    def __init__(self, liste):
        """
            >>> a = Mixed(fr.Fraction(1, 3))
            >>> b = Mixed(fr.Fraction(1, 4))
            >>> c = Mixed(fr.Fraction(2, 5))
            >>> x = Mixed(uc.ufloat(1.2, 0.1))
            >>> M = Matrix([Row([a, b]), Row([c, x])])
            >>> type(M)
            <class 'cryspy_numbers.Matrix'>
        """
        assert isinstance(liste, list), \
            "Object of type Matrix must be created by a list."
        for row in liste:
            assert isinstance(row, Row), \
             "Object of type Matrix must be created by a list of objects of type " \
             "Row."
        rowlength = liste[0].len()
        for row in liste:
            assert (row.len() == rowlength), \
              "Object of type Matrix must be created by a list of objects of type "\
              "Row of the same length each."
        self.liste = deepcopy(liste)

    def __str__(self):
        """
            >>> a = Mixed(fr.Fraction(1, 3))
            >>> b = Mixed(fr.Fraction(1, 4))
            >>> c = Mixed(fr.Fraction(2, 5))
            >>> d = Mixed(fr.Fraction(3, 4))
            >>> x = Mixed(uc.ufloat(1.2, 0.1))
            >>> y = Mixed(uc.ufloat(1.003, 0.001))
            >>> M = Matrix([Row([a, b]), Row([c, d])])
            >>> print(M)
             /  1/3  1/4  \ 
             \  2/5  3/4  / 
            >>> N = Matrix([Row([a, b, c, d]), Row([a, d, x, y]), Row([b, x, d, x])])
            >>> print(N)
             /  1/3       1/4       2/5         3/4  \ 
            |   1/3       3/4  1.20(10)  1.0030(10)   |
             \  1/4  1.20(10)       3/4    1.20(10)  / 
            >>> P = Matrix([Row([Mixed(1), Mixed(2), Mixed(3)])])
            >>> print(P)
             <  1  2  3  > 
        """
        str = ''
        length = [0]*self.shape()[1]
        for row in self.liste:
            for (i, item) in zip(range(row.len()), row.liste):
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
            for (j, item) in zip(range(row.len()), row.liste):
                codestr = '%' + '%i'%(length[j]) + 's  '
                str += codestr%(item.__str__())
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

    def shape(self):
        """
            >>> a = Mixed(fr.Fraction(1, 3))
            >>> b = Mixed(fr.Fraction(1, 4))
            >>> c = Mixed(fr.Fraction(2, 5))
            >>> d = Mixed(fr.Fraction(3, 4))
            >>> x = Mixed(uc.ufloat(1.2, 0.1))
            >>> y = Mixed(uc.ufloat(1.003, 0.001))
            >>> N = Matrix([Row([a, b, c, d]), Row([a, d, x, y]), Row([b, x, d, x])])
            >>> N.shape()
            (3, 4)
        """
        return (len(self.liste), self.liste[0].len())

    def __add__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> d = Mixed(fr.Fraction(4, 5))
            >>> x = Mixed(uc.ufloat(3.75, 0.23))
            >>> y = Mixed(uc.ufloat(4.25, 0.10))
            >>> M1 = Matrix([Row([a, b]), Row([x, y])])
            >>> M2 = Matrix([Row([c, x]), Row([d, y])])
            >>> print(M1)
             /       1/4       1/5  \ 
             \  3.75(23)  4.25(10)  / 
            >>> print(M2)
             /  3/7  3.75(23)  \ 
             \  4/5  4.25(10)  / 
            >>> print(M1 + M2)
             /     19/28  3.95(23)  \ 
             \  4.55(23)  8.50(14)  / 
        """
        assert isinstance(right, Matrix), \
            "Unknown Operator %s + %s"%(type(self), type(right))
        assert self.shape() == right.shape(), \
            "Two Matrices must have the same shape for Operator +"
        (numrows, numcolumns) = self.shape()
        return Matrix([\
            Row([self.liste[i].liste[j] + right.liste[i].liste[j] \
            for j in range(numcolumns)]) \
            for i in range(numrows)])

    def __sub__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> d = Mixed(fr.Fraction(4, 5))
            >>> x = Mixed(uc.ufloat(3.75, 0.23))
            >>> y = Mixed(uc.ufloat(4.25, 0.10))
            >>> M1 = Matrix([Row([a, b]), Row([x, y])])
            >>> M2 = Matrix([Row([c, x]), Row([d, y])])
            >>> print(M1)
             /       1/4       1/5  \ 
             \  3.75(23)  4.25(10)  / 
            >>> print(M2)
             /  3/7  3.75(23)  \ 
             \  4/5  4.25(10)  / 
            >>> print(M1 - M2)
             /     -5/28  -3.55(23)  \ 
             \  2.95(23)   0.00(14)  / 
        """
        assert isinstance(right, Matrix), \
            "Can subtract from object of typ Matrix object of type "\
            "Matrix only"
        (numrows, numcolumns) = self.shape()
        return Matrix([\
            Row([self.liste[i].liste[j] - right.liste[i].liste[j] \
            for j in range(numcolumns)]) \
            for i in range(numrows)])

    def __mul__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> eins = Mixed(fr.Fraction(1, 1))
            >>> null = Mixed(fr.Fraction(0, 1))
            >>> x = Mixed(uc.ufloat(3.75, 0.23))
            >>> z = Mixed(fr.Fraction(5, 1))
            >>> M = Matrix([Row([a, b]), Row([c, x])])
            >>> print(M)
             /  1/4       1/5  \ 
             \  3/7  3.75(23)  / 
            >>> print(M * z)
             /   5/4          1  \ 
             \  15/7  18.8(1.2)  / 
            >>> I = Matrix([Row([eins, null]), Row([null, eins])])
            >>> print(I)
             /  1  0  \ 
             \  0  1  / 
            >>> print(I * M)
             /  1/4       1/5  \ 
             \  3/7  3.75(23)  / 
            >>> N = Matrix([Row([a, b]), Row([a, c])])
            >>> print(M * N)
             /     9/80    19/140  \ 
             \  1.04(6)  1.69(10)  / 
        """
        assert isinstance(right, Mixed) or isinstance(right, Matrix), \
            "A Matrix can be multiplied only by a Mixed or a Matrix."
        if isinstance(right, Mixed):
            (numrows, numcols) = self.shape()
            return Matrix( \
                [ \
                    Row([self.liste[i].liste[j] * right for j in range(numcols)]) \
                    for i in range(numrows) \
                ] \
            )
        if isinstance(right, Matrix):
            numrows1 = len(self.liste)
            numcols1 = self.liste[0].len()
            numrows2 = len(right.liste)
            numcols2 = right.liste[0].len()
            assert (numcols1 == numrows2), \
                "Matrix-Multiplication needs two matrices, with "\
                " width of first matrix equals height of second matrix."
            def matrixitem(i, j):
                s = Mixed(fr.Fraction(0, 1))
                for k in range(numcols1):
                    s += self.liste[i].liste[k] * right.liste[k].liste[j]
                return s
            return Matrix( \
                [ \
                   Row([matrixitem(i, j) for j in range(numcols2)]) \
                   for i in range(numrows1) \
                ] \
            )

    def __eq__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> x = Mixed(uc.ufloat(3.75, 0.23))
            >>> z = Mixed(fr.Fraction(5, 1))
            >>> M1 = Matrix([Row([a, b]), Row([c, x])])
            >>> M2 = Matrix([Row([a, b]), Row([c, x])])
            >>> M3 = Matrix([Row([a, b]), Row([c, z])])
            >>> M4 = Matrix([Row([a, b]),])
            >>> M1 == M2
            True
            >>> M1 == M3
            False
            >>> M1 == M4
            False
            >>> M1 == a
            False
        """
        if isinstance(right, Matrix):
            if (self.shape() == right.shape()):
                return min([(self.liste[i] == right.liste[i]) \
                    for i in range(self.shape()[0])])
            else:
                return False
        else:
            return False

    def onematrix(dim):
        """
            >>> A = Matrix.onematrix(2)
            >>> print(A)
             /  1  0  \ 
             \  0  1  / 
        """
        assert isinstance(dim, int), \
            "Onematrix must be created via a dimension of type int."
        assert (dim > 0), \
            "Dimension for creating onematrix must be > 0."
        return Matrix([Row.canonical(dim, i) for i in range(dim)])
        def inv(self):
            return 0

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
            and (j1 <= numcols) and (j2 <= numrows), \
            "For cutting a block out of a matrix, use integers, which are between "\
            "0 and num of rows / num of cols"
        assert (i1 < i2) and (j1 < j2), \
            "For cutting a block out of a matrix, use integers (i1, i2, j1, j2) "\
            "with i1 < i2 and j1 < j2."
        return Matrix([self.liste[i].block(j1, j2) for i in range(i1, i2)])

    def swap_rows(self, i, j):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> eins = Mixed(fr.Fraction(1, 1))
            >>> x = Mixed(uc.ufloat(3.75, 0.23))
            >>> z = Mixed(fr.Fraction(5, 1))
            >>> M = Matrix([Row([a, b]), Row([c, x]), Row([eins, z])])
            >>> print(M)
             /  1/4       1/5  \ 
            |   3/7  3.75(23)   |
             \    1         5  / 
            >>> print(M.swap_rows(0, 1))
             /  3/7  3.75(23)  \ 
            |   1/4       1/5   |
             \    1         5  / 
        """
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
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> eins = Mixed(fr.Fraction(1, 1))
            >>> x = Mixed(uc.ufloat(3.75, 0.23))
            >>> z = Mixed(fr.Fraction(5, 1))
            >>> M = Matrix([Row([a, b]), Row([c, x])])
            >>> N = Matrix([Row([eins, z])])
            >>> print(Matrix.vglue(M, N))
             /  1/4       1/5  \ 
            |   3/7  3.75(23)   |
             \    1         5  / 
        """
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
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(1, 2))
            >>> eins = Mixed(fr.Fraction(1, 1))
            >>> x = Mixed(uc.ufloat(3.75, 0.23))
            >>> z = Mixed(fr.Fraction(5, 1))
            >>> M = Matrix([Row([a, b]), Row([c, x])])
            >>> print(M.subtract_x_times_rowj_from_rowi(Mixed(2.0), 1, 0))
             /     1/4       1/5  \ 
             \  0.0(0)  3.35(23)  / 
        """
        new = deepcopy(self)
        new.liste[i] = self.liste[i] + self.liste[j] * (Mixed(-1) * x)
        return new

    def inv(self):
        """
            >>> M = Matrix([Row([Mixed(2), Mixed(3)]), Row([Mixed(4), Mixed(5)])])
            >>> print(M)
             /  2  3  \ 
             \  4  5  / 
            >>> Minv = M.inv()
            >>> print(Minv)
             /  -5/2  3/2  \ 
             \     2   -1  / 
            >>> print(M * Minv)
             /  1  0  \ 
             \  0  1  / 
        """
        (numrows, numcols) = self.shape()
        assert (numrows == numcols), \
            "I can invert square matrices only (num of rows == num of cols)."
        dim = numrows
        right = Matrix.onematrix(dim) 
        def make_triangle(self, right):
            (dim, dim) = self.shape()
            for rownumber in range(dim - 1):
                i = rownumber
                while (self.liste[rownumber].liste[rownumber] == Mixed(0)) \
                    and (i < dim):
                    i += 1
                    self = self.swap_rows(0, i)
                    right = right.swap_row(0, i)

                if i == dim:
                    return (0, 0)
                else:
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
        """
            >>> a = Mixed(fr.Fraction(1, 2))
            >>> b = Mixed(fr.Fraction(3, 4))
            >>> c = Mixed(uc.ufloat(1.2, 0.1))
            >>> d = Mixed(uc.ufloat(2.5, 0.3))
            >>> M = Matrix([Row([a, b]), Row([c, d]), Row([a, d])])
            >>> print(M.transpose())
             /  1/2  1.20(10)       1/2  \ 
             \  3/4  2.50(30)  2.50(30)  / 
        """
        shape = self.shape()
        return Matrix([ \
                   Row([ \
                       self.liste[j].liste[i] \
                       for j in range(shape[0]) \
                   ]) \
                   for i in range(shape[1]) \
               ])
