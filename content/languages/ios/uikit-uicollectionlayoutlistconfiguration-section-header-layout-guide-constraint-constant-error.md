---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Constant Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint constant errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Constant Error

Layout guide constraint constant errors occur when the constant is not properly set, when the constant conflicts with the layout, or when the constant does not match the design.

## Common Causes
- Constant not set
- Constant conflicts with layout
- Constant not matching design
- Constant not updating with content changes

## How to Fix
1. Set constant properly
2. Ensure constant is compatible with layout
3. Match design specifications
4. Update constant with content changes

```swift
let constraint = contentGuide.heightAnchor.constraint(equalToConstant: 60)
constraint.constant = 80
constraint.isActive = true
```

## Examples
```swift
// Set initial constant
let constraint = contentGuide.heightAnchor.constraint(equalToConstant: 60)

// Update constant
constraint.constant = 80

// Update with animation
UIView.animate(withDuration: 0.3) {
    constraint.constant = 100
    self.view.layoutIfNeeded()
}
```
