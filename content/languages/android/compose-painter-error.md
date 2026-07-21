---
title: "Painter Error"
description: "Fix Compose Painter and custom drawing resource errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom Painter does not render or animate correctly in Compose

## Common Causes

- Painter not properly implementing DrawScope
- Painter size not matching target bounds
- Painter not invalidating on state change
- Painter resource not loading from assets

## Fixes

- Override DrawScope.draw() in custom Painter
- Use intrinsicSize for correct sizing
- Call invalidateSelf() when state changes
- Use painterResource() for drawable resources

## Code Example

```kotlin
// Custom Painter
class GradientPainter : Painter() {
    override val intrinsicSize = Size.Unspecified

    override fun DrawScope.onDraw() {
        drawRect(
            brush = Brush.linearGradient(
                colors = listOf(Color.Red, Color.Blue),
                start = Offset.Zero,
                end = Offset(size.width, size.height)
            )
        )
    }
}

// Usage:
Image(
    painter = GradientPainter(),
    contentDescription = "Gradient background"
)

// Painter resource:
Image(
    painter = painterResource(R.drawable.icon),
    contentDescription = "Icon"
)
```

# Painter: custom drawing in Compose
# painterResource(): load drawable resources
# rememberVectorPainter(): vector drawables
# AsyncImage(): network images with Coil
