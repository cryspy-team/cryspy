import pytest
import sys
sys.path.append("../src/")
import cryspy_geo as geo
import cryspy_fromstr as fs

def test_Pos():
    v = fs.fromstr('/ 1 \n 2 \n 3 \n 1 /')
    x = geo.Pos(v)
    assert x.__str__() == "Pos /  1  \ \n   |   2   |\n    \  3  / \n"

def test_Dif():
    v = fs.fromstr('/ 1 \n 2 \n 3 \n 0 /')
    x = geo.Dif(v)
    assert x.__str__() == "Dif /  1  \ \n   |   2   |\n    \  3  / \n"

def test_eq():
    r1 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 3 \n 1 /'))
    r2 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 3 \n 1 /'))
    r3 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 4 \n 1 /'))
    q1 = geo.Dif(fs.fromstr('/ 4 \n 5 \n 6 \n 0 /'))
    q2 = geo.Dif(fs.fromstr('/ 4 \n 5 \n 6 \n 0 /'))
    q3 = geo.Dif(fs.fromstr('/ 3 \n 5 \n 6 \n 0 /'))
    assert not (r1 == q1)
    assert     (r1 == r1) 
    assert     (r1 == r2)
    assert not (r1 == r3)
    assert     (q1 == q1)
    assert     (q1 == q2)
    assert not (q1 == q3)


def test_add_and_sub():
    x1 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 3 \n 1 /'))
    x2 = geo.Pos(fs.fromstr('/ 2 \n 3 \n 4 \n 1 /'))
    d1 = geo.Dif(fs.fromstr('/ 4 \n 5 \n 6 \n 0 /'))
    d2 = geo.Dif(fs.fromstr('/ 5 \n 5 \n 5 \n 0 /'))
    assert (x1 + d1) == geo.Pos(fs.fromstr('/ 5 \n 7 \n 9 \n 1 /'))
    assert (d1 + d2) == geo.Dif(fs.fromstr('/ 9 \n 10 \n 11 \n 0 /'))
    assert (d1 - d2) == geo.Dif(fs.fromstr('/ -1 \n 0 \n 1 \n 0 /'))
    assert (x1 - d1) == geo.Pos(fs.fromstr('/ -3 \n -3 \n -3 \n 1 /'))
    assert (x1 - x2) == geo.Dif(fs.fromstr('/ -1 \n -1 \n -1 \n 0 /'))

def test_Operator():
    id = geo.Operator(fs.fromstr("/ 1 0 0 0 \n"\
                                 "  0 1 0 0 \n"\
                                 "  0 0 1 0 \n "\
                                 "  0 0 0 1 /"))
    g = geo.Operator(fs.fromstr("/ -1  0 0 0 \n"\
                                "   0 -1 0 0 \n"\
                                "   0  0 1 0 \n "\
                                "   0  0 0 1 /"))
    g1 = geo.Operator(fs.fromstr("/ -1  0 0 0 \n"\
                                 "   0 -1 0 0 \n"\
                                 "   0  0 1 0 \n "\
                                 "   0  0 0 1 /"))
    assert g.__str__() == "Operator /  -1   0  0  0  \ \n"\
                          "        |    0  -1  0  0   |\n"\
                          "        |    0   0  1  0   |\n"\
                          "         \   0   0  0  1  / \n"
    assert g == g1

def test_apply_Operator():
    g = geo.Operator(fs.fromstr("/ -1  0 1 0 \n"\
                                "   0 -1 0 0 \n"\
                                "   0  0 1 0 \n"\
                                "   0  0 0 1 /"))
    h = geo.Operator(fs.fromstr("/ 1 0 0 0 \n"\
                                "  0 1 0 0 \n"\
                                "  0 0 2 0 \n"\
                                "  0 0 0 1 /"))
    r = geo.Pos(fs.fromstr("/ 1 \n 2 \n 3 \n 1 /"))
    assert g ** r == geo.Pos(fs.fromstr("/ 2 \n -2 \n 3 \n 1 /"))
    assert h ** g == geo.Operator(fs.fromstr("/ -1  0 1/2 0 \n"\
                                             "   0 -1   0 0 \n"\
                                             "   0  0   1 0 \n"\
                                             "   0  0   0 1 /"))

def test_Symmetry():
    M = fs.fromstr("/ 1 0 2 -1 \n 0 -2 0 0 \n 0 0 1 1/3 \n 0 0 0 1 /")
    g = geo.Symmetry(M)
    assert g.__str__() == "x+2z-1,-2y,z+1/3"
