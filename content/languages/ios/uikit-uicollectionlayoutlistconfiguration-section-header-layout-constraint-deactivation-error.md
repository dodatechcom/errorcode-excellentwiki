---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Deactivation Error"
description: "Fix UICollectionLayoutListConfiguration section header constraint deactivation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Deactivation Error

Constraint deactivation errors occur when the constraints are not properly deactivated, when the constraints conflict with the header layout, or when the constraints do not match the design.

## Common Causes
- Constraints not deactivated
- Constraints conflict with layout
- Constraints not matching design
- Constraints not updating with size changes

## How to Fix
1. Deactivate constraints properly
2. Ensure constraints are compatible with layout
3. Match design specifications
4. Update constraints with size changes

```swift
// Deactivate all constraints
header.constraints.forEach { $0.isActive = false }

// Or deactivate specific constraints
NSLayoutConstraint.deactivate([topConstraint, leadingConstraint])
```

## Examples
```swift
// Deactivate by attribute
header.constraints.filter { $0.firstAttribute == .height }.forEach { $0.isActive = false }

// Deactivate by identifier
header.constraints.filter { $0.identifier == "oldConstraint" }.forEach { $0.isActive = false }
```
