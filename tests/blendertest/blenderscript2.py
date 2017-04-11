import bpy
import bmesh

for ob in bpy.data.objects:
    if ob.name.startswith('structure'):
        ob.select = True
bpy.ops.object.delete()
for me in bpy.data.meshes:
    if me.name.startswith('structure'):
        bpy.data.meshes.remove(me)
for mat in bpy.data.materials:
    if mat.name.startswith('structure'):
        bpy.data.materials.remove(mat)
bpy.ops.object.select_all(action='DESELECT')
for object in bpy.data.objects:
    if object.type == 'LAMP':
        object.select = True
bpy.ops.object.delete()
bpy.data.worlds['World'].horizon_color = (1, 1, 1)
bpy.ops.object.lamp_add(type='POINT')
l = bpy.context.object
l.name = 'structure.Lamp1'
l.location = (5, -5, 10)
bpy.ops.object.lamp_add(type='HEMI')
l = bpy.context.object
l.name = 'structure.LampHemi'
l.location = (-10, -10, 10)
l.data.energy =     0.5000
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     4.7931)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     2.3966))
mesh = bpy.data.meshes.new('structure.meshXAxis_cylinder')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.XAxis_cylinder', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    1.0000,     0.0000,     0.0000,     0.0000], \
 [   -0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob1)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 24, diameter1 =     0.2000, diameter2 =     0.0100, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     5.0431))
mesh = bpy.data.meshes.new('structure.meshXAxis_cone')
bm.to_mesh(mesh)
ob2 = bpy.data.objects.new('structure.XAxis_cone', mesh)
ob2.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.data.transform([[    1.0000,     0.0000,     0.0000,     0.0000], \
 [   -0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob2)
bpy.ops.object.select_all(action='DESELECT')
ob1.select = True
ob2.select = True
bpy.context.scene.objects.active = ob1
bpy.ops.object.join()
mat = bpy.data.materials.new('structure.material.XAxis')
mat.diffuse_color = (0, 0, 0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     5.3384)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     2.6692))
mesh = bpy.data.meshes.new('structure.meshYAxis_cylinder')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.YAxis_cylinder', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.0000,     1.0000,     0.0000,     0.0000], \
 [   -1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob1)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 24, diameter1 =     0.2000, diameter2 =     0.0100, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     5.5884))
mesh = bpy.data.meshes.new('structure.meshYAxis_cone')
bm.to_mesh(mesh)
ob2 = bpy.data.objects.new('structure.YAxis_cone', mesh)
ob2.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.data.transform([[    0.0000,     1.0000,     0.0000,     0.0000], \
 [   -1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob2)
bpy.ops.object.select_all(action='DESELECT')
ob1.select = True
ob2.select = True
bpy.context.scene.objects.active = ob1
bpy.ops.object.join()
mat = bpy.data.materials.new('structure.material.YAxis')
mat.diffuse_color = (0, 0, 0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 6, diameter1 =     0.0500, diameter2 =     0.0500, depth =     6.9025)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     3.4512))
mesh = bpy.data.meshes.new('structure.meshZAxis_cylinder')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.ZAxis_cylinder', mesh)
ob1.data.transform([[    1.0000,     0.0000,    -0.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.7071,     0.7071,     0.0000,     0.0000], \
 [   -0.7071,     0.7071,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob1)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 24, diameter1 =     0.2000, diameter2 =     0.0100, depth =     0.5000)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     7.1525))
mesh = bpy.data.meshes.new('structure.meshZAxis_cone')
bm.to_mesh(mesh)
ob2 = bpy.data.objects.new('structure.ZAxis_cone', mesh)
ob2.data.transform([[    1.0000,     0.0000,    -0.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.data.transform([[    0.7071,     0.7071,     0.0000,     0.0000], \
 [   -0.7071,     0.7071,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob2.location = (    0.0000,     0.0000,     0.0000)
bpy.context.scene.objects.link(ob2)
bpy.ops.object.select_all(action='DESELECT')
ob1.select = True
ob2.select = True
bpy.context.scene.objects.active = ob1
bpy.ops.object.join()
mat = bpy.data.materials.new('structure.material.ZAxis')
mat.diffuse_color = (0, 0, 0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.delete(type='VERT')
bpy.ops.object.mode_set(mode='OBJECT')
posobject = bpy.context.object
posobject.name = 'structure.Positions'
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.292400, subdivisions=3)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.Mn'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.Mn')
mat.diffuse_color = (0.6118, 0.4784, 0.7804)
me.materials.append(mat)
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.200000, subdivisions=3)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.O'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.O')
mat.diffuse_color = (1.0, 0.051, 0.051)
me.materials.append(mat)
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.402100, subdivisions=3)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.Tb'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.Tb')
mat.diffuse_color = (0.1882, 1.0, 0.7804)
me.materials.append(mat)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 0.000000, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom001(Mn1_3r_1l)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 0.000000, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 5.838400, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom002(Mn1_3r_3rf)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 5.838400, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.293140, 2.919200, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom003(Mn1_3r_2r)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.293140, 2.919200, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.097142, 0.194419, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom004(O1_1l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-2.097142, 0.194419, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.557116, 3.400284, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom005(Tb1_3l)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (-2.557116, 3.400284, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 5.838400, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom006(Mn1_3r_1rf)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 5.838400, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.195998, 6.032819, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom007(O1_1f)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.195998, 6.032819, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.372411, 1.014714, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom008(O2_6l_7r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.372411, 1.014714, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.743712, 3.113619, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom009(O1_2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.743712, 3.113619, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.195998, 0.194419, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom010(O1_1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.195998, 0.194419, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.557116, 2.438116, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom011(Tb1_5)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (2.557116, 2.438116, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.842568, 2.724781, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom012(O1r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (5.842568, 2.724781, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.567299, 3.933914, 4.078777)
ob = bpy.data.objects.new(             'structure.Atom013(O2_6l_4)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.567299, 3.933914, 4.078777)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.390282, -0.194419, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom014(O1_3rb)', bpy.data.meshes['structure.mesh.O'])
ob.location = (7.390282, -0.194419, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.567299, 1.904486, 0.377527)
ob = bpy.data.objects.new(             'structure.Atom015(O2_6l_6l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.567299, 1.904486, 0.377527)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-0.549428, 3.113619, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom016(O1_2l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-0.549428, 3.113619, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.725841, 1.904486, 0.377527)
ob = bpy.data.objects.new(             'structure.Atom017(O2_6l_6)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.725841, 1.904486, 0.377527)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom018(Mn1_3r_3r)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 2.919200, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom019(Mn1_3r_2u)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 2.919200, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.725841, 1.904486, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom020(O2_6l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.725841, 1.904486, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.079271, 4.823686, 0.377527)
ob = bpy.data.objects.new(             'structure.Atom021(O2_6l_3l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.079271, 4.823686, 0.377527)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 5.838400, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom022(Mn1_3r_3rfu)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 5.838400, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.293140, 2.919200, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom023(Mn1_3r_2ru)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.293140, 2.919200, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.736024, 3.400284, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom024(Tb1_3)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (2.736024, 3.400284, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.097142, -0.194419, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom025(O1_3b)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.097142, -0.194419, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 0.000000, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom026(Mn1_3r_3u)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 0.000000, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.293140, 2.919200, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom027(Mn1_3rr)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (5.293140, 2.919200, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 5.838400, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom028(Mn1_3r_3lfu)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 5.838400, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 0.000000, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom029(Mn1_3r_3ru)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 0.000000, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 5.838400, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom030(Mn1_3r_3lf)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 5.838400, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.203686, 0.481084, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom031(Tb1_4)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (5.203686, 0.481084, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.213869, 4.823686, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom032(O2_6l_5)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.213869, 4.823686, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.089454, 5.357316, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom033(Tb1_2)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (0.089454, 5.357316, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.567299, 3.933914, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom034(O2_6l_2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.567299, 3.933914, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.372411, 1.014714, 4.078777)
ob = bpy.data.objects.new(             'structure.Atom035(O2_6l_1r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.372411, 1.014714, 4.078777)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 5.838400, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom036(Mn1_3r_3f)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 5.838400, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom037(Mn1_3r_3l)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.213869, 4.823686, 0.377527)
ob = bpy.data.objects.new(             'structure.Atom038(O2_6l_3)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.213869, 4.823686, 0.377527)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom039(Mn1_3r_3)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.390282, 5.643981, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom040(O1_3r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (7.390282, 5.643981, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 5.838400, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom041(Mn1_3r_3fu)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 5.838400, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.549428, 2.724781, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom042(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (0.549428, 2.724781, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 0.000000, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom043(Mn1_3r_1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 0.000000, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.079271, 4.823686, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom044(O2_6l_5l)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.079271, 4.823686, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.850256, 2.438116, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom045(Tb1_5r)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (7.850256, 2.438116, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.382594, 5.357316, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom046(Tb1_2r)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (5.382594, 5.357316, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (7.939710, 0.000000, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom047(Mn1_3r_1r)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (7.939710, 0.000000, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.097142, 5.643981, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom048(O1_3)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.097142, 5.643981, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 2.919200, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom049(Mn1_3r_2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 2.919200, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 5.838400, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom050(Mn1_3r_1lf)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 5.838400, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.079271, 1.014714, 4.078777)
ob = bpy.data.objects.new(             'structure.Atom051(O2_6l_1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.079271, 1.014714, 4.078777)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.646570, 0.000000, 7.402500)
ob = bpy.data.objects.new(             'structure.Atom052(Mn1_3r_3lu)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (-2.646570, 0.000000, 7.402500)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-2.097142, 6.032819, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom053(O1_1lf)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-2.097142, 6.032819, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.860439, 3.933914, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom054(O2_6l_2r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.860439, 3.933914, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (6.860439, 3.933914, 4.078777)
ob = bpy.data.objects.new(             'structure.Atom055(O2_6l_4r)', bpy.data.meshes['structure.mesh.O'])
ob.location = (6.860439, 3.933914, 4.078777)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-1.567299, 1.904486, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom056(O2_6ll)', bpy.data.meshes['structure.mesh.O'])
ob.location = (-1.567299, 1.904486, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.079271, 1.014714, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom057(O2_6l_7)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.079271, 1.014714, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (-0.089454, 0.481084, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom058(Tb1_4l)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (-0.089454, 0.481084, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 2.919200, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom059(Mn1_3r)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 2.919200, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 5.838400, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom060(Mn1_3r_1f)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 5.838400, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond001')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond001', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond001')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond002')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond002', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond002')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond003')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond003', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond003')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond004')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond004', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond004')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond005')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond005', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond005')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond006')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond006', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond006')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond007')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond007', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond007')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond008')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond008', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond008')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond009')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond009', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond009')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond010')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond010', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond010')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond011')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond011', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond011')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond012')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond012', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond012')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond013')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond013', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond013')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond014')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond014', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond014')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond015')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond015', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond015')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond016')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond016', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond016')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond017')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond017', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond017')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond018')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond018', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond018')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond019')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond019', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond019')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond020')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond020', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond020')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond021')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond021', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond021')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond022')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond022', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond022')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond023')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond023', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond023')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond024')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond024', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond024')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond025')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond025', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond025')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond026')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond026', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond026')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond027')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond027', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond027')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond028')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond028', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond028')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond029')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond029', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond029')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond030')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond030', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond030')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond031')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond031', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond031')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond032')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond032', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond032')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond033')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond033', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond033')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond034')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond034', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond034')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond035')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond035', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond035')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond036')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond036', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond036')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond037')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond037', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond037')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond038')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond038', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond038')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond039')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond039', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond039')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond040')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond040', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond040')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond041')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond041', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond041')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond042')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond042', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond042')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond043')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond043', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond043')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond044')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond044', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond044')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond045')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond045', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond045')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond046')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond046', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond046')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond047')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond047', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond047')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond048')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond048', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond048')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond049')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond049', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond049')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond050')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond050', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond050')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond051')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond051', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond051')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond052')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond052', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond052')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond053')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond053', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond053')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond054')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond054', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond054')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond055')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond055', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond055')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond056')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond056', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond056')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond057')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond057', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond057')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond058')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond058', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond058')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond059')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond059', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond059')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond060')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond060', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond060')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond061')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond061', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond061')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond062')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond062', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond062')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond063')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond063', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond063')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond064')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond064', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond064')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond065')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond065', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond065')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond066')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond066', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond066')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond067')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond067', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond067')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond068')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond068', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond068')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond069')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond069', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond069')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond070')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond070', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond070')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond071')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond071', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond071')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond072')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond072', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond072')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond073')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond073', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond073')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond074')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond074', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond074')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond075')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond075', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond075')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond076')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond076', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond076')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond077')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond077', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond077')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond078')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond078', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond078')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond079')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond079', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond079')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond080')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond080', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond080')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond081')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond081', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond081')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond082')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond082', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond082')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond083')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond083', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond083')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond084')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond084', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond084')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond085')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond085', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond085')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond086')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond086', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond086')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond087')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond087', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond087')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond088')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond088', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond088')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond089')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond089', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond089')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond090')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond090', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond090')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond091')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond091', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond091')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond092')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond092', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond092')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond093')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond093', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond093')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond094')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond094', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond094')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond095')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond095', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond095')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond096')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond096', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond096')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond097')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond097', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond097')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond098')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond098', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond098')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond099')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond099', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond099')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond100')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond100', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond100')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond101')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond101', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond101')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond102')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond102', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond102')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond103')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond103', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond103')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond104')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond104', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond104')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond105')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond105', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond105')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond106')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond106', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond106')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond107')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond107', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond107')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond108')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond108', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond108')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond109')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond109', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond109')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond110')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond110', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond110')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond111')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond111', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond111')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond112')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond112', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond112')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond113')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond113', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond113')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond114')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond114', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond114')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond115')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond115', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond115')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond116')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond116', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond116')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond117')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond117', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond117')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond118')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond118', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond118')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond119')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond119', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond119')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond120')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond120', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond120')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond121')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond121', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond121')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond122')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond122', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond122')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond123')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond123', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond123')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond124')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond124', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond124')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond125')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond125', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond125')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond126')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond126', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond126')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond127')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond127', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond127')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond128')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond128', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond128')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond129')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond129', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond129')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond130')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond130', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond130')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond131')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond131', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond131')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond132')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond132', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond132')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond133')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond133', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond133')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond134')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond134', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond134')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond135')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond135', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond135')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond136')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond136', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond136')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond137')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond137', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond137')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond138')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond138', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond138')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond139')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond139', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond139')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond140')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond140', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond140')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond141')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond141', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond141')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond142')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond142', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond142')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond143')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond143', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond143')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond144')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond144', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond144')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond145')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond145', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond145')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond146')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond146', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond146')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond147')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond147', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond147')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond148')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond148', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond148')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond149')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond149', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond149')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond150')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond150', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond150')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond151')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond151', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond151')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond152')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond152', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond152')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond153')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond153', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond153')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond154')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond154', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond154')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond155')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond155', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond155')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond156')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond156', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond156')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond157')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond157', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond157')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond158')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond158', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond158')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond159')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond159', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond159')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond160')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond160', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond160')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond161')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond161', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond161')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond162')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond162', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond162')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond163')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond163', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond163')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond164')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond164', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond164')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond165')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond165', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond165')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond166')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond166', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond166')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond167')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond167', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond167')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond168')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond168', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond168')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond169')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond169', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond169')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond170')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond170', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond170')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond171')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond171', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond171')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond172')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond172', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond172')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond173')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond173', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond173')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond174')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond174', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond174')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond175')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond175', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond175')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond176')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond176', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond176')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond177')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond177', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond177')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond178')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond178', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond178')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond179')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond179', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond179')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond180')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond180', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond180')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond181')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond181', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond181')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond182')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond182', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond182')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond183')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond183', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond183')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond184')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond184', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond184')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond185')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond185', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond185')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond186')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond186', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond186')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond187')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond187', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond187')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond188')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond188', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond188')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond189')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond189', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond189')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond190')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond190', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond190')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond191')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond191', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond191')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond192')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond192', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond192')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond193')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond193', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond193')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond194')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond194', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond194')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond195')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond195', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond195')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond196')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond196', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond196')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond197')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond197', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond197')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond198')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond198', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond198')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond199')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond199', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond199')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond200')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond200', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond200')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond201')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond201', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond201')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond202')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond202', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond202')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond203')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond203', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond203')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond204')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond204', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond204')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond205')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond205', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond205')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond206')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond206', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond206')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond207')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond207', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond207')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond208')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond208', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond208')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond209')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond209', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond209')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond210')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond210', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond210')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond211')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond211', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond211')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond212')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond212', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond212')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond213')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond213', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond213')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond214')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond214', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond214')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond215')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond215', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond215')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond216')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond216', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond216')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond217')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond217', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond217')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond218')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond218', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond218')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond219')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond219', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond219')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond220')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond220', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond220')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond221')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond221', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond221')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond222')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond222', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond222')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond223')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond223', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond223')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond224')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond224', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond224')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond225')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond225', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond225')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond226')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond226', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond226')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond227')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond227', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond227')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond228')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond228', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond228')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond229')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond229', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond229')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond230')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond230', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond230')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond231')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond231', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond231')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond232')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond232', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond232')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond233')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond233', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond233')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond234')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond234', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond234')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond235')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond235', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond235')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond236')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond236', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond236')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond237')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond237', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond237')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond238')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond238', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond238')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond239')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond239', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond239')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond240')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond240', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond240')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond241')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond241', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond241')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond242')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond242', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond242')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond243')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond243', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond243')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond244')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond244', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond244')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond245')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond245', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond245')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond246')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond246', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond246')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond247')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond247', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond247')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond248')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond248', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond248')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond249')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond249', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond249')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond250')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond250', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond250')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond251')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond251', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond251')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond252')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond252', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond252')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond253')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond253', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond253')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond254')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond254', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond254')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond255')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond255', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond255')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond256')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond256', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond256')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond257')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond257', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond257')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond258')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond258', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond258')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond259')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond259', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond259')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond260')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond260', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond260')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond261')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond261', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond261')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond262')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond262', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond262')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond263')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond263', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond263')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond264')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond264', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond264')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond265')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond265', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond265')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond266')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond266', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond266')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond267')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond267', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond267')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond268')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond268', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond268')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond269')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond269', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond269')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond270')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond270', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond270')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond271')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond271', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond271')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond272')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond272', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond272')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond273')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond273', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond273')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond274')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond274', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond274')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond275')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond275', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond275')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond276')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond276', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond276')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond277')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond277', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond277')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond278')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond278', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond278')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond279')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond279', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond279')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond280')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond280', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond280')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond281')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond281', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond281')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond282')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond282', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond282')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond283')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond283', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond283')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond284')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond284', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond284')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond285')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond285', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond285')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond286')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond286', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond286')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond287')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond287', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond287')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond288')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond288', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond288')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond289')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond289', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond289')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond290')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond290', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond290')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond291')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond291', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond291')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond292')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond292', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond292')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond293')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond293', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond293')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond294')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond294', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond294')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond295')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond295', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond295')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond296')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond296', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond296')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond297')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond297', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond297')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond298')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond298', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond298')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond299')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond299', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond299')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond300')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond300', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond300')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond301')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond301', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond301')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond302')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond302', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond302')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond303')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond303', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond303')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond304')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond304', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond304')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond305')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond305', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond305')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond306')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond306', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond306')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond307')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond307', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond307')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond308')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond308', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond308')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond309')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond309', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond309')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond310')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond310', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond310')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond311')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond311', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond311')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond312')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond312', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond312')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond313')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond313', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond313')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond314')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond314', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond314')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond315')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond315', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond315')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond316')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond316', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond316')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond317')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond317', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond317')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond318')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond318', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond318')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond319')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond319', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond319')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond320')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond320', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond320')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond321')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond321', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond321')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond322')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond322', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond322')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond323')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond323', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond323')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond324')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond324', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond324')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond325')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond325', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond325')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond326')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond326', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond326')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond327')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond327', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond327')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond328')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond328', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond328')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond329')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond329', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond329')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond330')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond330', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond330')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond331')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond331', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond331')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond332')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond332', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond332')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond333')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond333', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond333')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond334')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond334', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond334')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond335')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond335', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond335')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond336')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond336', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond336')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond337')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond337', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond337')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond338')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond338', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond338')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond339')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond339', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond339')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond340')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond340', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond340')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond341')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond341', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond341')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond342')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond342', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond342')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond343')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond343', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond343')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond344')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond344', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond344')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond345')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond345', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond345')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond346')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond346', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond346')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond347')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond347', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond347')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond348')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond348', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond348')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond349')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond349', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond349')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond350')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond350', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond350')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond351')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond351', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond351')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond352')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond352', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond352')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond353')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond353', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond353')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond354')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond354', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond354')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond355')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond355', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond355')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond356')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond356', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond356')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond357')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond357', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond357')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond358')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond358', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond358')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond359')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond359', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond359')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond360')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond360', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond360')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond361')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond361', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond361')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond362')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond362', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond362')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond363')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond363', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond363')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond364')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond364', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond364')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond365')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond365', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond365')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond366')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond366', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond366')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond367')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond367', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond367')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond368')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond368', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond368')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond369')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond369', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond369')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond370')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond370', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond370')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond371')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond371', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond371')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond372')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond372', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond372')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond373')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond373', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond373')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond374')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond374', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond374')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond375')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond375', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond375')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond376')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond376', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond376')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond377')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond377', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond377')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond378')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond378', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond378')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond379')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond379', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond379')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond380')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond380', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond380')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond381')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond381', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond381')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond382')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond382', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond382')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond383')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond383', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond383')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond384')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond384', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond384')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond385')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond385', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond385')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond386')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond386', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond386')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond387')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond387', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond387')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond388')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond388', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond388')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond389')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond389', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond389')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond390')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond390', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond390')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond391')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond391', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond391')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond392')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond392', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond392')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond393')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond393', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond393')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond394')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond394', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond394')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond395')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond395', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond395')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond396')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond396', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond396')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond397')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond397', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond397')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond398')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond398', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond398')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond399')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond399', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond399')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond400')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond400', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond400')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond401')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond401', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond401')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond402')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond402', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond402')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond403')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond403', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond403')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond404')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond404', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond404')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond405')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond405', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond405')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond406')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond406', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond406')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond407')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond407', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond407')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond408')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond408', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond408')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond409')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond409', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond409')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond410')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond410', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond410')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond411')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond411', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond411')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond412')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond412', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond412')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond413')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond413', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond413')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond414')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond414', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond414')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond415')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond415', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond415')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond416')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond416', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond416')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond417')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond417', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond417')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond418')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond418', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond418')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond419')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond419', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond419')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond420')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond420', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond420')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond421')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond421', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond421')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond422')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond422', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond422')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond423')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond423', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond423')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond424')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond424', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond424')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond425')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond425', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond425')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond426')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond426', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond426')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond427')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond427', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond427')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond428')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond428', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond428')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond429')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond429', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond429')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond430')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond430', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond430')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond431')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond431', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond431')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond432')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond432', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond432')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond433')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond433', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond433')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond434')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond434', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond434')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond435')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond435', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond435')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond436')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond436', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond436')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond437')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond437', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond437')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond438')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond438', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond438')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond439')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond439', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond439')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond440')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond440', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond440')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond441')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond441', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond441')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond442')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond442', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond442')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond443')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond443', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond443')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond444')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond444', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond444')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond445')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond445', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond445')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond446')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond446', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond446')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond447')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond447', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond447')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond448')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond448', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond448')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond449')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond449', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond449')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond450')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond450', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond450')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond451')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond451', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond451')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond452')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond452', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond452')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond453')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond453', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond453')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond454')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond454', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond454')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond455')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond455', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond455')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond456')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond456', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond456')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond457')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond457', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond457')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond458')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond458', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond458')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond459')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond459', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond459')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond460')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond460', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond460')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond461')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond461', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond461')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond462')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond462', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond462')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond463')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond463', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond463')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond464')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond464', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond464')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond465')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond465', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond465')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond466')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond466', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond466')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond467')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond467', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond467')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond468')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond468', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond468')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond469')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond469', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond469')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond470')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond470', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond470')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond471')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond471', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond471')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond472')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond472', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond472')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond473')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond473', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond473')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond474')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond474', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond474')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond475')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond475', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond475')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond476')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond476', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond476')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond477')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond477', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond477')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond478')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond478', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond478')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond479')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond479', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond479')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond480')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond480', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond480')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond481')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond481', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond481')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond482')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond482', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond482')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond483')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond483', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond483')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond484')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond484', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond484')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond485')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond485', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond485')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond486')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond486', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -0.5494,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond486')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond487')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond487', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond487')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond488')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond488', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond488')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond489')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond489', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond489')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond490')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond490', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond490')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond491')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond491', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     7.7429,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond491')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond492')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond492', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond492')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond493')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond493', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond493')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond494')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond494', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond494')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond495')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond495', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond495')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond496')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond496', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond496')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond497')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond497', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond497')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond498')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond498', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond498')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond499')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond499', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -4.2139,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond499')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond500')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond500', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond500')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond501')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond501', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond501')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond502')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond502', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond502')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond503')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond503', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond503')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond504')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond504', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     1.9045,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond504')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond505')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond505', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond505')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond506')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond506', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     7.7429,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond506')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond507')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond507', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond507')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond508')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond508', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond508')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond509')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond509', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond509')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond510')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond510', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond510')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond511')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond511', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond511')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond512')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond512', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond512')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond513')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond513', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond513')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond514')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond514', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond514')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond515')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond515', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond515')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond516')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond516', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,     4.8237,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond516')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond517')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond517', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.1960,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond517')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond518')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond518', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond518')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond519')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond519', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond519')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond520')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond520', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond520')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond521')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond521', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond521')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond522')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond522', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond522')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond523')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond523', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond523')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond524')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond524', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond524')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond525')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond525', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond525')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond526')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond526', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond526')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond527')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond527', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.8604,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond527')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond528')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond528', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond528')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond529')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond529', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond529')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond530')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond530', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond530')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond531')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond531', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -3.7258,    -1.9045,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond531')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond532')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond532', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond532')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond533')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond533', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond533')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond534')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond534', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond534')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond535')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond535', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond535')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond536')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond536', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond536')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond537')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond537', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond537')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond538')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond538', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond538')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond539')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond539', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond539')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond540')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond540', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond540')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond541')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond541', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    2.0971,    -0.1944,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond541')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond542')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond542', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond542')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond543')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond543', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.0793,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond543')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond544')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond544', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond544')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond545')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond545', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.0190,     7.7429,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond545')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond546')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond546', mesh)
ob1.data.transform([[   -0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,    -0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6131,     0.7900,     0.0000,     0.0000], \
 [   -0.7900,     0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond546')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond547')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond547', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.0793,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond547')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond548')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond548', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond548')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond549')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond549', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond549')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond550')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond550', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond550')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond551')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond551', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,    -0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond551')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond552')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond552', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond552')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond553')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond553', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,    -0.9863,     0.0000,     0.0000], \
 [    0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond553')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond554')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond554', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.2139,     4.8237,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond554')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond555')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond555', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     3.3237)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond555')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond556')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond556', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond556')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond557')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond557', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    4.7437,     3.1136,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond557')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond558')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond558', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond558')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond559')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond559', mesh)
ob1.data.transform([[   -0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,    -0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9479,    -0.3187,     0.0000,     0.0000], \
 [    0.3187,    -0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond559')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond560')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond560', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    0.5494,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond560')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond561')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond561', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -1.5673,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond561')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond562')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond562', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    8.4891,     6.0328,    -1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond562')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond563')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond563', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond563')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond564')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond564', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond564')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.9597)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4799))
mesh = bpy.data.meshes.new('structure.meshBond565')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond565', mesh)
ob1.data.transform([[    0.0000,     0.0000,    -1.0000,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    1.0000,     0.0000,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.1649,     0.9863,     0.0000,     0.0000], \
 [   -0.9863,     0.1649,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.7258,     1.9045,     7.7800)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond565')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond566')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond566', mesh)
ob1.data.transform([[   -0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,    -0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.2960,    -0.9552,     0.0000,     0.0000], \
 [    0.9552,     0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    5.8426,     2.7248,     9.2531)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond566')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8583)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4291))
mesh = bpy.data.meshes.new('structure.meshBond567')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond567', mesh)
ob1.data.transform([[    0.7795,     0.0000,    -0.6263,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.6263,     0.0000,     0.7795,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.2960,     0.9552,     0.0000,     0.0000], \
 [   -0.9552,    -0.2960,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     1.0147,     7.0250)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond567')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond568')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond568', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,     0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,    -0.1944,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond568')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond569')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond569', mesh)
ob1.data.transform([[    0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,     0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,     0.3613,     0.0000,     0.0000], \
 [   -0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    9.5070,    -1.0147,     0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond569')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond570')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond570', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond570')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.8924)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.4462))
mesh = bpy.data.meshes.new('structure.meshBond571')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond571', mesh)
ob1.data.transform([[    0.2610,     0.0000,    -0.9653,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.9653,     0.0000,     0.2610,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.9479,     0.3187,     0.0000,     0.0000], \
 [   -0.3187,     0.9479,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond571')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond572')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond572', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    6.3724,     6.8531,     4.0788)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond572')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond573')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond573', mesh)
ob1.data.transform([[    0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,     0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6440,     0.7650,     0.0000,     0.0000], \
 [   -0.7650,    -0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    7.3903,     5.6440,     1.8506)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond573')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7062)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3531))
mesh = bpy.data.meshes.new('structure.meshBond574')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond574', mesh)
ob1.data.transform([[   -0.5443,     0.0000,    -0.8389,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8389,     0.0000,    -0.5443,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.9324,    -0.3613,     0.0000,     0.0000], \
 [    0.3613,    -0.9324,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    1.5673,     3.9339,    -0.3775)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond574')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     2.7318)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.3659))
mesh = bpy.data.meshes.new('structure.meshBond575')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond575', mesh)
ob1.data.transform([[   -0.8156,     0.0000,    -0.5786,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.5786,     0.0000,    -0.8156,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[    0.6440,    -0.7650,     0.0000,     0.0000], \
 [    0.7650,     0.6440,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (   -2.0971,     6.0328,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond575')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
bm = bmesh.new()
bmesh.ops.create_cone(bm, cap_ends = True, cap_tris = True, segments = 32, diameter1 =     0.0500, diameter2 =     0.0500, depth =     3.0378)
bmesh.ops.translate(bm, verts=bm.verts, vec = (0, 0,     1.5189))
mesh = bpy.data.meshes.new('structure.meshBond576')
bm.to_mesh(mesh)
ob1 = bpy.data.objects.new('structure.Bond576', mesh)
ob1.data.transform([[    0.4849,     0.0000,    -0.8746,     0.0000], \
 [    0.0000,     1.0000,     0.0000,     0.0000], \
 [    0.8746,     0.0000,     0.4849,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.data.transform([[   -0.6131,    -0.7900,     0.0000,     0.0000], \
 [    0.7900,    -0.6131,     0.0000,     0.0000], \
 [    0.0000,     0.0000,     1.0000,     0.0000], \
 [    0.0000,     0.0000,     0.0000,     1.0000]])
ob1.location = (    3.1960,     0.1944,     5.5519)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Bond576')
mat.diffuse_color = (0.0, 0.0, 0.0)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace001')
mesh_data.from_pydata([(    6.8604,    -1.9045,     7.0250), (    9.5070,    -1.0147,     7.7800), (    8.4891,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face001', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face001')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace002')
mesh_data.from_pydata([(    1.0793,     6.8531,     7.0250), (    1.5673,     3.9339,     7.0250), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face002', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face002')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace003')
mesh_data.from_pydata([(    9.0190,     7.7429,     0.3775), (    6.3724,     6.8531,    -0.3775), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face003', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face003')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace004')
mesh_data.from_pydata([(    3.7258,     1.9045,     7.7800), (    1.0793,     1.0147,     7.0250), (    2.0971,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face004', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face004')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace005')
mesh_data.from_pydata([(    1.5673,     3.9339,    -0.3775), (    4.2139,     4.8237,     0.3775), (    3.1960,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face005', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face005')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace006')
mesh_data.from_pydata([(    6.8604,     3.9339,    -0.3775), (    9.5070,     4.8237,     0.3775), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face006', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face006')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace007')
mesh_data.from_pydata([(    6.8604,    -1.9045,     7.0250), (    9.5070,    -1.0147,     7.7800), (    7.3903,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face007', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face007')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace008')
mesh_data.from_pydata([(    1.5673,     3.9339,     7.0250), (    4.2139,     4.8237,     7.7800), (    2.0971,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face008', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face008')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace009')
mesh_data.from_pydata([(   -1.5673,     1.9045,     3.3237), (   -4.2139,     1.0147,     4.0788), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face009', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face009')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace010')
mesh_data.from_pydata([(    6.3724,     6.8531,    -0.3775), (    6.8604,     3.9339,    -0.3775), (    8.4891,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face010', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face010')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace011')
mesh_data.from_pydata([(   -1.5673,     1.9045,     7.7800), (   -4.2139,     1.0147,     7.0250), (   -3.1960,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face011', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face011')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace012')
mesh_data.from_pydata([(    9.0190,     7.7429,     7.7800), (    6.3724,     6.8531,     7.0250), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face012', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face012')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace013')
mesh_data.from_pydata([(   -1.0793,     4.8237,     7.7800), (   -1.5673,     7.7429,     7.7800), (   -3.1960,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face013', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face013')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace014')
mesh_data.from_pydata([(   -1.0793,     4.8237,     0.3775), (   -1.5673,     7.7429,     0.3775), (   -2.0971,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face014', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face014')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace015')
mesh_data.from_pydata([(   -3.7258,     3.9339,     4.0788), (   -1.0793,     4.8237,     3.3237), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face015', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face015')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace016')
mesh_data.from_pydata([(   -1.5673,     1.9045,     3.3237), (   -1.0793,     4.8237,     3.3237), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face016', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face016')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace017')
mesh_data.from_pydata([(   -3.7258,     3.9339,     7.0250), (   -1.0793,     4.8237,     7.7800), (   -3.1960,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face017', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face017')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace018')
mesh_data.from_pydata([(   -4.2139,     1.0147,     4.0788), (   -3.7258,    -1.9045,     4.0788), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face018', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face018')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace019')
mesh_data.from_pydata([(    6.8604,     3.9339,    -0.3775), (    6.3724,     1.0147,    -0.3775), (    5.8426,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face019', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face019')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace020')
mesh_data.from_pydata([(    1.5673,     3.9339,     4.0788), (    1.0793,     1.0147,     4.0788), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face020', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face020')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace021')
mesh_data.from_pydata([(    6.8604,     3.9339,     4.0788), (    9.5070,     4.8237,     3.3237), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face021', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face021')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace022')
mesh_data.from_pydata([(    1.5673,     3.9339,     4.0788), (    1.0793,     1.0147,     4.0788), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face022', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face022')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace023')
mesh_data.from_pydata([(    4.2139,    -1.0147,     7.7800), (    3.7258,     1.9045,     7.7800), (    2.0971,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face023', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face023')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace024')
mesh_data.from_pydata([(    4.2139,     4.8237,     3.3237), (    6.8604,     3.9339,     4.0788), (    5.8426,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face024', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face024')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace025')
mesh_data.from_pydata([(    4.2139,    -1.0147,     0.3775), (    3.7258,     1.9045,     0.3775), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face025', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face025')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace026')
mesh_data.from_pydata([(    1.0793,     6.8531,     4.0788), (    1.5673,     3.9339,     4.0788), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face026', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face026')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace027')
mesh_data.from_pydata([(   -1.5673,     1.9045,     7.7800), (   -4.2139,     1.0147,     7.0250), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face027', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face027')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace028')
mesh_data.from_pydata([(    3.7258,     1.9045,     0.3775), (    1.0793,     1.0147,    -0.3775), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face028', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face028')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace029')
mesh_data.from_pydata([(    1.0793,     1.0147,     4.0788), (   -1.5673,     1.9045,     3.3237), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face029', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face029')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace030')
mesh_data.from_pydata([(    9.5070,    -1.0147,     3.3237), (    9.0190,     1.9045,     3.3237), (    8.4891,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face030', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face030')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace031')
mesh_data.from_pydata([(   -3.7258,    -1.9045,     7.0250), (   -1.0793,    -1.0147,     7.7800), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face031', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face031')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace032')
mesh_data.from_pydata([(    1.0793,     6.8531,    -0.3775), (    1.5673,     3.9339,    -0.3775), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face032', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face032')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace033')
mesh_data.from_pydata([(    1.0793,     1.0147,     4.0788), (   -1.5673,     1.9045,     3.3237), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face033', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face033')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace034')
mesh_data.from_pydata([(   -1.5673,     1.9045,     0.3775), (   -4.2139,     1.0147,    -0.3775), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face034', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face034')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace035')
mesh_data.from_pydata([(    1.5673,    -1.9045,     7.0250), (    4.2139,    -1.0147,     7.7800), (    2.0971,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face035', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face035')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace036')
mesh_data.from_pydata([(    6.3724,     6.8531,     4.0788), (    6.8604,     3.9339,     4.0788), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face036', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face036')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace037')
mesh_data.from_pydata([(    4.2139,     4.8237,     0.3775), (    6.8604,     3.9339,    -0.3775), (    4.7437,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face037', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face037')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace038')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     3.3237), (   -1.5673,     1.9045,     3.3237), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face038', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face038')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace039')
mesh_data.from_pydata([(    6.3724,     6.8531,     7.0250), (    6.8604,     3.9339,     7.0250), (    7.3903,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face039', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face039')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace040')
mesh_data.from_pydata([(    3.7258,     1.9045,     7.7800), (    4.2139,     4.8237,     7.7800), (    5.8426,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face040', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face040')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace041')
mesh_data.from_pydata([(    4.2139,    -1.0147,     0.3775), (    3.7258,     1.9045,     0.3775), (    3.1960,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face041', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face041')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace042')
mesh_data.from_pydata([(    4.2139,     4.8237,     3.3237), (    3.7258,     7.7429,     3.3237), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face042', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face042')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace043')
mesh_data.from_pydata([(   -3.7258,     3.9339,    -0.3775), (   -1.0793,     4.8237,     0.3775), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face043', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face043')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace044')
mesh_data.from_pydata([(    4.2139,     4.8237,     3.3237), (    6.8604,     3.9339,     4.0788), (    4.7437,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face044', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face044')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace045')
mesh_data.from_pydata([(   -1.0793,     4.8237,     7.7800), (    1.5673,     3.9339,     7.0250), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face045', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face045')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace046')
mesh_data.from_pydata([(    6.3724,     1.0147,     4.0788), (    6.8604,    -1.9045,     4.0788), (    8.4891,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face046', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face046')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace047')
mesh_data.from_pydata([(   -1.5673,     1.9045,     3.3237), (   -4.2139,     1.0147,     4.0788), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face047', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face047')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace048')
mesh_data.from_pydata([(   -1.0793,     4.8237,     3.3237), (   -1.5673,     7.7429,     3.3237), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face048', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face048')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace049')
mesh_data.from_pydata([(   -1.5673,     1.9045,     7.7800), (   -1.0793,     4.8237,     7.7800), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face049', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face049')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace050')
mesh_data.from_pydata([(    6.8604,    -1.9045,    -0.3775), (    9.5070,    -1.0147,     0.3775), (    7.3903,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face050', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face050')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace051')
mesh_data.from_pydata([(    9.0190,     7.7429,     3.3237), (    6.3724,     6.8531,     4.0788), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face051', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face051')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace052')
mesh_data.from_pydata([(   -3.7258,     3.9339,     7.0250), (   -1.0793,     4.8237,     7.7800), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face052', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face052')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace053')
mesh_data.from_pydata([(    9.5070,    -1.0147,     0.3775), (    9.0190,     1.9045,     0.3775), (    8.4891,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face053', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face053')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace054')
mesh_data.from_pydata([(    1.5673,     3.9339,    -0.3775), (    1.0793,     1.0147,    -0.3775), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face054', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face054')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace055')
mesh_data.from_pydata([(    9.5070,     4.8237,     0.3775), (    9.0190,     7.7429,     0.3775), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face055', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face055')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace056')
mesh_data.from_pydata([(    9.5070,     4.8237,     7.7800), (    9.0190,     7.7429,     7.7800), (    7.3903,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face056', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face056')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace057')
mesh_data.from_pydata([(    6.3724,     1.0147,     7.0250), (    3.7258,     1.9045,     7.7800), (    4.7437,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face057', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face057')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace058')
mesh_data.from_pydata([(    6.3724,     6.8531,     4.0788), (    6.8604,     3.9339,     4.0788), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face058', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face058')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace059')
mesh_data.from_pydata([(    9.5070,    -1.0147,     0.3775), (    9.0190,     1.9045,     0.3775), (    7.3903,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face059', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face059')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace060')
mesh_data.from_pydata([(    3.7258,     1.9045,     7.7800), (    4.2139,     4.8237,     7.7800), (    4.7437,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face060', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face060')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace061')
mesh_data.from_pydata([(    6.8604,     3.9339,     7.0250), (    6.3724,     1.0147,     7.0250), (    4.7437,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face061', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face061')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace062')
mesh_data.from_pydata([(    9.5070,    -1.0147,     7.7800), (    9.0190,     1.9045,     7.7800), (    8.4891,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face062', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face062')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace063')
mesh_data.from_pydata([(    4.2139,     4.8237,     7.7800), (    6.8604,     3.9339,     7.0250), (    4.7437,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face063', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face063')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace064')
mesh_data.from_pydata([(    4.2139,    -1.0147,     7.7800), (    3.7258,     1.9045,     7.7800), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face064', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face064')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace065')
mesh_data.from_pydata([(    9.5070,     4.8237,     3.3237), (    9.0190,     7.7429,     3.3237), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face065', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face065')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace066')
mesh_data.from_pydata([(    9.5070,     4.8237,     3.3237), (    9.0190,     7.7429,     3.3237), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face066', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face066')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace067')
mesh_data.from_pydata([(    9.0190,     1.9045,     0.3775), (    6.3724,     1.0147,    -0.3775), (    8.4891,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face067', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face067')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace068')
mesh_data.from_pydata([(    6.8604,     3.9339,     7.0250), (    9.5070,     4.8237,     7.7800), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face068', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face068')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace069')
mesh_data.from_pydata([(   -3.7258,     3.9339,    -0.3775), (   -1.0793,     4.8237,     0.3775), (   -2.0971,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face069', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face069')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace070')
mesh_data.from_pydata([(    6.8604,     3.9339,    -0.3775), (    6.3724,     1.0147,    -0.3775), (    4.7437,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face070', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face070')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace071')
mesh_data.from_pydata([(    3.7258,     1.9045,     0.3775), (    1.0793,     1.0147,    -0.3775), (    3.1960,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face071', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face071')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace072')
mesh_data.from_pydata([(   -4.2139,     6.8531,     4.0788), (   -3.7258,     3.9339,     4.0788), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face072', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face072')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace073')
mesh_data.from_pydata([(   -4.2139,     6.8531,     7.0250), (   -3.7258,     3.9339,     7.0250), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face073', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face073')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace074')
mesh_data.from_pydata([(   -1.5673,     1.9045,     3.3237), (   -1.0793,     4.8237,     3.3237), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face074', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face074')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace075')
mesh_data.from_pydata([(   -1.5673,     1.9045,     7.7800), (   -1.0793,     4.8237,     7.7800), (    0.5494,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face075', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face075')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace076')
mesh_data.from_pydata([(   -3.7258,    -1.9045,    -0.3775), (   -1.0793,    -1.0147,     0.3775), (   -2.0971,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face076', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face076')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace077')
mesh_data.from_pydata([(    3.7258,     7.7429,     3.3237), (    1.0793,     6.8531,     4.0788), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face077', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face077')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace078')
mesh_data.from_pydata([(    9.0190,     7.7429,     3.3237), (    6.3724,     6.8531,     4.0788), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face078', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face078')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace079')
mesh_data.from_pydata([(    9.5070,    -1.0147,     3.3237), (    9.0190,     1.9045,     3.3237), (    7.3903,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face079', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face079')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace080')
mesh_data.from_pydata([(   -1.0793,     4.8237,     7.7800), (   -1.5673,     7.7429,     7.7800), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face080', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face080')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace081')
mesh_data.from_pydata([(   -3.7258,    -1.9045,    -0.3775), (   -1.0793,    -1.0147,     0.3775), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face081', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face081')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace082')
mesh_data.from_pydata([(    1.0793,     1.0147,     7.0250), (   -1.5673,     1.9045,     7.7800), (    0.5494,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face082', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face082')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace083')
mesh_data.from_pydata([(    1.0793,     1.0147,     4.0788), (    1.5673,    -1.9045,     4.0788), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face083', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face083')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace084')
mesh_data.from_pydata([(    4.2139,     4.8237,     0.3775), (    3.7258,     7.7429,     0.3775), (    3.1960,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face084', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face084')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace085')
mesh_data.from_pydata([(   -3.7258,     3.9339,     4.0788), (   -1.0793,     4.8237,     3.3237), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face085', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face085')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace086')
mesh_data.from_pydata([(    3.7258,     1.9045,     0.3775), (    4.2139,     4.8237,     0.3775), (    5.8426,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face086', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face086')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace087')
mesh_data.from_pydata([(    1.0793,     1.0147,    -0.3775), (    1.5673,    -1.9045,    -0.3775), (    3.1960,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face087', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face087')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace088')
mesh_data.from_pydata([(    3.7258,     1.9045,     3.3237), (    1.0793,     1.0147,     4.0788), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face088', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face088')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace089')
mesh_data.from_pydata([(    1.5673,    -1.9045,    -0.3775), (    4.2139,    -1.0147,     0.3775), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face089', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face089')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace090')
mesh_data.from_pydata([(   -1.5673,     1.9045,     0.3775), (   -1.0793,     4.8237,     0.3775), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face090', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face090')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace091')
mesh_data.from_pydata([(    3.7258,     1.9045,     0.3775), (    4.2139,     4.8237,     0.3775), (    4.7437,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face091', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face091')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace092')
mesh_data.from_pydata([(    6.8604,    -1.9045,     4.0788), (    9.5070,    -1.0147,     3.3237), (    8.4891,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face092', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face092')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace093')
mesh_data.from_pydata([(    6.3724,     1.0147,    -0.3775), (    6.8604,    -1.9045,    -0.3775), (    8.4891,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face093', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face093')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace094')
mesh_data.from_pydata([(    9.0190,     7.7429,     0.3775), (    6.3724,     6.8531,    -0.3775), (    8.4891,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face094', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face094')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace095')
mesh_data.from_pydata([(    4.2139,     4.8237,     7.7800), (    3.7258,     7.7429,     7.7800), (    2.0971,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face095', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face095')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace096')
mesh_data.from_pydata([(    6.3724,     1.0147,     4.0788), (    3.7258,     1.9045,     3.3237), (    5.8426,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face096', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face096')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace097')
mesh_data.from_pydata([(    6.8604,     3.9339,     7.0250), (    9.5070,     4.8237,     7.7800), (    7.3903,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face097', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face097')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace098')
mesh_data.from_pydata([(    3.7258,     7.7429,     0.3775), (    1.0793,     6.8531,    -0.3775), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face098', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face098')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace099')
mesh_data.from_pydata([(   -3.7258,    -1.9045,     7.0250), (   -1.0793,    -1.0147,     7.7800), (   -3.1960,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face099', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face099')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace100')
mesh_data.from_pydata([(    3.7258,     1.9045,     3.3237), (    4.2139,     4.8237,     3.3237), (    4.7437,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face100', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face100')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace101')
mesh_data.from_pydata([(   -1.0793,     4.8237,     3.3237), (    1.5673,     3.9339,     4.0788), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face101', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face101')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace102')
mesh_data.from_pydata([(    6.8604,     3.9339,     4.0788), (    9.5070,     4.8237,     3.3237), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face102', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face102')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace103')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     7.7800), (   -1.5673,     1.9045,     7.7800), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face103', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face103')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace104')
mesh_data.from_pydata([(   -1.0793,     4.8237,     7.7800), (    1.5673,     3.9339,     7.0250), (    0.5494,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face104', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face104')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace105')
mesh_data.from_pydata([(    4.2139,     4.8237,     7.7800), (    6.8604,     3.9339,     7.0250), (    5.8426,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face105', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face105')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace106')
mesh_data.from_pydata([(    9.5070,     4.8237,     0.3775), (    9.0190,     7.7429,     0.3775), (    8.4891,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face106', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face106')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace107')
mesh_data.from_pydata([(    6.8604,     3.9339,     4.0788), (    6.3724,     1.0147,     4.0788), (    4.7437,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face107', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face107')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace108')
mesh_data.from_pydata([(   -1.5673,     7.7429,     7.7800), (   -4.2139,     6.8531,     7.0250), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face108', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face108')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace109')
mesh_data.from_pydata([(   -4.2139,     6.8531,    -0.3775), (   -3.7258,     3.9339,    -0.3775), (   -2.0971,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face109', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face109')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace110')
mesh_data.from_pydata([(    9.5070,    -1.0147,     7.7800), (    9.0190,     1.9045,     7.7800), (    7.3903,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face110', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face110')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace111')
mesh_data.from_pydata([(    1.5673,    -1.9045,     4.0788), (    4.2139,    -1.0147,     3.3237), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face111', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face111')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace112')
mesh_data.from_pydata([(    6.8604,    -1.9045,     4.0788), (    9.5070,    -1.0147,     3.3237), (    7.3903,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face112', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face112')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace113')
mesh_data.from_pydata([(    6.3724,     1.0147,     4.0788), (    3.7258,     1.9045,     3.3237), (    4.7437,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face113', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face113')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace114')
mesh_data.from_pydata([(    3.7258,     7.7429,     7.7800), (    1.0793,     6.8531,     7.0250), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face114', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face114')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace115')
mesh_data.from_pydata([(    4.2139,    -1.0147,     3.3237), (    3.7258,     1.9045,     3.3237), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face115', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face115')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace116')
mesh_data.from_pydata([(    1.5673,     3.9339,     7.0250), (    1.0793,     1.0147,     7.0250), (    0.5494,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face116', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face116')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace117')
mesh_data.from_pydata([(    6.3724,     1.0147,     7.0250), (    6.8604,    -1.9045,     7.0250), (    8.4891,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face117', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face117')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace118')
mesh_data.from_pydata([(   -4.2139,     6.8531,    -0.3775), (   -3.7258,     3.9339,    -0.3775), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face118', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face118')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace119')
mesh_data.from_pydata([(   -1.5673,     7.7429,     3.3237), (   -4.2139,     6.8531,     4.0788), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face119', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face119')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace120')
mesh_data.from_pydata([(   -3.7258,    -1.9045,     4.0788), (   -1.0793,    -1.0147,     3.3237), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face120', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face120')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace121')
mesh_data.from_pydata([(    1.0793,     1.0147,     7.0250), (    1.5673,    -1.9045,     7.0250), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face121', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face121')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace122')
mesh_data.from_pydata([(    3.7258,     7.7429,     0.3775), (    1.0793,     6.8531,    -0.3775), (    3.1960,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face122', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face122')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace123')
mesh_data.from_pydata([(    1.0793,     1.0147,     4.0788), (    1.5673,    -1.9045,     4.0788), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face123', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face123')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace124')
mesh_data.from_pydata([(    1.5673,    -1.9045,     4.0788), (    4.2139,    -1.0147,     3.3237), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face124', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face124')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace125')
mesh_data.from_pydata([(    3.7258,     1.9045,     3.3237), (    4.2139,     4.8237,     3.3237), (    5.8426,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face125', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face125')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace126')
mesh_data.from_pydata([(   -1.5673,     7.7429,     7.7800), (   -4.2139,     6.8531,     7.0250), (   -3.1960,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face126', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face126')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace127')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     7.7800), (   -1.5673,     1.9045,     7.7800), (   -3.1960,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face127', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face127')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace128')
mesh_data.from_pydata([(    4.2139,    -1.0147,     3.3237), (    3.7258,     1.9045,     3.3237), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face128', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face128')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace129')
mesh_data.from_pydata([(    1.5673,     3.9339,     7.0250), (    1.0793,     1.0147,     7.0250), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face129', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face129')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace130')
mesh_data.from_pydata([(    1.0793,     6.8531,     7.0250), (    1.5673,     3.9339,     7.0250), (    2.0971,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face130', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face130')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace131')
mesh_data.from_pydata([(    1.0793,     1.0147,    -0.3775), (   -1.5673,     1.9045,     0.3775), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face131', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face131')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace132')
mesh_data.from_pydata([(   -4.2139,     1.0147,    -0.3775), (   -3.7258,    -1.9045,    -0.3775), (   -2.0971,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face132', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face132')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace133')
mesh_data.from_pydata([(    6.8604,     3.9339,     4.0788), (    6.3724,     1.0147,     4.0788), (    5.8426,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face133', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face133')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace134')
mesh_data.from_pydata([(   -1.5673,     7.7429,     3.3237), (   -4.2139,     6.8531,     4.0788), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face134', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face134')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace135')
mesh_data.from_pydata([(    6.3724,     1.0147,     4.0788), (    6.8604,    -1.9045,     4.0788), (    7.3903,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face135', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face135')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace136')
mesh_data.from_pydata([(   -4.2139,     1.0147,     7.0250), (   -3.7258,    -1.9045,     7.0250), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face136', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face136')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace137')
mesh_data.from_pydata([(    4.2139,     4.8237,     0.3775), (    3.7258,     7.7429,     0.3775), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face137', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face137')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace138')
mesh_data.from_pydata([(    1.5673,    -1.9045,    -0.3775), (    4.2139,    -1.0147,     0.3775), (    3.1960,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face138', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face138')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace139')
mesh_data.from_pydata([(    4.2139,     4.8237,     0.3775), (    6.8604,     3.9339,    -0.3775), (    5.8426,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face139', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face139')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace140')
mesh_data.from_pydata([(   -1.5673,     7.7429,     0.3775), (   -4.2139,     6.8531,    -0.3775), (   -2.0971,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face140', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face140')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace141')
mesh_data.from_pydata([(    9.0190,     1.9045,     0.3775), (    6.3724,     1.0147,    -0.3775), (    7.3903,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face141', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face141')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace142')
mesh_data.from_pydata([(   -4.2139,     1.0147,     4.0788), (   -3.7258,    -1.9045,     4.0788), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face142', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face142')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace143')
mesh_data.from_pydata([(    9.0190,     1.9045,     3.3237), (    6.3724,     1.0147,     4.0788), (    7.3903,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face143', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face143')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace144')
mesh_data.from_pydata([(    6.3724,     6.8531,     7.0250), (    6.8604,     3.9339,     7.0250), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face144', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face144')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace145')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     0.3775), (   -1.5673,     1.9045,     0.3775), (   -2.0971,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face145', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face145')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace146')
mesh_data.from_pydata([(    4.2139,     4.8237,     7.7800), (    3.7258,     7.7429,     7.7800), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face146', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face146')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace147')
mesh_data.from_pydata([(    1.5673,     3.9339,    -0.3775), (    1.0793,     1.0147,    -0.3775), (   -0.5494,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face147', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face147')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace148')
mesh_data.from_pydata([(   -4.2139,     6.8531,     4.0788), (   -3.7258,     3.9339,     4.0788), (   -2.0971,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face148', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face148')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace149')
mesh_data.from_pydata([(    9.0190,     7.7429,     7.7800), (    6.3724,     6.8531,     7.0250), (    7.3903,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face149', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face149')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace150')
mesh_data.from_pydata([(   -1.0793,     4.8237,     3.3237), (   -1.5673,     7.7429,     3.3237), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face150', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face150')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace151')
mesh_data.from_pydata([(    9.5070,     4.8237,     7.7800), (    9.0190,     7.7429,     7.7800), (    8.4891,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face151', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face151')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace152')
mesh_data.from_pydata([(   -1.0793,     4.8237,     0.3775), (    1.5673,     3.9339,    -0.3775), (   -0.5494,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face152', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face152')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace153')
mesh_data.from_pydata([(    6.3724,     1.0147,    -0.3775), (    3.7258,     1.9045,     0.3775), (    4.7437,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face153', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face153')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace154')
mesh_data.from_pydata([(    1.5673,     3.9339,    -0.3775), (    4.2139,     4.8237,     0.3775), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face154', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face154')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace155')
mesh_data.from_pydata([(    3.7258,     7.7429,     3.3237), (    1.0793,     6.8531,     4.0788), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face155', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face155')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace156')
mesh_data.from_pydata([(    6.3724,     1.0147,     7.0250), (    3.7258,     1.9045,     7.7800), (    5.8426,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face156', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face156')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace157')
mesh_data.from_pydata([(    1.0793,     1.0147,     7.0250), (   -1.5673,     1.9045,     7.7800), (   -0.5494,     3.1136,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face157', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face157')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace158')
mesh_data.from_pydata([(   -1.0793,     4.8237,     0.3775), (    1.5673,     3.9339,    -0.3775), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face158', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face158')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace159')
mesh_data.from_pydata([(   -1.5673,     7.7429,     0.3775), (   -4.2139,     6.8531,    -0.3775), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face159', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face159')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace160')
mesh_data.from_pydata([(    1.0793,     6.8531,    -0.3775), (    1.5673,     3.9339,    -0.3775), (    3.1960,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face160', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face160')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace161')
mesh_data.from_pydata([(    1.5673,     3.9339,     4.0788), (    4.2139,     4.8237,     3.3237), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face161', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face161')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace162')
mesh_data.from_pydata([(   -1.0793,     4.8237,     3.3237), (    1.5673,     3.9339,     4.0788), (    0.5494,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face162', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face162')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace163')
mesh_data.from_pydata([(   -4.2139,     6.8531,     7.0250), (   -3.7258,     3.9339,     7.0250), (   -3.1960,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face163', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face163')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace164')
mesh_data.from_pydata([(    3.7258,     7.7429,     7.7800), (    1.0793,     6.8531,     7.0250), (    2.0971,     5.6440,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face164', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face164')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace165')
mesh_data.from_pydata([(    6.3724,     1.0147,    -0.3775), (    6.8604,    -1.9045,    -0.3775), (    7.3903,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face165', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face165')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace166')
mesh_data.from_pydata([(    6.3724,     1.0147,     7.0250), (    6.8604,    -1.9045,     7.0250), (    7.3903,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face166', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face166')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace167')
mesh_data.from_pydata([(    6.3724,     6.8531,    -0.3775), (    6.8604,     3.9339,    -0.3775), (    7.3903,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face167', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face167')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace168')
mesh_data.from_pydata([(    3.7258,     1.9045,     3.3237), (    1.0793,     1.0147,     4.0788), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face168', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face168')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace169')
mesh_data.from_pydata([(   -1.5673,     1.9045,     0.3775), (   -1.0793,     4.8237,     0.3775), (   -0.5494,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face169', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face169')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace170')
mesh_data.from_pydata([(   -4.2139,     1.0147,    -0.3775), (   -3.7258,    -1.9045,    -0.3775), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face170', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face170')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace171')
mesh_data.from_pydata([(    1.5673,     3.9339,     4.0788), (    4.2139,     4.8237,     3.3237), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face171', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face171')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace172')
mesh_data.from_pydata([(    1.0793,     1.0147,     7.0250), (    1.5673,    -1.9045,     7.0250), (    2.0971,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face172', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face172')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace173')
mesh_data.from_pydata([(    3.7258,     1.9045,     7.7800), (    1.0793,     1.0147,     7.0250), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face173', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face173')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace174')
mesh_data.from_pydata([(   -3.7258,    -1.9045,     4.0788), (   -1.0793,    -1.0147,     3.3237), (   -2.0971,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face174', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face174')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace175')
mesh_data.from_pydata([(    9.0190,     1.9045,     7.7800), (    6.3724,     1.0147,     7.0250), (    7.3903,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face175', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face175')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace176')
mesh_data.from_pydata([(    6.8604,     3.9339,    -0.3775), (    9.5070,     4.8237,     0.3775), (    8.4891,     6.0328,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face176', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face176')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace177')
mesh_data.from_pydata([(    1.0793,     1.0147,    -0.3775), (   -1.5673,     1.9045,     0.3775), (   -0.5494,     3.1136,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face177', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face177')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace178')
mesh_data.from_pydata([(    4.2139,     4.8237,     3.3237), (    3.7258,     7.7429,     3.3237), (    2.0971,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face178', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face178')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace179')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     0.3775), (   -1.5673,     1.9045,     0.3775), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face179', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face179')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace180')
mesh_data.from_pydata([(    1.0793,     6.8531,     4.0788), (    1.5673,     3.9339,     4.0788), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face180', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face180')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace181')
mesh_data.from_pydata([(    9.0190,     1.9045,     7.7800), (    6.3724,     1.0147,     7.0250), (    8.4891,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face181', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face181')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace182')
mesh_data.from_pydata([(    6.8604,    -1.9045,    -0.3775), (    9.5070,    -1.0147,     0.3775), (    8.4891,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face182', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face182')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace183')
mesh_data.from_pydata([(    9.0190,     1.9045,     3.3237), (    6.3724,     1.0147,     4.0788), (    8.4891,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face183', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face183')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace184')
mesh_data.from_pydata([(    1.0793,     1.0147,    -0.3775), (    1.5673,    -1.9045,    -0.3775), (    2.0971,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face184', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face184')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace185')
mesh_data.from_pydata([(   -1.0793,    -1.0147,     3.3237), (   -1.5673,     1.9045,     3.3237), (   -3.1960,    -0.1944,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face185', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face185')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace186')
mesh_data.from_pydata([(   -4.2139,     1.0147,     7.0250), (   -3.7258,    -1.9045,     7.0250), (   -3.1960,    -0.1944,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face186', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face186')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace187')
mesh_data.from_pydata([(   -1.5673,     1.9045,     0.3775), (   -4.2139,     1.0147,    -0.3775), (   -2.0971,     0.1944,    -1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face187', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face187')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace188')
mesh_data.from_pydata([(    1.5673,    -1.9045,     7.0250), (    4.2139,    -1.0147,     7.7800), (    3.1960,     0.1944,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face188', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face188')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace189')
mesh_data.from_pydata([(    1.5673,     3.9339,     7.0250), (    4.2139,     4.8237,     7.7800), (    3.1960,     6.0328,     5.5519)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face189', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face189')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace190')
mesh_data.from_pydata([(    6.8604,     3.9339,     7.0250), (    6.3724,     1.0147,     7.0250), (    5.8426,     2.7248,     9.2531)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face190', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face190')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace191')
mesh_data.from_pydata([(    6.3724,     1.0147,    -0.3775), (    3.7258,     1.9045,     0.3775), (    5.8426,     2.7248,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face191', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face191')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
mesh_data = bpy.data.meshes.new('structure.meshFace192')
mesh_data.from_pydata([(   -1.0793,     4.8237,     0.3775), (   -1.5673,     7.7429,     0.3775), (   -3.1960,     5.6440,     1.8506)], [], [(0, 1, 2)])
mesh_data.update()
ob1 = bpy.data.objects.new('structure.Face192', mesh_data)
bpy.context.scene.objects.link(ob1)
mat = bpy.data.materials.new('structure.material.Face192')
mat.use_transparency = True
mat.alpha =     0.7000
mat.diffuse_color = (0.8, 0.1, 0.4)
mat.specular_color = (0, 0, 0)
ob1.data.materials.append(mat)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
