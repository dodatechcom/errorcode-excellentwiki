---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Custom Height Error"
description: "Fix UICollectionLayoutListConfiguration section header custom height calculation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Custom Height Error

Section header custom height errors occur when the height is not properly calculated, when the height conflicts with the header content, or when the height does not match the design.

## Common Causes
- Height not calculated properly
- Height conflicts with header content
- Height not matching design
- Height not updating with content changes

## How to Fix
1. Calculate height based on content
2. Ensure height fits header content
3. Match design specifications
4. Update height with content changes

```swift
let headerSize = NSCollectionLayoutSize(
    widthDimension: .fractionalWidth(1.0),
    heightDimension: .estimated(44)
)
let header = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: headerSize,
    elementKind: UICollectionView.elementKindSectionHeader,
    alignment: .top
)
section.boundarySupplementaryItems = [header]
```

## Examples
```swift
// Dynamic header height:
let headerSize = NSCollectionLayoutSize(
    widthDimension: .fractionalWidth(1.0),
    heightDimension: .estimated(80)
)

// Fixed header height:
let headerSize = NSCollectionLayoutSize(
    widthDimension: .fractionalWidth(1.0),
    heightDimension: .absolute(60)
)
```
