---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Conflict Error"
description: "Fix UICollectionLayoutListConfiguration section header layout constraint conflict errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Conflict Error

Layout constraint conflict errors occur when there are conflicting constraints, when the constraints are not properly resolved, or when the constraints do not match the design.

## Common Causes
- Conflicting constraints
- Constraints not resolved
- Constraints not matching design
- Constraints not updating with size changes

## How to Fix
1. Remove conflicting constraints
2. Resolve constraint issues
3. Match design specifications
4. Update constraints with size changes

```swift
header.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    header.topAnchor.constraint(equalTo: view.topAnchor),
    header.bottomAnchor.constraint(equalTo: view.bottomAnchor)
])
```

## Examples
```swift
// Avoid conflicting constraints:
header.translatesAutoresizingMaskIntoConstraints = false
let heightConstraint = header.heightAnchor.constraint(equalToConstant: 60)
heightConstraint.priority = .defaultHigh
heightConstraint.isActive = true

// Remove old constraints:
header.constraints.forEach { $0.isActive = false }
```
