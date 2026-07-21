---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Layout Error"
description: "Fix UICollectionLayoutListConfiguration section header layout configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Layout Error

Section header layout errors occur when the layout is not properly configured, when the layout conflicts with the header content, or when the layout does not match the design.

## Common Causes
- Layout not configured properly
- Layout conflicts with header content
- Layout not matching design
- Layout not updating with content changes

## How to Fix
1. Configure layout properly
2. Ensure layout is compatible with content
3. Match design specifications
4. Update layout with content changes

```swift
let headerSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .estimated(44))
let header = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: headerSize,
    elementKind: UICollectionView.elementKindSectionHeader,
    alignment: .top
)
section.boundarySupplementaryItems = [header]
```

## Examples
```swift
// Section with custom header layout:
var section = NSCollectionLayoutSection(group: group)
section.contentInsets = NSDirectionalEdgeInsets(top: 0, leading: 16, bottom: 0, trailing: 16)

let headerSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .estimated(50))
let header = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: headerSize,
    elementKind: UICollectionView.elementKindSectionHeader,
    alignment: .top
)
section.boundarySupplementaryItems = [header]
```
