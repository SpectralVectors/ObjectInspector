bl_info = {
    "name": "Object Inspector",
    "author": "Spectral Vectors",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Returns Vertex, Edge, Face Data",
    "warning": "",
    "doc_url": "",
    "category": "View3D",
}

import bpy
from bpy.types import Operator
from bpy.props import IntProperty

class ObjectInspectorProperties(bpy.types.PropertyGroup):

    vertexindex: IntProperty(
        name='Vertex Index',
        description='Index of the selected vertex',
        default=0,
    )

    edgeindex: IntProperty(
        name='Edge Index',
        description='Index of the selected edge',
        default=0,
    )

    faceindex: IntProperty(
        name='Face Index',
        description='Index of the selected face',
        default=0,
    )

def VertexInspect():
    bpy.ops.object.editmode_toggle()

    for vertex in bpy.context.object.data.vertices:
        if vertex.select == True:
            bpy.context.scene.oi_vars.vertexindex = vertex.index

    bpy.ops.object.editmode_toggle()
    
def EdgeInspect():
    
    bpy.ops.object.editmode_toggle()

    for edge in bpy.context.object.data.edges:
        if edge.select == True:
            bpy.context.scene.oi_vars.edgeindex = edge.index
            
    bpy.ops.object.editmode_toggle()

def FaceInspect():

    bpy.ops.object.editmode_toggle()

    for polygon in bpy.context.object.data.polygons:
        if polygon.select == True:
            bpy.context.scene.oi_vars.faceindex = polygon.index
            
    bpy.ops.object.editmode_toggle()

class OBJECT_OT_vertex_inspect(Operator):
    """Return info on selected vertex/vertices"""
    bl_idname = "mesh.vertex_inspect"
    bl_label = "Get Vertex Info"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        VertexInspect()

        return {'FINISHED'}

class OBJECT_OT_edge_inspect(Operator):
    """Return info on selected edge(s)"""
    bl_idname = "mesh.edge_inspect"
    bl_label = "Get Edge Info"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        EdgeInspect()

        return {'FINISHED'}

class OBJECT_OT_face_inspect(Operator):
    """Return info on selected face(s)"""
    bl_idname = "mesh.face_inspect"
    bl_label = "Get Face Info"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        FaceInspect()

        return {'FINISHED'}

class OBJECT_PT_object_inspector(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport"""
    bl_label = "Object Inspector"
    bl_category = "Object Inspector"
    bl_idname = "OBJECT_PT_object_inspector"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        column = layout.column()
        box = column.box()
        column = box.column(align=True)
        column.operator(OBJECT_OT_vertex_inspect.bl_idname,text="Get Vertex Info",icon='VERTEXSEL')
        column.prop(bpy.context.scene.oi_vars, 'vertexindex')
        column = box.column(align=True)
        column.operator(OBJECT_OT_edge_inspect.bl_idname,text="Get Edge Info",icon='EDGESEL')
        column.prop(bpy.context.scene.oi_vars, 'edgeindex')
        column = box.column(align=True)
        column.operator(OBJECT_OT_face_inspect.bl_idname,text="Get Face Info",icon='FACESEL')
        column.prop(bpy.context.scene.oi_vars, 'faceindex')


# Registration

def register():
    bpy.utils.register_class(OBJECT_OT_vertex_inspect)
    bpy.utils.register_class(OBJECT_OT_edge_inspect)
    bpy.utils.register_class(OBJECT_OT_face_inspect)
    bpy.utils.register_class(OBJECT_PT_object_inspector)
    bpy.utils.register_class(ObjectInspectorProperties)
    bpy.types.Scene.oi_vars = bpy.props.PointerProperty(type=ObjectInspectorProperties)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_vertex_inspect)
    bpy.utils.unregister_class(OBJECT_OT_edge_inspect)
    bpy.utils.unregister_class(OBJECT_OT_face_inspect)
    bpy.utils.unregister_class(OBJECT_PT_object_inspector)
    bpy.utils.unregister_class(ObjectInspectorProperties)


if __name__ == "__main__":
    register()