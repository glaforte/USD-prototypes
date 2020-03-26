# Allow module import from the parent path.
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import framework

cubeFilePath = framework.getDataFilePath("blender_cube.usda")
framework.viewUsdFile(cubeFilePath)
