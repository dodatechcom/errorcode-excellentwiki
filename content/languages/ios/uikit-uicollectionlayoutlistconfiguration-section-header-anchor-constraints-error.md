---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Anchor Constraints Error"
description: "Fix UICollectionLayoutListConfiguration section header anchor constraint configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Anchor Constraints Error

Anchor constraint errors occur when the constraints are not properly configured, when the constraints conflict with the header layout, or when the constraints do not match the design.

## Common Causes
- Constraints not configured
- Constraints conflict with layout
- Constraints not matching design
- Constraints not updating with size changes

## How to Fix
1. Configure constraints properly
2. Ensure constraints are compatible with layout
3. Match design specifications
4. Update constraints with size changes

```swift
header.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    header.topAnchor.constraint(equalTo: view.topAnchor),
    header.leadingAnchor.constraint(equalTo: view.leadingAnchor),
    header.trailingAnchor.constraint(equalTo: view.trailingAnchor)
])
```

## Examples
```swift
// Header with fixed height constraint:
header.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    header.heightAnchor.constraint(equalToConstant: 60)
])

// Header with aspect ratio:
header.widthAnchor.constraint(equalTo: header.heightAnchor, multiplier: 2.0)
```
