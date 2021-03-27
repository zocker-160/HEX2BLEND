bl_info = {
    "name" : "HEX2BLEND",
    "author" : "zocker_160",
    "description" : "description",
    "blender" : (2, 92, 0),
    "version" : (0, 2),
    "location" : "View Layer Properties",
    "warning" : "Work in Progress",
    "category" : "Import",
    "tracker_url": "https://github.com/zocker-160/HEX2BLEND/issues"
}

import bpy
from bpy.props import StringProperty, FloatProperty

from bpy_extras.io_utils import ImportHelper, path_reference_mode

from . import Importer as Im

class ImportCSV(bpy.types.Operator, ImportHelper):
    """ CSV importer, generates spotlights """

    bl_idname = "import_hex.csv"
    bl_label = "Import CSV"

    filename_ext =".csv"

    filter_glob: StringProperty(
        default="*.csv",
        options={'HIDDEN'}
    )

    csv_separator: StringProperty(
        name="CSV Separator",
        default=","
    )

    setting_scaling: FloatProperty(
        name="Parent Scale Factor",
        description="set the scale factor of the parent object",
        default=0.001,
        min=0.001
    )

    def execute(self, context):
        print("calling import csv...")

        if Im.main_import(csvFile=self.filepath, csvSep=self.csv_separator, parentScale=self.setting_scaling):
            return {'FINISHED'}
        else:
            return {'CANCELLED'}

class ImportAnim(bpy.types.Operator, ImportHelper):
    """ Animation importer """

    bl_idname = "import_hex.ledanim"
    bl_label = "Import LED animation"

    filename_ext =".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'}
    )

    def execute(self, context):
        print("calling import json....")

        if Im.anim_import(animFile=self.filepath):
            bpy.context.scene.frame_current = 1
            return {'FINISHED'}
        else:
            return {'CANCELLED'}

class ButtonPanel(bpy.types.Panel):
    """ Panel for triggering the import function """

    bl_label = "HEX2BLEND"
    bl_idname = "OBJECT_PT_hex2blend"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "view_layer"

    def draw(self, context):
        row1 = self.layout.row(align=True)
        row1.operator("import_hex.csv", text="Import CSV (Lamps)", icon="IMPORT")

        row2 = self.layout.row(align=True)
        row2.operator("import_hex.ledanim", text="Import JSON (Animation)", icon="IMPORT")

        sep1 = self.layout.separator_spacer()

        row3 = self.layout.row(align=True)
        row3.operator("import_hex.clean", text="Clear import cache", icon="TRASH")

class CleanOperator(bpy.types.Operator):
    """ Operator that allows to clear the data in memory from import """

    bl_idname = "import_hex.clean"
    bl_label = "clear HEX2BLEND import chache"

    def execute(self, context):
        Im.allLamps.clear()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ImportCSV)
    bpy.utils.register_class(ImportAnim)
    bpy.utils.register_class(ButtonPanel)
    bpy.utils.register_class(CleanOperator)

def unregister():
    bpy.utils.unregister_class(ImportCSV)
    bpy.utils.unregister_class(ImportAnim)
    bpy.utils.unregister_class(ButtonPanel)
    bpy.utils.unregister_class(CleanOperator)

if __name__ == "__main__":
    register()
