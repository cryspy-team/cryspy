from fromstr import fromstr as fs
import geo as geo

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


