from cryspy import geo
from cryspy import crystal
from cryspy.fromstr import fromstr as fs
from cryspy import tables

def make_blender_script(atomset, metric, structurename, outfilename):
    assert isinstance(atomset, crystal.Atomset), \
        "atomset must be of type crystal.Atomset."
    assert isinstance(metric, geo.Metric), \
        "metric must be of type geo.Metric."
    assert isinstance(outfilename, str), \
        "outfilename must be of type str."

    outstr = "import bpy \n" \
             "\n"

    # Delete the old structure, if exists:
    outstr += "for ob in bpy.data.objects:\n"
    outstr += "    if ob.name.startswith('%s'):\n"%(structurename)
    outstr += "        ob.select = True\n"
    outstr += "bpy.ops.object.delete()\n"

    outstr += "for me in bpy.data.meshes:\n"
    outstr += "    if me.name.startswith('%s'):\n"%(structurename)
    outstr += "        bpy.data.meshes.remove(me)\n"

    outstr += "for mat in bpy.data.materials:\n"
    outstr += "    if mat.name.startswith('%s'):\n"%(structurename)
    outstr += "        bpy.data.materials.remove(mat)\n"


    # Plot the axes:
    b = 0.02 # half axes-width in Angstroem
    t = metric.schmidttransformation
   
    pos = fs("p 1 0 0")
    x = float((t**pos).x())
    y = float((t**pos).y())
    z = float((t**pos).z())
    outstr += add_arrow(structurename, x, y, z)
#    outstr += "bpy.ops.mesh.primitive_cube_add(location = (0,0,0))\n"
#    outstr += "myaxis = bpy.context.object\n"
#    outstr += "myaxis.name = '%s.XAxis'\n"%(structurename)
#    outstr += "myaxis.data.vertices[0].co = (0.0, -%f, -%f)\n"%(b, b)
#    outstr += "myaxis.data.vertices[1].co = (0.0, -%f,  %f)\n"%(b, b)
#    outstr += "myaxis.data.vertices[2].co = (0.0,  %f, -%f)\n"%(b, b)
#    outstr += "myaxis.data.vertices[3].co = (0.0,  %f,  %f)\n"%(b, b)
#    outstr += "myaxis.data.vertices[4].co = (%f, %f, %f)\n"%(x, y - b, z - b)
#    outstr += "myaxis.data.vertices[5].co = (%f, %f, %f)\n"%(x, y - b, z + b)
#    outstr += "myaxis.data.vertices[6].co = (%f, %f, %f)\n"%(x, y + b, z - b)
#    outstr += "myaxis.data.vertices[7].co = (%f, %f, %f)\n"%(x, y + b, z + b)

    pos = fs("p 0 1 0")
    x = float((t**pos).x())
    y = float((t**pos).y())
    z = float((t**pos).z())
    outstr += "bpy.ops.mesh.primitive_cube_add(location = (0,0,0))\n"
    outstr += "myaxis = bpy.context.object\n"
    outstr += "myaxis.name = '%s.YAxis'\n"%(structurename)
    outstr += "myaxis.data.vertices[0].co = (-%f, 0.0, -%f)\n"%(b, b)
    outstr += "myaxis.data.vertices[1].co = ( %f, 0.0, -%f)\n"%(b, b)
    outstr += "myaxis.data.vertices[2].co = (-%f, 0.0,  %f)\n"%(b, b)
    outstr += "myaxis.data.vertices[3].co = ( %f, 0.0,  %f)\n"%(b, b)
    outstr += "myaxis.data.vertices[4].co = (%f, %f, %f)\n"%(x - b, y, z - b)
    outstr += "myaxis.data.vertices[5].co = (%f, %f, %f)\n"%(x + b, y, z - b)
    outstr += "myaxis.data.vertices[6].co = (%f, %f, %f)\n"%(x - b, y, z + b)
    outstr += "myaxis.data.vertices[7].co = (%f, %f, %f)\n"%(x + b, y, z + b)

    pos = fs("p 0 0 1")
    x = float((t**pos).x())
    y = float((t**pos).y())
    z = float((t**pos).z())
    outstr += "bpy.ops.mesh.primitive_cube_add(location = (0,0,0))\n"
    outstr += "myaxis = bpy.context.object\n"
    outstr += "myaxis.name = '%s.ZAxis'\n"%(structurename)
    outstr += "myaxis.data.vertices[0].co = (-%f, -%f, 0.0)\n"%(b, b)
    outstr += "myaxis.data.vertices[1].co = (-%f,  %f, 0.0)\n"%(b, b)
    outstr += "myaxis.data.vertices[2].co = ( %f, -%f, 0.0)\n"%(b, b)
    outstr += "myaxis.data.vertices[3].co = ( %f,  %f, 0.0)\n"%(b, b)
    outstr += "myaxis.data.vertices[4].co = (%f, %f, %f)\n"%(x - b, y - b, z)
    outstr += "myaxis.data.vertices[5].co = (%f, %f, %f)\n"%(x - b, y + b, z)
    outstr += "myaxis.data.vertices[6].co = (%f, %f, %f)\n"%(x + b, y - b, z)
    outstr += "myaxis.data.vertices[7].co = (%f, %f, %f)\n"%(x + b, y + b, z)


    # Create empty mesh for the positions of the atoms
    outstr += "bpy.ops.mesh.primitive_cube_add(location=(0,0,0))\n"
    outstr += "bpy.ops.object.mode_set(mode='EDIT')\n"
    outstr += "bpy.ops.mesh.delete(type='VERT')\n"
    outstr += "bpy.ops.object.mode_set(mode='OBJECT')\n"
    outstr += "posobject = bpy.context.object\n"
    outstr += "posobject.name = '%s.Positions'\n"%(structurename)


    # Create a mesh for each atom-type, respectively
    typs = []
    for atom in atomset.menge:
        if atom.typ not in typs:
            typs.append(atom.typ)

    for typ in typs:
        (spheresize, color) = tables.colorscheme_jmol(typ)
        outstr += "bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=%f)\n"%(spheresize)
        outstr += "ob = bpy.context.object\n"
        outstr += "me = ob.data\n"
        outstr += "me.name = '%s.mesh.%s'\n"%(structurename, typ)
        outstr += "bpy.ops.object.delete()\n"
        outstr += "mat = bpy.data.materials.new('%s.material.%s')\n" \
            %(structurename, typ)
        outstr += "mat.diffuse_color = %s\n"%(color.__str__())
        outstr += "me.materials.append(mat)\n"

    # Create spheres for the atoms and add a vertex
    # to the position-mesh, respectively
    materialnumber = 0
    atomnumber = 0
    for atom in atomset.menge:
        atomnumber += 1
        materialnumber += 1
        x = float((t**atom.pos).x())
        y = float((t**atom.pos).y())
        z = float((t**atom.pos).z())
        outstr += "posobject.data.vertices.add(1)\n"
        outstr += "posobject.data.vertices[-1].co = (%f, %f, %f)\n"%(x, y, z)
        outstr += "ob = bpy.data.objects.new( \
            '%s.Atom%03i(%s)', bpy.data.meshes['%s.mesh.%s'])\n" \
            %(structurename, atomnumber, atom.name, structurename, atom.typ)
        outstr += "ob.location = (%f, %f, %f)\n"%(x, y, z)
        outstr += "bpy.ops.object.shade_smooth()\n"
        outstr += "bpy.context.scene.objects.link(ob)\n"

    # Make all atoms looking smooth:
    outstr += "for ob in bpy.data.objects:\n"
    outstr += "    if ob.name.startswith('%s.Atom'):\n"%(structurename)
    outstr += "        ob.select = True\n"
    outstr += "    else:\n"
    outstr += "        ob.select = False\n"
    outstr += "bpy.ops.object.shade_smooth()\n"

    outfile = open(outfilename, "w")
    outfile.write(outstr)
    outfile.close()


def add_arrow(structurename, x, y, z):
    b = 0.02 # half axes-width in Angstroem
    tip_length = 1 # length of arrow-tip in Angstroem
    vertices = []
    

    outstr = ""
    outstr += "bpy.ops.mesh.primitive_cube_add(location = (0,0,0))\n"
    outstr += "myaxis = bpy.context.object\n"
    outstr += "myaxis.name = '%s.XAxis'\n"%(structurename)
    outstr += "myaxis.data.vertices[0].co = (0.0, -%f, -%f)\n"%(b, b)
    outstr += "myaxis.data.vertices[1].co = (0.0, -%f,  %f)\n"%(b, b)
    outstr += "myaxis.data.vertices[2].co = (0.0,  %f, -%f)\n"%(b, b)
    outstr += "myaxis.data.vertices[3].co = (0.0,  %f,  %f)\n"%(b, b)
    outstr += "myaxis.data.vertices[4].co = (%f, %f, %f)\n"%(x, y - b, z - b)
    outstr += "myaxis.data.vertices[5].co = (%f, %f, %f)\n"%(x, y - b, z + b)
    outstr += "myaxis.data.vertices[6].co = (%f, %f, %f)\n"%(x, y + b, z - b)
    outstr += "myaxis.data.vertices[7].co = (%f, %f, %f)\n"%(x, y + b, z + b)
    return outstr


