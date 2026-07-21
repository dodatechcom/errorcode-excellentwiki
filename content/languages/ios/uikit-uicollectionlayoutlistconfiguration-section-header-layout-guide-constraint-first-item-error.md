---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint First Item Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint first item errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint First Item Error

Layout guide constraint first item errors occur when the first item is not properly set, when the first item conflicts with the layout, or when the first item does not match the design.

## Common Causes
- First item not set
- First item conflicts with layout
- First item not matching design
- First item not updating with content changes

## How to Fix
1. Set first item properly
2. Ensure first item is compatible with layout
3. Match design specifications
4. Update first item with content changes

```swift
let constraint = contentGuide.topAnchor.constraint(equalTo: header.topAnchor)
constraint.firstItem = contentGuide
constraint.firstAttribute = .top
constraint.isActive = true
```

## Examples
```swift
// First item is layout guide
let constraint = contentGuide.topAnchor.constraint(equalTo: header.topAnchor)

// First item with second item
let constraint = contentGuide.leadingAnchor.constraint(equalTo: icon.trailingAnchor)

// First item to constant
let constraint = contentGuide.heightAnchor.constraint(equalToConstant: 60)
```
