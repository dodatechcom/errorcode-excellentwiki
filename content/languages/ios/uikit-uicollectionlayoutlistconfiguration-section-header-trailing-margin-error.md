---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Trailing Margin Error"
description: "Fix UICollectionLayoutListConfiguration section header trailing margin configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Trailing Margin Error

Section header trailing margin errors occur when the margin is not properly set, when the margin conflicts with the header content, or when the margin does not match the design.

## Common Causes
- Trailing margin not set
- Margin conflicts with header content
- Margin not matching design
- Margin not updating with layout changes

## How to Fix
1. Set trailing margin properly
2. Ensure margin complements header content
3. Match design specifications
4. Update margin with layout changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 0, leading: 16, bottom: 0, trailing: 16)
header.contentConfiguration = content
```

## Examples
```swift
// Header with custom trailing margin:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 8, leading: 20, bottom: 8, trailing: 32)
header.contentConfiguration = content
```
