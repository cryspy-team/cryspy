from cryspy import geo
from cryspy import crystal
from cryspy.fromstr import fromstr as fs

def make_blender_script(atomset, metric, outfilename):
    assert isinstance(atomset, crystal.Atomset), \
        "atomset must be of type crystal.Atomset."
    assert isinstance(metric, geo.Metric), \
        "metric must be of type geo.Metric."
    assert isinstance(outfilename, str), \
        "outfilename must be of type str."

    outstr = "import bpy \n" \
             "\n"


    t = metric.schmidttransformation
   
    pos = fs("p 1 0 0")
    x = float((t**pos).x())
    y = float((t**pos).y())
    z = float((t**pos).z())
    outstr += "bpy.ops.mesh.primitive_cube_add(location = (0,0,0))\n"
    outstr += "myaxis = bpy.context.object\n"
    outstr += "myaxis.data.vertices[0].co = (0.0, -0.1, -0.1)\n"
    outstr += "myaxis.data.vertices[1].co = (0.0, -0.1,  0.1)\n"
    outstr += "myaxis.data.vertices[2].co = (0.0,  0.1, -0.1)\n"
    outstr += "myaxis.data.vertices[3].co = (0.0,  0.1,  0.1)\n"
    outstr += "myaxis.data.vertices[4].co = (%f, %f, %f)\n"%(x, y-0.1, z-0.1)
    outstr += "myaxis.data.vertices[5].co = (%f, %f, %f)\n"%(x, y-0.1, z+0.1)
    outstr += "myaxis.data.vertices[6].co = (%f, %f, %f)\n"%(x, y+0.1, z-0.1)
    outstr += "myaxis.data.vertices[7].co = (%f, %f, %f)\n"%(x, y+0.1, z+0.1)

    pos = fs("p 0 1 0")
    x = float((t**pos).x())
    y = float((t**pos).y())
    z = float((t**pos).z())
    outstr += "bpy.ops.mesh.primitive_cube_add(location = (0,0,0))\n"
    outstr += "myaxis = bpy.context.object\n"
    outstr += "myaxis.data.vertices[0].co = (-0.1, 0.0, -0.1)\n"
    outstr += "myaxis.data.vertices[1].co = (0.1, 0.0,  -0.1)\n"
    outstr += "myaxis.data.vertices[2].co = (-0.1,  0.0, 0.1)\n"
    outstr += "myaxis.data.vertices[3].co = (0.1,  0.0,  0.1)\n"
    outstr += "myaxis.data.vertices[4].co = (%f, %f, %f)\n"%(x-0.1, y, z-0.1)
    outstr += "myaxis.data.vertices[5].co = (%f, %f, %f)\n"%(x+0.1, y, z-0.1)
    outstr += "myaxis.data.vertices[6].co = (%f, %f, %f)\n"%(x-0.1, y, z+0.1)
    outstr += "myaxis.data.vertices[7].co = (%f, %f, %f)\n"%(x+0.1, y, z+0.1)

    pos = fs("p 0 0 1")
    x = float((t**pos).x())
    y = float((t**pos).y())
    z = float((t**pos).z())
    outstr += "bpy.ops.mesh.primitive_cube_add(location = (0,0,0))\n"
    outstr += "myaxis = bpy.context.object\n"
    outstr += "myaxis.data.vertices[0].co = (-0.1, -0.1, 0.0)\n"
    outstr += "myaxis.data.vertices[1].co = (-0.1,  0.1, 0.0)\n"
    outstr += "myaxis.data.vertices[2].co = (0.1, -0.1, 0.0)\n"
    outstr += "myaxis.data.vertices[3].co = (0.1,  0.1, 0.0)\n"
    outstr += "myaxis.data.vertices[4].co = (%f, %f, %f)\n"%(x-0.1, y-0.1, z)
    outstr += "myaxis.data.vertices[5].co = (%f, %f, %f)\n"%(x-0.1, y+0.1, z)
    outstr += "myaxis.data.vertices[6].co = (%f, %f, %f)\n"%(x+0.1, y-0.1, z)
    outstr += "myaxis.data.vertices[7].co = (%f, %f, %f)\n"%(x+0.1, y+0.1, z)


    outstr += "bpy.ops.mesh.primitive_cube_add(location=(0,0,0))\n"
    outstr += "bpy.ops.object.mode_set(mode='EDIT')\n"
    outstr += "bpy.ops.mesh.delete(type='VERT')\n"
    outstr += "bpy.ops.object.mode_set(mode='OBJECT')\n"
    outstr += "posobject = bpy.context.object\n"


    materialnumber = 0
    for atom in atomset.menge:
        materialnumber += 1
        x = float((t**atom.pos).x())
        y = float((t**atom.pos).y())
        z = float((t**atom.pos).z())
        outstr += "posobject.data.vertices.add(1)\n"
        outstr += "posobject.data.vertices[-1].co = (%f, %f, %f)\n"%(x, y, z)
        (spheresize, color) = size_and_color(atom.typ)
        outstr += "bpy.ops.mesh.primitive_uv_sphere_add(location=(%f, %f, %f), size=%f)\n"%(x, y, z, spheresize)
        outstr += "mat = bpy.data.materials.new('material.%03i')\n"%(materialnumber)
        outstr += "mat.diffuse_color = %s\n"%(color.__str__())
        outstr += "bpy.context.object.data.materials.append(mat)\n"

    outfile = open(outfilename, "w")
    outfile.write(outstr)
    outfile.close()

def size_and_color(atomtype):
    assert isinstance(atomtype, str), \
        "atomtype must be of type str."
    if atomtype == "O":
        spheresize = 0.3
        color = (1.0, 0.0, 0.0)
    elif atomtype == "Ca":
        spheresize = 0.4
        color = (0.0, 0.0, 0.8)
    elif atomtype == "Mn":
        spheresize = 0.5
        color = (0.6, 0.0, 0.8)
    else:
        spheresize = 0.2
        color = (0.5, 0.5, 0.5)
    return (spheresize, color)
