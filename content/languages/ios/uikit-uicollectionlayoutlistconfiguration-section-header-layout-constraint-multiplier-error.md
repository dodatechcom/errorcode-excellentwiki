---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Multiplier Error"
description: "Fix UICollectionLayoutListConfiguration section header layout constraint multiplier errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Multiplier Error

Layout constraint multiplier errors occur when the multiplier is not properly set, when the multiplier conflicts with the header layout, or when the multiplier does not match the design.

## Common Causes
- Multiplier not set
- Multiplier conflicts with layout
- Multiplier not matching design
- Multiplier not updating with content changes

## How to Fix
1. Set multiplier properly
2. Ensure multiplier is compatible with layout
3. Match design specifications
4. Update multiplier with content changes

```swift
let constraint = header.heightAnchor.constraint(equalTo: view.heightAnchor, multiplier: 0.5)
constraint.isActive = true
```

## Examples
```swift
// Half height
let constraint = header.heightAnchor.constraint(equalTo: view.heightAnchor, multiplier: 0.5)

// Double width
let constraint = header.widthAnchor.constraint(equalTo: label.widthAnchor, multiplier: 2.0)

// Aspect ratio
let constraint = header.widthAnchor.constraint(equalTo: header.heightAnchor, multiplier: 16.0/9.0)
```
