---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Priority Conflict Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint priority conflict errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Priority Conflict Error

Layout guide constraint priority conflict errors occur when there are conflicting priorities, when the priorities cannot be resolved, or when the priorities do not match the design.

## Common Causes
- Conflicting priorities
- Priorities cannot be resolved
- Priorities not matching design
- Priorities not updating with size changes

## How to Fix
1. Resolve conflicting priorities
2. Set appropriate priorities
3. Match design specifications
4. Update priorities with size changes

```swift
let heightConstraint = contentGuide.heightAnchor.constraint(equalToConstant: 60)
heightConstraint.priority = UILayoutPriority(999)
heightConstraint.isActive = true
```

## Examples
```swift
// Priority hierarchy
let required = contentGuide.heightAnchor.constraint(greaterThanOrEqualToConstant: 44)
required.priority = .required

let high = contentGuide.heightAnchor.constraint(equalToConstant: 60)
high.priority = UILayoutPriority(999)

let low = contentGuide.heightAnchor.constraint(lessThanOrEqualToConstant: 100)
low.priority = UILayoutPriority(250)
```
