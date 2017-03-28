import sys
sys.path.append("../../src")
from cryspy_fromstr import fromstr as fs
import cryspy_geo as geo
import cryspy_crystal as cr
import cryspy_niceprint

atomset = \
cr.Atomset({cr.Atom("Dy1", "Dy", fs("p 0.982(0)    0.082(0)  1/4        ")), \
            cr.Atom("Mn1", "Mn", fs("p 1/2         0         0          ")), \
            cr.Atom("O1" , "O" , fs("p 0.108(2)    0.471(2)  1/4        ")), \
            cr.Atom("O2" , "O" , fs("p 0.707(1)    0.328(1)  0.052(1)   "))})

sg = geo.Spacegroup(geo.canonical, [fs("{x,y,z}"), fs("{-x,-y,-z}")])
liste = ["Dy1", "Mn1", "O1", "O2"]

atomset_all = (sg ** atomset) % geo.canonical

cellparameters = geo.Cellparameters(7.4288, 17.3131, 8.0696, 90, 90, 90)

metric = cellparameters.to_Metric()

print(cryspy_niceprint.print_cif_without_symmetries(liste, atomset_all, metric))
