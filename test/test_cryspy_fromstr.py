import pytest
import sys
sys.path.append("../src/")
import cryspy_fromstr as fs
import cryspy_geo as geo

def test_fromstr():
   string = "x+y,y - x +1/3,2z"
   g = fs.fromstr(string)
   assert g == geo.Symmetry(fs.fromstr("/ 1 1 0 0 \n"\
                                       " -1 1 0 1/3 \n"\
                                       "  0 0 2 0 \n"\
                                       "  0 0 0 1"))


