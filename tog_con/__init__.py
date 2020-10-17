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
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#
# ##### ACKNOWLEDGEMENT #####
#
# Toggle console addon by: Alex Paul
# Initial script programming: Alex Paul
# Description : this addon is mainly for blender scripting beginners

################################################################################################################################################################################################



bl_info = {
    'name': 'System Console Toggle',
    'author': 'Alex Paul',
    'version': (1,0,1),
    'blender': (2, 83, 0),
    'location': 'Scripting, workspace, Text Editor, side panel(ctrl+T), Toggle console',
    'description': 'this addon is mainly for blender scripting beginners',
    'wiki_url': '',
    'tracker_url': '',
    'category': 'Scripting'
    }




import bpy
 
from . Panel import TOGGLE_PT_main_panel
from . operators import Toggle_OT_console


classes = [TOGGLE_PT_main_panel, Toggle_OT_console]
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
 
 
 
if __name__ == "__main__":
    register()