---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Priority Conflict Error"
description: "Fix UICollectionLayoutListConfiguration section header constraint priority conflict errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Priority Conflict Error

Constraint priority conflict errors occur when there are conflicting priorities, when the priorities are not properly resolved, or when the priorities do not match the design.

## Common Causes
- Conflicting priorities
- Priorities not resolved
- Priorities not matching design
- Priorities not updating with size changes

## How to Fix
1. Resolve conflicting priorities
2. Set appropriate priorities
3. Match design specifications
4. Update priorities with size changes

```swift
let heightConstraint = header.heightAnchor.constraint(equalToConstant: 60)
heightConstraint.priority = UILayoutPriority(999)
heightConstraint.isActive = true
```

## Examples
```swift
// Priority hierarchy:
let requiredConstraint = header.heightAnchor.constraint(greaterThanOrEqualToConstant: 44)
requiredConstraint.priority = .required

let highConstraint = header.heightAnchor.constraint(equalToConstant: 60)
highConstraint.priority = UILayoutPriority(999)

let lowConstraint = header.heightAnchor.constraint(lessThanOrEqualToConstant: 100)
lowConstraint.priority = UILayoutPriority(250)
```
