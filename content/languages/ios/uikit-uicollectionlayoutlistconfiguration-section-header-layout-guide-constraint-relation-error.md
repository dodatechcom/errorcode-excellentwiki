---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Relation Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint relation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Relation Error

Layout guide constraint relation errors occur when the relation is not properly set, when the relation conflicts with the layout, or when the relation does not match the design.

## Common Causes
- Relation not set
- Relation conflicts with layout
- Relation not matching design
- Relation not updating with content changes

## How to Fix
1. Set relation properly
2. Ensure relation is compatible with layout
3. Match design specifications
4. Update relation with content changes

```swift
let constraint = contentGuide.heightAnchor.constraint(equalToConstant: 60)
constraint.isActive = true
```

## Examples
```swift
// Equal relation
let constraint = contentGuide.heightAnchor.constraint(equalTo: header.heightAnchor)

// Greater than or equal
let constraint = contentGuide.heightAnchor.constraint(greaterThanOrEqualToConstant: 44)

// Less than or equal
let constraint = contentGuide.heightAnchor.constraint(lessThanOrEqualToConstant: 200)
```
