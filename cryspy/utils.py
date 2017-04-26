import cryspy
from cryspy.fromstr import fromstr as fs
import cryspy.numbers as nb
import cryspy.geo as geo


class Karussell:
    def __init__(self, metric, zerodirection, positivedirection):

        self.zerodir = zerodirection * (1 / metric.length(zerodirection))
        self.positivedir = positivedirection - self.zerodir * metric.dot(positivedirection, self.zerodir)
        self.positivedir *= 1 / metric.length(self.positivedir)
        self.metric = metric

    def direction(self, angle):
        x = nb.cos(angle)
        y = nb.sin(angle)
        return self.zerodir * x + self.positivedir * y

def fill(atomset, extraextensions):
    assert isinstance(atomset, cryspy.crystal.Atomset), \
        "First argument of cryspy.utils.fill(...) must be of " \
        "type cryspy.crystal.Atomset."
    assert isinstance(extraextensions, list), \
        "Second argument of cryspy.utils.fill(...) must be of " \
        "type list."
    assert len(extraextensions) == 3, \
        "Second argument of cryspy.utils.fill(...) must be a " \
        "list of three numbers."
    for item in extraextensions:
        assert isinstance(item, cryspy.numbers.Mixed) \
            or isinstance(item, float) or isinstance(item, int), \
            "Scond argument of cryspy.utils.fill(...) must be a " \
            "list of three numbers."

    atomset_new =  \
                 ((atomset + "lbd") + fs("d -1 -1 -1")) \
               + ((atomset + "lb") + fs("d -1 -1  0")) \
               + ((atomset + "lbu") + fs("d -1 -1 +1")) \
               + ((atomset + "ld") + fs("d -1  0 -1")) \
               + ((atomset + "l") + fs("d -1  0  0")) \
               + ((atomset + "lu") + fs("d -1  0 +1")) \
               + ((atomset + "lfd") + fs("d -1 +1 -1")) \
               + ((atomset + "lf") + fs("d -1 +1  0")) \
               + ((atomset + "lfu") + fs("d -1 +1 +1")) \
               + ((atomset + "bd") + fs("d  0 -1 -1")) \
               + ((atomset + "b") + fs("d  0 -1  0")) \
               + ((atomset + "bu") + fs("d  0 -1 +1")) \
               + ((atomset + "d") + fs("d  0  0 -1")) \
               + ((atomset + "") + fs("d  0  0  0")) \
               + ((atomset + "u") + fs("d  0  0 +1")) \
               + ((atomset + "fd") + fs("d  0 +1 -1")) \
               + ((atomset + "f") + fs("d  0 +1  0")) \
               + ((atomset + "fu") + fs("d  0 +1 +1")) \
               + ((atomset + "rbd") + fs("d +1 -1 -1")) \
               + ((atomset + "rb") + fs("d +1 -1  0")) \
               + ((atomset + "rbu") + fs("d +1 -1 +1")) \
               + ((atomset + "rd") + fs("d +1  0 -1")) \
               + ((atomset + "r") + fs("d +1  0  0")) \
               + ((atomset + "ru") + fs("d +1  0 +1")) \
               + ((atomset + "rfd") + fs("d +1 +1 -1")) \
               + ((atomset + "rf") + fs("d +1 +1  0")) \
               + ((atomset + "rfu") + fs("d +1 +1 +1")) \

    menge = atomset_new.menge
    menge_new = set([])
    extra_x = extraextensions[0]
    extra_y = extraextensions[1]
    extra_z = extraextensions[2]
    for atom in menge:
        if (0 - extra_x <= float(atom.pos.x()) <= 1 + extra_x) \
            and (0 - extra_y <= float(atom.pos.y()) <= 1 + extra_y) \
            and (0 - extra_z <= float(atom.pos.z()) <= 1 + extra_z):
            menge_new.add(atom)
    return cryspy.crystal.Atomset(menge_new)


def octahedron(name, top, one, two, three, four, bottom, 
               facecolor, faceopacity, plotedges, edgecolor, edgewidth):
    # name: any string for a name, e.g. "MyFancyOctahedron"
    # top, one, two, three, four, bottom: The six corners of octahedron.
    #     top and bottom are the poles, one ... four are the
    #     equatorial corners. The corners must be objects of type
    #     cryspy.geo.Pos .
    # facecolor: e.g. (1, 0, 0) for red
    # faceopacity: 0 = invisible -> 1 = fully opaque
    # plot edge: True = with edges, False = without edges
    # edgecolor: e.g. (0, 0, 0) for black
    # edgewidth: width of edge in Angstroem, e.g. 0.1

    assert isinstance(name, str), \
        "The name of the octahedron must be of type str."
    for corner in [top, one, two, three, four, bottom]:
        assert isinstance(corner, cryspy.geo.Pos), \
            "The corners of the octahedron must be of type " \
            "cryspy.geo.Pos ."
    for color in [facecolor, edgecolor]:
        assert isinstance(color, list) or isinstance(color, tuple), \
            "The face- and edgecolor of the octahedron must be " \
            "lists or tuples."
        for item in color:
            assert isinstance(item, float) \
                or isinstance(item, int) \
                or isinstance(item, cryspy.numbers.Mixed), \
                "The face- and edgecolor of the octahedron must be " \
                "lists or tuples of type float, int or " \
                "cryspy.numbers.Mixed ."
    assert isinstance(faceopacity, float) \
        or isinstance(faceopacity, int), \
        "The faceopacity of the octahedron must be of type " \
        "float or int."
    assert isinstance(plotedges, bool), \
        "The parameter plotedges of the octahedron (says whether " \
        "to plot the edges as cylinders or not) must be of " \
        "of type bool (True or False). "
    assert isinstance(edgewidth, float) \
        or isinstance(edgewidth, int), \
        "The edgewidth of the octahedron must be of type " \
        "float or int."

    face1 = cryspy.crystal.Face("Face1", [one, two, top])
    face2 = cryspy.crystal.Face("Face2", [two, three, top])
    face3 = cryspy.crystal.Face("Face3", [three, four, top])
    face4 = cryspy.crystal.Face("Face4", [four, one, top])
    face5 = cryspy.crystal.Face("Face5", [one, two, bottom])
    face6 = cryspy.crystal.Face("Face6", [two, three, bottom])
    face7 = cryspy.crystal.Face("Face7", [three, four, bottom])
    face8 = cryspy.crystal.Face("Face8", [four, one, bottom])

    faces = {face1, face2, face3, face4, face5, face6, face7, face8}
    for face in faces:
        face.set_color(facecolor)
        face.set_opacity(faceopacity)

    if plotedges:
        edge1 = cryspy.crystal.Bond("Edge1", top, one)
        edge2 = cryspy.crystal.Bond("Edge2", top, two)
        edge3 = cryspy.crystal.Bond("Edge3", top, three)
        edge4 = cryspy.crystal.Bond("Edge4", top, four)
        edge5 = cryspy.crystal.Bond("Edge5", one, two)
        edge6 = cryspy.crystal.Bond("Edge6", two, three)
        edge7 = cryspy.crystal.Bond("Edge7", three, four)
        edge8 = cryspy.crystal.Bond("Edge8", four, one)
        edge9 = cryspy.crystal.Bond("Edge9", one, bottom)
        edge10 = cryspy.crystal.Bond("Edge10", two, bottom)
        edge11 = cryspy.crystal.Bond("Edge11", three, bottom)
        edge12 = cryspy.crystal.Bond("Edge12", four, bottom)
        edges = {edge1, edge2, edge3, edge4,
                 edge5, edge6, edge7, edge8,
                 edge9, edge10, edge11, edge12}
        for edge in edges:
            edge.set_color(edgecolor)
            edge.set_thickness(edgewidth)
    else:
        edges = set([])


    edges_and_faces = edges | faces

    centre_of_gravity = cryspy.geo.centre_of_gravity(
        [top, one, two, three, four, bottom]
    )
    subset = cryspy.crystal.Subset(
        name,
        centre_of_gravity,
        edges_and_faces
    )
    return subset

def read_metric_from_cif(infilepathname):
    # So far only for cif-files generated by JANA2006, and even this
    # without any warranty, and maybe not all parameters.

    infile = open(infilepathname, "r")
    for line in infile:
        words = line.split()
        if len(words) >= 2:
            if words[0] == "_cell_length_a":
                a = fs(words[1])
            if words[0] == "_cell_length_b":
                b = fs(words[1])
            if words[0] == "_cell_length_c":
                c = fs(words[1])
            if words[0] == "_cell_angle_alpha":
                alpha = fs(words[1])
            if words[0] == "_cell_angle_beta" :
                beta  = fs(words[1])
            if words[0] == "_cell_angle_gamma":
                gamma = fs(words[1])
    infile.close()
    return cryspy.geo.Cellparameters(
        a, b, c, alpha, beta, gamma
    ).to_Metric()

def read_atomset_from_cif(infilepathname):
    # So far only for cif-files generated by JANA2006, and even this
    # without any warranty, and maybe not all parameters.
    infile = open(infilepathname, "r")
    status = "waiting_for_loop"
    loop_header = []
    menge = set([])
    for line in infile:
        words = line.split()
        if len(words) >= 1:
            if status == "reading_loop_header":
                if words[0][0] == "_":
                    loop_header += [words[0]]
                else:
                    print(loop_header)
                    status = "reading_loop_data"
            if status == "reading_loop_data":
                if len(words) == len(loop_header):
                    atom_name = None
                    atom_type = None
                    x = None
                    y = None
                    z = None
                    for i in range(len(loop_header)):
                        if loop_header[i] == "_atom_site_label":
                            atom_name = words[i]
                        if loop_header[i] == "_atom_site_type_symbol":
                            atom_type = words[i]
                        if loop_header[i] == "_atom_site_fract_x":
                            x = fs(words[i])
                        if loop_header[i] == "_atom_site_fract_y":
                            y = fs(words[i])
                        if loop_header[i] == "_atom_site_fract_z":
                            z = fs(words[i])
                    if      isinstance(atom_name, str) \
                        and isinstance(atom_type, str) \
                        and isinstance(x, cryspy.numbers.Mixed) \
                        and isinstance(y, cryspy.numbers.Mixed) \
                        and isinstance(z, cryspy.numbers.Mixed):
                        print(atom_name, atom_type, x, y, z)
                        menge.add(
                            cryspy.crystal.Atom(
                                atom_name, atom_type,
                                cryspy.geo.Pos(
                                    cryspy.numbers.Matrix([[x], [y], [z], [1]])
                                )
                            )
                        )

            if words[0] == "loop_":
                loop_header = []
                status = "reading_loop_header"
        if len(words) == 0:
            if status == "reading_loop_data":
                status = "waiting_for_loop"
    infile.close()
    return cryspy.crystal.Atomset(menge)

