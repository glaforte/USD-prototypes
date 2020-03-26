# MultiColored Cube

This prototype tests the material binding of geometry sub-sets.
Storm fails to display the multi-colored cube.
It outputs the USDA code below.

```
#usda 1.0

over "Cube"
{
    uniform token subsetFamily:materialBind:familyType = "nonOverlapping"

    def GeomSubset "blueSubset"
    {
        uniform token elementType = "face"
        uniform token familyName = "materialBind"
        int[] indices = [0, 1]
        rel material:binding = </Looks/Blue>
    }

    def GeomSubset "redSubset"
    {
        uniform token elementType = "face"
        uniform token familyName = "materialBind"
        int[] indices = [2, 3]
        rel material:binding = </Looks/Red>
    }

    def GeomSubset "greenSubset"
    {
        uniform token elementType = "face"
        uniform token familyName = "materialBind"
        int[] indices = [4, 5]
        rel material:binding = </Looks/Green>
    }

    def GeomSubset "yellowSubset"
    {
        uniform token elementType = "face"
        uniform token familyName = "materialBind"
        int[] indices = [6, 7]
        rel material:binding = </Looks/Yellow>
    }
}
```