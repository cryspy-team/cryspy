import pytest
import sys
sys.path.append("../src/")
import cryspy_geo as geo
import cryspy_fromstr as fs

def test_Pos():
    v = fs.fromstr('/ 1 \n 2 \n 3 \n 1 /')
    x = geo.Pos(v)
    assert x.__str__() == "Pos /  1  \ \n   |   2   |\n    \  3  / "
    assert x.x() == 1
    assert x.y() == 2
    assert x.z() == 3

def test_Dif():
    v = fs.fromstr('/ 1 \n 2 \n 3 \n 0 /')
    x = geo.Dif(v)
    assert x.__str__() == "Dif /  1  \ \n   |   2   |\n    \  3  / "

def test_eq():
    r1 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 3 \n 1 /'))
    r2 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 3 \n 1 /'))
    r3 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 4 \n 1 /'))
    d1 = geo.Dif(fs.fromstr('/ 4 \n 5 \n 6 \n 0 /'))
    d2 = geo.Dif(fs.fromstr('/ 4 \n 5 \n 6 \n 0 /'))
    d3 = geo.Dif(fs.fromstr('/ 3 \n 5 \n 6 \n 0 /'))
    assert not (r1 == d1)
    assert     (r1 == r1) 
    assert     (r1 == r2)
    assert not (r1 == r3)
    assert     (d1 == d1)
    assert     (d1 == d2)
    assert not (d1 == d3)


def test_add_and_sub():
    x1 = geo.Pos(fs.fromstr('/ 1 \n 2 \n 3 \n 1 /'))
    x2 = geo.Pos(fs.fromstr('/ 2 \n 3 \n 4 \n 1 /'))
    d1 = geo.Dif(fs.fromstr('/ 4 \n 5 \n 6 \n 0 /'))
    d2 = geo.Dif(fs.fromstr('/ 5 \n 5 \n 5 \n 0 /'))
    assert (x1 + d1) == geo.Pos(fs.fromstr('/ 5 \n 7 \n 9 \n 1 /'))
    assert (d1 + d2) == geo.Dif(fs.fromstr('/ 9 \n 10 \n 11 \n 0 /'))
    assert (d1 - d2) == geo.Dif(fs.fromstr('/ -1 \n 0 \n 1 \n 0 /'))
    assert (x1 - d1) == geo.Pos(fs.fromstr('/ -3 \n -3 \n -3 \n 1 /'))
    assert (x1 - x2) == geo.Dif(fs.fromstr('/ -1 \n -1 \n -1 \n 0 /'))

def test_Operator():
    id = geo.Operator(fs.fromstr("/ 1 0 0 0 \n"\
                                 "  0 1 0 0 \n"\
                                 "  0 0 1 0 \n "\
                                 "  0 0 0 1 /"))
    g = geo.Operator(fs.fromstr("/ -1  0 0 0 \n"\
                                "   0 -1 0 0 \n"\
                                "   0  0 1 0 \n "\
                                "   0  0 0 1 /"))
    g1 = geo.Operator(fs.fromstr("/ -1  0 0 0 \n"\
                                 "   0 -1 0 0 \n"\
                                 "   0  0 1 0 \n "\
                                 "   0  0 0 1 /"))
    assert g.__str__() == "Operator /  -1   0  0  0  \ \n"\
                          "        |    0  -1  0  0   |\n"\
                          "        |    0   0  1  0   |\n"\
                          "         \   0   0  0  1  / "
    assert g == g1

def test_apply_Operator():
    g = geo.Operator(fs.fromstr("/ -1  0 1 0 \n"\
                                "   0 -1 0 0 \n"\
                                "   0  0 1 0 \n"\
                                "   0  0 0 1 /"))
    h = geo.Operator(fs.fromstr("/ 1 0 0 0 \n"\
                                "  0 1 0 0 \n"\
                                "  0 0 2 0 \n"\
                                "  0 0 0 1 /"))
    r = geo.Pos(fs.fromstr("/ 1 \n 2 \n 3 \n 1 /"))
    d = geo.Dif(fs.fromstr("/ 2 \n 4 \n 6 \n 0 /"))
    assert g ** r == geo.Pos(fs.fromstr("/ 2 \n -2 \n 3 \n 1 /"))
    assert h ** g == geo.Operator(fs.fromstr("/ -1  0 1/2 0 \n"\
                                             "   0 -1   0 0 \n"\
                                             "   0  0   1 0 \n"\
                                             "   0  0   0 1 /"))
    assert g ** d == geo.Dif(fs.fromstr("/ 4 \n -4 \n 6 \n 0 /"))

def test_str2linearterm():
    string = "a + b + 1/2 + 2a -1/3c"
    assert geo.str2linearterm(string, ["a", "b", "c"]) == \
        [fs.fromstr('3'), fs.fromstr('1'), fs.fromstr('-1/3'), \
         fs.fromstr('1/2')]


def test_Symmetry():
    M = fs.fromstr("/ 1 0 2 -1 \n 0 -2 0 0 \n 0 0 1 1/3 \n 0 0 0 1 /")
    g = geo.Symmetry(M)
    assert g.__str__() == "x+2z-1,-2y,z+1/3"

    transformation = geo.Transformation(fs.fromstr( \
        " 1 0 0 0 \n 0 1 0 0 \n 0 0 1 0 \n 0 0 0 1"))
    assert isinstance(transformation ** g, geo.Symmetry)

    transformation = geo.Transformation(fs.fromstr( \
        " 1/2 0 0 0 \n 0 1 0 0 \n 0 0 1 0 \n 0 0 0 1"))
    g1 = transformation ** g
    g2 = geo.Symmetry(fs.fromstr("1  0 1 -1/2 \n" \
                                 "0 -2 0  0   \n" \
                                 "0  0 1 1/3  \n" \
                                 "0  0 0  1"))
    assert g1.__str__() == g2.__str__()



def test_Transformation():
    M = fs.fromstr("/ 1/2 0 -1/2 1/4 \n 0 1 0 -1/2 \n 1/2 0 1/2 0 \n 0 0 0 1 /")
    t = geo.Transformation(M)
    assert t.__str__() == "Transformation a' = a-c-1/4\n"\
                          "               b' =   b+1/2\n"\
                          "               c' = a+c+1/4"
    t = geo.Transformation(fs.fromstr(" 1/2 0 0 0 \n" \
                                      " 0 1 0 0 \n" \
                                      " 0 0 1 0 \n" \
                                      " 0 0 0 1"))
    assert t.__str__() == "Transformation a' = 2a\n" \
                          "               b' =  b\n" \
                          "               c' =  c"
    p = fs.fromstr("p 1 0 0")
    assert (t ** p).__str__() == fs.fromstr("p 1/2 0 0").__str__()


    t = fs.fromstr("c, a, b")
    assert t.__str__() == "Transformation a' = c\n" \
                          "               b' = a\n" \
                          "               c' = b"
    assert t.value.__str__() == " /  0  0  1  0  \ \n" \
                                "|   1  0  0  0   |\n" \
                                "|   0  1  0  0   |\n" \
                                " \  0  0  0  1  / "

    p = fs.fromstr("p 1 2 3")
    assert (t**p).__str__() == "Pos /  3  \ \n" \
                               "   |   1   |\n" \
                               "    \  2  / "
def test_Metric():
    M = fs.fromstr("9 0 0 0 \n" \
                   "0 4 0 0 \n" \
                   "0 0 1 0 \n" \
                   "0 0 0 1")
    metric = geo.Metric(M)
    assert metric.__str__() == "Metric /  9  0  0  0  \ \n" \
                               "      |   0  4  0  0   |\n" \
                               "      |   0  0  1  0   |\n" \
                               "       \  0  0  0  1  / "
    o =  geo.Pos(fs.fromstr("0 \n 0 \n 0 \n 1"))
    p1 = geo.Pos(fs.fromstr("1 \n 0 \n 0 \n 1"))
    p2 = geo.Pos(fs.fromstr("0 \n 1 \n 0 \n 1"))
    assert metric.dot(p1 - o, p1 - o).__str__() == "9"
    assert metric.dot(p1 - o, p2 - o).__str__() == "0"
    cell = metric.to_Cellparameters()
    neunzig = fs.fromstr("90(0)")
    assert cell.__str__() == \
        geo.Cellparameters(3, 2, 1, neunzig, neunzig, neunzig).__str__()

    M = fs.fromstr("/ 1 0 0 0 \n 0 1 0 0 \n 0 0 1 0 \n 0 0 0 1 /")
    t = geo.Transformation(M)
    metric_ = t ** metric
    assert metric_.__str__() == metric.__str__()


def test_Cellparameters():
    cell = geo.Cellparameters(2, 3, 4, 90, 90, 90)
#    assert cell.to_Metric().__str__() == "Metric /             4  0.4(3.0)e-15  0(4)e-15  0  \ \n" \
#                                         "      |   0.4(3.0)e-15             9  1(6)e-15  0   |\n" \
#                                         "      |       0(4)e-15      1(6)e-15        16  0   |\n"\
#                                         "       \             0             0         0  1  / "


def test_Transgen():
    tg = geo.Transgen(fs.fromstr("d 1 0 0"), \
                      fs.fromstr("d 0 0 2"), \
                      fs.fromstr("d 0 3 0"))
    assert tg.__str__() == "Transgen /  1  \   /  0  \   /  0  \ \n"\
                           "        |   0   | |   0   | |   3   |\n"\
                           "         \  0  /   \  2  /   \  0  / "
    tg = geo.Transgen(fs.fromstr("d 1 0 0"), \
                      fs.fromstr("d 0 1 0"), \
                      fs.fromstr("d 0 0 2"))

    pos = geo.Pos(fs.fromstr(" 0.5 \n -0.5 \n -0.5 \n 1"))
    pos1 = pos % tg
    pos2 = geo.Pos(fs.fromstr("0.5 \n 0.5  \n  1.5 \n 1"))
    assert pos1 == pos2
    transformation = geo.Transformation(fs.fromstr( \
        " 1 0 0 0 \n 0 1 0 0 \n 0 0 1 0 \n 0 0 0 1"))
    assert isinstance(transformation ** tg, geo.Transgen)

def test_canonical():
    tg = geo.canonical
    assert tg.__str__() == "canonical"


def test_Coset():
    g = geo.Symmetry( \
        fs.fromstr("/ 1 0 2 -1 \n 0 -2 0 0 \n 0 0 1 1 \n 0 0 0 1 /"))
    tg = geo.Transgen(fs.fromstr("d 1 0 0"), \
                      fs.fromstr("d 0 1 0"), \
                      fs.fromstr("d 0 0 2"))
    tg1 = geo.Transgen(fs.fromstr("d 1 0 0"), \
                      fs.fromstr("d 0 1 0"), \
                      fs.fromstr("d 0 0 2"))
    assert tg == tg1
    c = geo.Coset(g, tg)
    assert c.__str__() == \
        "{x+2z,-2y,z+1}\n"\
        "     1  0  0  \n"\
        "     0  1  0  \n"\
        "     0  0  2  "

    c = geo.Coset(g, geo.canonical)
    assert c.__str__() == "{x+2z,-2y,z}"

    pos = geo.Pos(fs.fromstr("0.5 \n 0.25 \n 0 \n 1"))
    pos1 = c ** pos
    pos2 = geo.Pos(fs.fromstr("0.5 \n 0.5 \n 0 \n 1"))
    assert pos1 == pos2
   
def test_Spacegroup():
    transgen = geo.canonical
    c1 = geo.Coset(geo.Symmetry(\
                   fs.fromstr("1 0 0 0\n"\
                              "0 1 0 0\n"\
                              "0 0 1 0\n"\
                              "0 0 0 1")), \
                   transgen)
    c2 = geo.Coset(geo.Symmetry(\
                   fs.fromstr("-1 0 0 0\n"\
                              "0 -1 0 0\n"\
                              "0 0 -1 0\n"\
                              "0 0 0 1")), \
                   transgen)
    sg = geo.Spacegroup(transgen, [c1, c2])
    assert sg.__str__() == \
    "Spacegroup        \n"\
    "----------        \n"\
    " canonical        \n"\
    "             x,y,z\n"\
    "          -x,-y,-z"
    transgen = geo.Transgen(fs.fromstr("d 1 0 0"), \
                            fs.fromstr("d 0 1 0"), \
                            fs.fromstr("d 0 0 2"))
    c1 = geo.Coset(geo.Symmetry(\
                   fs.fromstr("1 0 0 0\n"\
                              "0 1 0 0\n"\
                              "0 0 1 0\n"\
                              "0 0 0 1")), \
                   transgen)
    c2 = geo.Coset(geo.Symmetry(\
                   fs.fromstr("-1 0 0 0\n"\
                              "0 -1 0 0\n"\
                              "0 0 -1 0\n"\
                              "0 0 0 1")), \
                   transgen)
    sg = geo.Spacegroup(transgen, [c1, c2])
    assert sg.__str__() == \
    "                           Spacegroup        \n"\
    "                           ----------        \n"\
    "Transgen /  1  \   /  0  \   /  0  \         \n"\
    "        |   0   | |   1   | |   0   |        \n"\
    "         \  0  /   \  0  /   \  2  /         \n"\
    "                                        x,y,z\n"\
    "                                     -x,-y,-z"

    sg = geo.Spacegroup(geo.canonical, [fs.fromstr("{x, y, z}"), \
                                        fs.fromstr("{x, -y,z}")])
    transformation = fs.fromstr("b, a, c")
    sg1 = transformation ** sg
    sg2 = geo.Spacegroup(transformation**geo.canonical, [fs.fromstr("{x, y, z}"), \
                                         fs.fromstr("{-x, y, z}")])

    assert sg.is_really_a_spacegroup() == True
    sg_error = geo.Spacegroup(geo.canonical, [fs.fromstr("{x, y, z}"), \
                                              fs.fromstr("{x+1/4, y, z}")])
    assert sg_error.is_really_a_spacegroup() == False
    # Hier ist noch folgender Fehler:
    # Das Programm berücksichtigt die Reihenfolge der
    # Symmetrieelemente eines Transgens. D.h. z.B.:
    #
    # / 1 \  / 0 \  / 0 \      / 0 \  / 1 \  / 0 \
    #|  0  ||  1  ||  0  | != |  1  ||  0  ||  0  |
    # \ 0 /  \ 0 /  \ 1 /      \ 0 /  \ 0 /  \ 1 /
    #
    # Was aber eigentlich gleich ist.

    #assert sg1.__str__() == sg2.__str__()

