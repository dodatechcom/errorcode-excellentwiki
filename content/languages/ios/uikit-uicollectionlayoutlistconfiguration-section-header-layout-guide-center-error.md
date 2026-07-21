---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Center Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide centering constraints errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Center Error

Layout guide centering errors occur when the centering constraints are not properly configured, when the constraints conflict with the header layout, or when the constraints do not match the design.

## Common Causes
- Centering constraints not configured
- Constraints conflict with layout
- Constraints not matching design
- Constraints not updating with size changes

## How to Fix
1. Configure centering constraints properly
2. Ensure constraints are compatible with layout
3. Match design specifications
4. Update constraints with size changes

```swift
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.centerXAnchor.constraint(equalTo: header.centerXAnchor),
    contentGuide.centerYAnchor.constraint(equalTo: header.centerYAnchor)
])
```

## Examples
```swift
// Center with size
NSLayoutConstraint.activate([
    contentGuide.centerXAnchor.constraint(equalTo: header.centerXAnchor),
    contentGuide.centerYAnchor.constraint(equalTo: header.centerYAnchor),
    contentGuide.widthAnchor.constraint(equalToConstant: 200),
    contentGuide.heightAnchor.constraint(equalToConstant: 100)
])
```
