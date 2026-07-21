---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Scroll Position Configuration Error"
description: "Fix UICollectionLayoutListConfiguration scroll position configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Scroll Position Configuration Error

Scroll position configuration errors occur when the scroll position is not properly set, when the position conflicts with the section layout, or when the position does not match the design.

## Common Causes
- Scroll position not set
- Position conflicts with layout
- Position not matching design
- Position not updating with content changes

## How to Fix
1. Set scroll position properly
2. Ensure position is compatible with layout
3. Match design specifications
4. Update position with content changes

```swift
var config = UICollectionLayoutListConfiguration(appearance: .plain)
config.supplementaryViewConfigurations = [
    .init(elementKind: UICollectionView.elementKindSectionHeader)
]

let layout = UICollectionViewCompositionalLayout.list(using: config)
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// Scroll position settings:
collectionView.scrollToItem(at: IndexPath(item: 0, section: 0), at: .centeredVertically, animated: true)
collectionView.scrollToItem(at: IndexPath(item: 0, section: 0), at: .top, animated: true)
collectionView.scrollToItem(at: IndexPath(item: 0, section: 0), at: .bottom, animated: true)
```
