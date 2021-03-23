bl_info = {
    "name" : "HEX2BLEND",
    "author" : "zocker_160",
    "description" : "description",
    "blender" : (2, 92, 0),
    "version" : (0, 1),
    "location" : "File > Import",
    "warning" : "Work in Progress",
    "category" : "Import-Export",
    "tracker_url": "https://github.com/zocker-160/HEX2BLEND"
}

import bpy
from bpy.props import StringProperty

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

    def execute(self, context):
        print("calling import csv...")

        if Im.main_import(csvFile=self.filepath, csvSep=self.csv_separator):
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

def register():
    bpy.utils.register_class(ImportCSV)
    bpy.utils.register_class(ImportAnim)

def unregister():
    bpy.utils.unregister_class(ImportCSV)
    bpy.utils.unregister_class(ImportAnim)

if __name__ == "__main__":
    register()
