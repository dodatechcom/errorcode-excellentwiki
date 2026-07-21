---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint First Item Error"
description: "Fix UICollectionLayoutListConfiguration section header layout constraint first item errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint First Item Error

Layout constraint first item errors occur when the first item is not properly set, when the first item conflicts with the header layout, or when the first item does not match the design.

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
let constraint = header.topAnchor.constraint(equalTo: view.topAnchor)
constraint.firstItem = header
constraint.firstAttribute = .top
constraint.isActive = true
```

## Examples
```swift
// First item to second item
let constraint = header.topAnchor.constraint(equalTo: view.topAnchor)

// First item to constant
let constraint = header.heightAnchor.constraint(equalToConstant: 60)

// First item to first item
let constraint = header.centerYAnchor.constraint(equalTo: view.centerYAnchor)
```
