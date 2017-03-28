import cryspy
from cryspy.fromstr import fromstr as fs
import cryspy.numbers as nb
import cryspy.geo as geo


class Karussell:
    def __init__(self, metric, zerodirection, positivedirection):

        self.zerodir = zerodirection * (1 / metric.length(zerodirection))
        self.positivedir = positivedirection - self.zerodir * metric.dot(positivedirection, self.zerodir)
        self.positivedir *= 1 / metric.length(self.positivedir)
        self.metric = metric

    def direction(self, angle):
        x = nb.cos(angle)
        y = nb.sin(angle)
        return self.zerodir * x + self.positivedir * y

def fill(atomset, extraextensions):
    assert isinstance(atomset, cryspy.crystal.Atomset), \
        "First argument of cryspy.utils.fill(...) must be of " \
        "type cryspy.crystal.Atomset."
    assert isinstance(extraextensions, list), \
        "Second argument of cryspy.utils.fill(...) must be of " \
        "type list."
    assert len(extraextensions) == 3, \
        "Second argument of cryspy.utils.fill(...) must be a " \
        "list of three numbers."
    for item in extraextensions:
        assert isinstance(item, cryspy.numbers.Mixed) \
            or isinstance(item, float) or isinstance(item, int), \
            "Scond argument of cryspy.utils.fill(...) must be a " \
            "list of three numbers."

    atomset_new =  \
                 ((atomset + "lbd") + fs("d -1 -1 -1")) \
               + ((atomset + "lb") + fs("d -1 -1  0")) \
               + ((atomset + "lbu") + fs("d -1 -1 +1")) \
               + ((atomset + "ld") + fs("d -1  0 -1")) \
               + ((atomset + "l") + fs("d -1  0  0")) \
               + ((atomset + "lu") + fs("d -1  0 +1")) \
               + ((atomset + "lfd") + fs("d -1 +1 -1")) \
               + ((atomset + "lf") + fs("d -1 +1  0")) \
               + ((atomset + "lfu") + fs("d -1 +1 +1")) \
               + ((atomset + "bd") + fs("d  0 -1 -1")) \
               + ((atomset + "b") + fs("d  0 -1  0")) \
               + ((atomset + "bu") + fs("d  0 -1 +1")) \
               + ((atomset + "d") + fs("d  0  0 -1")) \
               + ((atomset + "") + fs("d  0  0  0")) \
               + ((atomset + "u") + fs("d  0  0 +1")) \
               + ((atomset + "fd") + fs("d  0 +1 -1")) \
               + ((atomset + "f") + fs("d  0 +1  0")) \
               + ((atomset + "fu") + fs("d  0 +1 +1")) \
               + ((atomset + "rbd") + fs("d +1 -1 -1")) \
               + ((atomset + "rb") + fs("d +1 -1  0")) \
               + ((atomset + "rbu") + fs("d +1 -1 +1")) \
               + ((atomset + "rd") + fs("d +1  0 -1")) \
               + ((atomset + "r") + fs("d +1  0  0")) \
               + ((atomset + "ru") + fs("d +1  0 +1")) \
               + ((atomset + "rfd") + fs("d +1 +1 -1")) \
               + ((atomset + "rf") + fs("d +1 +1  0")) \
               + ((atomset + "rfu") + fs("d +1 +1 +1")) \

    menge = atomset_new.menge
    menge_new = set([])
    extra_x = extraextensions[0]
    extra_y = extraextensions[1]
    extra_z = extraextensions[2]
    for atom in menge:
        if (0 - extra_x <= float(atom.pos.x()) <= 1 + extra_x) \
            and (0 - extra_y <= float(atom.pos.y()) <= 1 + extra_y) \
            and (0 - extra_z <= float(atom.pos.z()) <= 1 + extra_z):
            menge_new.add(atom)
    return cryspy.crystal.Atomset(menge_new)
