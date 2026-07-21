---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Border Configuration Error"
description: "Fix UICollectionLayoutListConfiguration section header border configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Border Configuration Error

Border configuration errors occur when the border is not properly configured, when the border conflicts with the header content, or when the border does not match the design.

## Common Causes
- Border not configured
- Border conflicts with header content
- Border not matching design
- Border not updating with theme changes

## How to Fix
1. Configure border properly
2. Ensure border complements header content
3. Match design specifications
4. Update border with theme changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
header.layer.borderWidth = 1
header.layer.borderColor = UIColor.separator.cgColor
header.layer.cornerRadius = 8
header.contentConfiguration = content
```

## Examples
```swift
// Header with rounded border:
header.layer.borderWidth = 1
header.layer.borderColor = UIColor.systemGray4.cgColor
header.layer.cornerRadius = 8
header.layer.masksToBounds = true
```
