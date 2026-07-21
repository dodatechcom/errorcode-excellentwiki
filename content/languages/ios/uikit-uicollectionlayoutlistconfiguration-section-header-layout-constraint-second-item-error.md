---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Second Item Error"
description: "Fix UICollectionLayoutListConfiguration section header layout constraint second item errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Constraint Second Item Error

Layout constraint second item errors occur when the second item is not properly set, when the second item conflicts with the header layout, or when the second item does not match the design.

## Common Causes
- Second item not set
- Second item conflicts with layout
- Second item not matching design
- Second item not updating with content changes

## How to Fix
1. Set second item properly
2. Ensure second item is compatible with layout
3. Match design specifications
4. Update second item with content changes

```swift
let constraint = header.topAnchor.constraint(equalTo: view.topAnchor)
constraint.secondItem = view
constraint.secondAttribute = .top
constraint.isActive = true
```

## Examples
```swift
// Second item is another view
let constraint = header.leadingAnchor.constraint(equalTo: label.trailingAnchor)

// Second item is layout guide
let constraint = header.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor)

// Second item is nil (constant)
let constraint = header.heightAnchor.constraint(equalToConstant: 60)
```
