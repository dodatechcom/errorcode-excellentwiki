---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Deactivation Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint deactivation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Deactivation Error

Layout guide constraint deactivation errors occur when the constraints are not properly deactivated, when the deactivation conflicts with the layout, or when the deactivation does not match the design.

## Common Causes
- Constraints not deactivated
- Deactivation conflicts with layout
- Deactivation not matching design
- Deactivation not updating with size changes

## How to Fix
1. Deactivate constraints properly
2. Ensure deactivation is compatible with layout
3. Match design specifications
4. Update deactivation with size changes

```swift
// Deactivate specific constraints
NSLayoutConstraint.deactivate([topConstraint, leadingConstraint])

// Deactivate all constraints for view
header.constraints.forEach { $0.isActive = false }
```

## Examples
```swift
// Deactivate by identifier
header.constraints.filter { $0.identifier == "oldConstraint" }.forEach { $0.isActive = false }

// Deactivate by attribute
header.constraints.filter { $0.firstAttribute == .height }.forEach { $0.isActive = false }

// Deactivate all
header.removeConstraints(header.constraints)
```
