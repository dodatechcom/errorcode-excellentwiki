---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Update Error"
description: "Fix UICollectionLayoutListConfiguration section header layout constraint update errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Update Error

Layout constraint update errors occur when the constraints are not properly updated, when the updates conflict with the header layout, or when the updates do not match the design.

## Common Causes
- Constraints not updated
- Updates conflict with layout
- Updates not matching design
- Updates not reflecting in UI

## How to Fix
1. Update constraints properly
2. Ensure updates are compatible with layout
3. Match design specifications
4. Verify updates reflect in UI

```swift
headerConstraint?.constant = 80
view.layoutIfNeeded()
```

## Examples
```swift
// Update constraint constant:
if let constraint = header.constraints.first(where: { $0.firstAttribute == .height }) {
    constraint.constant = 80
}

// Update multiple constraints:
NSLayoutConstraint.activate([
    header.heightAnchor.constraint(equalToConstant: 80)
])
view.layoutIfNeeded()
```
