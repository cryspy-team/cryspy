import cryspy_numbers as nb
import blockprint as bp

class Pos:
    def __init__(self, value):
        assert isinstance(value, nb.Matrix), \
            "Must be created by an object of type Matrix."
        assert (value.shape() == (4, 1)), \
            "Must be createy by a 4x1-Matrix."
        assert (value.liste[3].liste[0] == 1), \
            "Must be created by a 4x1-Matrix with a 1 as last entry."
        self.value = value

    def __str__(self):
        return bp.block([["Pos", self.value.block(0, 3, 0, 1).__str__()],])

