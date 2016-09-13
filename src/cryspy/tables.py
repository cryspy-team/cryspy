from cryspy.fromstr import fromstr as fs
from cryspy import geo as geo

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
