# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {"name": "Generic Operator Pie",
           "author": "CDMJ",
           "version": (1, 0, 0),
           "blender": (2, 77, 0),
           "location": "",
           "description": "Generic Fill IN The Blank Pie",
           "warning": "Use after inserting operators, duh!",
           "category": "3D View"}






import bpy
from bpy.types import Menu

#operators

#one
class OperOne(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oper_one"
    bl_label = "Operator One"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        #bpy.context.object.draw_type = 'WIRE'
        return {'FINISHED'}
    
#two   
class OperTwo(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oper_two"
    bl_label = "Operator Two"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        #bpy.context.object.draw_type = 'SOLID'
        return {'FINISHED'}

#three
class OperThree(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oper_three"
    bl_label = "Operator Three"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        #bpy.context.object.draw_type = 'TEXTURED'
        return {'FINISHED'}
    
#four
class OperFour(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oper_four"
    bl_label = "Operator Four"
 
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
 
    #def execute(self, context):
        #if bpy.context.object.draw_type == 'SOLID':
            #bpy.context.object.draw_type = 'WIRE'
        #elif bpy.context.object.draw_type == 'WIRE':
            #bpy.context.object.draw_type = 'SOLID'
        #else: 
            #bpy.context.object.draw_type = 'WIRE'
        #return {'FINISHED'}

    
    
    
#------------------------------------#pie
class VIEW3D_PIE_generic(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "GENERIC"

    def draw(self, context):
        layout = self.layout
        
        pie = layout.menu_pie()
        #pie.operator("render.render", text='one')

        pie.operator("object.oper_one", text='One', icon='GRID')
        pie.operator("object.oper_two", text='Two', icon='SNAP_VOLUME')
        pie.operator("object.oper_three", text='Three', icon='TEXTURE')
        pie.operator("object.oper_four", text='Four', icon='SNAP_FACE')
        
        
        
def register():
    bpy.utils.register_module(__name__)

    km_list = ['3D View']
    for i in km_list:
        sm = bpy.context.window_manager
        km = sm.keyconfigs.default.keymaps[i]
        kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS', ctrl=True, shift=True, alt=True)
        kmi.properties.name = "VIEW3D_PIE_generic"

def unregister():
    bpy.utils.unregister_module(__name__)

    km_list = ['3D View']
    for i in km_list:
        sm = bpy.context.window_manager
        km = sm.keyconfigs.default.keymaps[i]
        for kmi in (kmi for kmi in km.keymap_items \
                            if (kmi.idname == "VIEW3D_PIE_generic")):
            km.keymap_items.remove(kmi)
        







if __name__ == "__main__":
    register()
