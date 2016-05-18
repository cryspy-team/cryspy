def height_of_block(string):
    assert isinstance(string, str), \
        "Argument must be of type str."
    return string.count('\n') + 1

def width_of_block(string):
    assert isinstance(string, str), \
        "Argument must be of type str."
    rows = string.split('\n')
    return max([len(row) for row in rows])

def shape(liste):
    numrows = len(liste)
    numitems = []
    for row in liste:
        numitems.append(len(row))
    numcols = max(numitems)
    return (numrows, numcols)

def maxsizes(liste):
    (numrows, numcols) = shape(liste)
    maxheights = []
    maxwidths = []
    for row in liste:
        maxheights.append(max([height_of_block(item) for item in row]))
    for i in range(numcols):
        maxwidth = 0
        for row in liste:
            if len(row) > i:
                maxwidth = max([width_of_block(row[i]), maxwidth])
        maxwidths.append(maxwidth)
    return (maxheights, maxwidths)

def block(liste):
    assert isinstance(liste, list), \
        "Argument must be of type list."
    for row in liste:
        assert isinstance(row, list), \
            "Argument must be a list of lists."
    for row in liste:
        for item in row:
            assert isinstance(item, str), \
                "Argument must be a list of lists of objects of type str."
    (numrows, numcols) = shape(liste)
    (maxheights, maxwidths) = maxsizes(liste)
    string = ''
    for i in range(numrows):
        for line in range(maxheights[i]):
            for j in range(len(liste[i])):
                if height_of_block(liste[i][j]) > line:
                    stringpart = liste[i][j].split('\n')[line]
                else:
                    stringpart = ''
                code = '%'
                code += "%i"%(maxwidths[j])
                code += 's'
                string += code%stringpart
            string += '\n'
    return string
