import pytest
import sys
sys.path.append("../src/")
import cryspy_numbers as nb
import quicktions as fr
import uncertainties as uc


def test_Mixed():
    # Create a number of type Mixed with 4 different types.
    q = fr.Fraction(2, 3)
    e = uc.ufloat(1.2, 0.1)
    i = 4
    f = 3.5
    q1 = fr.Fraction(2, 1)
    e1 = uc.ufloat(3.7, 0)
    assert isinstance(nb.Mixed(q).value, fr.Fraction)
    assert nb.Mixed(q).value == q
    assert isinstance(nb.Mixed(e).value, uc.UFloat)
    assert (nb.Mixed(e).value).n == e.n
    assert (nb.Mixed(e).value).s == e.s
    assert isinstance(nb.Mixed(i).value, int)
    assert nb.Mixed(i).value == i
    assert isinstance(nb.Mixed(f).value, float)
    assert nb.Mixed(f).value == f
    assert isinstance(nb.Mixed(q1).value, int)
    assert nb.Mixed(q1).value == 2
    assert isinstance(nb.Mixed(e1).value, float)
    assert nb.Mixed(e1).value == 3.7

    # Convert a number of type Mixed to float.
    assert isinstance(float(nb.Mixed(q)), float)
    assert float(nb.Mixed(q)) == float(2/3)
    assert isinstance(float(nb.Mixed(e)), float)
    assert float(nb.Mixed(e)) == 1.2
    assert isinstance(float(nb.Mixed(i)), float)
    assert float(nb.Mixed(i)) == 4.0
    assert isinstance(float(nb.Mixed(f)), float)
    assert float(nb.Mixed(f)) == 3.5

    # Print a number of type Mixed as str.
    assert isinstance(nb.Mixed(q).__str__(), str)
    assert nb.Mixed(q).__str__() == "2/3"
    assert isinstance(nb.Mixed(e).__str__(), str)
    assert nb.Mixed(e).__str__() == "1.20(10)"
    assert isinstance(nb.Mixed(i).__str__(), str)
    assert nb.Mixed(i).__str__() == "4"
    assert isinstance(nb.Mixed(f).__str__(), str)
    assert nb.Mixed(f).__str__() == "3.5"

    # Equal
    assert nb.Mixed(q) == nb.Mixed(q)
    assert nb.Mixed(e) == nb.Mixed(e)
    assert nb.Mixed(i) == nb.Mixed(i)
    assert nb.Mixed(f) == nb.Mixed(f)
    assert nb.Mixed(fr.Fraction(2, 3)) == nb.Mixed(fr.Fraction(2, 3))
    assert not(nb.Mixed(fr.Fraction(2, 3)) ==  nb.Mixed(fr.Fraction(1, 3)))
    assert nb.Mixed(uc.ufloat(1.2, 0.1)) == nb.Mixed(uc.ufloat(1.2, 0.1))
    assert not(nb.Mixed(uc.ufloat(1.2, 0.1)) == nb.Mixed(uc.ufloat(1.2, 0.2)))

    # Addition

    mq = nb.Mixed(q)
    me = nb.Mixed(e)
    mi = nb.Mixed(i)
    mf = nb.Mixed(f)

    """for x1 in [q, e, i, f]:
        for x2 in [q, e, i, f]:
            m1 = nb.Mixed(x1)
            m2 = nb.Mixed(x2)
            assert isinstance(m1 + m2, nb.Mixed)
            assert isinstance((m1 + m2).value
            assert isinstance(m1 + x2, nb.Mixed)
            assert isinstance(
            assert isinstance(m2 + m1, nb.Mixed)"""

    assert isinstance(mq + mq, nb.Mixed)
    assert isinstance((mq + mq).value, fr.Fraction)
    assert mq + mq == nb.Mixed(fr.Fraction(4, 3))
    assert isinstance(mq + q, nb.Mixed)
    assert isinstance((mq + q).value, fr.Fraction)
    assert mq + q == nb.Mixed(fr.Fraction(4, 3))
    assert isinstance(q + mq, nb.Mixed)
    assert isinstance((q + mq).value, fr.Fraction)
    assert q + mq == nb.Mixed(fr.Fraction(4, 3))

    assert isinstance(mq + me, nb.Mixed)
    assert isinstance((mq + me).value, uc.UFloat)
    assert mq + me == nb.Mixed(uc.ufloat(1.2, 0.10) + 2/3)
    assert isinstance(mq + e, nb.Mixed)
    assert isinstance((mq + e).value, uc.UFloat)
    assert mq + e == nb.Mixed(uc.ufloat(1.2, 0.10) + 2/3)
    assert isinstance(q + me, nb.Mixed)
    assert isinstance((q + me).value, uc.UFloat)
    assert q + me == nb.Mixed(uc.ufloat(1.2, 0.10) + 2/3)

    assert isinstance(mq + mi, nb.Mixed)
    assert isinstance((mq + mi).value, fr.Fraction)
    assert mq + mi == nb.Mixed(fr.Fraction(14, 3))
    assert isinstance(mq + i, nb.Mixed)
    assert isinstance((mq + i).value, fr.Fraction)
    assert mq + i == nb.Mixed(fr.Fraction(14, 3))
    assert isinstance(q + mi, nb.Mixed)
    assert isinstance((q + mi).value, fr.Fraction)
    assert q + mi == nb.Mixed(fr.Fraction(14, 3))

    assert isinstance(mq + mf, nb.Mixed)
    assert isinstance((mq + mf).value, float)
    assert mq + mf == nb.Mixed(3.5 + 2/3)
    assert isinstance(mq + f, nb.Mixed)
    assert isinstance((mq + f).value, float)
    assert mq + f == nb.Mixed(3.5 + 2/3)
    assert isinstance(q + mf, nb.Mixed)
    assert isinstance((q + mf).value, float)
    assert q + mf == nb.Mixed(3.5 + 2/3)

    assert isinstance(me + mq, nb.Mixed)
    assert isinstance((me + mq).value, uc.UFloat)
    assert me + mq == nb.Mixed(uc.ufloat(1.2, 0.1) + 2/3)
    assert isinstance(me + q, nb.Mixed)
    assert isinstance((me + q).value, uc.UFloat)
    assert me + q == nb.Mixed(uc.ufloat(1.2, 0.1) + 2/3)
    assert isinstance(e + mq, nb.Mixed)
    assert isinstance((e + mq).value, uc.UFloat)
    assert e + mq == nb.Mixed(uc.ufloat(1.2, 0.1) + 2/3)

    assert isinstance(me + me, nb.Mixed)
    assert isinstance((me + me).value, uc.UFloat)
    assert me + me == nb.Mixed(uc.ufloat(1.2, 0.1) + uc.ufloat(1.2, 0.1))
    assert isinstance(me + e, nb.Mixed)
    assert isinstance((me + e).value, uc.UFloat)
    assert me + e == nb.Mixed(uc.ufloat(1.2, 0.1) + uc.ufloat(1.2, 0.1))
    assert isinstance(e + me, nb.Mixed)
    assert isinstance((e + me).value, uc.UFloat)
    assert e + me == nb.Mixed(uc.ufloat(1.2, 0.1) + uc.ufloat(1.2, 0.1))

    assert isinstance(me + mi, nb.Mixed)
    assert isinstance((me + mi).value, uc.UFloat)
    assert me + mi == nb.Mixed(uc.ufloat(5.2, 0.1))
    assert isinstance(me + i, nb.Mixed)
    assert isinstance((me + i).value, uc.UFloat)
    assert me + i == nb.Mixed(uc.ufloat(5.2, 0.1))
    assert isinstance(e + mi, nb.Mixed)
    assert isinstance((e + mi).value, uc.UFloat)
    assert me + i == nb.Mixed(uc.ufloat(5.2, 0.1))

    assert isinstance(me + mf, nb.Mixed)
    assert isinstance((me + mf).value, uc.UFloat)
    assert me + mf == nb.Mixed(uc.ufloat(4.7, 0.1))
    assert isinstance(me + f, nb.Mixed)
    assert isinstance((me + f).value, uc.UFloat)
    assert me + f == nb.Mixed(uc.ufloat(4.7, 0.1))
    assert isinstance(e + mf, nb.Mixed)
    assert isinstance((e + mf).value, uc.UFloat)
    assert e + mf == nb.Mixed(uc.ufloat(4.7, 0.1))

    assert isinstance(mi + mq, nb.Mixed)
    assert isinstance((mi + mq), fr.Fraction)
    assert mi + mq == nb.Mixed(fr.Fraction(13, 3))




