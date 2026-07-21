---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Content Hugging Error"
description: "Fix UICollectionLayoutListConfiguration section header content hugging priority errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Content Hugging Error

Content hugging errors occur when the hugging priority is not properly configured, when the hugging conflicts with the header content, or when the hugging does not match the design.

## Common Causes
- Hugging priority not configured
- Hugging conflicts with content
- Hugging not matching design
- Hugging not updating with content changes

## How to Fix
1. Configure hugging priority properly
2. Ensure hugging complements content
3. Match design specifications
4. Update hugging with content changes

```swift
var content = UIListContentConfiguration.supplementaryHeader()
content.text = "Section"
header.contentHuggingPriority(for: .vertical) = .required
header.contentHuggingPriority(for: .horizontal) = .defaultHigh
header.contentConfiguration = content
```

## Examples
```swift
// High hugging priority:
header.contentHuggingPriority(for: .horizontal) = UILayoutPriority(999)

// Low hugging priority:
header.contentHuggingPriority(for: .vertical) = UILayoutPriority(250)
```
