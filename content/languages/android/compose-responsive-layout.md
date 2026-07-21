---
title: "Responsive Layout Error"
description: "Fix Compose responsive layout design for different screen sizes"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose layout does not adapt to different screen sizes and orientations

## Common Causes

- Layout not responding to screen size changes
- Content overflowing on small screens
- Two-pane layout not showing on tablets
- Orientation change not adapting layout

## Fixes

- Use WindowSizeClass for adaptive layouts
- Use BoxWithConstraints for size-based layouts
- Test on multiple screen sizes
- Use different layouts for portrait/landscape

## Code Example

```kotlin
// Adaptive layout based on screen size
val windowSizeClass = calculateWindowSizeClass(activity)

when {
    windowSizeClass.widthSizeClass == WindowWidthSizeClass.Compact -> {
        // Phone layout
        PhoneLayout()
    }
    windowSizeClass.widthSizeClass == WindowWidthSizeClass.Medium -> {
        // Tablet or foldable
        TabletLayout()
    }
    else -> {
        // Large screen
        LargeScreenLayout()
    }
}

// Or use BoxWithConstraints:
BoxWithConstraints {
    if (maxWidth > 600.dp) {
        Row { Sidebar(); Content() }
    } else {
        Column { TopBar(); Content() }
    }
}
```

# WindowSizeClass: Compact/Medium/Expanded
# BoxWithConstraints: size-based layout
# Test on: phone, tablet, foldable
# Consider orientation changes
