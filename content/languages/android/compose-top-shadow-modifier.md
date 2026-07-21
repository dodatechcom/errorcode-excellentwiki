---
title: "Shadow Modifier Error"
description: "Fix Compose shadow modifier for elevation and shadow rendering"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Shadow not appearing correctly or causing rendering issues on composable

## Common Causes

- Shadow not visible on composable
- Shadow shape not matching expected outline
- Shadow causing dark edges or artifacts
- Shadow not matching Material Design specs

## Fixes

- Use shadow modifier with elevation and shape
- Ensure shadow is applied before background
- Test shadow on different backgrounds
- Use Material Design elevation values

## Code Example

```kotlin
Modifier
    .shadow(
        elevation = 4.dp,
        shape = RoundedCornerShape(8.dp)
    )
    .background(Color.White)
    .padding(16.dp)

// With clip:
Modifier
    .shadow(
        elevation = 4.dp,
        shape = RoundedCornerShape(8.dp),
        clip = true  // Clip to shape
    )
    .background(Color.White)
    .padding(16.dp)
```

# shadow(elevation, shape): elevation shadow# Apply before background for proper rendering# clip=true: clip content to shape# Use Material Design elevation values
