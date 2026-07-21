---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Leading Margin Error"
description: "Fix UICollectionLayoutListConfiguration section header leading margin configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Leading Margin Error

Section header leading margin errors occur when the margin is not properly set, when the margin conflicts with the header content, or when the margin does not match the design.

## Common Causes
- Leading margin not set
- Margin conflicts with header content
- Margin not matching design
- Margin not updating with layout changes

## How to Fix
1. Set leading margin properly
2. Ensure margin complements header content
3. Match design specifications
4. Update margin with layout changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 0, leading: 20, bottom: 0, trailing: 20)
header.contentConfiguration = content
```

## Examples
```swift
// Header with custom margins:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.textProperties.font = .preferredFont(forTextStyle: .headline)
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 8, leading: 16, bottom: 8, trailing: 16)
header.contentConfiguration = content
```
