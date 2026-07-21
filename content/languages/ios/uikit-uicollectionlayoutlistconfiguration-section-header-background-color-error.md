---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Background Color Error"
description: "Fix UICollectionLayoutListConfiguration section header background color configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Background Color Error

Section header background color errors occur when the color is not properly set, when the color conflicts with the header content, or when the color does not update with theme changes.

## Common Causes
- Color not set
- Color conflicts with header content
- Color not updating with theme
- Color not matching design

## How to Fix
1. Set color properly
2. Ensure color complements header content
3. Update color with theme changes
4. Match design specifications

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
header.backgroundColor = .systemBackground
header.contentConfiguration = content
```

## Examples
```swift
// Header with gradient background:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.textProperties.color = .white
header.backgroundColor = .systemBlue
header.contentConfiguration = content
```
