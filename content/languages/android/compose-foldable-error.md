---
title: "Foldable Device Error"
description: "Fix Compose foldable device and large screen adaptation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose UI does not adapt correctly to foldable device states

## Common Causes

- Layout not responding to fold state changes
- Two-pane layout not showing on unfolded devices
- Content not adapting to different screen sizes
- Fold position not being tracked

## Fixes

- Use WindowSizeClass for adaptive layouts
- Track fold state with FoldingFeature
- Use BoxWithConstraints for responsive design
- Test on foldable emulator and devices

## Code Example

```kotlin
// Adaptive layout based on window size
val windowSizeClass = calculateWindowSizeClass(activity)

when (windowSizeClass.widthSizeClass) {
    WindowWidthSizeClass.Compact -> {
        // Phone layout
        PhoneLayout()
    }
    WindowWidthSizeClass.Medium -> {
        // Tablet or foldable folded
        TabletLayout()
    }
    WindowWidthSizeClass.Expanded -> {
        // Foldable unfolded or large tablet
        TwoPaneLayout()
    }
}
```

# WindowSizeClass: Compact, Medium, Expanded
# FoldingFeature: fold/hinge state
# Test on: Pixel Fold, Galaxy Z Fold
# Use res/layout-sw600dp for alternate layouts
