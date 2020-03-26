# Allow module import from the parent path.
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import framework
from pxr import Usd, UsdGeom, UsdShade, Vt

stage = framework.createWorkStage("fort.usda")
framework.appendLayer(stage, "more_materials.usda")

doorPrim = stage.GetPrimAtPath("/Meshes/Door/Cube_002")
leftTowerPrim = stage.GetPrimAtPath("/Meshes/LeftTower/Cylinder")
leftCanopyPrim = stage.GetPrimAtPath("/Meshes/LeftCanopy/Cone")
mainPrim = stage.GetPrimAtPath("/Meshes/Main/Cube")
outcroppingPrim = stage.GetPrimAtPath("/Meshes/Outcropping/Cube_001")
rightTowerPrim = stage.GetPrimAtPath("/Meshes/RightTower/Cylinder_001")
rightCanopyPrim = stage.GetPrimAtPath("/Meshes/RightCanopy/Cone_001")

blueMaterial = UsdShade.Material(stage.GetPrimAtPath("/Looks/Blue"))
redMaterial = UsdShade.Material(stage.GetPrimAtPath("/Looks/Red"))
greenMaterial = UsdShade.Material(stage.GetPrimAtPath("/Looks/Green"))
yellowMaterial = UsdShade.Material(stage.GetPrimAtPath("/Looks/Yellow"))

rootPrim = stage.GetPrimAtPath("/Meshes")
collections = [
    Usd.CollectionAPI.ApplyCollection(rootPrim, "left"),
    Usd.CollectionAPI.ApplyCollection(rootPrim, "right"),
    Usd.CollectionAPI.ApplyCollection(rootPrim, "centre"),
    Usd.CollectionAPI.ApplyCollection(rootPrim, "misc")
]

collections[0].IncludePath("/Meshes/LeftTower/Cylinder")
collections[0].IncludePath("/Meshes/LeftCanopy/Cone")
collections[1].IncludePath("/Meshes/RightTower/Cylinder_001")
collections[1].IncludePath("/Meshes/RightCanopy/Cone_001")
collections[2].IncludePath("/Meshes/Main/Cube")
collections[2].IncludePath("/Meshes/Outcropping/Cube_001")
collections[3].IncludePath("/Meshes/Door/Cube_002")

UsdShade.MaterialBindingAPI(rootPrim).Bind(collections[0], blueMaterial, "left")
UsdShade.MaterialBindingAPI(rootPrim).Bind(collections[1], redMaterial, "right")
UsdShade.MaterialBindingAPI(rootPrim).Bind(collections[2], greenMaterial, "centre")
UsdShade.MaterialBindingAPI(rootPrim).Bind(collections[3], yellowMaterial, "misc")

framework.viewUsdStage(stage)
framework.printWorkStage(stage)

