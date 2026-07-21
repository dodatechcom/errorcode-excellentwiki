---
title: "[Solution] UIKit UICollectionView Supplementary View Error"
description: "Fix UICollectionView supplementary view registration and display errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionView Supplementary View Error

Supplementary views fail to display when not registered, when the element kind does not match, or when the delegate method does not return a valid view.

## Common Causes
- Supplementary view not registered before use
- Element kind string does not match registration
- View not returned from delegate method
- Size not configured properly

## How to Fix
1. Register supplementary view class or nib
2. Match element kind strings exactly
3. Return the dequeued view from delegate
4. Set proper size using layout or delegate

```swift
// Register and dequeue supplementary view:
collectionView.register(HeaderView.self, forSupplementaryViewOfKind: UICollectionView.elementKindSectionHeader, withReuseIdentifier: "Header")

func collectionView(_ collectionView: UICollectionView, viewForSupplementaryElementOfKind kind: String, at indexPath: IndexPath) -> UICollectionReusableView {
    let header = collectionView.dequeueReusableSupplementaryView(ofKind: kind, withReuseIdentifier: "Header", for: indexPath) as! HeaderView
    header.titleLabel.text = sections[indexPath.section].title
    return header
}
```

## Examples
```swift
// Section header with layout:
let headerSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .estimated(44))
let header = NSCollectionLayoutBoundarySupplementaryItem(layoutSize: headerSize, elementKind: UICollectionView.elementKindSectionHeader, alignment: .top)
let section = NSCollectionLayoutSection(group: group)
section.boundarySupplementaryItems = [header]

// Register:
collectionView.register(SectionHeaderView.self, forSupplementaryViewOfKind: UICollectionView.elementKindSectionHeader, withReuseIdentifier: "SectionHeader")
```
