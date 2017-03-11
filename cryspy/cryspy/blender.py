import numpy as np
from cryspy import const
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
    outstr += "    if ob.name.startswith('%s'):\n" % (structurename)
    outstr += "        ob.select = True\n"
    outstr += "bpy.ops.object.delete()\n"

    outstr += "for me in bpy.data.meshes:\n"
    outstr += "    if me.name.startswith('%s'):\n" % (structurename)
    outstr += "        bpy.data.meshes.remove(me)\n"

    outstr += "for mat in bpy.data.materials:\n"
    outstr += "    if mat.name.startswith('%s'):\n" % (structurename)
    outstr += "        bpy.data.materials.remove(mat)\n"

    # Delete all existing lamps:
    outstr += "bpy.ops.object.select_all(action='DESELECT')\n"
    outstr += "for object in bpy.data.objects:\n"
    outstr += "    if object.type == 'LAMP':\n"
    outstr += "        object.select = True\n"
    outstr += "bpy.ops.object.delete()\n"

    # Set background color:
    outstr += "bpy.data.worlds['World'].horizon_color = %s\n" \
        % (str(const.blender__background_color))

    # Place some cool lamps:
    outstr += "bpy.ops.object.lamp_add(type='POINT')\n"
    outstr += "l = bpy.context.object\n"
    outstr += "l.name = '%s.Lamp1'\n" % (structurename)
    outstr += "l.location = %s\n" % (str(const.blender__location_of_lamp1))
    outstr += "bpy.ops.object.lamp_add(type='HEMI')\n"
    outstr += "l = bpy.context.object\n"
    outstr += "l.name = '%s.LampHemi'\n" % (structurename)
    outstr += "l.location = (-10, -10, 10)\n"
    outstr += "l.data.energy = %10.4f\n" % (const.blender__diffuse_light)

    # Plot the axes:
    t = metric.schmidttransformation

    pos = fs("p 1 0 0")
    x = float((t ** pos).x())
    y = float((t ** pos).y())
    z = float((t ** pos).z())
    outstr += add_axis(structurename, 'XAxis', x, y, z)

    pos = fs("p 0 1 0")
    x = float((t ** pos).x())
    y = float((t ** pos).y())
    z = float((t ** pos).z())
    outstr += add_axis(structurename, 'YAxis', x, y, z)

    pos = fs("p 0 0 1")
    x = float((t ** pos).x())
    y = float((t ** pos).y())
    z = float((t ** pos).z())
    outstr += add_axis(structurename, 'ZAxis', x, y, z)

    # Create empty mesh for the positions of the atoms
    outstr += "bpy.ops.mesh.primitive_cube_add(location=(0,0,0))\n"
    outstr += "bpy.ops.object.mode_set(mode='EDIT')\n"
    outstr += "bpy.ops.mesh.delete(type='VERT')\n"
    outstr += "bpy.ops.object.mode_set(mode='OBJECT')\n"
    outstr += "posobject = bpy.context.object\n"
    outstr += "posobject.name = '%s.Positions'\n" % (structurename)

    # Create a mesh for each atom-type, respectively
    typs = []
    atomlist = []
    momentumlist = []
    for item in atomset.menge:
        if isinstance(item, crystal.Atom):
            atomlist.append(item)
        elif isinstance(item, crystal.Momentum):
            momentumlist.append(item)

    for atom in atomlist:
        if atom.typ not in typs:
            typs.append(atom.typ)

    for typ in typs:
        (spheresize, color) = tables.colorscheme_jmol(typ)
        outstr += "bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=%f, subdivisions=%i)\n" \
            % (spheresize, const.blender__atom_icosphere_subdivisions)
        outstr += "ob = bpy.context.object\n"
        outstr += "me = ob.data\n"
        outstr += "me.name = '%s.mesh.%s'\n" % (structurename, typ)
        outstr += "bpy.ops.object.delete()\n"
        outstr += "mat = bpy.data.materials.new('%s.material.%s')\n" \
            % (structurename, typ)
        outstr += "mat.diffuse_color = %s\n" % (color.__str__())
        outstr += "me.materials.append(mat)\n"

    # Create spheres for the atoms and add a vertex
    # to the position-mesh, respectively
    materialnumber = 0
    atomnumber = 0
    for atom in atomlist:
        atomnumber += 1
        materialnumber += 1
        x = float((t ** atom.pos).x())
        y = float((t ** atom.pos).y())
        z = float((t ** atom.pos).z())
        outstr += "posobject.data.vertices.add(1)\n"
        outstr += "posobject.data.vertices[-1].co = (%f, %f, %f)\n" % (x, y, z)
        outstr += "ob = bpy.data.objects.new( \
            '%s.Atom%03i(%s)', bpy.data.meshes['%s.mesh.%s'])\n" \
            % (structurename, atomnumber, atom.name, structurename, atom.typ)
        outstr += "ob.location = (%f, %f, %f)\n" % (x, y, z)
        outstr += "bpy.ops.object.shade_smooth()\n"
        outstr += "bpy.context.scene.objects.link(ob)\n"

    # Create arrows for the momentums:
    momentumindex = 0
    for momentum in momentumlist:
        momentumindex += 1
        momentumname = "Momentum%03i" % (momentumindex)
        if momentum.has_plotlength:
            plotlength = momentum.plotlength
        else:
            plotlength = const.blender__std_momentum_plotlength
        if momentum.has_color:
            color = momentum.color
        else:
            color = const.blender__std_momentum_color

        x0 = float((t ** momentum.pos).x())
        y0 = float((t ** momentum.pos).y())
        z0 = float((t ** momentum.pos).z())
        dx = float((t ** momentum.direction).x())
        dy = float((t ** momentum.direction).y())
        dz = float((t ** momentum.direction).z())

        length = np.sqrt(dx * dx + dy * dy + dz * dz)
        x1 = x0 - dx * plotlength / length
        y1 = y0 - dy * plotlength / length
        z1 = z0 - dz * plotlength / length
        x2 = x0 + dx * plotlength / length
        y2 = y0 + dy * plotlength / length
        z2 = z0 + dz * plotlength / length

        outstr += add_momentum(structurename, momentumname,
                               x1, y1, z1, x2, y2, z2, color)

    # Make all atoms looking smooth:
    outstr += "for ob in bpy.data.objects:\n"
    outstr += "    if ob.name.startswith('%s.Atom'):\n" % (structurename)
    outstr += "        ob.select = True\n"
    outstr += "    else:\n"
    outstr += "        ob.select = False\n"
    outstr += "bpy.ops.object.shade_smooth()\n"

    outfile = open(outfilename, "w")
    outfile.write(outstr)
    outfile.close()


def add_axis(structurename, arrowname, x, y, z):
    outstr = add_arrow(structurename, arrowname, 0, 0, 0, x, y, z,
                       const.blender__thickness_of_axis_shaft,
                       const.blender__num_of_segments_of_axis_shaft,
                       const.blender__thickness_of_axis_tip,
                       const.blender__height_of_axis_tip,
                       const.blender__num_of_segments_of_axis_tip,
                       const.blender__axes_color)
    return outstr


def add_momentum(structurename, momentumname, x1, y1, z1, x2, y2, z2, color):
    outstr = add_arrow(structurename, momentumname, x1, y1, z1, x2, y2, z2,
                       const.blender__thickness_of_momentum_shaft,
                       const.blender__num_of_segments_of_momentum_shaft,
                       const.blender__thickness_of_momentum_tip,
                       const.blender__height_of_momentum_tip,
                       const.blender__num_of_segments_of_momentum_tip,
                       color)
    return outstr


def add_arrow(structurename, arrowname, x1, y1, z1, x2, y2, z2,
              thickness_of_arrow_shaft, num_of_segments_of_arrow_shaft,
              thickness_of_arrow_tip, height_of_arrow_tip, num_of_segments_of_arrow_tip, color):
    h = height_of_arrow_tip
    l = np.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1))
    x2kurz = x1 + (x2 - x1) * (1 - h / l)
    y2kurz = y1 + (y2 - y1) * (1 - h / l)
    z2kurz = z1 + (z2 - z1) * (1 - h / l)
    outstr = add_cylinder(structurename, arrowname + "_cylinder",
                          x1, y1, z1, x2kurz, y2kurz, z2kurz,
                          thickness_of_arrow_shaft, num_of_segments_of_arrow_shaft)
    outstr += add_cone(structurename, arrowname + "_cone", x1, y1, z1, x2, y2, z2,
                       thickness_of_arrow_tip, height_of_arrow_tip, num_of_segments_of_arrow_tip)
    outstr += "bpy.ops.object.select_all(action='DESELECT')\n"
    outstr += "ob1.select = True\n"
    outstr += "ob2.select = True\n"
    outstr += "bpy.context.scene.objects.active = ob1\n"
    outstr += "bpy.ops.object.join()\n"
    outstr += "mat = bpy.data.materials.new('%s.material.%s')\n"\
        % (structurename, arrowname)
    outstr += "mat.diffuse_color = %s\n"\
        % (str(color))
    outstr += "mat.specular_color = (0, 0, 0)\n"
    outstr += "ob1.data.materials.append(mat)\n"
    return outstr


def add_cylinder(structurename, cylindername, x1, y1, z1, x2, y2, z2,
                 thickness_of_arrow_shaft, num_of_segments_of_arrow_shaft):
    b = thickness_of_arrow_shaft
    segments = num_of_segments_of_arrow_shaft
    outstr = ""
    x = x2 - x1
    y = y2 - y1
    z = z2 - z1
    l = np.sqrt(x * x + y * y + z * z)
    theta = np.arccos(z / l)
    phi = np.arctan2(y, x)
    cosphi = np.cos(phi)
    sinphi = np.sin(phi)
    costheta = np.cos(theta)
    sintheta = np.sin(theta)
    Mtheta =  "[[%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f]]" % \
              (costheta, 0.0, -sintheta, 0.0,
               0.0, 1.0, 0.0, 0.0,
               sintheta, 0.0, costheta, 0.0,
               0.0, 0.0, 0.0, 1.0)
    Mphi =  "[[%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f]]" % \
    (cosphi, sinphi, 0.0, 0.0,
     -sinphi, cosphi, 0.0, 0.0,
     0.0, 0.0, 1.0, 0.0,
     0.0, 0.0, 0.0, 1.0)

    outstr += "bm = bmesh.new()\n"
    outstr += "bmesh.ops.create_cone(bm, " \
    "cap_ends = True, " \
    "cap_tris = True, " \
    "segments = %i, " \
    "diameter1 = %10.4f, " \
    "diameter2 = %10.4f, " \
    "depth = %10.4f)\n" \
    % (segments, b, b, l)
    outstr += "bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0, %10.4f))\n" % (l / 2)
    outstr += "mesh = bpy.data.meshes.new('%s.mesh%s')\n" % (structurename, cylindername)
    outstr += "bm.to_mesh(mesh)\n"
    outstr += "ob1 = bpy.data.objects.new('%s.%s', mesh)\n" % (structurename, cylindername)
    outstr += "ob1.data.transform(%s)\n" % (Mtheta)
    outstr += "ob1.data.transform(%s)\n" % (Mphi)
    outstr += "ob1.location = (%10.4f, %10.4f, %10.4f)\n" % (x1, y1, z1)
    outstr += "bpy.context.scene.objects.link(ob1)\n"
    return outstr


def add_cone(structurename, conename, x1, y1, z1, x2, y2, z2,
             thickness_of_arrow_tip, height_of_arrow_tip, num_of_segments_of_arrow_tip):
    segments = num_of_segments_of_arrow_tip
    b = thickness_of_arrow_tip
    h = height_of_arrow_tip
    outstr = ""
    x = x2 - x1
    y = y2 - y1
    z = z2 - z1
    l = np.sqrt(x * x + y * y + z * z)
    theta = np.arccos(z / l)
    phi = np.arctan2(y, x)
    cosphi = np.cos(phi)
    sinphi = np.sin(phi)
    costheta = np.cos(theta)
    sintheta = np.sin(theta)
    Mtheta =  "[[%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
              " [%10.4f, %10.4f, %10.4f, %10.4f]]" % \
              (costheta, 0.0, -sintheta, 0.0,
               0.0, 1.0, 0.0, 0.0,
               sintheta, 0.0, costheta, 0.0,
               0.0, 0.0, 0.0, 1.0)
    Mphi =  "[[%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f], \\\n" \
            " [%10.4f, %10.4f, %10.4f, %10.4f]]" % \
    (cosphi, sinphi, 0.0, 0.0,
     -sinphi, cosphi, 0.0, 0.0,
     0.0, 0.0, 1.0, 0.0,
     0.0, 0.0, 0.0, 1.0)

    outstr += "bm = bmesh.new()\n"
    outstr += "bmesh.ops.create_cone(bm, " \
    "cap_ends = True, " \
    "cap_tris = True, " \
    "segments = %i, " \
    "diameter1 = %10.4f, " \
    "diameter2 = %10.4f, " \
    "depth = %10.4f)\n" \
    % (segments, b, 0.01, h)
    outstr += "bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0, %10.4f))\n" % (l - h / 2)
    outstr += "mesh = bpy.data.meshes.new('%s.mesh%s')\n" % (structurename, conename)
    outstr += "bm.to_mesh(mesh)\n"
    outstr += "ob2 = bpy.data.objects.new('%s.%s', mesh)\n" % (structurename, conename)
    outstr += "ob2.data.transform(%s)\n" % (Mtheta)
    outstr += "ob2.data.transform(%s)\n" % (Mphi)
    outstr += "ob2.location = (%10.4f, %10.4f, %10.4f)\n" % (x1, y1, z1)
    outstr += "bpy.context.scene.objects.link(ob2)\n"
    return outstr
