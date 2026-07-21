---
title: "[Solution] UIKit UICollectionView Compositional Layout Error"
description: "Fix UICollectionView compositional layout configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionView Compositional Layout Error

Compositional layout errors occur when section or group configurations create invalid sizes, when estimated sizes conflict with constraints, or when supplementary views are not registered.

## Common Causes
- Item or group size exceeding section bounds
- Estimated size used without proper constraints
- Missing supplementary view registration
- Section snapshot configuration invalid

## How to Fix
1. Ensure item and group sizes fit within section bounds
2. Register all supplementary views before layout
3. Use absolute sizes or fractional sizes correctly
4. Verify section insets allow content to display

```swift
// Compositional layout setup:
let layout = UICollectionViewCompositionalLayout { sectionIndex, environment in
    let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .absolute(80))
    let item = NSCollectionLayoutItem(layoutSize: itemSize)
    let group = NSCollectionLayoutGroup.horizontal(layoutSize: itemSize, subitems: [item])
    let section = NSCollectionLayoutSection(group: group)
    section.interGroupSpacing = 8
    return section
}
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// Compositional layout with header:
let layout = UICollectionViewCompositionalLayout { sectionIndex, env in
    let headerSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .estimated(44))
    let header = NSCollectionLayoutBoundarySupplementaryItem(layoutSize: headerSize, elementKind: UICollectionView.elementKindSectionHeader, alignment: .top)
    let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .absolute(60))
    let item = NSCollectionLayoutItem(layoutSize: itemSize)
    let group = NSCollectionLayoutGroup.vertical(layoutSize: itemSize, subitems: [item])
    let section = NSCollectionLayoutSection(group: group)
    section.boundarySupplementaryItems = [header]
    return section
}
```
