---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Content Compression Error"
description: "Fix UICollectionLayoutListConfiguration section header content compression resistance errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Content Compression Error

Content compression errors occur when the compression resistance is not properly configured, when the compression conflicts with the header content, or when the compression does not match the design.

## Common Causes
- Compression resistance not configured
- Compression conflicts with content
- Compression not matching design
- Compression not updating with content changes

## How to Fix
1. Configure compression resistance properly
2. Ensure compression complements content
3. Match design specifications
4. Update compression with content changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
content.textProperties.alignment = .natural
header.contentCompressionResistancePriority(for: .horizontal) = .required
header.contentCompressionResistancePriority(for: .vertical) = .required
header.contentConfiguration = content
```

## Examples
```swift
// High compression resistance:
header.contentCompressionResistancePriority(for: .vertical) = UILayoutPriority(999)

// Low compression resistance:
header.contentCompressionResistancePriority(for: .horizontal) = UILayoutPriority(250)
```
