---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Margins Error"
description: "Fix UICollectionLayoutListConfiguration section header layout margins configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Margins Error

Layout margins errors occur when the margins are not properly configured, when the margins conflict with the header content, or when the margins do not match the design.

## Common Causes
- Margins not configured
- Margins conflict with header content
- Margins not matching design
- Margins not updating with layout changes

## How to Fix
1. Configure margins properly
2. Ensure margins complement header content
3. Match design specifications
4. Update margins with layout changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 8, leading: 16, bottom: 8, trailing: 16)
content.preservesSuperviewLayoutMargins = true
header.contentConfiguration = content
```

## Examples
```swift
// Custom margins:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 0, leading: 0, bottom: 0, trailing: 0)
content.preservesSuperviewLayoutMargins = false
header.contentConfiguration = content
```
