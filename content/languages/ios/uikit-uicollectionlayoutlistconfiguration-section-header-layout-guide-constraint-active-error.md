---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Active Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint active state errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Active Error

Layout guide constraint active state errors occur when the active state is not properly set, when the active state conflicts with the layout, or when the active state does not match the design.

## Common Causes
- Active state not set
- Active state conflicts with layout
- Active state not matching design
- Active state not updating with content changes

## How to Fix
1. Set active state properly
2. Ensure active state is compatible with layout
3. Match design specifications
4. Update active state with content changes

```swift
let constraint = contentGuide.heightAnchor.constraint(equalToConstant: 60)
constraint.isActive = true
```

## Examples
```swift
// Activate constraint
constraint.isActive = true

// Deactivate constraint
constraint.isActive = false

// Toggle constraint
constraint.isActive.toggle()

// Activate multiple constraints
NSLayoutConstraint.activate([constraint1, constraint2, constraint3])
```
