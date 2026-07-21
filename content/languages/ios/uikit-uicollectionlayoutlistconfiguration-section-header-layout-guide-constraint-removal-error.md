---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Removal Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint removal errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Removal Error

Layout guide constraint removal errors occur when the constraints are not properly removed, when the removal conflicts with the layout, or when the removal does not match the design.

## Common Causes
- Constraints not removed
- Removal conflicts with layout
- Removal not matching design
- Removal not reflecting in UI

## How to Fix
1. Remove constraints properly
2. Ensure removal is compatible with layout
3. Match design specifications
4. Verify removal reflects in UI

```swift
// Remove specific constraint
if let constraint = header.constraints.first(where: { $0.identifier == "oldConstraint" }) {
    constraint.isActive = false
}

// Remove all constraints
header.removeConstraints(header.constraints)
```

## Examples
```swift
// Remove by attribute
header.constraints.filter { $0.firstAttribute == .height }.forEach { $0.isActive = false }

// Remove by identifier
header.constraints.filter { $0.identifier == "headerHeight" }.forEach { $0.isActive = false }

// Remove all inactive
header.constraints.filter { !$0.isActive }.forEach { header.removeConstraint($0) }
```
