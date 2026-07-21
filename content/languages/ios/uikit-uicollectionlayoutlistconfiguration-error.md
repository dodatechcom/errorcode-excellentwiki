---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Error"
description: "Fix UICollectionLayoutListConfiguration setup errors for list-style collection views."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Error

List configuration errors occur when the appearance is not set, when header and footer sizes are not configured, or when swipe actions conflict with the list configuration.

## Common Causes
- Appearance not configured (insetGrouped, plain, etc.)
- Header/Footer supplementary views not configured
- Swipe actions not compatible with list style
- Separator styling not matching design

## How to Fix
1. Set the appearance on the configuration
2. Configure header and footer with proper sizes
3. Ensure swipe actions are compatible with list style
4. Customize separator and background appearance

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.headerMode = .supplementary
config.separatorConfiguration.color = .separator

let layout = UICollectionViewCompositionalLayout.list(using: config)
collectionView.collectionViewLayout = layout
```

## Examples
```swift
// List with custom header:
var config = UICollectionLayoutListConfiguration(appearance: .plain)
config.headerMode = .supplementary
config.headerTopPadding = 0

config.trailingSwipeActionsConfigurationProvider = { indexPath in
    let delete = UIContextualAction(style: .destructive, title: "Delete") { _, _, completion in
        completion(true)
    }
    return UISwipeActionsConfiguration(actions: [delete])
}
```
