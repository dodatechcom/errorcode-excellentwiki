---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Footer Error"
description: "Fix UICollectionLayoutListConfiguration section footer configuration and display errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Footer Error

Section footer errors occur when the footer is not registered, when the footer size is not set, or when the footer delegate method is not implemented.

## Common Causes
- Footer not registered
- Footer size not configured
- Delegate method not implemented
- Footer not displaying due to layout issues

## How to Fix
1. Register footer supplementary view
2. Configure footer size in layout
3. Implement footer delegate method
4. Verify footer displays correctly

```swift
let footerSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0), heightDimension: .estimated(44))
let footer = NSCollectionLayoutBoundarySupplementaryItem(layoutSize: footerSize, elementKind: UICollectionView.elementKindSectionFooter, alignment: .bottom)
section.boundarySupplementaryItems = [header, footer]
```

## Examples
```swift
// Footer with content:
func collectionView(_ collectionView: UICollectionView, viewForSupplementaryElementOfKind kind: String, at indexPath: IndexPath) -> UICollectionReusableView {
    if kind == UICollectionView.elementKindSectionFooter {
        let footer = collectionView.dequeueReusableSupplementaryView(ofKind: kind, withReuseIdentifier: "Footer", for: indexPath)
        var content = footer.defaultContentConfiguration()
        content.text = "End of section"
        footer.contentConfiguration = content
        return footer
    }
    // Handle header
    let header = collectionView.dequeueReusableSupplementaryView(ofKind: kind, withReuseIdentifier: "Header", for: indexPath)
    return header
}
```
