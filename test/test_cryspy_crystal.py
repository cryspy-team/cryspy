import pytest
import sys
sys.path.append("../src/")
import cryspy_geo as geo
import cryspy_fromstr as fs
import cryspy_crystal as cr

def test_Atom():
    atom = cr.Atom("Cs1", "Cs", fs.fromstr(
