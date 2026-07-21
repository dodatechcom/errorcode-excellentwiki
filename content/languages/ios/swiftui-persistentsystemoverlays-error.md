---
title: "[Solution] SwiftUI .persistentSystemOverlays Error"
description: "Fix SwiftUI persistent system overlays configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .persistentSystemOverlays Error

System overlay configuration errors occur when the modifier is not properly applied, when the overlay type is incompatible with the view hierarchy, or when safe area handling conflicts.

## Common Causes
- Modifier not on the root view
- Overlay type conflicts with view content
- Safe area not properly accounted for
- Multiple overlay modifiers conflicting

## How to Fix
1. Apply modifier to the root or appropriate view
2. Choose overlay type that works with your content
3. Account for safe area in layout calculations
4. Use only one overlay configuration

```swift
// Hide home indicator:
Text("Content")
    .persistentSystemOverlays(.hidden)

// Show home indicator:
Text("Content")
    .persistentSystemOverlays(.visible)
```

## Examples
```swift
// Full screen with hidden overlay:
VideoPlayer(player: player)
    .persistentSystemOverlays(.hidden)
    .ignoresSafeArea()

// Game view:
GameView()
    .persistentSystemOverlays(.hidden)
    .statusBarHidden()
```
