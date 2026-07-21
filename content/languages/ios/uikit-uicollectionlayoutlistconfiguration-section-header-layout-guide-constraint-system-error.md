---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint System Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide constraint system errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Constraint System Error

Layout guide constraint system errors occur when the constraint system is not properly configured, when the system conflicts with the layout, or when the system does not match the design.

## Common Causes
- System not configured
- System conflicts with layout
- System not matching design
- System not updating with size changes

## How to Fix
1. Configure system properly
2. Ensure system is compatible with layout
3. Match design specifications
4. Update system with size changes

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
// Layout guide for content
let contentGuide = UILayoutGuide()
header.addLayoutGuide(contentGuide)
NSLayoutConstraint.activate([
    contentGuide.topAnchor.constraint(equalTo: header.topAnchor, constant: 12),
    contentGuide.leadingAnchor.constraint(equalTo: header.leadingAnchor, constant: 16),
    contentGuide.trailingAnchor.constraint(equalTo: header.trailingAnchor, constant: -16),
    contentGuide.bottomAnchor.constraint(equalTo: header.bottomAnchor, constant: -12)
])
```
