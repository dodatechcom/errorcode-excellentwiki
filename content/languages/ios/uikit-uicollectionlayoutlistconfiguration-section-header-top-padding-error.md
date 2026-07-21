---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Top Padding Error"
description: "Fix UICollectionLayoutListConfiguration section header top padding configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Top Padding Error

Section header top padding errors occur when the padding is not properly set, when the padding conflicts with the header content, or when the padding does not match the design.

## Common Causes
- Top padding not set
- Padding conflicts with header content
- Padding not matching design
- Padding not updating with layout changes

## How to Fix
1. Set top padding properly
2. Ensure padding complements header content
3. Match design specifications
4. Update padding with layout changes

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.headerTopPadding = 16

let layout = UICollectionViewCompositionalLayout.list(using: config)
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// Section with custom top padding:
var config = UICollectionLayoutListConfiguration(appearance: .plain)
config.headerTopPadding = 8
config.headerMode = .supplementary

// Inset grouped with no padding:
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.headerTopPadding = 0
```
