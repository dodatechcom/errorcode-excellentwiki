---
title: "[Solution] UIKit UICollectionLayoutListConfiguration HeaderTopPadding Error"
description: "Fix UICollectionLayoutListConfiguration headerTopPadding spacing errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration HeaderTopPadding Error

Header top padding errors occur when the padding value is too large, when it conflicts with safe area insets, or when the padding does not match the design specifications.

## Common Causes
- Padding value too large for available space
- Padding conflicts with safe area
- Padding not matching design specs
- Padding not updating with layout changes

## How to Fix
1. Set padding value to match design specs
2. Account for safe area in padding calculations
3. Verify padding matches design specifications
4. Update padding after layout changes

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.headerTopPadding = 16

let layout = UICollectionViewCompositionalLayout.list(using: config)
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// Section with custom header padding:
var config = UICollectionLayoutListConfiguration(appearance: .plain)
config.headerTopPadding = 8
config.headerMode = .supplementary

// Inset grouped with no header padding:
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.headerTopPadding = 0
```
