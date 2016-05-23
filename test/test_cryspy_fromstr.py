import pytest
import sys
sys.path.append("../src/")
import cryspy_numbers as nb
import uncertainties as uc
import quicktions as fr
import cryspy_fromstr as fs
import cryspy_geo as geo

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
   string = "a+b,b-a +1/3, 2c"
   g = fs.fromstr(string)
   assert g == geo.Transformation(fs.fromstr(" 1 1 0 0 \n"\
                                             "-1 1 0 1/3\n"\
                                             " 0 0 2 0 \n"\
                                             " 0 0 0 1"))

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
