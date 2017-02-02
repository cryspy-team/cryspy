# cryspy
Python3-module for crystallographic calculations.

# Authors


# Links

# Contribute

Setup Zim

* Open Zim
* File -> open another Notebook -> Add -> select path to this Zim-Notebook.


# Dependencies
Following commands should work with Linux Mint and Python 3

```sh
$ sudo aptitude install python3-dev
$ sudo aptitude install python3-pip
$ sudo pip3 install -U setuptools   
$ sudo pip3 install quicktions       # >= quicktions-1.2
$ sudo pip3 install uncertainties    # >= uncertainties-2.4.8.1
$ sudo pip3 install numpy            # >= numpy-1.11.0
```

# Usage

```py
import cryspy
from cryspy.fromstr import fromstr as fs

a = fs("1.5+/-0.2")

print(a)
>> 1.50(20)

A1 = cryspy.crystal.Atom("O1", "O", fs("p 0 0 1"))

print(A1)
>> Atom O1 O Pos /  0  \ 
>>              |   0   |
>>               \  1  / 


t = fs("O -> (1, 2, 3)\nthen\na' = a+b\nb' = a-b\nc' = c+a")

A1 = cryspy.crystal.Atom("O1", "O", fs("p 1/2 1/2 1/2"))

A2=t ** A1

print(A2)
>> Atom O1 O Pos /   1/4  \ 
>>              |    7/4   |
>>               \  -5/2  / 


# prepare spacegroup
sg = cryspy.tables.spacegroup(13)
print(sg)


```
