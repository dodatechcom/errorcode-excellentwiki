---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Anchors Error"
description: "Fix UICollectionLayoutListConfiguration section header layout anchor configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Anchors Error

Layout anchor errors occur when the anchors are not properly configured, when the anchors conflict with the header layout, or when the anchors do not match the design.

## Common Causes
- Anchors not configured
- Anchors conflict with layout
- Anchors not matching design
- Anchors not updating with size changes

## How to Fix
1. Configure anchors properly
2. Ensure anchors are compatible with layout
3. Match design specifications
4. Update anchors with size changes

```swift
header.translatesAutoresizingMaskIntoConstraints = false
let topAnchor = header.topAnchor.constraint(equalTo: view.topAnchor)
let leadingAnchor = header.leadingAnchor.constraint(equalTo: view.leadingAnchor)
let trailingAnchor = header.trailingAnchor.constraint(equalTo: view.trailingAnchor)
NSLayoutConstraint.activate([topAnchor, leadingAnchor, trailingAnchor])
```

## Examples
```swift
// Centered header:
header.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
header.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true

// Pinned to edges:
header.topAnchor.constraint(equalTo: view.topAnchor).isActive = true
header.leadingAnchor.constraint(equalTo: view.leadingAnchor).isActive = true
header.trailingAnchor.constraint(equalTo: view.trailingAnchor).isActive = true
```
