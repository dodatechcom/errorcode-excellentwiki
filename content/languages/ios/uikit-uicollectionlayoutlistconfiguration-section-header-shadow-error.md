---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Shadow Error"
description: "Fix UICollectionLayoutListConfiguration section header shadow configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Shadow Error

Shadow errors occur when the shadow is not properly configured, when the shadow conflicts with the header content, or when the shadow does not match the design.

## Common Causes
- Shadow not configured
- Shadow conflicts with header content
- Shadow not matching design
- Shadow not updating with theme changes

## How to Fix
1. Configure shadow properly
2. Ensure shadow complements header content
3. Match design specifications
4. Update shadow with theme changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
header.layer.shadowColor = UIColor.black.cgColor
header.layer.shadowOffset = CGSize(width: 0, height: 2)
header.layer.shadowOpacity = 0.1
header.layer.shadowRadius = 4
header.contentConfiguration = content
```

## Examples
```swift
// Header with subtle shadow:
header.layer.shadowColor = UIColor.label.cgColor
header.layer.shadowOffset = CGSize(width: 0, height: 1)
header.layer.shadowOpacity = 0.05
header.layer.shadowRadius = 2
header.layer.masksToBounds = false
```
