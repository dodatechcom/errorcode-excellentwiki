---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Header Mode Configuration Error"
description: "Fix UICollectionLayoutListConfiguration header mode configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Header Mode Configuration Error

Header mode configuration errors occur when the header mode is not properly set, when the mode conflicts with the section layout, or when the mode does not match the design.

## Common Causes
- Header mode not set
- Mode conflicts with layout
- Mode not matching design
- Mode not updating with section changes

## How to Fix
1. Set header mode properly
2. Ensure mode is compatible with layout
3. Match design specifications
4. Update mode with section changes

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.headerMode = .supplementary

let layout = UICollectionViewCompositionalLayout.list(using: config)
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// Header modes:
config.headerMode = .none // No header
config.headerMode = .supplementary // Section header
config.headerMode = .firstItemInSection // First cell as header
```
