The module cryspy.fromstr
=========================

Most objects of cryspy can be constructed from a string by the function *cryspy.fromstr.fromstr*. cryspy tries to use the convention, that (as far as possible) every object can be constructed via *fromstr* with the same string, which is return by *print()*. Here is an example for a matrix:

>>> from cryspy.fromstr import fromstr as fs
>>> M = fs(" / 1 2 3 \  \n" \
...        "|  4 5 6  | \n" \
           " \ 7 8 9 /  ")
>>> type(M)
cryspy.numbers.Matrix
>>>

