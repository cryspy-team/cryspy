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

    if number == 62:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-x+1/2,-y,z+1/2}"), fs("{-x,y+1/2,-z}"), fs("{x+1/2,-y+1/2,-z+1/2}"), \
             fs("{-x,-y,-z}"), fs("{x+1/2,y,-z+1/2}"), fs("{x,-y+1/2,z}"), fs("{-x+1/2,y+1/2,z+1/2}")])

    if number == 63:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-x,-y,z+1/2}"), fs("{-x,y,-z+1/2}"), fs("{x,-y,-z}"), \
             fs("{-x,-y,-z}"), fs("{x,y,-z+1/2}"), fs("{x,-y,z+1/2}"), fs("{-x,y,z}"), \
             fs("{x+1/2,y+1/2,z}"), fs("{-x+1/2,-y+1/2,z+1/2}"), fs("{-x+1/2,y+1/2,-z+1/2}"), fs("{x+1/2,-y+1/2,-z}"), \
             fs("{-x+1/2,-y+1/2,-z}"), fs("{x+1/2,y+1/2,-z+1/2}"), fs("{x+1/2,-y+1/2,z+1/2}"), fs("{-x+1/2,y+1/2,z}")])

    if number == 73:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-x+1/2,-y,z+1/2}"), fs("{-x,y+1/2,-z+1/2}"), fs("{x+1/2,-y+1/2,-z}"), \
             fs("{-x,-y,-z}"), fs("{x+1/2,y,-z+1/2}"), fs("{x,-y+1/2,z+1/2}"), fs("{-x+1/2,y+1/2,z}"), \
             fs("{x+1/2,y+1/2,z+1/2}"), fs("{-x,-y+1/2,z}"), fs("{-x+1/2,y,-z}"), fs("{x,-y,-z+1/2}"), \
             fs("{-x+1/2,-y+1/2,-z+1/2}"), fs("{x,y+1/2,-z}"), fs("{x+1/2,-y,z}"), fs("{-x,y,z+1/2}")])
             

    if number == 142:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-x+1/2,-y+1/2,z+1/2}"), fs("{-y,x+1/2,z+1/4}"), fs("{y+1/2,-x,z+3/4}"), \
             fs("{-x+1/2,y,-z+1/4}"), fs("{x,-y+1/2,-z+3/4}"), fs("{y+1/2,x+1/2,-z}"), fs("{-y,-x,-z+1/2}"), \
             fs("{-x,-y+1/2,-z+1/4}"), fs("{x+1/2,y,-z+3/4}"), fs("{y,-x,-z}"), fs("{-y+1/2,x+1/2,-z+1/2}"), \
             fs("{x+1/2,-y+1/2,z}"), fs("{-x,y,z+1/2}"), fs("{-y+1/2,-x,z+1/4}"), fs("{y,x+1/2,z+3/4}"), \
             fs("{x+1/2,y+1/2,z+1/2}"), fs("{-x,-y,z}"), fs("{-y+1/2,x,z+3/4}"), fs("{y,-x+1/2,z+1/4}"), \
             fs("{-x,y+1/2,-z+3/4}"), fs("{x+1/2,-y,-z+1/4}"), fs("{y,x,-z+1/2}"), fs("{-y+1/2,-x+1/2,-z}"), \
             fs("{-x+1/2,-y,-z+3/4}"), fs("{x,y+1/2,-z+1/4}"), fs("{y+1/2,-x+1/2,-z+1/2}"), fs("{-y,x,-z}"), \
             fs("{x,-y,z+1/2}"), fs("{-x+1/2,y+1/2,z}"), fs("{-y,-x+1/2,z+3/4}"), fs("{y+1/2,x,z+1/4}")])

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

    if number == 186:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-y,x-y,z}"), fs("{-x+y,-x,z}"), \
             fs("{-x,-y,z+1/2}"), fs("{y,-x+y,z+1/2}"), fs("{x-y,x,z+1/2}"), \
             fs("{-y,-x,z}"), fs("{-x+y,y,z}"), fs("{x,x-y,z}"), \
             fs("{y,x,z+1/2}"), fs("{x-y,-y,z+1/2}"), fs("{-x,-x+y,z+1/2}")])

    if number == 198:
        return geo.Spacegroup(geo.canonical, \
            [fs("{x,y,z}"), fs("{-x+1/2,-y,z+1/2}"), fs("{-x,y+1/2,-z+1/2}"), fs("{x+1/2,-y+1/2,-z}"), \
             fs("{z,x,y}"), fs("{z+1/2,-x+1/2,-y}"), fs("{-z+1/2,-x,y+1/2}"), fs("{-z,x+1/2,-y+1/2}"), \
             fs("{y,z,x}"), fs("{-y,z+1/2,-x+1/2}"), fs("{y+1/2,-z+1/2,-x}"), fs("{-y+1/2,-z,x+1/2}")])

    if number == 212:
        return geo.Spacegroup(geo.canonical, \
             [fs("{x,y,z}"),              fs("{-x+1/2,-y,z+1/2}"),      fs("{-x,y+1/2,-z+1/2}"),      fs("{x+1/2,-y+1/2,-z}"), \
              fs("{z,x,y}"),              fs("{z+1/2,-x+1/2,-y}"),      fs("{-z+1/2,-x,y+1/2}"),      fs("{-z,x+1/2,-y+1/2}"), \
              fs("{y,z,x}"),              fs("{-y,z+1/2,-x+1/2}"),      fs("{y+1/2,-z+1/2,-x}"),      fs("{-y+1/2,-z,x+1/2}"), \
              fs("{y+1/4,x+3/4,-z+3/4}"), fs("{-y+1/4,-x+1/4,-z+1/4}"), fs("{ y+3/4,-x+3/4, z+1/4}"), fs("{-y+3/4, x+1/4, z+3/4}"), \
              fs("{x+1/4,z+3/4,-y+3/4}"), fs("{-x+3/4, z+1/4, y+3/4}"), fs("{-x+1/4,-z+1/4,-y+1/4}"), fs("{ x+3/4,-z+3/4, y+1/4}"), \
              fs("{z+1/4,y+3/4,-x+3/4}"), fs("{ z+3/4,-y+3/4, x+1/4}"), fs("{-z+3/4, y+1/4, x+3/4}"), fs("{-z+1/4,-y+1/4,-x+1/4}")])

    if number == 227:
        sg = geo.Spacegroup(geo.canonical, \
            [fs("{ x,     y,     z    }"), fs("{    -x,    -y+1/2, z+1/2}"), fs("{-x+1/2, y+1/2,-z    }"), fs("{ x+1/2,-y,    -z+1/2}"), \
             fs("{ z,     x,     y    }"), fs("{     z+1/2,-x,    -y+1/2}"), fs("{-z,    -x+1/2, y+1/2}"), fs("{-z+1/2, x+1/2,-y    }"), \
             fs("{ y,     z,     x    }"), fs("{    -y+1/2, z+1/2,-x    }"), fs("{ y+1/2,-z,    -x+1/2}"), fs("{-y,    -z+1/2, x+1/2}"), \
             fs("{ y+3/4, x+1/4,-z+3/4}"), fs("{-y+1/4,    -x+1/4,-z+1/4}"), fs("{ y+1/4,-x+3/4, z+3/4}"), fs("{-y+3/4, x+3/4, z+1/4}"), \
             fs("{ x+3/4, z+1/4,-y+3/4}"), fs("{-x+3/4,     z+3/4, y+1/4}"), fs("{-x+1/4,-z+1/4,-y+1/4}"), fs("{ x+1/4,-z+3/4, y+3/4}"), \
             fs("{ z+3/4, y+1/4,-x+3/4}"), fs("{ z+1/4,    -y+3/4, x+3/4}"), fs("{-z+3/4, y+3/4, x+1/4}"), fs("{-z+1/4,-y+1/4,-x+1/4}"), \
             fs("{-x+1/4,-y+1/4,-z+1/4}"), fs("{ x+1/4,     y+3/4,-z+3/4}"), fs("{ x+3/4,-y+3/4, z+1/4}"), fs("{-x+3/4, y+1/4, z+3/4}"), \
             fs("{-z+1/4,-x+1/4,-y+1/4}"), fs("{-z+3/4,     x+1/4, y+3/4}"), fs("{ z+1/4, x+3/4,-y+3/4}"), fs("{ z+3/4,-x+3/4, y+1/4}"), \
             fs("{-y+1/4,-z+1/4,-x+1/4}"), fs("{ y+3/4,    -z+3/4, x+1/4}"), fs("{-y+3/4, z+1/4, x+3/4}"), fs("{ y+1/4, z+3/4,-x+3/4}"), \
             fs("{-y+1/2,-x,     z+1/2}"), fs("{ y,         x,     z    }"), fs("{-y,     x+1/2,-z+1/2}"), fs("{ y+1/2,-x+1/2,-z    }"), \
             fs("{-x+1/2,-z,     y+1/2}"), fs("{ x+1/2,    -z+1/2,-y    }"), fs("{ x,     z,     y    }"), fs("{-x,     z+1/2,-y+1/2}"), \
             fs("{-z+1/2,-y,     x+1/2}"), fs("{-z,         y+1/2,-x+1/2}"), fs("{ z+1/2,-y+1/2,-x    }"), fs("{ z,     y,     x    }")])
        sg = geo.Spacegroup( \
            geo.canonical, \
            sg.liste_cosets + \
            [fs("{x,y+1/2,z+1/2}")*coset for coset in sg.liste_cosets]+ \
            [fs("{x+1/2,y,z+1/2}")*coset for coset in sg.liste_cosets]+ \
            [fs("{x+1/2,y+1/2,z}")*coset for coset in sg.liste_cosets] \
        )
        return sg

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

def colorscheme_jmol(typ):
    assert isinstance(typ, str), \
        "Argument typ must be of type str."

    if typ == "H":
        spheresize = 0.1000
        color = (1.0000, 1.0000, 1.0000)
    elif typ == "He":
        spheresize = 0.1260
        color = (0.8510, 1.0000, 1.0000)
    elif typ == "Li":
        spheresize = 0.1442
        color = (0.8000, 0.5020, 1.0000)
    elif typ == "Be":
        spheresize = 0.1587
        color = (0.7608, 1.0000, 0.0000)
    elif typ == "B":
        spheresize = 0.1710
        color = (1.0000, 0.7098, 0.7098)
    elif typ == "C":
        spheresize = 0.1817
        color = (0.5647, 0.5647, 0.5647)
    elif typ == "N":
        spheresize = 0.1913
        color = (0.1882, 0.3137, 0.9725)
    elif typ == "O":
        spheresize = 0.2000
        color = (1.0000, 0.0510, 0.0510)
    elif typ == "F":
        spheresize = 0.2080
        color = (0.5647, 0.8784, 0.3137)
    elif typ == "Ne":
        spheresize = 0.2154
        color = (0.7020, 0.8902, 0.9608)
    elif typ == "Na":
        spheresize = 0.2224
        color = (0.6706, 0.3608, 0.9490)
    elif typ == "Mg":
        spheresize = 0.2289
        color = (0.5412, 1.0000, 0.0000)
    elif typ == "Al":
        spheresize = 0.2351
        color = (0.7490, 0.6510, 0.6510)
    elif typ == "Si":
        spheresize = 0.2410
        color = (0.9412, 0.7843, 0.6275)
    elif typ == "P":
        spheresize = 0.2466
        color = (1.0000, 0.5020, 0.0000)
    elif typ == "S":
        spheresize = 0.2520
        color = (1.0000, 1.0000, 0.1882)
    elif typ == "Cl":
        spheresize = 0.2571
        color = (0.1216, 0.9412, 0.1216)
    elif typ == "Ar":
        spheresize = 0.2621
        color = (0.5020, 0.8196, 0.8902)
    elif typ == "K":
        spheresize = 0.2668
        color = (0.5608, 0.2510, 0.8314)
    elif typ == "Ca":
        spheresize = 0.2714
        color = (0.2392, 1.0000, 0.0000)
    elif typ == "Sc":
        spheresize = 0.2759
        color = (0.9020, 0.9020, 0.9020)
    elif typ == "Ti":
        spheresize = 0.2802
        color = (0.7490, 0.7608, 0.7804)
    elif typ == "V":
        spheresize = 0.2844
        color = (0.6510, 0.6510, 0.6706)
    elif typ == "Cr":
        spheresize = 0.2884
        color = (0.5412, 0.6000, 0.7804)
    elif typ == "Mn":
        spheresize = 0.2924
        color = (0.6118, 0.4784, 0.7804)
    elif typ == "Fe":
        spheresize = 0.2962
        color = (0.8784, 0.4000, 0.2000)
    elif typ == "Co":
        spheresize = 0.3000
        color = (0.9412, 0.5647, 0.6275)
    elif typ == "Ni":
        spheresize = 0.3037
        color = (0.3137, 0.8157, 0.3137)
    elif typ == "Cu":
        spheresize = 0.3072
        color = (0.7843, 0.5020, 0.2000)
    elif typ == "Zn":
        spheresize = 0.3107
        color = (0.4902, 0.5020, 0.6902)
    elif typ == "Ga":
        spheresize = 0.3141
        color = (0.7608, 0.5608, 0.5608)
    elif typ == "Ge":
        spheresize = 0.3175
        color = (0.4000, 0.5608, 0.5608)
    elif typ == "As":
        spheresize = 0.3208
        color = (0.7412, 0.5020, 0.8902)
    elif typ == "Se":
        spheresize = 0.3240
        color = (1.0000, 0.6314, 0.0000)
    elif typ == "Br":
        spheresize = 0.3271
        color = (0.6510, 0.1608, 0.1608)
    elif typ == "Kr":
        spheresize = 0.3302
        color = (0.3608, 0.7216, 0.8196)
    elif typ == "Rb":
        spheresize = 0.3332
        color = (0.4392, 0.1804, 0.6902)
    elif typ == "Sr":
        spheresize = 0.3362
        color = (0.0000, 1.0000, 0.0000)
    elif typ == "Y":
        spheresize = 0.3391
        color = (0.5804, 1.0000, 1.0000)
    elif typ == "Zr":
        spheresize = 0.3420
        color = (0.5804, 0.8784, 0.8784)
    elif typ == "Nb":
        spheresize = 0.3448
        color = (0.4510, 0.7608, 0.7882)
    elif typ == "Mo":
        spheresize = 0.3476
        color = (0.3294, 0.7098, 0.7098)
    elif typ == "Tc":
        spheresize = 0.3503
        color = (0.2314, 0.6196, 0.6196)
    elif typ == "Ru":
        spheresize = 0.3530
        color = (0.1412, 0.5608, 0.5608)
    elif typ == "Rh":
        spheresize = 0.3557
        color = (0.0392, 0.4902, 0.5490)
    elif typ == "Pd":
        spheresize = 0.3583
        color = (0.0000, 0.4118, 0.5216)
    elif typ == "Ag":
        spheresize = 0.3609
        color = (0.7529, 0.7529, 0.7529)
    elif typ == "Cd":
        spheresize = 0.3634
        color = (1.0000, 0.8510, 0.5608)
    elif typ == "In":
        spheresize = 0.3659
        color = (0.6510, 0.4588, 0.4510)
    elif typ == "Sn":
        spheresize = 0.3684
        color = (0.4000, 0.5020, 0.5020)
    elif typ == "Sb":
        spheresize = 0.3708
        color = (0.6196, 0.3882, 0.7098)
    elif typ == "Te":
        spheresize = 0.3733
        color = (0.8314, 0.4784, 0.0000)
    elif typ == "I":
        spheresize = 0.3756
        color = (0.5804, 0.0000, 0.5804)
    elif typ == "Xe":
        spheresize = 0.3780
        color = (0.2588, 0.6196, 0.6902)
    elif typ == "Cs":
        spheresize = 0.3803
        color = (0.3412, 0.0902, 0.5608)
    elif typ == "Ba":
        spheresize = 0.3826
        color = (0.0000, 0.7882, 0.0000)
    elif typ == "La":
        spheresize = 0.3849
        color = (0.4392, 0.8314, 1.0000)
    elif typ == "Ce":
        spheresize = 0.3871
        color = (1.0000, 1.0000, 0.7804)
    elif typ == "Pr":
        spheresize = 0.3893
        color = (0.8510, 1.0000, 0.7804)
    elif typ == "Nd":
        spheresize = 0.3915
        color = (0.7804, 1.0000, 0.7804)
    elif typ == "Pm":
        spheresize = 0.3936
        color = (0.6392, 1.0000, 0.7804)
    elif typ == "Sm":
        spheresize = 0.3958
        color = (0.5608, 1.0000, 0.7804)
    elif typ == "Eu":
        spheresize = 0.3979
        color = (0.3804, 1.0000, 0.7804)
    elif typ == "Gd":
        spheresize = 0.4000
        color = (0.2706, 1.0000, 0.7804)
    elif typ == "Tb":
        spheresize = 0.4021
        color = (0.1882, 1.0000, 0.7804)
    elif typ == "Dy":
        spheresize = 0.4041
        color = (0.1216, 1.0000, 0.7804)
    elif typ == "Ho":
        spheresize = 0.4062
        color = (0.0000, 1.0000, 0.6118)
    elif typ == "Er":
        spheresize = 0.4082
        color = (0.0000, 0.9020, 0.4588)
    elif typ == "Tm":
        spheresize = 0.4102
        color = (0.0000, 0.8314, 0.3216)
    elif typ == "Yb":
        spheresize = 0.4121
        color = (0.0000, 0.7490, 0.2196)
    elif typ == "Lu":
        spheresize = 0.4141
        color = (0.0000, 0.6706, 0.1412)
    elif typ == "Hf":
        spheresize = 0.4160
        color = (0.3020, 0.7608, 1.0000)
    elif typ == "Ta":
        spheresize = 0.4179
        color = (0.3020, 0.6510, 1.0000)
    elif typ == "W":
        spheresize = 0.4198
        color = (0.1294, 0.5804, 0.8392)
    elif typ == "Re":
        spheresize = 0.4217
        color = (0.1490, 0.4902, 0.6706)
    elif typ == "Os":
        spheresize = 0.4236
        color = (0.1490, 0.4000, 0.5882)
    elif typ == "Ir":
        spheresize = 0.4254
        color = (0.0902, 0.3294, 0.5294)
    elif typ == "Pt":
        spheresize = 0.4273
        color = (0.8157, 0.8157, 0.8784)
    elif typ == "Au":
        spheresize = 0.4291
        color = (1.0000, 0.8196, 0.1373)
    elif typ == "Hg":
        spheresize = 0.4309
        color = (0.7216, 0.7216, 0.8157)
    elif typ == "Tl":
        spheresize = 0.4327
        color = (0.6510, 0.3294, 0.3020)
    elif typ == "Pb":
        spheresize = 0.4344
        color = (0.3412, 0.3490, 0.3804)
    elif typ == "Bi":
        spheresize = 0.4362
        color = (0.6196, 0.3098, 0.7098)
    elif typ == "Po":
        spheresize = 0.4380
        color = (0.6706, 0.3608, 0.0000)
    elif typ == "At":
        spheresize = 0.4397
        color = (0.4588, 0.3098, 0.2706)
    elif typ == "Rn":
        spheresize = 0.4414
        color = (0.2588, 0.5098, 0.5882)
    elif typ == "Fr":
        spheresize = 0.4431
        color = (0.2588, 0.0000, 0.4000)
    elif typ == "Ra":
        spheresize = 0.4448
        color = (0.0000, 0.4902, 0.0000)
    elif typ == "Ac":
        spheresize = 0.4465
        color = (0.4392, 0.6706, 0.9804)
    elif typ == "Th":
        spheresize = 0.4481
        color = (0.0000, 0.7294, 1.0000)
    elif typ == "Pa":
        spheresize = 0.4498
        color = (0.0000, 0.6314, 1.0000)
    elif typ == "U":
        spheresize = 0.4514
        color = (0.0000, 0.5608, 1.0000)
    elif typ == "Np":
        spheresize = 0.4531
        color = (0.0000, 0.5020, 1.0000)
    elif typ == "Pu":
        spheresize = 0.4547
        color = (0.0000, 0.4196, 1.0000)
    elif typ == "Am":
        spheresize = 0.4563
        color = (0.3294, 0.3608, 0.9490)
    elif typ == "Cm":
        spheresize = 0.4579
        color = (0.4706, 0.3608, 0.8902)
    elif typ == "Bk":
        spheresize = 0.4595
        color = (0.5412, 0.3098, 0.8902)
    elif typ == "Cf":
        spheresize = 0.4610
        color = (0.6314, 0.2118, 0.8314)
    elif typ == "Es":
        spheresize = 0.4626
        color = (0.7020, 0.1216, 0.8314)
    elif typ == "Fm":
        spheresize = 0.4642
        color = (0.7020, 0.1216, 0.7294)
    elif typ == "Md":
        spheresize = 0.4657
        color = (0.7020, 0.0510, 0.6510)
    elif typ == "No":
        spheresize = 0.4672
        color = (0.7412, 0.0510, 0.5294)
    elif typ == "Lr":
        spheresize = 0.4688
        color = (0.7804, 0.0000, 0.4000)
    elif typ == "Rf":
        spheresize = 0.4703
        color = (0.8000, 0.0000, 0.3490)
    elif typ == "Db":
        spheresize = 0.4718
        color = (0.8196, 0.0000, 0.3098)
    elif typ == "Sg":
        spheresize = 0.4733
        color = (0.8510, 0.0000, 0.2706)
    elif typ == "Bh":
        spheresize = 0.4747
        color = (0.8784, 0.0000, 0.2196)
    elif typ == "Hs":
        spheresize = 0.4762
        color = (0.9020, 0.0000, 0.1804)
    elif typ == "Mt":
        spheresize = 0.4777
        color = (0.9216, 0.0000, 0.1490)
    else:
        spheresize = 0.5
        color = (0.0000, 0.0000, 0.0000)

    return (spheresize, color)
