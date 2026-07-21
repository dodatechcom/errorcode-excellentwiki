---
title: "Material3 Shape Error"
description: "Fix Material 3 shape configuration and rounded corner errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Material 3 shapes not applying correctly or corners not rendering

## Common Causes

- ShapeTheme not provided to MaterialTheme
- RoundedCornerShape values not matching design
- CutoutShape or BottomSheet shape incorrect
- Shape not applied to container or surface

## Fixes

- Pass Shape to MaterialTheme
- Use RoundedCornerShape with dp values
- Override shapeAppearance in theme
- Apply shape to Card, Surface, or Button

## Code Example

```kotlin
val.shapes = Shapes(
    small = RoundedCornerShape(8.dp),
    medium = RoundedCornerShape(12.dp),
    large = RoundedCornerShape(16.dp),
    extraLarge = RoundedCornerShape(28.dp)
)

MaterialTheme(shapes = shapes) {
    Card(
        shape = MaterialTheme.shapes.medium,
        modifier = Modifier.fillMaxWidth()
    ) {
        Text("Card with medium shape")
    }
}
```

# Shape sizes: small, medium, large, extraLarge
# RoundedCornerShape for uniform corners
# CutoutShape for cutout effects
# Apply to Card, Surface, Dialog, etc.
