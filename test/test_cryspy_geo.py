import pytest
import sys
sys.path.append("../src/")
import cryspy_geo as geo
import cryspy_fromstr as fs

def test_Pos():
    v = fs.fromstr('/ 1 \n 2 \n 3 \n 1 /')
    x = geo.Pos(v)
    assert x.__str__() == "Pos /  1  \ \n   |   2   |\n    \  3  / "

def test_Dif():
    v = fs.fromstr('/ 1 \n 2 \n 3 \n 0 /')
    x = geo.Dif(v)
    assert x.__str__() == "Dif /  1  \ \n   |   2   |\n    \  3  / "

def test_eq():
    r1 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 3 \n 1 /'))
    r2 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 3 \n 1 /'))
    r3 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 4 \n 1 /'))
    d1 = geo.Dif(fs.fromstr('/ 4 \n 5 \n 6 \n 0 /'))
    d2 = geo.Dif(fs.fromstr('/ 4 \n 5 \n 6 \n 0 /'))
    d3 = geo.Dif(fs.fromstr('/ 3 \n 5 \n 6 \n 0 /'))
    assert not (r1 == d1)
    assert     (r1 == r1) 
    assert     (r1 == r2)
    assert not (r1 == r3)
    assert     (d1 == d1)
    assert     (d1 == d2)
    assert not (d1 == d3)


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
                          "         \   0   0  0  1  / "
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
    d = geo.Dif(fs.fromstr("/ 2 \n 4 \n 6 \n 0 /"))
    assert g ** r == geo.Pos(fs.fromstr("/ 2 \n -2 \n 3 \n 1 /"))
    assert h ** g == geo.Operator(fs.fromstr("/ -1  0 1/2 0 \n"\
                                             "   0 -1   0 0 \n"\
                                             "   0  0   1 0 \n"\
                                             "   0  0   0 1 /"))
    assert g ** d == geo.Dif(fs.fromstr("/ 4 \n -4 \n 6 \n 0 /"))

def test_str2linearterm():
    string = "a + b + 1/2 + 2a -1/3c"
    assert geo.str2linearterm(string, ["a", "b", "c"]) == \
        [fs.fromstr('3'), fs.fromstr('1'), fs.fromstr('-1/3'), \
         fs.fromstr('1/2')]

def test_Symmetry():
    M = fs.fromstr("/ 1 0 2 -1 \n 0 -2 0 0 \n 0 0 1 1/3 \n 0 0 0 1 /")
    g = geo.Symmetry(M)
    assert g.__str__() == "x+2z-1,-2y,z+1/3"

def test_Transformation():
    M = fs.fromstr("/ 1 0 1 0 \n 0 1 0 1/2 \n -1 0 1 0 \n 0 0 0 1 /")
    g = geo.Transformation(M)
    assert g.__str__() == "Transformation a' =   a+c\n"\
                          "               b' = b+1/2\n"\
                          "               c' =  -a+c"

def test_Transgen():
    tg = geo.Transgen(fs.fromstr("1 0 0 0 \n"\
                                 "0 0 3 0 \n"\
                                 "0 2 0 0 \n"\
                                 "0 0 0 1"))
    assert tg.__str__() == "Transgen /  1  \   /  0  \   /  0  \ \n"\
                           "        |   0   | |   0   | |   3   |\n"\
                           "         \  0  /   \  2  /   \  0  / "

def test_CanonicalTransgen():
    tg = geo.CanonicalTransgen
    assert tg.__str__() == "Transgen /  1  \   /  0  \   /  0  \ \n"\
                           "        |   0   | |   1   | |   0   |\n"\
                           "         \  0  /   \  0  /   \  1  / "


def test_Coset():
    g = geo.Symmetry( \
        fs.fromstr("/ 1 0 2 -1 \n 0 -2 0 0 \n 0 0 1 1 \n 0 0 0 1 /"))
    tg = geo.Transgen(fs.fromstr("1 0 0 0 \n"\
                                 "0 1 0 0 \n"\
                                 "0 0 2 0 \n"\
                                 "0 0 0 1"))
    tg1 = geo.Transgen(fs.fromstr("1 0 0 0 \n"\
                                 "0 1 0 0 \n"\
                                 "0 0 2 0 \n"\
                                 "0 0 0 1"))
    assert tg == tg1
    c = geo.Coset(g, tg)
    assert c.__str__() == \
        "{x+2z,-2y,z+1}\n"\
        "     1  0  0  \n"\
        "     0  1  0  \n"\
        "     0  0  2  "

    c = geo.Coset(g, geo.CanonicalTransgen)
    assert c.__str__() == "{x+2z,-2y,z}"
    

   
