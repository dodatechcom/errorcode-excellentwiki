---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Attribute Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint attribute errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Attribute Error

Layout guide constraint attribute errors occur when the attribute is not properly set, when the attribute conflicts with the layout, or when the attribute does not match the design.

## Common Causes
- Attribute not set
- Attribute conflicts with layout
- Attribute not matching design
- Attribute not updating with content changes

## How to Fix
1. Set attribute properly
2. Ensure attribute is compatible with layout
3. Match design specifications
4. Update attribute with content changes

```swift
let constraint = contentGuide.topAnchor.constraint(equalTo: header.topAnchor)
constraint.firstAttribute = .top
constraint.secondAttribute = .top
constraint.isActive = true
```

## Examples
```swift
// X attribute
let constraint = contentGuide.centerXAnchor.constraint(equalTo: header.centerXAnchor)

// Y attribute
let constraint = contentGuide.centerYAnchor.constraint(equalTo: header.centerYAnchor)

// Width attribute
let constraint = contentGuide.widthAnchor.constraint(equalToConstant: 200)

// Height attribute
let constraint = contentGuide.heightAnchor.constraint(equalToConstant: 60)
```
