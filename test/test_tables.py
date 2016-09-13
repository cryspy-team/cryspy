import pytest
import sys
sys.path.append("../src/")
from cryspy import geo as geo
from cryspy import fromstr as fs
from cryspy import tables as tb

def test_cryspy_tables():
    sg = tb.spacegroup(15)
#    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(33)
#    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(46)
#    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(63)
#    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(166)
    assert sg.is_really_a_spacegroup() == True
