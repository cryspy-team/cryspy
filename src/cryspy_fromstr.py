import cryspy_numbers as nb
import quicktions as fr
import uncertainties as uc
import cryspy_geo as geo

def fromstr(string):
    """
        >>> print(fromstr("1/2"))
        1/2
        >>> print(fromstr("1.2+/-0.1"))
        1.20(10)
        >>> print(fromstr("1.2(1)"))
        1.20(10)
        >>> print(fromstr("4"))
        4
        >>> print(fromstr("/ 1 2 \ \\n \ 3 4 /"))
         /  1  2  \ 
         \  3  4  / 

    """
    assert isinstance(string, str), \
        "Function fromstr must have an argument of type string."
    typ = typefromstr(string)
    if typ == nb.Mixed:
        try:
            result = mixedfromstr(string)
            assert (result != None), \
                "The following string looks like a number, but I "\
                "cannot convert it: %s"%(string)
            return result
        except:
            pass
    elif typ == nb.Matrix:
        try:
            return matrixfromstr(string)
        except ValueError:
            raise(Exception("The following string looks like a Matrix, "\
                            "but I cannot convert it: %s"%(string)))
    elif typ == geo.Symmetry:
        try:
            return symmetryfromstr(string)
        except ValueError:
            raise(Exception("The following string looks like a Symmetry, "\
                            "but I cannot convert it: %s"%(string)))
    elif typ == geo.Transformation:
        try:
            return transformationfromstr(string)
        except ValueError:
            raise(Exception("The following string looks like a "\
                            "Transformation, but I cannot convert it: %s"\
                            %(string)))
    elif typ == geo.Coset:
        try:
            return cosetfromstr(string)
        except ValueError:
            raise(Exception("The following string looks like a Coset "\
                            "but I cannot convert it: %s"%(string)))

def typefromstr(string):
    words = string.split()

    if (words[0][0] == '/') and words[-1][-1] == '/':
        return nb.Matrix
    elif (words[0][0] == '<') and (words[-1][-1] == '>'):
        return nb.Matrix
    elif ('\n' in string) or ('\\' in string):
        return nb.Matrix
    elif ('{' in string) and ('}' in string):
        return geo.Coset
    elif ('x' in string) or ('y' in string) or ('z' in string):
        return geo.Symmetry
    elif ('a' in string) or ('b' in string) or ('c' in string):
        return geo.Transformation
    else:
        return nb.Mixed

def mixedfromstr(string):
    try:
        return nb.Mixed(fr.Fraction(string))
    except ValueError:
        try:
            return nb.Mixed(uc.ufloat_fromstr(string))
        except ValueError:
            raise(Exception("The following string looks like a number, "\
                            "but I can't convert it: %s"%(string)))


def matrixfromstr(string):
     string = string.replace('|', '\\')
     string = string.replace('/ ', ' ')
     string = string.replace('<', ' ')
     string = string.replace('>', ' ')
     string = string.replace(' /', ' ')
     string = string.replace('\n', '\\')
     for i in range(4):
        string = string.replace('\\ \\', '\\')
        string = string.replace('\\  \\', '\\')
        string = string.replace('\\   \\', '\\')
     rowwords = string.split('\\')
     rowliste = []
     for rowword in rowwords:
         words = rowword.split()
         liste = []
         for word in words:
             liste.append(mixedfromstr(word))
         rowliste.append(nb.Row(liste))
     return nb.Matrix(rowliste)


def symmetryfromstr(string):
    words = string.split(',')
    assert len(words) == 3, \
        "The following string looks like a Symmetry, but it has not "\
        "three comma-separated terms: %s"%(string)
    liste = []
    for word in words:
        row = nb.Row(geo.str2linearterm(word, ['x', 'y', 'z']))
        liste.append(row)
    liste.append(nb.Row([fromstr("0"), fromstr("0"), fromstr("0"), \
        fromstr("1")]))
    return geo.Symmetry(nb.Matrix(liste))


def transformationfromstr(string):
    words = string.split(',')
    assert len(words) == 3, \
        "The following string looks like a Symmetry, but it has not "\
        "three comma-seperated terms: %s"%(string)
    liste = []
    for word in words:
        row = nb.Row(geo.str2linearterm(word, ['a', 'b', 'c']))
        liste.append(row)
    liste.append(nb.Row([fromstr("0"), fromstr("0"), fromstr("0"), \
        fromstr("1")]))
    return geo.Transformation(nb.Matrix(liste))


def cosetfromstr(string):
    if '\n' in string:
        lines = string.split('\n')
        
