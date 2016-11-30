import pytest
import sys
sys.path.append("../src/")
from cryspy import geo as geo
from cryspy.fromstr import fromstr as fs
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
    sg = tb.spacegroup(148)
#    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(198)
    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(166)
#    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(212)
#    assert sg.is_really_a_spacegroup() == True
    sg = tb.spacegroup(227)
#    assert sg.is_really_a_spacegroup() == True


def test_formfactor():
    assert 72.633286681565636 == tb.formfactor('Au', fs('0.13445'))
