import pytest
import sys
sys.path.append("../src/")
import cryspy_geo as geo
import cryspy_fromstr as fs
import cryspy_tables as tb

def test_cryspy_tables():
    sg = tb.spacegroup(15)
#    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(33)
    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(46)
#    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(63)
#    assert sg.is_really_a_spacegroup() == True

