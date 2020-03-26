# Allow module import from the parent path.
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import framework
from pxr import Usd, UsdGeom, UsdShade

stage = framework.createWorkStage("clean_cube.usda")
framework.appendLayer(stage, "more_materials.usda")

cubePrim = stage.GetPrimAtPath("/Cube")
blueMaterial = UsdShade.Material(stage.GetPrimAtPath("/Looks/Blue"))
UsdShade.MaterialBindingAPI(cubePrim).Bind(blueMaterial)

framework.viewUsdStage(stage)
framework.printWorkStage(stage)
