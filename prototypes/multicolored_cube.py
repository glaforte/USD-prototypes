# Allow module import from the parent path.
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import framework
from pxr import Usd, UsdGeom, UsdShade, Vt

stage = framework.createWorkStage("clean_cube.usda")
framework.appendLayer(stage, "more_materials.usda")

cubePrim = stage.GetPrimAtPath("/Cube")
blueMaterial = UsdShade.Material(stage.GetPrimAtPath("/Looks/Blue"))
redMaterial = UsdShade.Material(stage.GetPrimAtPath("/Looks/Red"))
greenMaterial = UsdShade.Material(stage.GetPrimAtPath("/Looks/Green"))
yellowMaterial = UsdShade.Material(stage.GetPrimAtPath("/Looks/Yellow"))

cubeBinder = UsdShade.MaterialBindingAPI(cubePrim)
blueSubset = cubeBinder.CreateMaterialBindSubset("blueSubset", Vt.IntArray([0, 1]))
redSubset = cubeBinder.CreateMaterialBindSubset("redSubset", Vt.IntArray([2, 3]))
greenSubset = cubeBinder.CreateMaterialBindSubset("greenSubset", Vt.IntArray([4, 5]))
yellowSubset = cubeBinder.CreateMaterialBindSubset("yellowSubset", Vt.IntArray([6, 7]))

UsdShade.MaterialBindingAPI(blueSubset).Bind(blueMaterial)
UsdShade.MaterialBindingAPI(redSubset).Bind(redMaterial)
UsdShade.MaterialBindingAPI(greenSubset).Bind(greenMaterial)
UsdShade.MaterialBindingAPI(yellowSubset).Bind(yellowMaterial)

framework.viewUsdStage(stage)
framework.printWorkStage(stage)

