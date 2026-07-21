---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Priority Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint priority errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Priority Error

Layout guide constraint priority errors occur when the priorities are not properly set, when the priorities conflict with each other, or when the priorities do not match the design.

## Common Causes
- Priorities not set
- Priorities conflict
- Priorities not matching design
- Priorities not updating with size changes

## How to Fix
1. Set priorities properly
2. Resolve priority conflicts
3. Match design specifications
4. Update priorities with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)

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
