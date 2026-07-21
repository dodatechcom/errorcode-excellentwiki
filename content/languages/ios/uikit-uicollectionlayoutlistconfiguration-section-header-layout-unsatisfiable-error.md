---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Unsatisfiable Error"
description: "Fix UICollectionLayoutListConfiguration section header layout unsatisfiable constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Unsatisfiable Error

Unsatisfiable constraint errors occur when the constraints cannot be satisfied simultaneously, when the constraints are not properly configured, or when the constraints do not match the design.

## Common Causes
- Constraints cannot be satisfied
- Constraints not properly configured
- Constraints not matching design
- Constraints not updating with size changes

## How to Fix
1. Resolve unsatisfiable constraints
2. Configure constraints properly
3. Match design specifications
4. Update constraints with size changes

```swift
header.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    header.topAnchor.constraint(equalTo: view.topAnchor),
    header.leadingAnchor.constraint(equalTo: view.leadingAnchor),
    header.trailingAnchor.constraint(equalTo: view.trailingAnchor)
])
```

## Examples
```swift
// Avoid unsatisfiable constraints:
let heightConstraint = header.heightAnchor.constraint(equalToConstant: 60)
heightConstraint.priority = .defaultHigh
heightConstraint.isActive = true

// Remove conflicting constraints:
header.constraints.filter { $0.firstAttribute == .height }.forEach { $0.isActive = false }
```
