import quicktions as fr
import uncertainties as uc

class Frac(fr.Fraction):
#    def __init__(self, enumerator, denominator):
#        fr.Fraction.__init__(enumerator, denominator)

    def __add__(self, right):
        if isinstance(right, Erno):
            return Erno(float(self) + right)
        else:
            return Frac(fr.Fraction.__add__(self, right))    

class Erno(uc.core.Variable):
#    def __init__(self, nominal, error):
#        uc.core.Variable.__init__(self, nominal, error)

    def __add__(self, right):
        if isinstance(right, Frac):
            return 0
