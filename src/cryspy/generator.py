#!/usr/bin/env python3

import cryspy
from cryspy.fromstr import fromstr as fs
from cryspy import geo as geo
import numpy as np



with open("cryspy/sg/63.py") as f:
    code = compile(f.read(), "cryspy/sg/63.py", 'exec')
    exec(code)

fsarray = []

for k in WP.split():
    print("WP: ", k)
    fsarray.append(fs('{' + k + '}'))


sg = geo.Spacegroup(geo.canonical, fsarray)


