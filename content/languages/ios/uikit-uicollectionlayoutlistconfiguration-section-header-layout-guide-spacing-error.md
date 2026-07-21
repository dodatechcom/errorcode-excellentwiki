---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Spacing Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide spacing constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Spacing Error

Layout guide spacing errors occur when the spacing constraints are not properly configured, when the constraints conflict with the header layout, or when the constraints do not match the design.

## Common Causes
- Spacing constraints not configured
- Constraints conflict with layout
- Constraints not matching design
- Constraints not updating with size changes

## How to Fix
1. Configure spacing constraints properly
2. Ensure constraints are compatible with layout
3. Match design specifications
4. Update constraints with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.topAnchor.constraint(equalTo: header.topAnchor, constant: 8),
    contentGuide.bottomAnchor.constraint(equalTo: header.bottomAnchor, constant: -8)
])
```

## Examples
```swift
// Equal spacing
NSLayoutConstraint.activate([
    contentGuide.topAnchor.constraint(equalTo: header.topAnchor, constant: 8),
    contentGuide.leadingAnchor.constraint(equalTo: header.leadingAnchor, constant: 16),
    contentGuide.trailingAnchor.constraint(equalTo: header.trailingAnchor, constant: -16),
    contentGuide.bottomAnchor.constraint(equalTo: header.bottomAnchor, constant: -8)
])

// Custom spacing
contentGuide.layoutMargins = UIEdgeInsets(top: 12, left: 20, bottom: 12, right: 20)
```
