---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Custom View Error"
description: "Fix UICollectionLayoutListConfiguration section header custom view configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Custom View Error

Section header custom view errors occur when the custom view is not properly configured, when the view conflicts with the header layout, or when the view does not match the design.

## Common Causes
- Custom view not configured
- View conflicts with layout
- View not matching design
- View not updating with content changes

## How to Fix
1. Configure custom view properly
2. Ensure view is compatible with layout
3. Match design specifications
4. Update view with content changes

```swift
let headerRegistration = UICollectionView.SupplementaryRegistration<ListHeaderSupplementaryView>(elementKind: UICollectionView.elementKindSectionHeader) { supplementaryView, string, indexPath in
    var content = UIListContentConfiguration.supplementaryHeader()
    content.text = "Section \(indexPath.section)"
    supplementaryView.contentConfiguration = content
}
```

## Examples
```swift
// Custom header view:
let headerRegistration = UICollectionView.SupplementaryRegistration<CustomHeaderView>(elementKind: "custom-header") { supplementaryView, string, indexPath in
    supplementaryView.title = "Section \(indexPath.section)"
    supplementaryView.subtitle = "\(collectionView.numberOfItems(inSection: indexPath.section)) items"
}
```
