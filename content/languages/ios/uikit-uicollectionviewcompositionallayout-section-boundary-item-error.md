---
title: "[Solution] UIKit UICollectionViewCompositionalLayout Section Boundary Item Error"
description: "Fix collection view compositional layout boundary supplementary item errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionViewCompositionalLayout Section Boundary Item Error

Boundary items fail when the layout size is not properly configured, when the element kind does not match registration, or when the boundary item configuration conflicts with the section.

## Common Causes
- Boundary item layout size not set
- Element kind string mismatch
- Boundary item not registered
- Section boundary items array empty

## How to Fix
1. Set proper layout size for boundary items
2. Match element kind with registration
3. Register boundary item view class
4. Add boundary items to section configuration

```swift
let headerSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .estimated(44))
let header = NSCollectionLayoutBoundarySupplementaryItem(layoutSize: headerSize, elementKind: UICollectionView.elementKindSectionHeader, alignment: .top)
section.boundarySupplementaryItems = [header]
```

## Examples
```swift
// Section with header and footer:
let header = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .estimated(50)),
    elementKind: UICollectionView.elementKindSectionHeader,
    alignment: .top
)
let footer = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .estimated(50)),
    elementKind: UICollectionView.elementKindSectionFooter,
    alignment: .bottom
)
section.boundarySupplementaryItems = [header, footer]
```
