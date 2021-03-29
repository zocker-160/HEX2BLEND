import bpy
import json

from mathutils import Vector

allLamps = list()

def add_collection(name: str) -> bpy.types.Collection:
    new_col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(new_col)
    return new_col

def set_fps(value: int):
    bpy.context.scene.render.fps = value

def create_spot(name: str, pos: Vector, collection: bpy.types.Collection, parent: bpy.types.Object):
    print(f"creating spot {name} at {pos}")

    lightData = bpy.data.lights.new(name=name, type='SPOT')
    lightObject = bpy.data.objects.new(name=name, object_data=lightData)

    lightObject.parent = parent
    lightObject.location = pos

    collection.objects.link(lightObject)

    return lightData

def insert_keyframe(frame: int, keyframes: list):
    # check if keyframe data is valid - this implementation really sucks
    #if len(keyframes) != len(allLamps):
    #    raise TypeError("number of leds does not match with animation data")

    fps: int = bpy.context.scene.render.fps

    bpy.context.scene.frame_end = frame * fps

    for i, lamp in enumerate(allLamps):
        l: bpy.types.Object = lamp

        l.color = keyframes[i]["r"], keyframes[i]["g"], keyframes[i]["b"]

        print(f"inserting keyframe at frame {frame} with {l.color}")
        lamp.keyframe_insert('color', frame=(frame-1)*fps+1)


def main_import(csvFile: str, csvSep: str, parentScale: float):
    # clear all lamp data; TODO: this is not a great solution
    allLamps.clear()

    with open(csvFile, "r") as csv:

        importCol = add_collection("import")
        parentEmpty = bpy.data.objects.new("parent", None)
        parentEmpty.empty_display_size = 2
        parentEmpty.empty_display_type = 'PLAIN_AXES'
        parentEmpty.scale = [parentScale]*3
        
        importCol.objects.link(parentEmpty)

        for i, line in enumerate(csv):
            # first line of CSV is the header
            if i == 0:
                numValues = len(line.split(csvSep))
            else:
                tmpPos = line.split(csvSep)

                # skip empty lines
                if len(line) <= 1 or len(tmpPos) != numValues:
                    print("skipping line")
                    continue

                allLamps.append( create_spot(
                    name=tmpPos[0],
                    pos=Vector((float(tmpPos[1]), float(tmpPos[2]), 0)),
                    collection=importCol,
                    parent=parentEmpty
                    )
                )
    
    return True

def anim_import(animFile: str):
    with open(animFile, "r") as f:

        for i, line in enumerate(f):
            # first line contains header
            if i == 0:
                print(line)
                header: dict = json.loads(line)
                print(header)

                set_fps(header.get("FPS"))

                ##
            else:
                if len(line) <= 1: continue

                try:
                    tmpFrame = json.loads(line)
                except:
                    print("on line" + str(i))
                    raise

                insert_keyframe(tmpFrame["frame"], tmpFrame["leds"])

    return True
