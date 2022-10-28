import bpy
from pathlib import Path
import os
import math


# Stops blender form Checking objekts after adding a new object. This improves performance
def run_ops_without_view_layer_update(func):
    from bpy.ops import _BPyOpsSubModOp

    view_layer_update = _BPyOpsSubModOp._view_layer_update

    def dummy_view_layer_update(context):
        pass

    try:
        _BPyOpsSubModOp._view_layer_update = dummy_view_layer_update

        func()

    finally:
        _BPyOpsSubModOp._view_layer_update = view_layer_update





path = "//genom.txt"  # file path to genomdata 

f = Path(bpy.path.abspath(path))

dataString = ""

if f.exists():
    dataString = f.read_text()
else:
    print("File not fond")


dataList = []
dataSize = len(dataList)


rootDataSize = math.sqrt(dataSize)
sqerSide = int(rootDataSize)
if rootDataSize > int(rootDataSize):
    sqerSide = int(rootDataSize) + 1


def add_cubes():
    
    posisionX = 0
    posisionY = 0

    basesRead = 1

    readError = False

    for base in dataList:

        readError = False

        if base == 'A':

            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD',
                                            location=(posisionX, posisionY, 0),
                                            scale=(1, 1, 1))

        elif base == 'T':
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD',
                                            location=(posisionX, posisionY, 0.25),
                                            scale=(1, 1, 1.5))

        elif base == 'G':
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD',
                                            location=(posisionX, posisionY, 0.5),
                                            scale=(1, 1, 2))

        elif base == 'C':
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD',
                                            location=(posisionX, posisionY, 0.75),
                                            scale=(1, 1, 2.5))

        else:
            
            readError = True


        if readError == False:
            
            posisionX += 1
            basesRead += 1

        if posisionX == sqerSide:

            posisionX = 0
            posisionY -= 1
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.booltool_auto_union()


run_ops_without_view_layer_update(add_cubes)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.booltool_auto_union()
