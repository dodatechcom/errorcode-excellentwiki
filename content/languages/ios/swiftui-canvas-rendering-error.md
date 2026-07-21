---
title: "[Solution] SwiftUI Canvas Rendering Error"
description: "Fix SwiftUI Canvas and GraphicsContext rendering failures in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI Canvas Rendering Error

Canvas fails to render when GraphicsContext is used incorrectly or when the drawing operations exceed GPU limits.

## Common Causes
- Canvas closure too complex for single render
- GraphicsContext operations performed off main thread
- Image resolution too large for Canvas
- Resolving text or images fails silently

## How to Fix
1. Simplify Canvas drawing operations
2. Ensure Canvas renders on the main thread
3. Use appropriate image resolutions
4. Check resolvedText and resolvedImage return values

```swift
Canvas { context, size in
    let rect = CGRect(origin: .zero, size: size)
    context.fill(Path(rect), with: .color(.blue))
    if let text = context.resolve(Text("Hello")) {
        context.draw(text, at: CGPoint(x: size.width/2, y: size.height/2))
    }
}
.frame(width: 200, height: 100)
```

## Examples
```swift
// Canvas with complex drawing:
Canvas { context, size in
    // Draw background
    let bgPath = Path(CGRect(origin: .zero, size: size))
    context.fill(bgPath, with: .color(.white))

    // Draw shapes
    let circle = Path(ellipseIn: CGRect(x: 50, y: 50, width: 100, height: 100))
    context.fill(circle, with: .color(.red))

    // Draw text
    let text = context.resolve(Text("Canvas"))
    context.draw(text, at: CGPoint(x: size.width/2, y: size.height/2))
}
```
