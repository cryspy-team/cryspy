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
                if self.value == fr.Fraction(0, 1):
                    return Mixed(fr.Fraction(0, 1))
                else:
                    return Mixed(float(self.value) * right.value)
        if isinstance(self.value, uc.UFloat):
            if isinstance(right.value, fr.Fraction):
                if right.value == fr.Fraction(0, 1):
                    return Mixed(fr.Fraction(0, 1))
                else:
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
            >>> x = Mixed(uc.ufloat(1.2, 0.1))
            >>> M = Matrix([[a, b], [c, x]])
            >>> type(M)
            <class 'cryspy_numbers.Matrix'>
        """
        assert isinstance(liste, list), \
            "Object of type Matrix must be created by a list."
        for row in liste:
            assert isinstance(row, list), \
             "Object of type Matrix must be created by a list of lists"
        if len(liste) > 0:
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
        self.liste = deepcopy(liste)

    def __str__(self):
        """
            >>> a = Mixed(fr.Fraction(1, 3))
            >>> b = Mixed(fr.Fraction(1, 4))
            >>> c = Mixed(fr.Fraction(2, 5))
            >>> d = Mixed(fr.Fraction(3, 4))
            >>> x = Mixed(uc.ufloat(1.2, 0.1))
            >>> y = Mixed(uc.ufloat(1.003, 0.001))
            >>> M = Matrix([[a, b], [c, d]])
            >>> print(M)
             /  1/3  1/4  \ 
             \  2/5  3/4  / 
            >>> N = Matrix([[a, b, c, d], [a, d, x, y], [b, x, d, x]])
            >>> print(N)
             /  1/3          1/4          2/5              3/4  \ 
            |   1/3          3/4  1.20+/-0.10  1.0030+/-0.0010   |
             \  1/4  1.20+/-0.10          3/4      1.20+/-0.10  / 
            >>> P = Matrix([[a, b]])
            >>> print(P)
            (  1/3  1/4  )
        """
        str = ''
        length = [0]*len(self.liste[0])
        for row in self.liste:
            for (i, item) in zip(range(len(row)), row):
                length[i] = max(length[i], len(item.__str__()))
        
        (numrow, numcol) = self.shape()
        for (i, row) in zip(range(len(self.liste)), self.liste):
            if (numrow == 1):
                str += '(  '
            else:
                if i == 0:
                    str += ' /  '
                elif i == len(self.liste) - 1:
                    str += ' \\  '
                else:
                    str += '|   '
            for (j, item) in zip(range(len(row)), row):
                codestr = '%' + '%i'%(length[j]) + 's  '
                str += codestr%(item.__str__())
            if (numrow == 1):
                str += ')'
            else:
                if i == 0:
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
            >>> N = Matrix([[a, b, c, d], [a, d, x, y], [b, x, d, x]])
            >>> N.shape()
            (3, 4)
        """
        return (len(self.liste), len(self.liste[0]))

    def __add__(self, right):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> d = Mixed(fr.Fraction(4, 5))
            >>> x = Mixed(uc.ufloat(3.75, 0.23))
            >>> y = Mixed(uc.ufloat(4.25, 0.10))
            >>> M1 = Matrix([[a, b], [x, y]])
            >>> M2 = Matrix([[c, x], [d, y]])
            >>> print(M1)
             /          1/4          1/5  \ 
             \  3.75+/-0.23  4.25+/-0.10  / 
            >>> print(M2)
             /  3/7  3.75+/-0.23  \ 
             \  4/5  4.25+/-0.10  / 
            >>> print(M1 + M2)
             /        19/28  3.95+/-0.23  \ 
             \  4.55+/-0.23  8.50+/-0.14  / 
        """
        assert isinstance(right, Matrix), \
            "Unknown Operator %s + %s"%(type(self), type(right))
        assert self.shape() == right.shape(), \
            "Two Matrices must have the same shape for Operator +"
        (numrows, numcolumns) = self.shape()
        return Matrix([\
            [self.liste[i][j] + right.liste[i][j] \
            for j in range(numcolumns)] \
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
            >>> M = Matrix([[a, b], [c, x]])
            >>> print(M)
             /  1/4          1/5  \ 
             \  3/7  3.75+/-0.23  / 
            >>> print(M * z)
             /   5/4           1  \ 
             \  15/7  18.8+/-1.2  / 
            >>> I = Matrix([[eins, null], [null, eins]])
            >>> print(I)
             /  1  0  \ 
             \  0  1  / 
            >>> print(I * M)
             /  1/4          1/5  \ 
             \  3/7  3.75+/-0.23  / 
            >>> N = Matrix([[a, b], [a, c]])
            >>> print(M * N)
             /         9/80       19/140  \ 
             \  1.04+/-0.06  1.69+/-0.10  / 
        """
        assert isinstance(right, Mixed) or isinstance(right, Matrix), \
            "A Matrix can be multiplied only by a Mixed or a Matrix."
        if isinstance(right, Mixed):
            numrows = len(self.liste)
            numcols = len(self.liste[0])
            return Matrix( \
                [ \
                    [self.liste[i][j] * right for j in range(numcols)] \
                    for i in range(numrows) \
                ] \
            )
        if isinstance(right, Matrix):
            numrows1 = len(self.liste)
            numcols1 = len(self.liste[0])
            numrows2 = len(right.liste)
            numcols2 = len(right.liste[0])
            assert (numcols1 == numrows2), \
                "Matrix-Multiplication needs two matrices, with "\
                " width of first matrix equals height of second matrix."
            def matrixitem(i, j):
                s = Mixed(fr.Fraction(0, 1))
                for k in range(numcols1):
                    s += self.liste[i][k] * right.liste[k][j]
                return s
            return Matrix( \
                [ \
                   [matrixitem(i, j) for j in range(numcols2)] \
                   for i in range(numrows1) \
                ] \
            )

    def onematrix(self):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> d = Mixed(fr.Fraction(4, 5))
            >>> M = Matrix([[a, b], [c, d]])
            >>> print(M.onematrix())
             /  1  0  \ 
             \  0  1  / 
        """
        (numrows, numcols) = self.shape()
        def kronecker(i, j):
            if (i == j):
                return Mixed(fr.Fraction(1, 1))
            else:
                return Mixed(fr.Fraction(0, 1))
        return Matrix([ \
                          [kronecker(i, j) for j in range(numcols)] \
                          for i in range(numrows) \
                      ])

    def block(self, fromrow, torow, fromcol, tocol):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> d = Mixed(fr.Fraction(4, 5))
            >>> M = Matrix([[a, b, c], [c, d, a], [b, a, b]])
            >>> print(M.block(1,2,0,2))
            (  3/7  4/5  )
        """
        assert isinstance(fromrow, int) and isinstance(torow, int) \
            and isinstance(fromcol, int) and isinstance(tocol, int), \
            "Attribute block needs indexes of type int."
        (numrows, numcols) = self.shape()
        return Matrix([\
                          [self.liste[i][j] for j in range(fromcol, tocol)] \
                          for i in range(fromrow, torow) \
                      ])

    def append_below(self, lower):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> d = Mixed(fr.Fraction(4, 5))
            >>> M = Matrix([[a, b], [c, d]])
            >>> N = Matrix([[a, b]])
            >>> print(M.append_below(N))
             /  1/4  1/5  \ 
            |   3/7  4/5   |
             \  1/4  1/5  / 
        """
        assert isinstance(lower, Matrix), \
            "Only a Matrix can be appended below a Matrix."
        (numrows1, numcols1) = self.shape()
        (numrows2, numcols2) = self.shape()
        assert (numcols1 == numcols2), \
            "Matrix to be appended below has to be the same number of "\
            "columns."
        return Matrix(self.liste + lower.liste)

    def swap_rows(self, rowindex1, rowindex2):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> d = Mixed(fr.Fraction(4, 5))
            >>> M = Matrix([[a, b], [c, d]])
            >>> print(M.swap_rows(0, 1))
             /  3/7  4/5  \ 
             \  1/4  1/5  / 
            >>> print(M)
             /  1/4  1/5  \ 
             \  3/7  4/5  / 
        """
        (numrows, numcols) = self.shape()
        new = deepcopy(self)
        row1 = new.liste[rowindex1]
        new.liste[rowindex1] = new.liste[rowindex2]
        new.liste[rowindex2] = row1
        return new

    def inv(self):
        """
            >>> a = Mixed(fr.Fraction(1, 4))
            >>> b = Mixed(fr.Fraction(1, 5))
            >>> c = Mixed(fr.Fraction(3, 7))
            >>> d = Mixed(fr.Fraction(4, 5))
            >>> M = Matrix([[a, b], [c, d]])
            >>> print(M.inv())
             /      7  -7/4  \ 
             \  -15/4  2.1875 / 
        """
        L = deepcopy(self)
        R = self.onematrix()
        
        return 0
