import bpy

 ###################### class for buttons and panel##############################
class TOGGLE_PT_main_panel(bpy.types.Panel):
    bl_label = "Toogle"
    bl_idname = "TOGGLE_PT_main_menu"
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Toggle Console"
 
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("sysconole.toggleopr")



 