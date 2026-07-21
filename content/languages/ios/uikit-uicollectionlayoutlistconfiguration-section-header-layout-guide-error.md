---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Error"
description: "Fix UICollectionLayoutListConfiguration section header layout guide configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Guide Error

Layout guide errors occur when the layout guide is not properly configured, when the guide conflicts with the header content, or when the guide does not match the design.

## Common Causes
- Layout guide not configured
- Guide conflicts with content
- Guide not matching design
- Guide not updating with layout changes

## How to Fix
1. Configure layout guide properly
2. Ensure guide complements content
3. Match design specifications
4. Update guide with layout changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 8, leading: 16, bottom: 8, trailing: 16)
header.contentConfiguration = content
```

## Examples
```swift
// Custom layout margins:
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.axesPreservingSuperviewLayoutMargins = .horizontal
content.directionalLayoutMargins = NSDirectionalEdgeInsets(top: 12, leading: 20, bottom: 12, trailing: 20)
header.contentConfiguration = content
```
