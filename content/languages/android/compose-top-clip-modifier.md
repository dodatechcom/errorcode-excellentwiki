---
title: "Clip Modifier Error"
description: "Fix Compose clip modifier for clipping content to shape or outline"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Content not clipped correctly to expected shape or outline

## Common Causes

- Clip not applying to composable content
- Shape not matching expected outline
- Clip causing rendering artifacts
- Clip not working with complex shapes

## Fixes

- Use clip modifier with shape or outline
- Ensure clip is applied after background
- Test with different shapes
- Verify clip does not cause rendering issues

## Code Example

```kotlin
Modifier
    .clip(RoundedCornerShape(8.dp))
    .background(Color.Red)
    .padding(16.dp)

// With custom outline:
Modifier.clip(object : Shape {
    override fun createOutline(size: Size, layoutDirection: LayoutDirection, density: Density): Outline {
        return Outline.Rounded(roundedCorner = RoundedCornerShape(8.dp).createOutline(size, layoutDirection, density))
    }
})
```

# clip(shape): clip to shape# clip(outline): clip to custom outline# Apply after background for proper clipping# Test with different shapes
