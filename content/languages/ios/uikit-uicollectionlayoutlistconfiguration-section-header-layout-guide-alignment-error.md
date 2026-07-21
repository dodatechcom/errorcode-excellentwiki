---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Alignment Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide alignment constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Alignment Error

Layout guide alignment errors occur when the alignment constraints are not properly configured, when the constraints conflict with the header layout, or when the constraints do not match the design.

## Common Causes
- Alignment constraints not configured
- Constraints conflict with layout
- Constraints not matching design
- Constraints not updating with size changes

## How to Fix
1. Configure alignment constraints properly
2. Ensure constraints are compatible with layout
3. Match design specifications
4. Update constraints with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.leadingAnchor.constraint(equalTo: header.leadingAnchor, constant: 16),
    contentGuide.trailingAnchor.constraint(equalTo: header.trailingAnchor, constant: -16)
])
```

## Examples
```swift
// Leading alignment
contentGuide.leadingAnchor.constraint(equalTo: header.leadingAnchor, constant: 16).isActive = true

// Trailing alignment
contentGuide.trailingAnchor.constraint(equalTo: header.trailingAnchor, constant: -16).isActive = true

// Center alignment
contentGuide.centerXAnchor.constraint(equalTo: header.centerXAnchor).isActive = true
```
