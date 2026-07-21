---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Activation Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint activation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Activation Error

Layout guide constraint activation errors occur when the constraints are not properly activated, when the activation conflicts with the layout, or when the activation does not match the design.

## Common Causes
- Constraints not activated
- Activation conflicts with layout
- Activation not matching design
- Activation not updating with size changes

## How to Fix
1. Activate constraints properly
2. Ensure activation is compatible with layout
3. Match design specifications
4. Update activation with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)

NSLayoutConstraint.activate([
    contentGuide.topAnchor.constraint(equalTo: header.topAnchor, constant: 8),
    contentGuide.leadingAnchor.constraint(equalTo: header.leadingAnchor, constant: 16)
])
```

## Examples
```swift
// Individual activation
topConstraint.isActive = true

// Batch activation
NSLayoutConstraint.activate([topConstraint, leadingConstraint, trailingConstraint])

// Conditional activation
if isExpanded {
    heightConstraint.isActive = true
} else {
    compactHeightConstraint.isActive = true
}
```
