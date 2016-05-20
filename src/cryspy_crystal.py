import cryspy_numbers as nb
import cryspy_geo as geo
import cryspy_blockprint as bp

class Atom():
    def __init__(self, name, typ, pos):
        assert isinstance(name, str), \
            "First argument must be of type str."
        assert isinstance(typ, 

