---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Separator Configuration Error"
description: "Fix UICollectionLayoutListConfiguration section header separator configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Separator Configuration Error

Section header separator configuration errors occur when the separator is not properly configured, when the separator conflicts with the header content, or when the separator does not match the design.

## Common Causes
- Separator not configured
- Separator conflicts with header content
- Separator not matching design
- Separator not updating with layout changes

## How to Fix
1. Configure separator properly
2. Ensure separator complements header content
3. Match design specifications
4. Update separator with layout changes

```swift
var config = UICollectionLayoutListConfiguration(appearance: .plain)
config.headerMode = .supplementary
config.separatorConfiguration = .init(top: 0, leading: 0, bottom: 1, trailing: 0)
```

## Examples
```swift
// Header with bottom separator:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 0, leading: 0, bottom: 8, trailing: 0)
header.contentConfiguration = content
```
