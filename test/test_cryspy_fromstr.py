import pytest
import sys
sys.path.append("../src/")
import cryspy_numbers as nb
import uncertainties as uc
import quicktions as fr
import cryspy_fromstr as fs
import cryspy_geo as geo


def test_removeletters():
    string = "hallo 1 2 3"
    assert fs.removeletters(string) == "      1 2 3"


def test_fromstr():
    string = "1/2"
    assert fs.fromstr(string) == nb.Mixed(fr.Fraction(1, 2))
    string = "1.2+/-0.1"
    assert fs.fromstr(string) == nb.Mixed(uc.ufloat(1.2, 0.1))
    string = "1.2(1)"
    assert fs.fromstr(string) == nb.Mixed(uc.ufloat(1.2, 0.1))
    string = "4"
    assert fs.fromstr(string) == nb.Mixed(fr.Fraction(4, 1))
    string = "4.5"
    assert fs.fromstr(string) == nb.Mixed(uc.ufloat(4.5, 0.0))
    string = "/ 1 2 \ \n \ 3 4 /"
    assert fs.fromstr(string) == \
        nb.Matrix([nb.Row([nb.Mixed(1), nb.Mixed(2)]), \
                   nb.Row([nb.Mixed(3), nb.Mixed(4)])])
    string = "1 2 \n 3 4"
    assert fs.fromstr(string) == \
        nb.Matrix([nb.Row([nb.Mixed(1), nb.Mixed(2)]), \
                   nb.Row([nb.Mixed(3), nb.Mixed(4)])])
    string = "x+y,y - x +1/3,2z"
    g = fs.fromstr(string)
    assert g == geo.Symmetry(fs.fromstr("/ 1 1 0 0 \n"\
                                        " -1 1 0 1/3 \n"\
                                        "  0 0 2 0 \n"\
                                        "  0 0 0 1"))
    string = "a-b,b+a+1/3, 2c"
    g = fs.fromstr(string)
    assert g == geo.Transformation(fs.fromstr(" 1 1 0 0 \n"\
                                              "-1 1 0 1/3\n"\
                                              " 0 0 2 0 \n"\
                                              " 0 0 0 1").inv())

    string = "c,a,b"
    g = fs.fromstr(string)
    assert g == geo.Transformation(fs.fromstr("0 1 0 0 \n" \
                                              "0 0 1 0 \n" \
                                              "1 0 0 0 \n" \
                                              "0 0 0 1").inv())


    string = "p0 0 0"
    p = fs.fromstr(string)
    assert p == geo.Pos(fs.fromstr("0 \n 0 \n 0 \n 1"))
    string = "P0 0 0"
    p = fs.fromstr(string)
    assert p == geo.Pos(fs.fromstr("0 \n 0 \n 0 \n 1"))
    string = "r0 0 0"
    p = fs.fromstr(string)
    assert p == geo.Pos(fs.fromstr("0 \n 0 \n 0 \n 1"))
    string = "R0 0 0"
    p = fs.fromstr(string)
    assert p == geo.Pos(fs.fromstr("0 \n 0 \n 0 \n 1"))
    string = p.__str__()
    assert string == "Pos /  0  \ \n" \
                     "   |   0   |\n" \
                     "    \  0  / "
    p1 = fs.fromstr(string)
    assert p == p1
    string = "R1/2 1/2 1/2"
    p = fs.fromstr(string)
    assert p == geo.Pos(fs.fromstr("1/2 \n 1/2 \n 1/2 \n 1"))



def test_typefromstr():
  string = "/ 1 2 \ \\n\ 3 4/"
  assert fs.typefromstr(string) == nb.Matrix
  string = "<1 2 3>"
  assert fs.typefromstr(string) == nb.Matrix
  string = "1/2"
  assert fs.typefromstr(string) == nb.Mixed
  string = "1.2+/-0.1"
  assert fs.typefromstr(string) == nb.Mixed
  string = "1.2(1)"
  assert fs.typefromstr(string) == nb.Mixed
  string = "4"
  assert fs.typefromstr(string) == nb.Mixed
  string = "x+y,y -x + 1/3, 2z"
  assert fs.typefromstr(string) == geo.Symmetry
  string = "a+b,b-a+1/3,2c"
  assert fs.typefromstr(string) == geo.Transformation
  string = "{-x,-y,z+1/2}"
  assert fs.typefromstr(string) == geo.Coset
  string = "p0 0 0"
  assert fs.typefromstr(string) == geo.Pos
  string = "P0 0 0"
  assert fs.typefromstr(string) == geo.Pos
  string = "r0 0 0"
  assert fs.typefromstr(string) == geo.Pos
  string = "R0 0 0"
  assert fs.typefromstr(string) == geo.Pos
