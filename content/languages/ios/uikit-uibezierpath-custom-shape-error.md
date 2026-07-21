---
title: "[Solution] UIKit UIBezierPath Custom Shape Error"
description: "Fix UIBezierPath shape creation and clipping errors in UIKit."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIBezierPath Custom Shape Error

Bezier path errors occur when the path is not properly closed, when the path intersects itself, or when the path is used for clipping with incorrect bounds.

## Common Causes
- Path not properly closed
- Path intersects itself causing rendering issues
- Clipping path bounds not matching view bounds
- Path created with wrong coordinate system

## How to Fix
1. Ensure path is properly closed with close()
2. Avoid self-intersecting paths for clipping
3. Match path bounds to view bounds
4. Use correct coordinate system for path creation

```swift
// Create bezier path:
let path = UIBezierPath()
path.move(to: CGPoint(x: 0, y: 0))
path.addLine(to: CGPoint(x: 100, y: 0))
path.addLine(to: CGPoint(x: 100, y: 100))
path.close()

// Apply as mask:
let mask = CAShapeLayer()
mask.path = path.cgPath
view.layer.mask = mask
```

## Examples
```swift
// Custom shape path:
func roundedRectPath(bounds: CGRect, cornerRadius: CGFloat) -> UIBezierPath {
    let path = UIBezierPath(roundedRect: bounds, byRoundingCorners: [.topLeft, .topRight], cornerRadii: CGSize(width: cornerRadius, height: cornerRadius))
    return path
}

// Oval clipping:
let ovalPath = UIBezierPath(ovalIn: CGRect(x: 0, y: 0, width: 100, height: 100))
let mask = CAShapeLayer()
mask.path = ovalPath.cgPath
imageView.layer.mask = mask
```
