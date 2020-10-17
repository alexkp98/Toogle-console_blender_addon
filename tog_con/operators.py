import bpy 
 
 
 
  ###################### class for toggleing system console##############################
class Toggle_OT_console(bpy.types.Operator):
  bl_label = "Toggle system console"
  bl_idname = "sysconole.toggleopr" 
  def execute(self, context):
      bpy.ops.wm.console_toggle()
      return {'FINISHED'}
    