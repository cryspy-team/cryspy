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
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.200000, subdivisions=3)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.O'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.O')
mat.diffuse_color = (1.0, 0.051, 0.051)
me.materials.append(mat)
bpy.ops.mesh.primitive_ico_sphere_add(location=(0,0,0), size=0.292400, subdivisions=3)
ob = bpy.context.object
me = ob.data
me.name = 'structure.mesh.Mn'
bpy.ops.object.delete()
mat = bpy.data.materials.new('structure.material.Mn')
mat.diffuse_color = (0.6118, 0.4784, 0.7804)
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
posobject.data.vertices[-1].co = (4.213869, 4.823686, 0.377527)
ob = bpy.data.objects.new(             'structure.Atom001(O2_5)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.213869, 4.823686, 0.377527)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 0.000000, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom002(Mn1_2)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 0.000000, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.549428, 2.724781, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom003(O1_6)', bpy.data.meshes['structure.mesh.O'])
ob.location = (0.549428, 2.724781, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.557116, 2.438116, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom004(Tb1_7)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (2.557116, 2.438116, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.743712, 3.113619, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom005(O1_2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.743712, 3.113619, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.725841, 1.904486, 0.377527)
ob = bpy.data.objects.new(             'structure.Atom006(O2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.725841, 1.904486, 0.377527)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 2.919200, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom007(Mn1_1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 2.919200, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.195998, 0.194419, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom008(O1_1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.195998, 0.194419, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.567299, 3.933914, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom009(O2_4)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.567299, 3.933914, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.079271, 1.014714, 4.078778)
ob = bpy.data.objects.new(             'structure.Atom010(O2_7)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.079271, 1.014714, 4.078778)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.203686, 0.481084, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom011(Tb1)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (5.203686, 0.481084, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.743712, 3.113619, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom012(O1_4)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.743712, 3.113619, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.736024, 3.400284, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom013(Tb1_3)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (2.736024, 3.400284, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (5.203686, 0.481084, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom014(Tb1_6)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (5.203686, 0.481084, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.195998, 0.194419, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom015(O1_7)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.195998, 0.194419, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.557116, 2.438116, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom016(Tb1_1)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (2.557116, 2.438116, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (4.213869, 4.823686, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom017(O2_3)', bpy.data.meshes['structure.mesh.O'])
ob.location = (4.213869, 4.823686, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.089454, 5.357316, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom018(Tb1_4)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (0.089454, 5.357316, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.097142, 5.643981, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom019(O1_5)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.097142, 5.643981, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.097142, 5.643981, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom020(O1_3)', bpy.data.meshes['structure.mesh.O'])
ob.location = (2.097142, 5.643981, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.000000, 2.919200, 3.701250)
ob = bpy.data.objects.new(             'structure.Atom021(Mn1_3)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (0.000000, 2.919200, 3.701250)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.079271, 1.014714, 7.024972)
ob = bpy.data.objects.new(             'structure.Atom022(O2_1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.079271, 1.014714, 7.024972)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.089454, 5.357316, 5.551875)
ob = bpy.data.objects.new(             'structure.Atom023(Tb1_2)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (0.089454, 5.357316, 5.551875)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (1.567299, 3.933914, 4.078778)
ob = bpy.data.objects.new(             'structure.Atom024(O2_2)', bpy.data.meshes['structure.mesh.O'])
ob.location = (1.567299, 3.933914, 4.078778)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (3.725841, 1.904486, 3.323722)
ob = bpy.data.objects.new(             'structure.Atom025(O2_6)', bpy.data.meshes['structure.mesh.O'])
ob.location = (3.725841, 1.904486, 3.323722)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.736024, 3.400284, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom026(Tb1_5)', bpy.data.meshes['structure.mesh.Tb'])
ob.location = (2.736024, 3.400284, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (2.646570, 0.000000, 0.000000)
ob = bpy.data.objects.new(             'structure.Atom027(Mn1)', bpy.data.meshes['structure.mesh.Mn'])
ob.location = (2.646570, 0.000000, 0.000000)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
posobject.data.vertices.add(1)
posobject.data.vertices[-1].co = (0.549428, 2.724781, 1.850625)
ob = bpy.data.objects.new(             'structure.Atom028(O1)', bpy.data.meshes['structure.mesh.O'])
ob.location = (0.549428, 2.724781, 1.850625)
bpy.ops.object.shade_smooth()
bpy.context.scene.objects.link(ob)
for ob in bpy.data.objects:
    if ob.name.startswith('structure.Atom'):
        ob.select = True
    else:
        ob.select = False
bpy.ops.object.shade_smooth()
