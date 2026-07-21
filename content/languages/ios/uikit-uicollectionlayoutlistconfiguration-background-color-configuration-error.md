---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Background Color Configuration Error"
description: "Fix UICollectionLayoutListConfiguration background color configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Background Color Configuration Error

Background color configuration errors occur when the color is not properly set, when the color conflicts with the cell content, or when the color does not update with theme changes.

## Common Causes
- Color not set
- Color conflicts with cell content
- Color not updating with theme
- Color not matching design

## How to Fix
1. Set color properly
2. Ensure color complements cell content
3. Update color with theme changes
4. Match design specifications

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.backgroundColor = .systemGroupedBackground

let layout = UICollectionViewCompositionalLayout.list(using: config)
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// Dynamic background color:
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.backgroundColor = UIColor { traitCollection in
    traitCollection.userInterfaceStyle == .dark ? .systemGray6 : .systemGroupedBackground
}
```
