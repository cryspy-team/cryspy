import cryspy_numbers as nb
import cryspy_geo as geo
import blockprint as bp

class Atom():
    def __init__(self, name, typ, pos):
        assert isinstance(name, str), \
            "First argument must be of type str."
        assert isinstance(typ, str), \
            "Second argument must be of type str."
        assert isinstance(pos, geo.Pos), \
            "Third argument must be of type Pos."
    return 0

