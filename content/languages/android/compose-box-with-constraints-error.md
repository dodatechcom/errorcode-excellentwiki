---
title: "BoxWithConstraints Error"
description: "Fix Compose BoxWithConstraints responsive layout errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
BoxWithConstraints does not provide correct size information

## Common Causes

- Constraints not reflecting actual available size
- Layout not adapting to different screen sizes
- Constraints changing during recomposition
- Nested BoxWithConstraints not working

## Fixes

- Use BoxWithConstraints for size-dependent layouts
- Check maxWidth/maxHeight for breakpoints
- Use WindowSizeClass for adaptive layouts
- Avoid deep nesting of BoxWithConstraints

## Code Example

```kotlin
BoxWithConstraints(modifier = Modifier.fillMaxSize()) {
    if (maxWidth < 600.dp) {
        // Phone layout - vertical
        Column {
            Header()
            Content()
        }
    } else {
        // Tablet layout - horizontal
        Row {
            Sidebar()
            Content()
        }
    }
}
```

# maxWidth/maxHeight: available size
# minWidth/minHeight: minimum size
# Use dp comparisons for breakpoints
# Avoid in performance-critical composables
