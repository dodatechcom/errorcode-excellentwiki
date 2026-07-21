---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Disclosure Indicator Style Error"
description: "Fix UICollectionLayoutListConfiguration section header disclosure indicator style configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Disclosure Indicator Style Error

Disclosure indicator style errors occur when the style is not properly configured, when the style conflicts with the header content, or when the style does not match the design.

## Common Causes
- Disclosure style not configured
- Style conflicts with header content
- Style not matching design
- Style not updating with state changes

## How to Fix
1. Configure disclosure style properly
2. Ensure style complements header content
3. Match design specifications
4. Update style with state changes

```swift
header.accessories = [
    .outlineDisclosure(options: .init(
        style: .header,
        tintColor: .systemBlue
    ))
]
```

## Examples
```swift
// Disclosure with custom style:
header.accessories = [
    .outlineDisclosure(options: .init(
        style: .header,
        tintColor: .systemGreen,
        font: .preferredFont(forTextStyle: .callout)
    ))
]
```
