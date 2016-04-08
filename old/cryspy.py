import numpy as np

class Dif:
    def __init__ (self, dif):
        assert isinstance(dif, np.matrix), \
            "Error: class Dif must be constructed via a " \
            "numpy-matrix."
        assert (dif.shape == (4, 1)), \
            "Error: class Dif must be constructed via" \
            " a 4x1-numpy-matrix."
        assert (dif[3, 0] == 0), \
            "Error: class Dif must be " \
            "constructed" \
            " via a 4x1-numpy-matrix with a 0 " \
            "in the last entry."
        self.dif = dif
                
    def transform(self, transformation):
        assert isinstance(transformation, Transformation), \
            "Error: Argument of Dif.transform must be " \
            "of type Transformation."
        return \
         Dif(np.linalg.inv(transformation.gP) * self.dif)

    def printe(self):
        print("Difference")
        print(self.dif)

class Pos:
    def __init__ (self, pos):
        assert isinstance(pos, np.matrix), \
            "Error: class Pos must be constructed via a " \
            "numpy-matrix."
        assert (pos.shape == (4, 1)), \
            "Error: class Pos must be constructed " \
            "via a 4x1-numpy-matrix."
        assert (pos[3, 0] == 1), \
            "Error: class Pos must be " \
            "constructed via a 4x1-numpy-matrix " \
            "with a 1 in the last entry."
        self.pos = pos

    def __sub__ (pos1, pos2):
        return Dif(pos1.pos - pos2.pos)

    def transform(self, transformation):
        assert isinstance(transformation, Transformation), \
            "Error: Argument of Dif.transform must be " \
            " of type Transformation."
        return \
         Pos(np.linalg.inv(transformation.gP) * self.pos)

    def apply_symmetry(self, symmetry):
        assert isinstance(symmetry, Symmetry), \
            "Argument of Pos.apply_symmetry() must be " \
            "of type Symmetry."
        return Pos(symmetry.symmetry * self.pos)

    def printe(self):
        print("Position")
        print(self.pos)

class Rec:
    def __init__(self, rec):
        assert isinstance(rec, np.matrix), \
            "Object of type Rec must be "\
            "created via a numpy-matrix."
        assert (rec.shape == (1, 4)), \
            "Object of type Rec must be "\
            "created via a 1x4-numpy-matrix."
        assert (rec[0, 3] == 0), \
            "Object of type Rec must be "\
            "created via a 1x4-numpy-matrix "\
            "of the form"\
            "               (* * * 0) ."
        self.rec = rec

    def length(self, metric):
        assert isinstance(metric, Metric), \
            "Argument of Rec.length() must be of " \
            "Type Metric."
        return np.sqrt(metric.recscalarproduct(self, self))

    def printe(self):
        print('Reciprocal Vector')
        print(self.rec)    


class Metric:
    def __init__ (self, M):
        assert isinstance(M, np.matrix), \
            "Error: Metric must be constructed via a " \
            "numpy-matrix."
        assert (M.shape == (4, 4)), \
            "Error: Metric must be constructed via " \
            " a 4x4-numpy-matrix."
        assert (  all(M[:, 3] == \
                   np.matrix([[0], [0], [0], [1]])) \
                   and all(M[3, :].transpose() == \
                   np.matrix([[0, 0, 0, 1]]).transpose()) ) , \
            "Error: Metric must be constructed " \
                  "via a 4x4-numpy-matrix of the form\n"\
                  "      * * * 0 \n" \
                  "      * * * 0 \n" \
                  "      * * * 0 \n" \
                  "      0 0 0 1 ."
        self.M = M

    def transform(self, transformation):
        assert isinstance(transformation, Transformation), \
            "Error: Argument of Metric.transform must " \
            "be of type Transformation."
        M = transformation.gP.transpose() \
          * self.M \
          * transformation.gP
        # Fixme: Das hier ist noch seeeehr unschoen!
        M[3, 0] = 0
        M[3, 1] = 0
        M[3, 2] = 0
        M[3, 3] = 1
        M[0, 3] = 0
        M[1, 3] = 0
        M[2, 3] = 0
        return Metric(M)
        
    def scalarproduct(self, dif1, dif2):
        assert isinstance(dif1, Dif) and isinstance(dif2, Dif), \
            "Error: Arguments of Metric.scalarproduct " \
            "must be of type Dif."
        return (  dif1.dif.transpose() \
                * self.M \
                * dif2.dif  )[0, 0]

    def recscalarproduct(self, rec1, rec2):
        assert isinstance(rec1, Rec) and \
               isinstance(rec2, Rec),\
               "Arguments of "\
               "Metric.recscalarproduct "\
               "must be of type Rec."
        return (  rec1.rec \
                * np.linalg.inv(self.M)\
                * rec2.rec.transpose())[0, 0]

    def distance(self, pos1, pos2):
        assert ( isinstance(pos1, Pos) \
         and isinstance(pos2, Pos) ), \
            "Arguments of Metric.distance() must be of type" \
            " Pos."
        return np.sqrt((  (pos1 - pos2).dif.transpose() \
                        * self.M \
                        * (pos1 - pos2).dif  )[0, 0] )

    def angle(self, pos1, pos2, pos3):
        assert isinstance(pos1, Pos) and isinstance(pos2, Pos) \
         and isinstance(pos3, Pos), \
            "Arguments of Metric.angle() must be of type Pos."
        return np.rad2deg( \
         np.arccos(self.scalarproduct(pos1-pos2, pos3-pos2) \
         / (self.distance(pos2, pos1) * self.distance(pos2, pos3))) \
         )


    def printe(self):
        print("Metric Tensor")
        print(self.M)
        print("Metric as Cell Parameters")
        print(metric2cellparameters(self))


class Transformation:
    def __init__(self, gP):
        assert isinstance(gP, np.matrix), \
            "Error: Transformation " \
            "must be constructed via a " \
            "numpy-matrix."
        assert (gP.shape == (4, 4)), \
            "Error: Transformation "\
            "must be constructed via " \
            " a 4x4-numpy-matrix."
        assert all(gP[3, :].transpose() == \
            np.matrix([[0, 0, 0, 1]]).transpose()), \
            "Error: Transformation " \
            "must be constructed " \
            "via a 4x4-numpy-matrix of the form\n"\
            "      * * * * \n" \
            "      * * * * \n" \
            "      * * * * \n" \
            "      0 0 0 1 ."
        self.gP = gP

    def printe(self):
        print("Transformation Matrix")
        print(self.gP)


class Atom:
    def __init__(self, atomtype, pos, occ):
        assert ( isinstance(atomtype, str)
         and isinstance(pos, Pos) 
         and isinstance(occ, float) ), \
            "Error: Atom must be constructed via " \
            "an atomtype of type string and a position " \
            "of type Pos and an Occupation of type float."
        self.atomtype = atomtype
        self.pos = pos
        self.occ = occ

    def transform(self, transformation):
        assert isinstance(transformation, Transformation), \
            "Argument of Atom.transform() must be of " \
            "Type Transformation."
        return Atom(self.atomtype, \
         self.pos.transform(transformation), \
         self.occ)

    def apply_symmetry(self, symmetry):
        assert isinstance(symmetry, Symmetry), \
            "Argument of Atom.apply_symmetry() must " \
            "be of type Symmetry."
        return Atom(self.atomtype, \
         self.pos.apply_symmetry(symmetry), \
         self.occ)

    def printe(self):
        print("Atom")
        print(self.atomtype)
        self.pos.printe()


class AsymmetricUnit:
    def __init__(self, metric):
        assert isinstance(metric, Metric), \
            "Error: AsymmetricUnit must be created " \
            "via a metric of type Metric."
        self.metric = metric
        self.names = []
        self.atoms = []

    def add_atom(self, name, atom):
        assert ( isinstance(name, str) \
        and isinstance(atom, Atom) ), \
            "Error: atom must be added to AsymmetricUnit "\
            "via a name of type string and " \
            "an atom of type Atom."
        self.atoms.append(atom)
        self.names.append(name)

    def del_atom(self, name):
        assert isinstance(name, str), \
            "Error: To delete an atom from " \
            "AsymmetricUnit, you must give its name " \
            "of type string."
        assert name in names, \
            "Error: The atom that you want to " \
            "delete, does not exsist."
        i = names.index(name)
        del(self.atoms[i])
        del(self.names[i])

    def transform(self, transformation):
        assert isinstance(transformation, Transformation), \
            "Error: Argument of AsymmetricUnit.transform " \
            "must be of type Transformation."
        asymmetricunit = AsymmetricUnit( \
         self.metric.transform(transformation))
        for i in range(len(self.atoms)):
            asymmetricunit.add_atom(self.names[i], \
             self.atoms[i].transform(transformation))
        return asymmetricunit

    def apply_symmetry(self, symmetry):
        assert isinstance(symmetry, Symmetry), \
            "Argument of AsymmetricUnit.apply_symmetry() " \
            "must be of type Symmetry."
        asymmetricunit = AsymmetricUnit(self.metric)
        for i in range(len(self.atoms)):
            asymmetricunit.add_atom(self.names[i], \
             self.atoms[i].apply_symmetry(symmetry))
        return asymmetricunit

    def printe(self):
        print("Asymmetric Unit")
        cellpar = metric2cellparameters(self.metric)
        print("  ___________________________________")
        print(" |                                   |")
        print(" |  a =%8.4f     alpha =%8.3f  |" % (cellpar[0], cellpar[3]))
        print(" |  b =%8.4f     beta  =%8.3f  |" % (cellpar[1], cellpar[4]))
        print(" |  c =%8.4f     gamma =%8.3f  |" % (cellpar[2], cellpar[5]))
        print(" |___________________________________|")
        print(" ______________________________________________________")
        print("|                                                      |")
        print("|   Name   |    Type  |    x     |    y     |     z    |")
        print("|------------------------------------------------------|")
        for i in range(len(self.atoms)):
            print("|%9s |%9s |%9.4f |%9.4f |%9.4f |" % \
                 (self.names[i], \
                  self.atoms[i].atomtype, \
                  self.atoms[i].pos.pos[0, 0], \
                  self.atoms[i].pos.pos[1, 0], \
                  self.atoms[i].pos.pos[2, 0]))
        print("|______________________________________________________|")
        print("")


class Symmetry:
    def __init__(self, symmetry):
        assert isinstance(symmetry, np.matrix), \
            "Error: Symmetry must be created via " \
            " a numpy-matrix"
        assert (symmetry.shape == (4, 4)), \
            "Error: Symmetry must be created via " \
            " a 4x4-numpy-matrix."
        assert all(symmetry[3, :].transpose() \
         == np.matrix([0, 0, 0, 1]).transpose()), \
            "Error: Symmetry must be created " \
            "via a 4x4-numpy-matrix of the " \
            " form: \n" \
            "     * * * * \n" \
            "     * * * * \n" \
            "     * * * * \n" \
            "     0 0 0 1    ."
        self.symmetry = symmetry

    def transform(self, transformation): 
        assert isinstance(transformation, Transformation), \
            "Error: Argument of Symmetry.transform" \
            " needs to be a transformation of type " \
            " Transformation."
        return Symmetry( \
                   transformation.gP \
                   * self.symmetry \
                   * np.linalg.inv(transformation.gP)
               )

    def __mul__(self, other):
        assert isinstance(self, Symmetry),\
            "Error: The first element of a multiplication of two"\
            " symmetry elements must be of type Symmetry (as the second"\
            " one as well, of course)."
        assert isinstance(other, Symmetry),\
            "Error: The second element of a multiplication of two"\
            " symmetry elements must be of type Symmetry (as the first"\
            " one as well, of course)."
        return Symmetry(self.symmetry * other.symmetry)

    def printe(self):
        print("Symmetry")
        print(self.symmetry)


class Group:
    def __init__(self):
        self.names = []
        self.symmetries = []

    def add_symmetry(self, name, symmetry):
        assert isinstance(name, str), \
            "1. Argument of Group.add_symmetry " \
            "must be of type string."
        assert isinstance(symmetry, Symmetry), \
            "2. Argument of Group.add_symmetry " \
            " must be a symmetry of type Symmetry."
        self.names.append(name)
        self.symmetries.append(symmetry)

    def transform(self, transformation):
        assert isinstance(transformation, Transformation), \
            "Error: argument of Group.transform must " \
            " be a transformation of type Transformation."
        group = Group()
        for i in range(len(self.symmetries)):
            group.add_symmetry( \
             self.names[i], \
             self.symmetries[i].transform(transformation))
        return group


    def printe(self):
        print("Symmetry-Group")
        for i in range(len(self.symmetries)):
            print(self.names[i])
            self.symmetries[i].printe()

class Translationgenerators:
    def __init__(self, gen1, gen2, gen3):
        assert isinstance(gen1, Dif), \
            "1. argument of Translationgenerators.__init__() must be "\
            "of type Dif."
        assert isinstance(gen2, Dif), \
            "2. argument of Translationgenerators.__init__() must be "\
            "of type Dif."
        assert isinstance(gen3, Dif), \
            "3. argument of Translationgenerators.__init__() must be "\
            "of type Dif."
        self.gen1 = gen1
        self.gen2 = gen2
        self.gen3 = gen3

    def printe(self):
        print("Translationgenerators:")
        self.gen1.printe()
        self.gen2.printe()
        self.gen3.printe()

class Spacegroup:
    def __init__(self, group, transgen):
        assert isinstance(group, Group),\
            "1. argument of Spacegroup.__init__() must be of type Group."
        assert isinstance(transgen, Translationgenerators),\
            "2. argument of Spacegroup.__init__() must be of type "\
            "Translationgenerators."
        self.transgen = transgen
        self.group = Group()
        for i in range(len(group.names)):
            symmetry = group.symmetries[i]
            symmetry = self.representative(symmetry)
            self.group.add_symmetry(group.names[i], symmetry)

    def representative(self, symmetry):
        assert isinstance(symmetry, Symmetry),\
            "Argument of Spacegroup.representative() must be of type "\
            "Symmetry."
        gen1 = self.transgen.gen1.dif
        gen2 = self.transgen.gen2.dif
        gen3 = self.transgen.gen3.dif
        gP = np.matrix([[gen1[0, 0], gen2[0, 0], gen3[0, 0], 0],\
                        [gen1[1, 0], gen2[1, 0], gen3[1, 0], 0],\
                        [gen1[2, 0], gen2[2, 0], gen3[2, 0], 0],\
                        [0      , 0      , 0      , 1]])
        transformation = Transformation(np.linalg.inv(gP))
        back_transformation = Transformation(gP)
        symmetry_trans = symmetry.transform(transformation)
        M = symmetry_trans.symmetry
        M[0, 3] = np.mod(M[0, 3], 1)
        M[1, 3] = np.mod(M[1, 3], 1)
        M[2, 3] = np.mod(M[2, 3], 1)
        symmetry_trans = Symmetry(M)
        symmetry = symmetry_trans.transform(back_transformation)
        return symmetry

    def symmetryname(self, symmetry):
        symmetry = self.representative(symmetry)
        name = "Error: This Symmetry does not exsist!"
        for i in range(len(self.group.names)):
            if np.allclose(self.group.symmetries[i].symmetry, symmetry.symmetry):
                name = self.group.names[i]
        return name


    def printe(self):
        print("Spacegroup:")
        self.group.printe()
        self.transgen.printe()
    
class SymmetricUnit:
    def __init__(self, asymmetricunit, group):
        assert isinstance(asymmetricunit, AsymmetricUnit), \
            "1. argument of SymmetricUnit.__init__() must be of " \
            "type AsymmetricUnit."
        assert isinstance(group, Group), \
            "2. argument of SymmetricUnit.__init__() must be of "\
            "type Group."
        self.symmetry_names = group.names
        self.atom_names = asymmetricunit.names
        self.atoms = []
        for j in range(len(group.symmetries)):
            self.atoms.append([])
            for i in range(len(asymmetricunit.atoms)):
                self.atoms[j].append(
                 asymmetricunit.atoms[i].apply_symmetry(group.symmetries[j]))

    def printe(self):
        print("Symmetric Unit")
        s = '                      ||'
        for j in range(len(self.atoms)):
            s += '%9s |'%(self.symmetry_names[j])
        s += '\n|=====================||'
        for j in range(len(self.atoms)):
            s += '==========='
        s = s[:-1]
        s += '|\n'
        for i in range(len(self.atom_names)):
            s += '|%9s |%9s ||'%\
             (self.atom_names[i], self.atoms[0][i].atomtype)
            for j in range(len(self.atoms)):
                s += '%9.4f |'%(self.atoms[j][i].pos.pos[0, 0])
            s += '\n|          |          ||'
            for j in range(len(self.atoms)):
                s += '%9.4f |'%(self.atoms[j][i].pos.pos[1, 0])
            s += '\n|          |          ||'
            for j in range(len(self.atoms)):
                s += '%9.4f |'%(self.atoms[j][i].pos.pos[2, 0])

            if (i < len(self.atom_names) - 1) :
                s += '\n|---------------------||'
    
                for j in range(len(self.atoms)):
                    
                    s += '-----------'
                s = s[:-1]
                s += '|\n'
            else:
                s += '\n|__________|__________||'
    
                for j in range(len(self.atoms)):
                    
                    s += '___________'
                s = s[:-1]
                s += '|\n'


        print(s)
        print("")

class Cell:
    def __init__(self, asymmetricunit, group):
        assert isinstance(asymmetricunit, AsymmetricUnit), \
            "1. argument of Cell.__init__ must be of type " \
            "AsymmetricUnit."
        assert isinstance(group, Group), \
            "2. arugment of Cell.__init__ must be of type Group. "
        self.asymmetricunit = asymmetricunit
        self.group = group
        self.explicit = []

    def transform(self, transformation):
        assert isinstance(transformation, Transformation), \
            "Error: transformation must be of type " \
            " Transformation."
        asymmetricunit = self.asymmetricunit.transform(transformation)
        group = self.group.transform(transformation)
        return Cell(asymmetricunit, group)

    def printe(self):
        print("Cell")
        self.group.printe()
        self.asymmetricunit.printe()


def cellparameters2metric(a, b, c, alpha, beta, gamma):
    aa = a**2
    bb = b**2
    cc = c**2
    ab = a * b * np.cos(np.deg2rad(gamma))
    ac = a * c * np.cos(np.deg2rad(beta))
    bc = b * c * np.cos(np.deg2rad(alpha))
    return Metric(np.matrix([[aa, ab, ac, 0], [ab, bb, bc, 0], [ac, bc, cc, 0], [0, 0, 0, 1]]))

def metric2cellparameters(metric):
    assert isinstance(metric, Metric), \
        "Error: metric2cellparameters needs a metric of " \
        "type Metric."
    pos0 = Pos(np.matrix([[0], [0], [0], [1]]))
    pos1 = Pos(np.matrix([[1], [0], [0], [1]]))
    pos2 = Pos(np.matrix([[0], [1], [0], [1]]))
    pos3 = Pos(np.matrix([[0], [0], [1], [1]]))
    a = metric.distance(pos1, pos0)
    b = metric.distance(pos2, pos0)
    c = metric.distance(pos3, pos0)
    alpha = metric.angle(pos2, pos0, pos3)
    beta = metric.angle(pos3, pos0, pos1)
    gamma = metric.angle(pos1, pos0, pos2)
    return [a, b, c, alpha, beta, gamma]

def xyz2symmetry(xyz):
   words = xyz.replace(" ", "").replace("-", "+-").split(",")
   def term2line(term):
       summanden = term.split("+")
       [a, b, c, d] = [0, 0, 0, 0]
       for summand in summanden:
           [a1, b1, c1, d1] = parse_summand(summand)
           a += a1
           b += b1
           c += c1
           d += d1
       return [a, b, c, d]
   def parse_summand(summand):
       sign = +1
       if len(summand) == 0:
           return [0, 0, 0, 0]
       if summand[0] == '-':
           sign = -1
           summand = summand[1:]
       if summand.isdigit():
           a = 0
           b = 0
           c = 0
           d = int(summand)
       elif len(summand) == 1:
           if summand == "x":
               a = 1
               b = 0
               c = 0
               d = 0
           elif summand == "y":
               a = 0
               b = 1
               c = 0
               d = 0
           elif summand == "z":
               a = 0
               b = 0
               c = 1
               d = 0
       else:
           words = summand.split("/")
           if len(words) > 2:
               print("Ein Bruch kann nur zwei Zahlen enthalten!")
           elif len(words) < 2:
               print("%s ist keine Zahl, kein x, y, z und kein Bruch."\
                     "Was ist es dann?"%(summand))
           elif len(words) == 2:
               a = 0
               b = 0
               c = 0
               d = float(words[0]) / float(words[1])
       return [sign*a, sign*b, sign*c, sign*d]
   symmetry = Symmetry(np.matrix([term2line(words[0]),\
                                  term2line(words[1]),\
                                  term2line(words[2]),\
                                  [0, 0, 0, 1]]))
   return symmetry
   
