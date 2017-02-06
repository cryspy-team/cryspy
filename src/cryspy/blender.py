import numpy as np
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

    outstr = "import bpy\n" \
             "import bmesh\n" \
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
    outstr += add_arrow(structurename, 'XAxis', x, y, z)

    pos = fs("p 0 1 0")
    x = float((t**pos).x())
    y = float((t**pos).y())
    z = float((t**pos).z())
    outstr += add_arrow(structurename, 'YAxis', x, y, z)

    pos = fs("p 0 0 1")
    x = float((t**pos).x())
    y = float((t**pos).y())
    z = float((t**pos).z())
    outstr += add_arrow(structurename, 'ZAxis', x, y, z)

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


def add_arrow(structurename, arrowname, x, y, z):
    b = 0.02 # half axes-width in Angstroem
    tip_length = 1 # length of arrow-tip in Angstroem
    l = np.sqrt(x*x + y*y + z*z)
    xkurz = x * (1 - 0.5/l)
    ykurz = y * (1 - 0.5/l)
    zkurz = z * (1 - 0.5/l)
    outstr = add_cylinder(structurename, arrowname + "_cylinder", 0, 0, 0, xkurz, ykurz, zkurz)
    outstr += add_cone(structurename, arrowname + "_cone", 0, 0, 0, x, y, z)
    return outstr

def add_cylinder(structurename, cylindername, x1, y1, z1, x2, y2, z2):
    b = 0.1 # half cylinder width in Angstroem
    segments = 6
    outstr = ""
    x = x2 - x1
    y = y2 - y1
    z = z2 - z1
    l = np.sqrt(x*x + y*y + z*z)
    theta = np.arccos(z/l)
    phi = np.arctan2(y, x)
    print("theta = " + str(theta/np.pi*180))
    print("phi   = " + str(phi/np.pi*180))
    cosphi = np.cos(phi)
    sinphi = np.sin(phi)
    costheta = np.cos(theta)
    sintheta = np.sin(theta)
    Mtheta =  "[[%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f]]"% \
              (costheta, 0.0, -sintheta, 0.0, \
               0.0,  1.0, 0.0, 0.0, \
              sintheta,        0.0,      costheta, 0.0, \
              0.0, 0.0, 0.0, 1.0)
    Mphi =  "[[%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f]]"% \
             (cosphi, sinphi, 0.0, 0.0, \
              -sinphi, cosphi, 0.0, 0.0, \
              0.0,        0.0,   1.0, 0.0, \
             0.0, 0.0, 0.0, 1.0)
    
    outstr += "bm = bmesh.new()\n"
    outstr += "bmesh.ops.create_cone(bm, " \
                                    "cap_ends = True, " \
                                    "cap_tris = True, " \
                                    "segments = %i, " \
                                    "diameter1 = %10.4f, " \
                                    "diameter2 = %10.4f, " \
                                    "depth = %10.4f)\n" \
                                    %(segments, b, b, l)
    outstr += "bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0, %10.4f))\n"%(l/2)
#    outstr += "bmesh.ops.rotate(bm, verts=bm.verts, cent = (0.0, 0.0, 0.0), matrix = %s)\n"%(M)
    outstr += "mesh = bpy.data.meshes.new('%s.mesh%s')\n"%(structurename, cylindername)
    outstr += "bm.to_mesh(mesh)\n"
    outstr += "ob = bpy.data.objects.new('%s.%s', mesh)\n"%(structurename, cylindername)
    outstr += "ob.data.transform(%s)\n"%(Mtheta)
    outstr += "ob.data.transform(%s)\n"%(Mphi)
    outstr += "bpy.context.scene.objects.link(ob)\n"
    return outstr

def add_cone(structurename, conename, x1, y1, z1, x2, y2, z2):
    segments = 6
    b = 0.5 # Thickness of cone in Angstroem
    h = 1 # Height of cone in Anstroem
    outstr = ""
    x = x2 - x1
    y = y2 - y1
    z = z2 - z1
    l = np.sqrt(x*x + y*y + z*z)
    theta = np.arccos(z/l)
    phi = np.arctan2(y, x)
    print("theta = " + str(theta/np.pi*180))
    print("phi   = " + str(phi/np.pi*180))
    cosphi = np.cos(phi)
    sinphi = np.sin(phi)
    costheta = np.cos(theta)
    sintheta = np.sin(theta)
    Mtheta =  "[[%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f]]"% \
              (costheta, 0.0, -sintheta, 0.0, \
               0.0,  1.0, 0.0, 0.0, \
              sintheta,        0.0,      costheta, 0.0, \
              0.0, 0.0, 0.0, 1.0)
    Mphi =  "[[%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f]]"% \
             (cosphi, sinphi, 0.0, 0.0, \
              -sinphi, cosphi, 0.0, 0.0, \
              0.0,        0.0,   1.0, 0.0, \
             0.0, 0.0, 0.0, 1.0)
    
    outstr += "bm = bmesh.new()\n"
    outstr += "bmesh.ops.create_cone(bm, " \
                                    "cap_ends = True, " \
                                    "cap_tris = True, " \
                                    "segments = %i, " \
                                    "diameter1 = %10.4f, " \
                                    "diameter2 = %10.4f, " \
                                    "depth = %10.4f)\n" \
                                    %(segments, b, 0.01, h)
    outstr += "bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0, %10.4f))\n"%(l - 0.5)
    outstr += "mesh = bpy.data.meshes.new('%s.mesh%s')\n"%(structurename, conename)
    outstr += "bm.to_mesh(mesh)\n"
    outstr += "ob = bpy.data.objects.new('%s.%s', mesh)\n"%(structurename, conename)
    outstr += "ob.data.transform(%s)\n"%(Mtheta)
    outstr += "ob.data.transform(%s)\n"%(Mphi)
    outstr += "bpy.context.scene.objects.link(ob)\n"
    return outstr
