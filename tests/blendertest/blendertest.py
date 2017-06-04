import sys
sys.path.append('../../src/')
import cryspy
from cryspy.fromstr import fromstr as fs

metric = cryspy.geo.Cellparameters(10.4416, 10.4416, 6.3432, 90, 90, 120).to_Metric()

atomset = cryspy.crystal.Atomset( { \
    cryspy.crystal.Atom("Ca1", "Ca", fs("p 0       0      0      ")), \
    cryspy.crystal.Atom("Mn1", "Mn", fs("p 1/2     0      0      ")), \
    cryspy.crystal.Atom("Mn2", "Mn", fs("p 1/2     0      1/2    ")), \
    cryspy.crystal.Atom("Mn3", "Mn", fs("p 0       0      1/2    ")), \
    cryspy.crystal.Atom("O1",  "O",  fs("p 0.2226  0.2731 0.0814 ")), \
    cryspy.crystal.Atom("O2",  "O",  fs("p 0.34219 0.5221 0.3410 "))
    } )

Rm3 = cryspy.tables.spacegroup(148)

atomset = Rm3 ** atomset
atomset1 = fs("x,   y,   z+1") ** atomset
atomset2 = fs("x,   y+1, z  ") ** atomset
atomset3 = fs("x,   y+1, z+1") ** atomset
atomset4 = fs("x+1, y,   z  ") ** atomset
atomset5 = fs("x+1, y,   z+1") ** atomset
atomset6 = fs("x+1, y+1, z  ") ** atomset
atomset7 = fs("x+1, y+1, z+1") ** atomset

menge = set([])
    
for atom in atomset.menge:
    menge = menge.union({atom})

for atomseti in [atomset1, atomset2, atomset3, atomset4, \
                 atomset5, atomset6, atomset7]:
    for atom in atomseti.menge:
        if      -0.05 <= float(atom.pos.x()) <= 1.05 \
            and -0.05 <= float(atom.pos.y()) <= 1.05 \
            and -0.05 <= float(atom.pos.z()) <= 1.05:
            menge = menge.union({atom})

momentum = cryspy.crystal.Momentum("M", fs("p 1/2 1/2 1/2"), fs("d 1 0 0"))
menge.add(momentum)
bond = cryspy.crystal.Bond("B", fs("p 0 0 0"), fs("p 1/2 1/2 0"))
menge.add(bond)
face = cryspy.crystal.Face("F", [fs("p 0 0 0"), fs("p 1 0 0"), fs("p 0 1 0")])
menge.add(face)
atomset = cryspy.crystal.Atomset(menge)
cryspy.blender.make_blender_script(atomset, metric, "structure", "blenderscript.py")

