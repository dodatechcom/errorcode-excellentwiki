---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Size Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide size constraint errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Size Error

Layout guide size errors occur when the size constraints are not properly configured, when the constraints conflict with the header layout, or when the constraints do not match the design.

## Common Causes
- Size constraints not configured
- Constraints conflict with layout
- Constraints not matching design
- Constraints not updating with size changes

## How to Fix
1. Configure size constraints properly
2. Ensure constraints are compatible with layout
3. Match design specifications
4. Update constraints with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.widthAnchor.constraint(equalToConstant: 200),
    contentGuide.heightAnchor.constraint(equalToConstant: 100)
])
```

## Examples
```swift
// Fixed size
NSLayoutConstraint.activate([
    contentGuide.widthAnchor.constraint(equalToConstant: 200),
    contentGuide.heightAnchor.constraint(equalToConstant: 100)
])

// Proportional size
NSLayoutConstraint.activate([
    contentGuide.widthAnchor.constraint(equalTo: header.widthAnchor, multiplier: 0.8),
    contentGuide.heightAnchor.constraint(equalTo: header.heightAnchor, multiplier: 0.5)
])

// Minimum size
NSLayoutConstraint.activate([
    contentGuide.widthAnchor.constraint(greaterThanOrEqualToConstant: 100),
    contentGuide.heightAnchor.constraint(greaterThanOrEqualToConstant: 44)
])
```
