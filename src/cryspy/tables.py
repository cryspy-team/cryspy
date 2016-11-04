from cryspy.fromstr import fromstr as fs
import cryspy.numbers as numbers
from cryspy import geo as geo
import numpy as np

def spacegroup(number):
    if number == 15:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-x,y,-z+1/2}"), fs("{-x,-y,-z}"), fs("{x,-y,z+1/2}"), \
             fs("{x+1/2,y+1/2,z}"), fs("{-x+1/2,y+1/2,-z+1/2}"), fs("{-x+1/2,-y+1/2,-z}"), fs("{x+1/2,-y+1/2,z+1/2}")])

    if number == 33:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-x,-y,z+1/2}"), fs("{x+1/2,-y+1/2,z}"), fs("{-x+1/2,y+1/2,z+1/2}")])

    if number == 46:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-x,-y,z}"), fs("{x+1/2,-y,z}"), fs("{-x+1/2,y,z}"), \
             fs("{x+1/2,y+1/2,z+1/2}"), fs("{-x+1/2,-y+1/2,z+1/2}"), fs("{x,-y+1/2,z+1/2}"), fs("{-x,y+1/2,z+1/2}")])

    if number == 63:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-x,-y,z+1/2}"), fs("{-x,y,-z+1/2}"), fs("{x,-y,-z}"), \
             fs("{-x,-y,-z}"), fs("{x,y,-z+1/2}"), fs("{x,-y,z+1/2}"), fs("{-x,y,z}"), \
             fs("{x+1/2,y+1/2,z}"), fs("{-x+1/2,-y+1/2,z+1/2}"), fs("{-x+1/2,y+1/2,-z+1/2}"), fs("{x+1/2,-y+1/2,-z}"), \
             fs("{-x+1/2,-y+1/2,-z}"), fs("{x+1/2,y+1/2,-z+1/2}"), fs("{x+1/2,-y+1/2,z+1/2}"), fs("{-x+1/2,y+1/2,z}")])

    if number == 148:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-y,x-y,z}"), fs("{-x+y,-x,z}"), \
             fs("{-x,-y,-z}"), fs("{y,-x+y,-z}"), fs("{x-y,x,-z}"), \

             fs("{x+2/3,y+1/3,z+1/3}"), fs("{-y+2/3,x-y+1/3,z+1/3}"), fs("{-x+y+2/3,-x+1/3,z+1/3}"), \
             fs("{-x+2/3,-y+1/3,-z+1/3}"), fs("{y+2/3,-x+y+1/3,-z+1/3}"), fs("{x-y+2/3,x+1/3,-z+1/3}"), \

             fs("{x+1/3,y+2/3,z+2/3}"), fs("{-y+1/3,x-y+2/3,z+2/3}"), fs("{-x+y+1/3,-x+2/3,z+2/3}"), \
             fs("{-x+1/3,-y+2/3,-z+2/3}"), fs("{y+1/3,-x+y+2/3,-z+2/3}"), fs("{x-y+1/3,x+2/3,-z+2/3}")])

    if number == 166:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x ,y ,z }"), fs("{-y  , x-y, z}"), fs("{-x+y,-x  ,z }"), \
             fs("{y ,x ,-z}"), fs("{x-y ,-y  ,-z}"), fs("{-x  ,-x+y,-z}"), \
             fs("{-x,-y,-z}"), fs("{y   ,-x+y,-z}"), fs("{x-y ,x   ,-z}"), \
             fs("{-y,-x,z }"), fs("{-x+y,y   ,z }"), fs("{x   ,x-y ,z }"), \
             
             fs("{x  +2/3,y  +1/3,z  +1/3}"), fs("{-y   +2/3, x-y +1/3, z +1/3}"), fs("{-x+y +2/3,-x   +1/3,z  +1/3}"), \
             fs("{y  +2/3,x  +1/3,-z +1/3}"), fs("{x-y  +2/3,-y   +1/3,-z +1/3}"), fs("{-x   +2/3,-x+y +1/3,-z +1/3}"), \
             fs("{-x +2/3,-y +1/3,-z +1/3}"), fs("{y    +2/3,-x+y +1/3,-z +1/3}"), fs("{x-y  +2/3,x    +1/3,-z +1/3}"), \
             fs("{-y +2/3,-x +1/3,z  +1/3}"), fs("{-x+y +2/3,y    +1/3,z  +1/3}"), fs("{x    +2/3,x-y  +1/3,z  +1/3}"), \
              
             fs("{x  +1/3,y  +2/3,z  +2/3}"), fs("{-y   +1/3, x-y +2/3, z +2/3}"), fs("{-x+y +1/3,-x   +2/3,z  +2/3}"), \
             fs("{y  +1/3,x  +2/3,-z +2/3}"), fs("{x-y  +1/3,-y   +2/3,-z +2/3}"), fs("{-x   +1/3,-x+y +2/3,-z +2/3}"), \
             fs("{-x +1/3,-y +2/3,-z +2/3}"), fs("{y    +1/3,-x+y +2/3,-z +2/3}"), fs("{x-y  +1/3,x    +2/3,-z +2/3}"), \
             fs("{-y +1/3,-x +2/3,z  +2/3}"), fs("{-x+y +1/3,y    +2/3,z  +2/3}"), fs("{x    +1/3,x-y  +2/3,z  +2/3}")])


def formfactor(atomtype, sintl):
    assert isinstance(atomtype, str), \
        "atomtype must be of type str."
    assert isinstance(sintl, numbers.Mixed), \
        "sintl (sin(theta)/lambda) must be of type numbers.Mixed."
    if not (0.0 <= float(sintl) <= 2.0):
        print("Warning: sintl must be smaller than 2.0 Angstrom^(-1).")

    # Formula from [international tables C, S565 eq. 6.1.1.15].

    [a1, b1, a2, b2, a3, b3, a4, b4, c] = formfactorparameters(atomtype)
    sintl2 = float(sintl)**2
    f = a1 * np.exp(-b1 * sintl2) \
      + a2 * np.exp(-b2 * sintl2) \
      + a3 * np.exp(-b3 * sintl2) \
      + a4 * np.exp(-b4 * sintl2) \
      + c

    return f


def formfactorparameters(atomtype):
    assert isinstance(atomtype, str), \
        "atomtype must be of type str."

    # Data from [international tables C, table 6.1.1.4].

    if atomtype == "O":
        pars = [3.04850, 13.2771, 2.28680, 5.70110, 1.54630, \
                0.323900, 0.867000, 32.9089, 0.250800]

    if atomtype == "Ca":
        pars = [8.62660, 10.4421, 7.38730, 0.659900, 1.58990, \
                85.7484, 1.02110, 178.437, 1.37510]

    if atomtype == "Mn":
        pars = [11.2819, 5.34090, 7.35730, 0.343200, 3.01930, \
                17.8674, 2.24410, 83.7543, 1.08960]

    if atomtype == "Au":
        pars = [16.8819, 0.461100, 18.5913, 8.62160, 25.5582, \
                1.48260, 5.86000, 36.3956, 12.0658]


    return pars
