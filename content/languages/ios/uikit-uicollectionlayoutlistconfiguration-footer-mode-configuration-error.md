---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Footer Mode Configuration Error"
description: "Fix UICollectionLayoutListConfiguration footer mode configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Footer Mode Configuration Error

Footer mode configuration errors occur when the footer mode is not properly set, when the mode conflicts with the section layout, or when the mode does not match the design.

## Common Causes
- Footer mode not set
- Mode conflicts with layout
- Mode not matching design
- Mode not updating with section changes

## How to Fix
1. Set footer mode properly
2. Ensure mode is compatible with layout
3. Match design specifications
4. Update mode with section changes

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.footerMode = .supplementary

let layout = UICollectionViewCompositionalLayout.list(using: config)
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// Footer modes:
config.footerMode = .none // No footer
config.footerMode = .supplementary // Section footer
config.footerMode = .lastItemInSection // Last cell as footer
```
