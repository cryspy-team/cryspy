import numpy as np


floatlist = []
hashlist = []

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

