---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint Error

Layout guide constraint errors occur when the layout guide constraints are not properly configured, when the constraints conflict with the header layout, or when the constraints do not match the design.

## Common Causes
- Layout guide constraints not configured
- Constraints conflict with layout
- Constraints not matching design
- Constraints not updating with size changes

## How to Fix
1. Configure layout guide constraints properly
2. Ensure constraints are compatible with layout
3. Match design specifications
4. Update constraints with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.topAnchor.constraint(equalTo: header.topAnchor, constant: 8),
    contentGuide.leadingAnchor.constraint(equalTo: header.leadingAnchor, constant: 16)
])
```

## Examples
```swift
// Layout guide with safe area
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.topAnchor.constraint(equalTo: header.safeAreaLayoutGuide.topAnchor),
    contentGuide.leadingAnchor.constraint(equalTo: header.leadingAnchor, constant: 16)
])
```
