---
title: "Intrinsic Measurement Error"
description: "Fix Compose intrinsic measurement and size calculation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable sizes calculated incorrectly because of intrinsic measurement issues

## Common Causes

- intrinsicSize not properly implemented
- widthIntrinsic or heightIntrinsic returning wrong values
- Layout consuming too much time measuring intrinsics
- Nested intrinsic measurements causing O(n²) complexity

## Fixes

- Implement intrinsicSize correctly in custom layouts
- Use wrapContentSize for flexible sizing
- Avoid deep nesting of intrinsic measurements
- Cache intrinsic measurements when possible

## Code Example

```kotlin
// Intrinsic measurement
Column {
    Text("Title", modifier = Modifier.wrapContentSize())
    Box(modifier = Modifier.fillMaxWidth().heightIn(min = 100.dp)) {
        // Content determines height, minimum 100dp
    }
}

// Custom intrinsic:
@Composable
fun CustomLayout(modifier: Modifier = Modifier) {
    Layout(
        modifier = modifier,
        content = { /* children */ }
    ) { measurables, constraints ->
        val intrinsics = measurables.map { it.maxIntrinsicWidth(constraints.maxWidth) }
        // Use intrinsics for layout decisions
        layout(constraints.maxWidth, intrinsics.sum()) { /* place */ }
    }
}
```

# wrapContentSize: fit to content
# widthIn/heightIn: min/max constraints
# minIntrinsicWidth/Height: smallest possible size
# maxIntrinsicWidth/Height: largest preferred size
