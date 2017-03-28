import pytest
import sys
sys.path.append("../src/")
from cryspy import numbers as nb
import quicktions as fr
import uncertainties as uc


def approx(a, b):
    allowed_error = 1e-9
    assert isinstance(a, float), \
        "Can only compare two floats for approx equality"
    assert isinstance(b, float), \
        "Can only compare two floats for approx aquality"
    return abs(a - b) < allowed_error


def test_Row():

    # Create

    R = nb.Row([nb.Mixed(fr.Fraction(1, 2)),
                nb.Mixed(uc.ufloat(1.2, 0.1)),
                nb.Mixed(1),
                nb.Mixed(0.5)])
    assert isinstance(R.liste, list)
    assert isinstance(R.liste[0], nb.Mixed)
    assert isinstance(R.liste[0].value, fr.Fraction)
    assert R.liste[0] == nb.Mixed(fr.Fraction(1, 2))
    assert isinstance(R.liste[1], nb.Mixed)
    assert isinstance(R.liste[1].value, uc.UFloat)
    assert R.liste[1] == nb.Mixed(uc.ufloat(1.2, 0.1))
    assert isinstance(R.liste[2], nb.Mixed)
    assert isinstance(R.liste[2].value, int)
    assert R.liste[2] == nb.Mixed(1)
    assert isinstance(R.liste[3], nb.Mixed)
    assert isinstance(R.liste[3].value, float)
    assert approx(R.liste[3].value, 0.5)

    R = nb.Row([fr.Fraction(1, 2),
                uc.ufloat(1.2, 0.1),
                1,
                0.5])
    assert isinstance(R.liste, list)
    assert isinstance(R.liste[0], nb.Mixed)
    assert isinstance(R.liste[0].value, fr.Fraction)
    assert R.liste[0] == nb.Mixed(fr.Fraction(1, 2))
    assert isinstance(R.liste[1], nb.Mixed)
    assert isinstance(R.liste[1].value, uc.UFloat)
    assert R.liste[1] == nb.Mixed(uc.ufloat(1.2, 0.1))
    assert isinstance(R.liste[2], nb.Mixed)
    assert isinstance(R.liste[2].value, int)
    assert R.liste[2] == nb.Mixed(1)
    assert isinstance(R.liste[3], nb.Mixed)
    assert isinstance(R.liste[3].value, float)
    assert approx(R.liste[3].value, 0.5)

    # len

    R = nb.Row([fr.Fraction(1, 2),
                uc.ufloat(1.2, 0.1),
                1,
                0.5])
    assert len(R) == 4

    assert R.__str__() == "(  1/2  1.20(10)  1  0.5  )"

    # Equal

    R1 = nb.Row([fr.Fraction(1, 2),
                uc.ufloat(1.2, 0.1),
                1,
                0.5])
    R2 = nb.Row([fr.Fraction(1, 2),
                uc.ufloat(1.2, 0.1),
                1,
                0.5])
    R3 = nb.Row([fr.Fraction(1, 2),
                uc.ufloat(1.2, 0.1),
                1,
                fr.Fraction(1, 2)])
    R4 = nb.Row([fr.Fraction(1, 2),
                uc.ufloat(1.2, 0.1),
                1])

    assert R1 == R2
    assert (R1 == R3) == False
    assert (R1 == R4) == False
    assert (R1 == 5) == False

    # canonical

    assert nb.Row.canonical(5, 3) == nb.Row([0, 0, 0, 1, 0])

    # block

    R = nb.Row([1, 2, 3, 4])
    assert R.block(1, 3) == nb.Row([2, 3])

    # Addition

    R1 = nb.Row([1, 2, fr.Fraction(1, 2)])
    R2 = nb.Row([2, 3, 4])
    assert R1 + R2 == nb.Row([3, 5, fr.Fraction(9, 2)])

    # Subtraction

    R1 = nb.Row([1, 2, fr.Fraction(1, 2)])
    R2 = nb.Row([2, 3, 4])
    assert R1 - R2 == nb.Row([-1, -1, fr.Fraction(-7, 2)])

    # Multiplication

    R1 = nb.Row([1, 2, fr.Fraction(1, 2)])
    assert R1 * nb.Mixed(2) == nb.Row([2, 4, 1])
    assert nb.Mixed(2) * R1 == nb.Row([2, 4, 1])
    assert R1 * 2 == nb.Row([2, 4, 1])
    assert 2 * R1 == nb.Row([2, 4, 1])

    # neg
    R1 = nb.Row([1, 2, 3])
    assert -R1 == nb.Row([-1, -2, -3])


def test_Matrix():

    # create and shape

    M1 = nb.Matrix([nb.Row([1, 2, 3]), nb.Row([4, 5, 6])])
    M2 = nb.Matrix([[1, 2, 3], [4, 5, 6]])
    assert M1.shape() == (2, 3)
    assert M2.shape() == (2, 3)

    # Equal

    M1 = nb.Matrix([nb.Row([1, 2, 3]), nb.Row([4, 5, 6])])
    M2 = nb.Matrix([[1, 2, 3], [4, 5, 6]])
    M3 = nb.Matrix([[1, 2, 3], [4, 5.1, 6]])
    M4 = nb.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    M5 = nb.Matrix([[1, 2], [4, 5]])
    M6 = nb.Matrix([[1, 2, 3], [4, 5.0, 6]])
    M7 = nb.Matrix([[1, 2, 3], [4, fr.Fraction(5, 1), 6]])
    assert M1 == M2
    assert (M1 == M3) == False
    assert (M1 == M4) == False
    assert (M1 == M5) == False
    assert (M1 == M6) == False
    assert M1 == M7

    # print

    assert nb.Matrix([[1, 2]]).__str__() == " <  1  2  > "
    assert nb.Matrix([[1, 2], [3, 4]]).__str__() == " /  1  2  \ \n" \
                                                    " \  3  4  / "
    assert nb.Matrix([[1, 2, 3], [4, 5, 6], [7, 800, 9]]).__str__() == \
        " /  1    2  3  \ \n" \
        "|   4    5  6   |\n" \
        " \  7  800  9  / "

    # Addition

    assert nb.Matrix([[1, 2], [3, 4]]) + nb.Matrix([[5, 6], [7, 8]]) == \
        nb.Matrix([[6, 8], [10, 12]])

    assert nb.Matrix([[1, 2], [3, 4], [5, 6]]) + \
           nb.Matrix([[1, 1], [1, 1], [1, 1]]) == \
           nb.Matrix([[2, 3], [4, 5], [6, 7]])

    # Subtraction

    assert nb.Matrix([[1, 2], [3, 4]]) - nb.Matrix([[5, 6], [7, 8]]) == \
        nb.Matrix([[-4, -4], [-4, -4]])

    assert nb.Matrix([[1, 2], [3, 4], [5, 6]]) - \
           nb.Matrix([[1, 1], [1, 1], [1, 1]]) == \
           nb.Matrix([[0, 1], [2, 3], [4, 5]])

    # neg

    M1 = nb.Matrix([[1, 2, 3], [4, 5, 6]])
    assert -M1 == nb.Matrix([[-1, -2, -3], [-4, -5, -6]])

    # Multiplication "Matrix * Matrix"

    M1 = nb.Matrix([[1, 2], [3, 4]])
    M2 = nb.Matrix([[5, 6], [7, 8]])
    assert isinstance(M1 * M2, nb.Matrix)
    assert M1 * M2 == nb.Matrix([[19, 22], [43, 50]])

    # Multiplication "Scalar * Matrix"

    assert M1 * nb.Mixed(fr.Fraction(1, 2)) == \
        nb.Matrix([[fr.Fraction(1, 2), 1], [fr.Fraction(3, 2), 2]])
    assert M1 * fr.Fraction(1, 2) == \
        nb.Matrix([[fr.Fraction(1, 2), 1], [fr.Fraction(3, 2), 2]])
    assert nb.Mixed(fr.Fraction(1, 2)) * M1 == \
        nb.Matrix([[fr.Fraction(1, 2), 1], [fr.Fraction(3, 2), 2]])
    assert fr.Fraction(1, 2) * M1 == \
        nb.Matrix([[fr.Fraction(1, 2), 1], [fr.Fraction(3, 2), 2]])

    M = M1 * nb.Mixed(uc.ufloat(1.2, 0.1))
    assert approx(M.liste[0].liste[0].value.n, 1.2)
    assert approx(M.liste[0].liste[0].value.s, 0.1)
    assert approx(M.liste[0].liste[1].value.n, 2.4)
    assert approx(M.liste[0].liste[1].value.s, 0.2)
    assert approx(M.liste[1].liste[0].value.n, 3.6)
    assert approx(M.liste[1].liste[0].value.s, 0.3)
    assert approx(M.liste[1].liste[1].value.n, 4.8)
    assert approx(M.liste[1].liste[1].value.s, 0.4)
    M = M1 * uc.ufloat(1.2, 0.1)
    assert approx(M.liste[0].liste[0].value.n, 1.2)
    assert approx(M.liste[0].liste[0].value.s, 0.1)
    assert approx(M.liste[0].liste[1].value.n, 2.4)
    assert approx(M.liste[0].liste[1].value.s, 0.2)
    assert approx(M.liste[1].liste[0].value.n, 3.6)
    assert approx(M.liste[1].liste[0].value.s, 0.3)
    assert approx(M.liste[1].liste[1].value.n, 4.8)
    assert approx(M.liste[1].liste[1].value.s, 0.4)
    M = nb.Mixed(uc.ufloat(1.2, 0.1)) * M1
    assert approx(M.liste[0].liste[0].value.n, 1.2)
    assert approx(M.liste[0].liste[0].value.s, 0.1)
    assert approx(M.liste[0].liste[1].value.n, 2.4)
    assert approx(M.liste[0].liste[1].value.s, 0.2)
    assert approx(M.liste[1].liste[0].value.n, 3.6)
    assert approx(M.liste[1].liste[0].value.s, 0.3)
    assert approx(M.liste[1].liste[1].value.n, 4.8)
    assert approx(M.liste[1].liste[1].value.s, 0.4)
    M = uc.ufloat(1.2, 0.1) * M1
    assert approx(M.liste[0].liste[0].value.n, 1.2)
    assert approx(M.liste[0].liste[0].value.s, 0.1)
    assert approx(M.liste[0].liste[1].value.n, 2.4)
    assert approx(M.liste[0].liste[1].value.s, 0.2)
    assert approx(M.liste[1].liste[0].value.n, 3.6)
    assert approx(M.liste[1].liste[0].value.s, 0.3)
    assert approx(M.liste[1].liste[1].value.n, 4.8)
    assert approx(M.liste[1].liste[1].value.s, 0.4)

    assert M1 * nb.Mixed(2) == nb.Matrix([[2, 4], [6, 8]])
    assert M1 * 2 == nb.Matrix([[2, 4], [6, 8]])
    assert nb.Mixed(2) * M1 == nb.Matrix([[2, 4], [6, 8]])
    assert 2 * M1 == nb.Matrix([[2, 4], [6, 8]])

    M = M1 * nb.Mixed(2.5)
    assert approx(M.liste[0].liste[0].value, 2.5)
    assert approx(M.liste[0].liste[1].value, 5.0)
    assert approx(M.liste[1].liste[0].value, 7.5)
    assert approx(M.liste[1].liste[1].value, 10.0)
    M = M1 * 2.5
    assert approx(M.liste[0].liste[0].value, 2.5)
    assert approx(M.liste[0].liste[1].value, 5.0)
    assert approx(M.liste[1].liste[0].value, 7.5)
    assert approx(M.liste[1].liste[1].value, 10.0)
    M = nb.Mixed(2.5) * M1
    assert approx(M.liste[0].liste[0].value, 2.5)
    assert approx(M.liste[0].liste[1].value, 5.0)
    assert approx(M.liste[1].liste[0].value, 7.5)
    assert approx(M.liste[1].liste[1].value, 10.0)
    M = 2.5 * M1
    assert approx(M.liste[0].liste[0].value, 2.5)
    assert approx(M.liste[0].liste[1].value, 5.0)
    assert approx(M.liste[1].liste[0].value, 7.5)
    assert approx(M.liste[1].liste[1].value, 10.0)

    # onematrix

    assert nb.Matrix.onematrix(2) == nb.Matrix([[1, 0], [0, 1]])
    assert nb.Matrix.onematrix(3) == nb.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # block

    M = nb.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert M.block(0, 2, 0, 2) == nb.Matrix([[1, 2], [4, 5]])
    assert M.block(1, 2, 0, 3) == nb.Matrix([[4, 5, 6]])
    M = nb.Matrix([[1, 2, 3, 4]])
    assert M.block(0, 1, 0, 3) == nb.Matrix([[1, 2, 3]])

    # swap_rows

    M = nb.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert M.swap_rows(0, 1) == nb.Matrix([[4, 5, 6], [1, 2, 3], [7, 8, 9]])

    # vglue

    M1 = nb.Matrix([[1, 2, 3]])
    M2 = nb.Matrix([[4, 5, 6]])
    assert nb.Matrix.vglue(M1, M2) == nb.Matrix([[1, 2, 3], [4, 5, 6]])

    # subtract_x_times_rowj_from_rowi

    M = nb.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert M.subtract_x_times_rowj_from_rowi(2, 2, 0) == \
        nb.Matrix([[1, 2, 3], [4, 5, 6], [5, 4, 3]])

    # inv

    assert nb.Matrix([[2, 3],
                      [4, 5]]).inv() == \
        nb.Matrix([[-fr.Fraction(5, 2), fr.Fraction(3, 2)],
                   [2,                -1]])
    assert nb.Matrix([[0, 1,  1],
                      [1, 0,  0],
                      [0, 0, -1]]).inv() == \
           nb.Matrix([[0, 1,  0],
                      [1, 0,  1],
                      [0, 0, -1]])

    assert nb.Matrix([[0, 0, 1, 0],
                      [1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]]).inv() == \
           nb.Matrix([[0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [1, 0, 0, 0],
                      [0, 0, 0, 1]])

    # transpose

    assert nb.Matrix([[1, 2, 3], [4, 5, 6]]).transpose() == \
           nb.Matrix([[1, 4], [2, 5], [3, 6]])

    # delete_ith_row_and_first_column
    M = nb.Matrix([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
    assert M.delete_ith_row_and_first_column(1) == nb.Matrix([[2, 3, 4],
                                                              [10, 11, 12]])

    # det
    M = nb.Matrix([[3]])
    assert M.det() == 3
    M = nb.Matrix([[1, 2],
                   [3, 4]])
    assert M.det() == -2
    M = nb.Matrix([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
    assert M.det() == 0
    M = nb.Matrix([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 8, 11, 12],
                   [13, 14, 15, 17]])
    assert M.det() == -16

    # delete_translation

    M = nb.Matrix([[1,  2,  3,  4],
                   [5,  6,  7,  8],
                   [9, 10, 11, 12],
                   [0,  0,  0,  1]])

    assert M.delete_translation() == nb.Matrix([[1,  2,  3, 0],
                                              [5,  6,  7, 0],
                                              [9, 10, 11, 0],
                                              [0,  0,  0, 1]])
