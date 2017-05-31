import numpy as np
import pytest
import sys
sys.path.append("../src/")
import quicktions as fr
import uncertainties as uc
from cryspy import numbers as nb
from cryspy import geo as geo
from cryspy.fromstr import fromstr as fs

def test_Pos():
    x = geo.Pos(nb.Matrix([[1], [2], [3], [1]]))
    assert x.__str__() == "Pos /  1  \ \n   |   2   |\n    \  3  / "
    assert x.x() == 1
    assert x.y() == 2
    assert x.z() == 3
    x = geo.origin
    assert x == geo.Pos(nb.Matrix([[0], [0], [0], [1]]))
    x = geo.Pos(nb.Matrix([[0], [0], [1.00000000], [1]]))
    y = geo.Pos(nb.Matrix([[0], [0], [0.99999999], [1]]))
    assert hash(x) == hash(y)


def test_Dif():
    x = geo.Dif(nb.Matrix([[1], [2], [3], [0]]))
    assert x.__str__() == "Dif /  1  \ \n   |   2   |\n    \  3  / "
    assert x.x() == 1
    assert x.y() == 2
    assert x.z() == 3
    assert x.to_Symmetry() == geo.Symmetry(nb.Matrix([[1, 0, 0, 1],
                                                      [0, 1, 0, 2],
                                                      [0, 0, 1, 3],
                                                      [0, 0, 0, 1]]))
    x = geo.Dif(nb.Matrix([[0], [0], [1.00000000], [0]]))
    y = geo.Dif(nb.Matrix([[0], [0], [0.99999999], [0]]))
    assert hash(x) == hash(y)

def test_Rec():
    q = geo.Rec(nb.Matrix([[1, 2, 3, 0]]))
    assert q.__str__() == "Rec <  1  2  3  > "
    assert q.h() == 1
    assert q.k() == 2
    assert q.l() == 3
    x = geo.Rec(nb.Matrix([[0, 0, 1.00000000, 0]]))
    y = geo.Rec(nb.Matrix([[0, 0, 0.99999999, 0]]))
    assert hash(x) == hash(y)


def test_eq():
    r1 = geo.Pos(nb.Matrix([[1], [2], [3], [1]]))
    r2 = geo.Pos(nb.Matrix([[1], [2], [3], [1]]))
    r3 = geo.Pos(nb.Matrix([[1], [2], [4], [1]]))
    d1 = geo.Dif(nb.Matrix([[4], [5], [6], [0]]))
    d2 = geo.Dif(nb.Matrix([[4], [5], [6], [0]]))
    d3 = geo.Dif(nb.Matrix([[3], [5], [6], [0]]))
    q1 = geo.Rec(nb.Matrix([[1, 2, 3, 0]]))
    q2 = geo.Rec(nb.Matrix([[1, 2, 3, 0]]))
    q3 = geo.Rec(nb.Matrix([[2, 3, 4, 0]]))
    assert not (r1 == d1)
    assert     (r1 == r1)
    assert     (r1 == r2)
    assert not (r1 == r3)
    assert     (d1 == d1)
    assert     (d1 == d2)
    assert not (d1 == d3)
    assert not (r1 == q1)
    assert not (d1 == q1)
    assert     (q1 == q1)
    assert     (q1 == q2)
    assert not (q1 == q3)


def test_add_and_sub():
    x1 = geo.Pos(nb.Matrix([[1], [2], [3], [1]]))
    x2 = geo.Pos(nb.Matrix([[2], [3], [4], [1]]))
    d1 = geo.Dif(nb.Matrix([[4], [5], [6], [0]]))
    d2 = geo.Dif(nb.Matrix([[5], [5], [5], [0]]))
    assert (x1 + d1) == geo.Pos(nb.Matrix([[5], [7], [9], [1]]))
    assert (d1 + d2) == geo.Dif(nb.Matrix([[9], [10], [11], [0]]))
    assert (d1 - d2) == geo.Dif(nb.Matrix([[-1], [0], [1], [0]]))
    assert (x1 - d1) == geo.Pos(nb.Matrix([[-3], [-3], [-3], [1]]))
    assert (x1 - x2) == geo.Dif(nb.Matrix([[-1], [-1], [-1], [0]]))
    q1 = geo.Rec(nb.Matrix([[1, 2, 3, 0]]))
    q2 = geo.Rec(nb.Matrix([[4, 5, 6, 0]]))
    assert (q1 + q2) == geo.Rec(nb.Matrix([[5, 7, 9, 0]]))
    assert (q1 - q2) == geo.Rec(nb.Matrix([[-3, -3, -3, 0]]))
    assert -d1 == geo.Dif(nb.Matrix([[-4], [-5], [-6], [0]]))
    assert -q1 == geo.Rec(nb.Matrix([[-1, -2, -3, 0]]))


def test_Skalarprodukt():
    d1 = geo.Dif(nb.Matrix([[1], [2], [3], [0]]))
    q1 = geo.Rec(nb.Matrix([[4, 5, 6, 0]]))
    assert q1 * d1 == 32


def test_Operator():
    id = geo.Operator(nb.Matrix([[1, 0, 0, 0],
                                 [0, 1, 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 1]]))
    g = geo.Operator(nb.Matrix([[-1,  0, 0, 0],
                                [0, -1, 0, 0],
                                [0,  0, 1, 0],
                                [0,  0, 0, 1]]))
    g1 = geo.Operator(nb.Matrix([[-1,  0, 0, 0],
                                 [0, -1, 0, 0],
                                 [0,  0, 1, 0],
                                 [0,  0, 0, 1]]))
    assert g.__str__() == "Operator /  -1   0  0  0  \ \n"\
                          "        |    0  -1  0  0   |\n"\
                          "        |    0   0  1  0   |\n"\
                          "         \   0   0  0  1  / "
    assert g == g1


def test_Symmetry():
    g = geo.Symmetry(nb.Matrix([[1,  0, 2, -1],
                                [0, -2, 0,  0],
                                [0,  0, 1,  fr.Fraction(1, 3)],
                                [0,  0, 0,  1]]))
    assert g.__str__() == "x+2z-1,-2y,z+1/3"

    assert isinstance(g.inv(), geo.Symmetry)
    assert g * g.inv() == geo.Symmetry(nb.Matrix.onematrix(4))

    g = geo.Symmetry(nb.Matrix([[0,-1, 0, 0],
                                [1, -1,  0, 0],
                                [0,  0,  1, 0],
                                [0,  0,  0, 1]]))
    print(g)
    assert g.__str__() == "-y,x-y,z"
    x = uc.ufloat(0.4, 0.1)
    p = geo.Pos(nb.Matrix([[x], [x], [0], [1]]))
    print(p)
    print((g*g*g)**p)
    assert (g*g*g)**p == p


def test_Pointgroup():
    pg = geo.Pointgroup([geo.Symmetry(nb.Matrix([[1, 0, 0, 0],
                                                 [0, 1, 0, 0],
                                                 [0, 0, 1, 0],
                                                 [0, 0, 0, 1]])),
                         geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                                 [0, -1, 0, 0],
                                                 [0, 0, -1, 0],
                                                 [0, 0, 0, 1]]))])

    assert isinstance(pg, geo.Pointgroup)
    assert pg.__str__() == "Pointgroup\n" \
                           "==========\n" \
                           "x,y,z\n" \
                           "-x,-y,-z\n"

    assert pg.is_really_a_pointgroup()

    pg1 = geo.Pointgroup([geo.Symmetry(nb.Matrix([[1, 0, 0, 0],
                                                 [0, 1, 0, 0],
                                                 [0, 0, 1, 0],
                                                 [0, 0, 0, 1]])),
                         geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                                 [0, -1, 0, 0],
                                                 [0, 0, -1, 0],
                                                 [0, 0, 0, 1]]))])

    pg2 = geo.Pointgroup([geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                                  [0, -1, 0, 0],
                                                  [0, 0, -1, 0],
                                                  [0, 0, 0, 1]]))])

    assert pg == pg1
    assert not (pg == pg2)
    assert not (pg == 2)

    assert not pg2.is_really_a_pointgroup()

    G = geo.Pointgroup([geo.Symmetry(nb.Matrix([[1, 0, 0, 0],
                                                [0, 1, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                                [0, -1, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                                [0, 1, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[1, 0, 0, 0],
                                                [0, -1, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, 1, 0, 0],
                                                [1, 0, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, -1, 0, 0],
                                                [-1, 0, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, -1, 0, 0],
                                                [1, 0, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, 1, 0, 0],
                                                [-1, 0, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                                [0, -1, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[1, 0, 0, 0],
                                                [0, 1, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[1, 0, 0, 0],
                                                [0, -1, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                                [0, 1, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, -1, 0, 0],
                                                [-1, 0, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, 1, 0, 0],
                                                [1, 0, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, 1, 0, 0],
                                                [-1, 0, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, -1, 0, 0],
                                                [1, 0, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]]))])

    assert G.is_really_a_pointgroup()

    g = G.liste
    # For this test, the order of the symmetry elements must not be
    # completely arbitrary, because there are several valid possibilities
    # to sort the symmetryelements.
    G1 = geo.Pointgroup([g[6], g[7], g[0], g[14], g[15], g[9], g[10], g[11],
                         g[12], g[13], g[8], g[1], g[2], g[3], g[4], g[5]])

    print(G1.sort())
    print(G)
    assert G1.sort() == G

    H = geo.Pointgroup([geo.Symmetry(nb.Matrix([[1, 0, 0, 0],
                                                [0, 1, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                                [0, -1, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, -1, 0, 0],
                                                [1, 0, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, 1, 0, 0],
                                                [-1, 0, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                                [0, -1, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[1, 0, 0, 0],
                                                [0, 1, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, 1, 0, 0],
                                                [-1, 0, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]])),
                        geo.Symmetry(nb.Matrix([[0, -1, 0, 0],
                                                [1, 0, 0, 0],
                                                [0, 0, -1, 0],
                                                [0, 0, 0, 1]]))])

    assert H.is_really_a_pointgroup()
    assert G1.coset_decomposition_with_respect_to(H) \
        == "x,y,z\n" \
           "-x,y,-z\n"


def test_Transformation():
    t1 = geo.Transformation(nb.Matrix([[0, 1, 0, 0],
                                       [1, 0, 0, 0],
                                       [0, 0, 1, 0],
                                       [0, 0, 0, 1]]))

    assert t1.__str__() == "Transformation O -> (0, 0, 0)\n" \
                           "               then\n" \
                           "               a' = b\n" \
                           "               b' = a\n" \
                           "               c' = c"

    t2 = geo.Transformation(nb.Matrix([[1, 0, 0, fr.Fraction(1, 2)],
                                       [0, 1, 0, fr.Fraction(1, 4)],
                                       [0, 0, 1, fr.Fraction(1, 3)],
                                       [0, 0, 0, 1]]))

    assert t2.__str__() == "Transformation O -> (-1/2, -1/4, -1/3)\n" \
                           "               then\n" \
                           "               a' = a\n" \
                           "               b' = b\n" \
                           "               c' = c"

    assert isinstance(t2.inv(), geo.Transformation)
    assert t2 * t2.inv() == geo.Transformation(nb.Matrix.onematrix(4))

    t3 = geo.Transformation(nb.Matrix([[1.0, 0, 0, 0],
                                       [0, 1, 0, 0],
                                       [0, 0, 1, 0],
                                       [0, 0, 0, 1]]))
    print(t3.value)
    assert t3.__str__() == "Transformation O -> (0, 0, 0)\n" \
                           "               then\n" \
                           "               a' = 1.0a\n" \
                           "               b' = b\n" \
                           "               c' = c"

    q1 = geo.Rec(nb.Matrix([[1, 0, 0, 0]]))
    t = geo.Transformation(nb.Matrix([[0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [1, 0, 0, 0],
                                      [0, 0, 0, 1]]))
    assert isinstance(t ** q1, geo.Rec)
    assert (t ** q1) == geo.Rec(nb.Matrix([[0, 0, 1, 0]]))

    q1 = geo.Rec(nb.Matrix([[1, 0, 0, 0]]))
    t = geo.Transformation(nb.Matrix([[0, 1, 0, 0.3],
                                      [0, 0, 1, 0.7],
                                      [1, 0, 0, 100],
                                      [0, 0, 0, 1]]))
    assert isinstance(t ** q1, geo.Rec)
    assert (t ** q1) == geo.Rec(nb.Matrix([[0, 0, 1, 0]]))

    q1 = geo.Rec(nb.Matrix([[0, 0, 1, 0]]))
    t = geo.Transformation(nb.Matrix([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 2, 0],
                                      [0, 0, 0, 1]]))
    assert t.__str__()  == "Transformation O -> (0, 0, 0)\n" \
                           "               then\n" \
                           "               a' = a\n" \
                           "               b' = b\n" \
                           "               c' = 1/2c"
    assert isinstance(t ** q1, geo.Rec)
    assert (t ** q1) == \
        geo.Rec(nb.Matrix([[0, 0, nb.Mixed(fr.Fraction(1, 2)), 0]]))

    q1 = geo.Rec(nb.Matrix([[0, 0, 1, 0]]))
    t = geo.Transformation(nb.Matrix([[1, 0, 0, 0],
                                      [0, 0, 2, 0],
                                      [0, -1, 0, 0],
                                      [0, 0, 0, 1]]))
    assert t.__str__()  == "Transformation O -> (0, 0, 0)\n" \
                           "               then\n" \
                           "               a' = a\n" \
                           "               b' = 1/2c\n" \
                           "               c' = -b"
    assert isinstance(t ** q1, geo.Rec)
    print(t)
    assert (t ** q1) == \
        geo.Rec(nb.Matrix([[0, nb.Mixed(fr.Fraction(1, 2)), 0, 0]]))


def test_Metric():
    M = nb.Matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    metric = geo.Metric(M)
    t = metric.schmidttransformation

    assert t ** geo.canonical_e0 == geo.Dif(nb.Matrix([[1], [0], [0], [0]]))
    assert t ** geo.canonical_e1 == geo.Dif(nb.Matrix([[0], [1], [0], [0]]))
    assert t ** geo.canonical_e2 == geo.Dif(nb.Matrix([[0], [0], [1], [0]]))

    metric = geo.Cellparameters(1, 1, 1, 90, 90, 45).to_Metric()
    t = metric.schmidttransformation
    assert t ** geo.canonical_e0 == geo.Dif(nb.Matrix([[1], [0], [0], [0]]))
    e1 = t ** geo.canonical_e1
    assert abs(e1.x() - 0.70710678).value < 0.000001
    assert abs(e1.y() - 0.70710678).value < 0.000001
    assert abs(e1.z() - 0).value < 0.000001
    e2 = t ** geo.canonical_e2
    assert abs(e2.x() - 0).value < 0.000001
    assert abs(e2.y() - 0).value < 0.000001
    assert abs(e2.z() - 1).value < 0.000001

    t = metric.schmidttransformation.inv()

    M = nb.Matrix([[9, 0, 0, 0],
                   [0, 4, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    metric = geo.Metric(M)
    assert metric.__str__() == "Metric /  9  0  0  0  \ \n" \
                               "      |   0  4  0  0   |\n" \
                               "      |   0  0  1  0   |\n" \
                               "       \  0  0  0  1  / "
    o = geo.Pos(nb.Matrix([[0], [0], [0], [1]]))
    p1 = geo.Pos(nb.Matrix([[1], [0], [0], [1]]))
    p2 = geo.Pos(nb.Matrix([[0], [1], [0], [1]]))
    q1 = geo.Rec(nb.Matrix([[1, 0, 0, 0]]))
    q2 = geo.Rec(nb.Matrix([[0, 1, 0, 0]]))
    q3 = geo.Rec(nb.Matrix([[1, 1, 0, 0]]))
    assert metric.dot(p1 - o, p1 - o).__str__() == "9"
    assert metric.dot(p1 - o, p2 - o).__str__() == "0"
    assert metric.dot(q1, q1).__str__() == "1/9"
    assert metric.dot(q2, q2).__str__() == "1/4"
    assert metric.dot(q3, q3).__str__() == "13/36"
    assert metric.length(p1 - o) == 3
    assert abs(float((metric.angle(p1 - o, p2 - o) - nb.deg2rad(90)))) < 0.00001
    assert metric.length(q1).__str__() == "1/3"
    assert abs(float((metric.angle(q1, q2) - nb.deg2rad(90)))) < 0.00001
    assert metric.angle(p1 - o, p1 - o).__str__() == "0.0"
    assert metric.angle(q1, q1).__str__() == "0.0"

    metric = geo.Cellparameters(4.15, 4.15, 28.64, 90, 90, 120).to_Metric()

    M = nb.Matrix([[9, 0, 0, 0],
                   [0, 4, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    metric = geo.Metric(M)

    cell = metric.to_Cellparameters()
    assert cell.__str__() == \
        geo.Cellparameters(3, 2, 1, 90.0, 90.0, 90.0).__str__()

    t = geo.Transformation(nb.Matrix([[0, 1, 0, 0],
                                      [1, 0, 0, 0],
                                      [0, 0, 1, 0.5],
                                      [0, 0, 0, 1]]))

    assert t ** metric == geo.Metric(nb.Matrix([[4, 0, 0, 0],
                                                [0, 9, 0, 0],
                                                [0, 0, 1, 0],
                                                [0, 0, 0, 1]]))

    metric = geo.Cellparameters(fs("8.534(5)"), fs("8.556(5)"), fs("7.015(5)"),
                                fs("101.53(8)"), fs("114.97(8)"), 
                                fs("103.38(8)")).to_Metric()
    assert np.abs(metric.cellvolume().value.n - 425.24239) < 0.0001

    metric = geo.Cellparameters(fs("1.0(1)"), 1, 1, 90, 90, 90).to_Metric()
    print(metric.cellvolume())
    assert np.abs(metric.cellvolume().value.n - 1) < 0.00000001
    assert np.abs(metric.cellvolume().value.s - 0.1) < 0.00000001

    a = fs("1.0(1)")
    metric = geo.Cellparameters(a, a, a, 90, 90, 90).to_Metric()
    m00 = metric.value.liste[0].liste[0]
    m11 = metric.value.liste[1].liste[1]
    assert (m00 - m11).value.n == 0.0
    assert (m00 - m11).value.s == 0.0


def test_Transgen():
    tg = geo.Transgen(geo.Dif(nb.Matrix([[1], [0], [0], [0]])),
                      geo.Dif(nb.Matrix([[0], [0], [2], [0]])),
                      geo.Dif(nb.Matrix([[0], [3], [0], [0]])))
    assert tg.__str__() == "Transgen /  1  \   /  0  \   /  0  \ \n"\
                           "        |   0   | |   0   | |   3   |\n"\
                           "         \  0  /   \  2  /   \  0  / "


def test_canonical():
    tg = geo.canonical
    assert tg.__str__() == "canonical"


def test_Coset():
    g = geo.Symmetry(nb.Matrix([[1,  0, 2, -1],
                                [0, -2, 0,  0],
                                [0,  0, 1,  1],
                                [0,  0, 0,  1]]))
    tg = geo.Transgen(geo.Dif(nb.Matrix([[1], [0], [0], [0]])),
                      geo.Dif(nb.Matrix([[0], [1], [0], [0]])),
                      geo.Dif(nb.Matrix([[0], [0], [2], [0]])))
    tg1 = geo.Transgen(geo.Dif(nb.Matrix([[1], [0], [0], [0]])),
                       geo.Dif(nb.Matrix([[0], [1], [0], [0]])),
                       geo.Dif(nb.Matrix([[0], [0], [2], [0]])))
    assert tg == tg1
    c = geo.Coset(g, tg)
    assert c.__str__() == \
        "{x+2z,-2y,z+1}\n"\
        "     1  0  0  \n"\
        "     0  1  0  \n"\
        "     0  0  2  "
    c = geo.Coset(g, geo.canonical)
    assert c.__str__() == "{x+2z,-2y,z}"
    g = geo.Symmetry(nb.Matrix([[ 1, 0, 0, 0.5],
                                [ 0, 1, 0, 0],
                                [ 0, 0, 1, 0],
                                [ 0, 0, 0, 1]]))
    c = geo.Coset(g, geo.canonical)
    g2 = geo.Symmetry(nb.Matrix([[ 1, 0, 0, -0.5],
                                 [ 0, 1, 0, 0],
                                 [ 0, 0, 1, 0],
                                 [ 0, 0, 0, 1]]))
    p1 = geo.Pos(nb.Matrix([[0.3], [0], [0], [1]]))
    p2 = geo.Pos(nb.Matrix([[0.8], [0], [0], [1]]))
    assert c.coset_representant_for_pos(p1) == g
    assert c.coset_representant_for_pos(p2) == g2


def test_Spacegroup():
    transgen = geo.canonical
    c1 = geo.Coset(geo.Symmetry(nb.Matrix.onematrix(4)),
                   transgen)
    c2 = geo.Coset(geo.Symmetry(nb.Matrix([[-1,  0,  0, 0],
                                           [0, -1,  0, 0],
                                           [0,  0, -1, 0],
                                           [0,  0,  0, 1]])),
                   transgen)
    sg = geo.Spacegroup(transgen, [c1, c2])
    assert sg.__str__() == \
        "Spacegroup        \n"\
        "----------        \n"\
        " canonical        \n"\
        "             x,y,z\n"\
        "          -x,-y,-z"
    transgen = geo.Transgen(geo.Dif(nb.Matrix([[1], [0], [0], [0]])),
                            geo.Dif(nb.Matrix([[0], [1], [0], [0]])),
                            geo.Dif(nb.Matrix([[0], [0], [2], [0]])))
    c1 = geo.Coset(geo.Symmetry(nb.Matrix.onematrix(4)),
                   transgen)
    c2 = geo.Coset(geo.Symmetry(nb.Matrix([[-1,  0,  0, 0],
                                           [0, -1,  0, 0],
                                           [0,  0, -1, 0],
                                           [0,  0,  0, 1]])),
                   transgen)
    sg = geo.Spacegroup(transgen, [c1, c2])
    assert sg.__str__() == \
        "                           Spacegroup        \n"\
        "                           ----------        \n"\
        "Transgen /  1  \   /  0  \   /  0  \         \n"\
        "        |   0   | |   1   | |   0   |        \n"\
        "         \  0  /   \  0  /   \  2  /         \n"\
        "                                        x,y,z\n"\
        "                                     -x,-y,-z"

    sg = geo.Spacegroup(geo.canonical,
        [geo.Coset(geo.Symmetry(nb.Matrix.onematrix(4)), geo.canonical),
         geo.Coset(geo.Symmetry(nb.Matrix([[1,  0, 0, 0],
                                           [0, -1, 0, 0],
                                           [0,  0, 1, 0],
                                           [0,  0, 0, 1]])), geo.canonical)])

    transformation = geo.Transformation(nb.Matrix([[0, 1, 0, 0],
                                                   [1, 0, 0, 0],
                                                   [0, 0, 1, 0],
                                                   [0, 0, 0, 1]]))
    sg1 = transformation ** sg
    sg2 = geo.Spacegroup(transformation ** geo.canonical,
        [geo.Coset(geo.Symmetry(nb.Matrix.onematrix(4)), geo.canonical),
         geo.Coset(geo.Symmetry(nb.Matrix([[-1, 0, 0, 0],
                                           [0, 1, 0, 0],
                                           [0, 0, 1, 0],
                                           [0, 0, 0, 1]])), geo.canonical)])

    assert sg.is_really_a_spacegroup() == True
    sg_error = geo.Spacegroup(geo.canonical,
        [geo.Coset(geo.Symmetry(nb.Matrix.onematrix(4)), geo.canonical),
         geo.Coset(geo.Symmetry(nb.Matrix([[1, 0, 0, fr.Fraction(1, 4)],
                                           [0, 1, 0, 0],
                                           [0, 0, 1, 0],
                                           [0, 0, 0, 1]])),
                   geo.canonical)])
    assert sg_error.is_really_a_spacegroup() == False
    # Hier ist noch folgender Fehler:
    # Das Programm berücksichtigt die Reihenfolge der
    # Symmetrieelemente eines Transgens. D.h. z.B.:
    #
    # / 1 \  / 0 \  / 0 \      / 0 \  / 1 \  / 0 \
    #|  0  ||  1  ||  0  | != |  1  ||  0  ||  0  |
    # \ 0 /  \ 0 /  \ 1 /      \ 0 /  \ 0 /  \ 1 /
    #
    # Was aber eigentlich gleich ist.

    #assert sg1.__str__() == sg2.__str__()


def test_operations():
    # Here I want to test all operations between equal and different types.
    # It shall be as follows:
    #
    #         *         | Symmetry    Transformation   Transgen   Coset  Pos Dif Metric  Spacegroup
    # ----------------------------------------------------------------------------------------------
    #   Symmetry        | Symmetry         -              -         -     -   -    -          -
    #   Transformation  |    -        Transformation      -         -     -   -    -          -
    #   Transgen        |    -             -              -         -     -   -    -          -
    #   Coset           |    -             -              -       Coset   -   -    -          -
    #   Pos             |    -             -              -         -     -   -    -          -
    #   Dif             |    -             -              -         -     -   -    -          -
    #   Metric          |    -             -              -         -     -   -    -          -
    #   Spacegroup      |    -             -              -         -     -   -    -          -
    #
    #
    #         **        | Symmetry  Transformation  Transgen  Coset    Pos   Dif Metric  Spacegroup
    # -----------------------------------------------------------------------------------------------
    #   Symmetry        |    -             -           -        -      Pos   Dif   -         -
    #   Transformation  | Symmetry         -        Transgen  Coset    Pos   Dif Metric  Spacegroup
    #   Transgen        |    -             -           -        -       -     -    -         -
    #   Coset           |    -             -           -        -      Pos   Dif   -         -
    #   Pos             |    -             -           -        -       -     -    -         -
    #   Dif             |    -             -           -        -       -     -    -         -
    #   Metric          |    -             -           -        -       -     -    -         -
    #   Spacegroup      |    -             -           -        -       -     -    -         -
    #
    #
    #         %         | Symmetry  Transformation   Transgen  Coset   Pos   Dif Metric  Spacegroup
    #  ---------------------------------------------------------------------------------------------
    #   Symmetry        |    -            -          Symmetry    -      -     -    -         -
    #   Transformation  |    -            -             -        -      -     -    -         -
    #   Transgen        |    -            -             -        -      -     -    -         -
    #   Coset           |    -            -           Coset      -      -     -    -         -
    #   Pos             |    -            -            Pos       -      -     -    -         -
    #   Dif             |    -            -            Dif       -      -     -    -         -
    #   Metric          |    -            -             -        -      -     -    -         -
    #   Spacegroup      |    -            -          Spacegroup  -      -     -    -         -

    # Coset needs some pow()-declarations, so first I test everything else:
    symmetry = geo.Symmetry(nb.Matrix([[-1,  0, 0, 0],
                                       [0, -1, 0, 0],
                                       [0,  0, 1, 0],
                                       [0,  0, 0, 1]]))
    transformation = geo.Transformation(nb.Matrix([[0, 1, 0, 0],
                                                   [1, 0, 0, 0],
                                                   [0, 0, 2, 0],
                                                   [0, 0, 0, 1]]))
    transgen = geo.canonical
    pos = geo.Pos(nb.Matrix([[1], [2], [3], [1]]))
    dif = geo.Dif(nb.Matrix([[4], [5], [6], [0]]))
    metric = geo.Metric(nb.Matrix([[4, 0, 0, 0],
                                   [0, 9, 0, 0],
                                   [0, 0, 1, 0],
                                   [0, 0, 0, 1]]))
    spacegroup = geo.Spacegroup(geo.canonical,
        [geo.Coset(geo.Symmetry(nb.Matrix.onematrix(4)), geo.canonical),
         geo.Coset(geo.Symmetry(nb.Matrix([[-1,  0,  0, 0],
                                           [0, -1,  0, 0],
                                           [0,  0, -1, 0],
                                           [0,  0,  0, 1]])), geo.canonical)])

    # * :
    #====

    # symmetry * symmetry:
    assert isinstance(symmetry * symmetry, geo.Symmetry)

    # transformation * transformation
    assert isinstance(transformation * transformation, geo.Transformation)

    # **:
    #====

    # symmetry ** pos:
    assert isinstance(symmetry ** pos, geo.Pos)

    # symmetry ** dif:
    assert isinstance(symmetry ** dif, geo.Dif)

    # transformation ** symmetry:
    assert isinstance(transformation ** symmetry, geo.Symmetry)

    # transformation ** transgen:
    assert isinstance(transformation ** transgen, geo.Transgen)

    # transformation ** pos:
    assert isinstance(transformation ** pos, geo.Pos)

    # transformation ** dif:
    assert isinstance(transformation ** dif, geo.Dif)

    # transformation ** metric:
    assert isinstance(transformation ** metric, geo.Metric)

    # transformation ** spacegroup:
    assert isinstance(transformation ** spacegroup, geo.Spacegroup)

    # %:
    #===

    # symmetry % transgen:
    assert isinstance(symmetry % transgen, geo.Symmetry)

    # pos % transgen:
    assert isinstance(pos % transgen, geo.Pos)
    transgen1 = geo.Transgen(geo.Dif(nb.Matrix([[1], [0], [0], [0]])),
                             geo.Dif(nb.Matrix([[0], [1], [0], [0]])),
                             geo.Dif(nb.Matrix([[0], [0], [2], [0]])))
    pos1 = geo.Pos(nb.Matrix([[0], [0], [fr.Fraction(3, 2)], [1]]))
    pos1_ = geo.Pos(nb.Matrix([[0], [0], [fr.Fraction(3, 2)], [1]]))
    assert pos1 % transgen1 == pos1_

    transgen1 = geo.Transgen(geo.Dif(nb.Matrix([[0], [0], [2], [0]])),
                             geo.Dif(nb.Matrix([[0], [1], [0], [0]])),
                             geo.Dif(nb.Matrix([[1], [0], [0], [0]])))
    pos1 = geo.Pos(nb.Matrix([[0], [0], [fr.Fraction(3, 2)], [1]]))
    pos1_ = geo.Pos(nb.Matrix([[0], [0], [fr.Fraction(3, 2)], [1]]))
    assert pos1 % transgen1 == pos1_

    # dif % transgen:
    assert isinstance(dif % transgen, geo.Dif)

    transgen1 = geo.Transgen(geo.Dif(nb.Matrix([[0], [0], [2], [0]])),
                             geo.Dif(nb.Matrix([[0], [1], [0], [0]])),
                             geo.Dif(nb.Matrix([[1], [0], [0], [0]])))
    dif1 = geo.Dif(nb.Matrix([[0], [0], [fr.Fraction(3, 2)], [0]]))
    dif1_ = geo.Dif(nb.Matrix([[0], [0], [fr.Fraction(3, 2)], [0]]))
    assert dif1 % transgen1 == dif1_

    # spacegroup % transgen:
    assert isinstance(spacegroup % transgen, geo.Spacegroup)

    # Here comes Coset:
    #==================

    coset = geo.Coset(symmetry, transgen)

    # coset * coset:
    assert isinstance(coset * coset, geo.Coset)

    # coset ** pos:
    assert isinstance(coset ** pos, geo.Pos)

    # coset ** dif:
    assert isinstance(coset ** dif, geo.Dif)

    # coset % transgen:
    assert isinstance(coset % transgen, geo.Coset)

    transgen1 = geo.Transgen(geo.Dif(nb.Matrix([[0], [0], [2], [0]])),
                             geo.Dif(nb.Matrix([[0], [1], [0], [0]])),
                             geo.Dif(nb.Matrix([[1], [0], [0], [0]])))
    coset1 = geo.Coset(geo.Symmetry(nb.Matrix([[1, 0, 0, fr.Fraction(3, 2)],
                                               [0, 1, 0, fr.Fraction(3, 2)],
                                               [0, 0, 1, fr.Fraction(7, 2)],
                                               [0, 0, 0, 1]])), transgen1)
    coset1_ = geo.Coset(geo.Symmetry(nb.Matrix([[1, 0, 0, fr.Fraction(1, 2)],
                                                [0, 1, 0, fr.Fraction(1, 2)],
                                                [0, 0, 1, fr.Fraction(3, 2)],
                                                [0, 0, 0, 1]])), transgen1)
    assert coset1 % transgen1 == coset1_


def test_centre_of_gravity():
    p1 = geo.Pos(nb.Matrix([[1], [0], [0], [1]]))
    p2 = geo.Pos(nb.Matrix([[3], [0], [0], [1]]))
    assert geo.centre_of_gravity([p1, p2]) == geo.Pos(nb.Matrix([[2], [0], [0], [1]]))

