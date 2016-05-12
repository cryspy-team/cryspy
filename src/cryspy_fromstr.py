import cryspy_numbers as nb
import quicktions as fr
import uncertainties as uc

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
            return mixedfromstr(string)
        except:
            pass
    elif typ == nb.Matrix:
        try:
            return matrixfromstr(string)
        except ValueError:
            raise(Exception("The following string looks like a Matrix, but "\
                            "I can't convert it: %s"%(string)))

def typefromstr(string):
    """
        >>> string = "/ 1 2 \ \\n\ 3 4 /"
        >>> print(string)
        / 1 2 \ 
        \ 3 4 /
        >>> typefromstr(string)
        <class 'cryspy_numbers.Matrix'>
        >>> string = "< 1 2 3>"
        >>> print(string)
        < 1 2 3>
        >>> typefromstr(string)
        <class 'cryspy_numbers.Matrix'>
        >>> string = '1/2'
        >>> typefromstr(string)
        <class 'cryspy_numbers.Mixed'>
        >>> string = '1.2+/-0.1'
        >>> typefromstr(string)
        <class 'cryspy_numbers.Mixed'>
        >>> string = '1.2(1)'
        >>> typefromstr(string)
        <class 'cryspy_numbers.Mixed'>
        >>> string = '4'
        >>> typefromstr(string)
        <class 'cryspy_numbers.Mixed'>
    """
    words = string.split()

    if (words[0][0] == '/') and words[-1][-1] == '/':
        return nb.Matrix
    elif (words[0][0] == '<') and (words[-1][-1] == '>'):
        return nb.Matrix
    elif ('\n' in string) or ('\\' in string):
        return nb.Matrix
    else:
        return nb.Mixed

def mixedfromstr(string):
    try:
        return nb.Mixed(fr.Fraction(string))
    except ValueError:
        try:
            return nb.Mixed(uc.ufloat_fromstr(string))
        except ValueError:
            raise(Exception("The following string looks like a number, but "\
                            "I can't convert it: %s"%(string)))

def matrixfromstr(string):
     string = string.replace('|', '\\')
     string = string.replace('/ ', ' ')
     string = string.replace('<', ' ')
     string = string.replace('>', ' ')
     string = string.replace(' /', ' ')
     string = string.replace('\\n', '\\')
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
