---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Divider Configuration Error"
description: "Fix UICollectionLayoutListConfiguration section header divider configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Divider Configuration Error

Section header divider configuration errors occur when the divider is not properly configured, when the divider conflicts with the header content, or when the divider does not match the design.

## Common Causes
- Divider not configured
- Divider conflicts with header content
- Divider not matching design
- Divider not updating with layout changes

## How to Fix
1. Configure divider properly
2. Ensure divider complements header content
3. Match design specifications
4. Update divider with layout changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 8, leading: 0, bottom: 8, trailing: 0)
header.contentConfiguration = content
```

## Examples
```swift
// Header with custom divider:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 12, leading: 0, bottom: 4, trailing: 0)
header.backgroundColor = .clear
header.contentConfiguration = content
```
