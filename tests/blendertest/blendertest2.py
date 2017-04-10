import cryspy
from cryspy.fromstr import fromstr as fs

cryspy.const.blender__std_face_opacity = 0.4

# Nach [Alonso2000a table 2]
metric = cryspy.geo.Cellparameters(fs("5.29314(5)"), fs("5.8384(1)"), fs("7.4025(1)"), 90, 90, 90).to_Metric()

atomset = cryspy.crystal.Atomset({
    cryspy.crystal.Atom("Tb1", "Tb", fs("p 0.9831(4) 0.0824(3) 1/4      ")),
    cryspy.crystal.Atom("Mn1", "Mn", fs("p 1/2       0         0        ")),
    cryspy.crystal.Atom("O1",  "O",  fs("p 0.1038(5) 0.4667(4) 1/4      ")),
    cryspy.crystal.Atom("O2",  "O",  fs("p 0.7039(4) 0.3262(3) 0.0510(2)"))
})

# Raumgruppe Pbnm (durch Transformation aus Pnma):
sg = fs("a' = c\n"
        "b' = a\n"
        "c' = b") \
        ** \
        cryspy.tables.spacegroup(62)


atomset = sg ** atomset

atomset = cryspy.utils.fill(atomset, [0.5, 0.05, 0.05])        


face1 = cryspy.crystal.Face("Face1", [atomset.get_atom("O2_6").pos, atomset.get_atom("O2_3").pos, atomset.get_atom("O1_2").pos])
face2 = cryspy.crystal.Face("Face2", [atomset.get_atom("O2_2r").pos, atomset.get_atom("O2_3").pos, atomset.get_atom("O1_2").pos])
face3 = cryspy.crystal.Face("Face3", [atomset.get_atom("O2_2r").pos, atomset.get_atom("O2_7r").pos, atomset.get_atom("O1_2").pos])
face4 = cryspy.crystal.Face("Face4", [atomset.get_atom("O2_6").pos, atomset.get_atom("O2_7r").pos, atomset.get_atom("O1_2").pos])
face5 = cryspy.crystal.Face("Face5", [atomset.get_atom("O2_6").pos, atomset.get_atom("O2_3").pos, atomset.get_atom("O1r").pos])
face6 = cryspy.crystal.Face("Face6", [atomset.get_atom("O2_2r").pos, atomset.get_atom("O2_3").pos, atomset.get_atom("O1r").pos])
face7 = cryspy.crystal.Face("Face7", [atomset.get_atom("O2_2r").pos, atomset.get_atom("O2_7r").pos, atomset.get_atom("O1r").pos])
face8 = cryspy.crystal.Face("Face8", [atomset.get_atom("O2_6").pos, atomset.get_atom("O2_7r").pos, atomset.get_atom("O1r").pos])

subset = cryspy.crystal.Subset("Octahedron", atomset.get_atom("Mn1_3r").pos, {face1, face2, face3, face4, face5, face6, face7, face8})

atomset.add(subset)
atomset = sg ** atomset
atomset = cryspy.utils.fill(atomset, [0.5, 0.05, 0.05])
print(atomset)
cryspy.blender.make_blender_script(atomset, metric, "structure", "blenderscript2.py")
