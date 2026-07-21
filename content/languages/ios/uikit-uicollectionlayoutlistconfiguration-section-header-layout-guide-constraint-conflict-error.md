---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Conflict Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint conflict errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Conflict Error

Layout guide constraint conflict errors occur when the constraints conflict with each other, when the conflicts cannot be resolved, or when the conflicts do not match the design.

## Common Causes
- Constraints conflict
- Conflicts cannot be resolved
- Conflicts not matching design
- Conflicts not updating with size changes

## How to Fix
1. Resolve constraint conflicts
2. Ensure conflicts can be resolved
3. Match design specifications
4. Update conflicts with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)

let top = contentGuide.topAnchor.constraint(equalTo: header.topAnchor, constant: 8)
top.priority = .defaultHigh

let bottom = contentGuide.bottomAnchor.constraint(equalTo: header.bottomAnchor, constant: -8)
bottom.priority = .defaultHigh

NSLayoutConstraint.activate([top, bottom])
```

## Examples
```swift
// Resolve conflicts with priority
let heightConstraint = contentGuide.heightAnchor.constraint(equalToConstant: 60)
heightConstraint.priority = UILayoutPriority(999)
heightConstraint.isActive = true

// Remove conflicting constraints
header.constraints.filter { $0.firstAttribute == .height }.forEach { $0.isActive = false }
```
