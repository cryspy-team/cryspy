import pytest
import sys
sys.path.append("../src/")
import cryspy_geo as geo
import cryspy_fromstr as fs

def test_Pos():
    v = fs.fromstr('/ 1 \n 2 \n 3 \n 1 /')
    x = geo.Pos(v)
    assert x.__str__() == "Pos /  1  \ \n   |   2   |\n    \  3  / \n"
