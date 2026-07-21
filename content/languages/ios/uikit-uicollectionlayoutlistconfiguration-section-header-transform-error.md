---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Transform Error"
description: "Fix UICollectionLayoutListConfiguration section header transform configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Transform Error

Transform errors occur when the transform is not properly configured, when the transform conflicts with the header layout, or when the transform does not match the design.

## Common Causes
- Transform not configured
- Transform conflicts with layout
- Transform not matching design
- Transform not updating with state changes

## How to Fix
1. Configure transform properly
2. Ensure transform is compatible with layout
3. Match design specifications
4. Update transform with state changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
header.transform = CGAffineTransform(rotationAngle: .pi / 180)
header.contentConfiguration = content
```

## Examples
```swift
// Header with scale transform:
header.transform = CGAffineTransform(scaleX: 1.1, y: 1.1)

// Header with translation transform:
header.transform = CGAffineTransform(translationX: 0, y: -10)
```
