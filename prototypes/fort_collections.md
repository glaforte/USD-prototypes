# Fort Collections

The goal of this prototype is to experience the USD SDK API about the creation collections and their binding to materials.

## Impressions

I was able to get Storm to display the materials bound through collections.
Reading the code of the USD SDK, there are some rules: direct bindings should win over collection bindings unless they are in the same prim.
This hints that collection bindings could be more beneficial in the prim hierarchy.

I had issues with collection bindings where the material only contained a displayColor parameter.
Changing to use a "preview" shader fixed the issue.
It is my conclusion that collection bindings are discarded for the simplest of materials.

### Version 1

This first version was setting up the collection bindings at the prim-level.
Since the Mesh prim collection bindings describe both the material and the collection: why is this useful?
It really feels like the collections are only useful when binding at the root of the hierarchy.

### Version 2

![GitHub Logo](/images/logo.png)

This second version is setting up the collection bindings at the root-level.
The root prim also includes the declaration of the collections.
I think that this works better than Version 1, but I question how well root-level collection bindings would accept references.

## USD Generated

### Version 2

```
over "Meshes" (
    prepend apiSchemas = ["CollectionAPI:left", "CollectionAPI:right", "CollectionAPI:centre", "CollectionAPI:misc"]
)
{
    uniform token collection:centre:expansionRule = "expandPrims"
    prepend rel collection:centre:includes = [
        </Meshes/Main/Cube>,
        </Meshes/Outcropping/Cube_001>,
    ]
    uniform token collection:left:expansionRule = "expandPrims"
    prepend rel collection:left:includes = [
        </Meshes/LeftTower/Cylinder>,
        </Meshes/LeftCanopy/Cone>,
    ]
    uniform token collection:misc:expansionRule = "expandPrims"
    prepend rel collection:misc:includes = </Meshes/Door/Cube_002>
    uniform token collection:right:expansionRule = "expandPrims"
    prepend rel collection:right:includes = [
        </Meshes/RightTower/Cylinder_001>,
        </Meshes/RightCanopy/Cone_001>,
    ]

    rel material:binding:collection:centre = [
        </Meshes.collection:centre>,
        </Looks/Green>,
    ]
    rel material:binding:collection:left = [
        </Meshes.collection:left>,
        </Looks/Blue>,
    ]
    rel material:binding:collection:misc = [
        </Meshes.collection:misc>,
        </Looks/Yellow>,
    ]
    rel material:binding:collection:right = [
        </Meshes.collection:right>,
        </Looks/Red>,
    ]
}
```

# References

https://graphics.pixar.com/usd/docs/UsdShade-Material-Assignment.html