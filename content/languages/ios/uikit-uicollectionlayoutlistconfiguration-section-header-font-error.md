---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Font Error"
description: "Fix UICollectionLayoutListConfiguration section header font configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Font Error

Section header font errors occur when the font is not properly configured, when the font conflicts with the header content, or when the font does not match the design.

## Common Causes
- Font not configured
- Font conflicts with header content
- Font not matching design
- Font not updating with Dynamic Type

## How to Fix
1. Configure font properly
2. Ensure font complements header content
3. Match design specifications
4. Support Dynamic Type

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.textProperties.font = .preferredFont(forTextStyle: .headline)
header.contentConfiguration = content
```

## Examples
```swift
// Header with custom font:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.textProperties.font = UIFont.systemFont(ofSize: 16, weight: .semibold)
content.textProperties.color = .label
content.secondaryTextProperties.font = UIFont.systemFont(ofSize: 12, weight: .regular)
header.contentConfiguration = content
```
