import numpy as np


floatlist = []
hashlist = []

ufloatlist = []
ufloathashlist = []

delta = 1e-5

def floathash(number):
    global floatlist
    global hashlist
    for i in range(len(floatlist)):
        if np.abs(number - floatlist[i]) < delta:
            return hashlist[i]
    h = hash(number)
    if len(floatlist) == 0:
        floatlist = [number]
        hashlist = [h]
    elif floatlist[0] > number:
        floatlist = [number] + floatlist
        hashlist = [h] + hashlist
    elif floatlist[-1] < number:
        floatlist = floatlist + [number]
        hashlist = hashlist + [h]
    else:
        for i in range(len(floatlist) - 1):
            if floatlist[i] < number < floatlist[i+1]:
                floatlist = floatlist[0:i+1] + [number] + floatlist[i+1:]
                hashlist = hashlist[0:i+1] + [h] + hashlist[i+1:] 
    return h

def ufloathash(number):
    global ufloatlist
    global ufloathashlist
    for i in range(len(ufloatlist)):
        if ufloatlist[i] == number:
            return ufloathashlist[i]
    h = len(ufloatlist)
    ufloatlist.append(number)
    ufloathashlist.append(h)
    """for i in range(len(ufloatlist)):
        if np.abs(number - ufloatlist[i]) < delta:
            return ufloathashlist[i]
    h = hash(number)
    if len(ufloatlist) == 0:
        ufloatlist = [number]
        ufloathashlist = [h]
    elif ufloatlist[0] > number:
        ufloatlist = [number] + ufloatlist
        ufloathashlist = [h] + ufloathashlist
    elif ufloatlist[-1] < number:
        ufloatlist = ufloatlist + [number]
        ufloathashlist = ufloathashlist + [h]
    else:
        for i in range(len(ufloatlist) - 1):
            if ufloatlist[i] < number < ufloatlist[i+1]:
                ufloatlist = ufloatlist[0:i+1] + [number] + ufloatlist[i+1:]
                ufloathashlist = ufloathashlist[0:i+1] + [h] + ufloathashlist[i+1:] 
    """
    return h

