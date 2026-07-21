---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Identifier Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint identifier configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Identifier Error

Layout guide constraint identifier errors occur when the identifier is not properly set, when the identifier conflicts with the layout, or when the identifier does not match the design.

## Common Causes
- Identifier not set
- Identifier conflicts with layout
- Identifier not matching design
- Identifier not updating with layout changes

## How to Fix
1. Set identifier properly
2. Ensure identifier is compatible with layout
3. Match design specifications
4. Update identifier with layout changes

```swift
let constraint = contentGuide.heightAnchor.constraint(equalToConstant: 60)
constraint.identifier = "headerHeight"
constraint.isActive = true
```

## Examples
```swift
// Set identifier for debugging
let topConstraint = contentGuide.topAnchor.constraint(equalTo: header.topAnchor)
topConstraint.identifier = "contentGuide.top"

// Find constraint by identifier
if let constraint = header.constraints.first(where: { $0.identifier == "headerHeight" }) {
    constraint.constant = 80
}
```
