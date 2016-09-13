import pytest
import sys
sys.path.append("../src/")
from cryspy import numbers as nb
import uncertainties as uc
import quicktions as fr
from cryspy import fromstr
from cryspy.fromstr import fromstr as fs
from cryspy import geo as geo


def test_removeletters():
    string = "hallo 1 2 3"
    assert fromstr.removeletters(string) == "      1 2 3"

def test_str2linearterm():
    term = fromstr.str2linearterm("a + b", ['a', 'b', 'c'])
    assert term == [1, 1, 0, 0] 

def test_fromstr():
    string = "1/2"
    assert isinstance(fs(string), nb.Mixed)
    assert fs(string) == nb.Mixed(fr.Fraction(1, 2))
    string = "1.2+/-0.1"
    assert fs(string) == nb.Mixed(uc.ufloat(1.2, 0.1))
    string = "1.2(1)"
    assert fs(string) == nb.Mixed(uc.ufloat(1.2, 0.1))
    string = "4"
    assert fs(string) == nb.Mixed(fr.Fraction(4, 1))
    string = "4.5"
    assert fs(string) == nb.Mixed(4.5)

    string = "1 2 3"
    assert fromstr.typefromstr(string) == nb.Matrix
    assert fs(string) == nb.Matrix([[1, 2, 3]])

    string = "/ 1 2 \ \n \ 3 4 /"
    assert fs(string) == \
        nb.Matrix([nb.Row([nb.Mixed(1), nb.Mixed(2)]), \
                   nb.Row([nb.Mixed(3), nb.Mixed(4)])])
    string = "1 2 \n 3 4"
    assert fs(string) == \
        nb.Matrix([nb.Row([nb.Mixed(1), nb.Mixed(2)]), \
                   nb.Row([nb.Mixed(3), nb.Mixed(4)])])
    string = "x+y,y - x +1/3,2z"
    g = fs(string)
    assert g == geo.Symmetry(fs("/ 1 1 0 0 \n"\
                                " -1 1 0 1/3 \n"\
                                "  0 0 2 0 \n"\
                                "  0 0 0 1"))
    string = "O->(0,0,0)\n" \
             "then\n" \
             "a' = a-b \n" \
             "b' = b+a \n" \
             "c' = 2c"
    g = fs(string)
    assert g == geo.Transformation(fs(" 1 1 0 0 \n"\
                                      "-1 1 0 0 \n"\
                                      " 0 0 2 0 \n"\
                                      " 0 0 0 1").inv())

    string = "O->(0,0,0) \n" \
             "then\n" \
             "a' = c \n" \
             "b' = a \n" \
             "c' = b"
    g = fs(string)
    assert g == geo.Transformation(fs("0 1 0 0 \n" \
                                      "0 0 1 0 \n" \
                                      "1 0 0 0 \n" \
                                      "0 0 0 1").inv())
    string = "O -> (1/2, 0, 0) \n" \
             "then\n" \
             "a' = a \n" \
             "b' = b \n" \
             "c' = c"
    g = fs(string)
    assert g == geo.Transformation(fs("1 0 0 -1/2 \n" \
                                      "0 1 0    0 \n" \
                                      "0 0 1    0 \n" \
                                      "0 0 0    1"))
    
    string1 = "O -> (1/2, 0, 0) \n" \
              "then\n" \
              "a' = a \n" \
              "b' = b \n" \
              "c' = c"

    string2 = "O -> (0,0,0) \n" \
              "then\n" \
              "a' = b\n" \
              "b' = a\n" \
              "c' = c"
    string = "O -> (1/2, 0, 0) \n" \
             "then\n"\
             "a' = b\n"\
             "b' = a\n"\
             "c' = c"

    g1 = fs(string1)
    g2 = fs(string2)
    g = fs(string)
    assert g == g2 * g1


    string = "O -> (1/2, 0, 0) \n" \
             "then\n" \
             "a' = a + b\n" \
             "b' = b\n" \
             "c' = c"
    print("--------")
    g = fs(string)
    print(g.value)
    assert g ** fs("p 1/2 0 0") == fs("p 0 0 0")
    assert g ** fs("p 1/2 1/3 0") == fs("p 0 1/3 0")
    assert g ** fs("p 0 0 0") == fs("p -1/2 1/2 0")

    assert g * g.inv() == geo.Transformation(nb.Matrix.onematrix(4))
    


    string = "p0 0 0"
    p = fs(string)
    assert p == geo.Pos(fs("0 \n 0 \n 0 \n 1"))
    string = "P0 0 0"
    p = fs(string)
    assert p == geo.Pos(fs("0 \n 0 \n 0 \n 1"))
    string = "r0 0 0"
    p = fs(string)
    assert p == geo.Pos(fs("0 \n 0 \n 0 \n 1"))
    string = "R0 0 0"
    p = fs(string)
    assert p == geo.Pos(fs("0 \n 0 \n 0 \n 1"))
    string = p.__str__()
    assert string == "Pos /  0  \ \n" \
                     "   |   0   |\n" \
                     "    \  0  / "
    p1 = fs(string)
    assert p == p1
    string = "R1/2 1/2 1/2"
    p = fs(string)
    assert p == geo.Pos(fs("1/2 \n 1/2 \n 1/2 \n 1"))

    q = fs("k1 2 3")
    assert q == geo.Rec(fs("1 2 3 0"))
    q = fs("K 1 2 3")
    assert q == geo.Rec(fs("1 2 3 0"))
    q = fs("q 1/2 1/2 0")
    assert q == geo.Rec(fs("1/2 1/2 0 0"))
    q = fs("Q0 0 0")
    assert q == geo.Rec(fs("0 0 0 0"))
    q = fs("Rec <  1  2  3  > ")
    assert q == geo.Rec(fs("1 2 3 0"))

def test_typefromstr():
  string = "/ 1 2 \ \\n\ 3 4/"
  assert fromstr.typefromstr(string) == nb.Matrix
  string = "<1 2 3>"
  assert fromstr.typefromstr(string) == nb.Matrix
  string = "1/2"
  assert fromstr.typefromstr(string) == nb.Mixed
  string = "1.2+/-0.1"
  assert fromstr.typefromstr(string) == nb.Mixed
  string = "1.2(1)"
  assert fromstr.typefromstr(string) == nb.Mixed
  string = "4"
  assert fromstr.typefromstr(string) == nb.Mixed
  string = "x+y,y -x + 1/3, 2z"
  assert fromstr.typefromstr(string) == geo.Symmetry
  string = "a+b,b-a+1/3,2c"
  assert fromstr.typefromstr(string) == geo.Transformation
  string = "{-x,-y,z+1/2}"
  assert fromstr.typefromstr(string) == geo.Coset
  string = "p0 0 0"
  assert fromstr.typefromstr(string) == geo.Pos
  string = "P0 0 0"
  assert fromstr.typefromstr(string) == geo.Pos
  string = "r0 0 0"
  assert fromstr.typefromstr(string) == geo.Pos
  string = "R0 0 0"
  assert fromstr.typefromstr(string) == geo.Pos
  string = "k0 0 0"
  assert fromstr.typefromstr(string) == geo.Rec
  string = "K0 0 0"
  assert fromstr.typefromstr(string) == geo.Rec
  string = "q0 0 0"
  assert fromstr.typefromstr(string) == geo.Rec
  string = "Q0 0 0"
  assert fromstr.typefromstr(string) == geo.Rec
  

