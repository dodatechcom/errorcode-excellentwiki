---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Header Footer Error"
description: "Fix UICollectionLayoutListConfiguration header and footer sizing errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Header Footer Error

Header and footer sizing errors occur when the estimated size is too small, when the header mode is not configured, or when the supplementary views do not match the layout expectations.

## Common Causes
- Header mode not set to .supplementary
- Estimated size too small for content
- Supplementary view not returning correct size
- Footer not properly configured

## How to Fix
1. Set headerMode to .supplementary
2. Use estimated or absolute size for headers
3. Return proper size from supplementary view delegate
4. Configure footer similarly to header

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.headerMode = .supplementary
config.headerTopPadding = 0

let layout = UICollectionViewCompositionalLayout.list(using: config)
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// Section header with estimated height:
let headerSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .estimated(50))
let header = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: headerSize,
    elementKind: UICollectionView.elementKindSectionHeader,
    alignment: .top
)
section.boundarySupplementaryItems = [header]
```
