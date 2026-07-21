---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Section Header Swipe Actions Error"
description: "Fix UICollectionLayoutListConfiguration section header swipe actions configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Section Header Swipe Actions Error

Section header swipe actions errors occur when swipe actions are configured on section headers (typically only available on cells), when the swipe conflicts with header interaction, or when the swipe is not visible.

## Common Causes
- Swipe actions configured on header instead of cells
- Swipe conflicts with header interaction
- Swipe not visible
- Swipe configuration provider not returning valid configuration

## How to Fix
1. Configure swipe actions on cells, not headers
2. Use context menu for header actions instead
3. Ensure swipe does not conflict with header interaction
4. Return valid configuration from provider

```swift
// Swipe actions on cells (not headers):
config.trailingSwipeActionsConfigurationProvider = { indexPath in
    let delete = UIContextualAction(style: .destructive, title: "Delete") { _, _, completion in
        completion(true)
    }
    return UISwipeActionsConfiguration(actions: [delete])
}
```

## Examples
```swift
// Context menu on section header instead of swipe:
func collectionView(_ collectionView: UICollectionView, contextMenuConfigurationForItemsAt indexPaths: [IndexPath], point: CGPoint) -> UIContextMenuConfiguration? {
    guard let indexPath = indexPaths.first, indexPath.item == 0 else { return nil }
    return UIContextMenuConfiguration(identifier: indexPath.section, previewProvider: nil) { _ in
        UIMenu(children: [
            UIAction(title: "Rename Section") { _ in },
            UIAction(title: "Delete Section", attributes: .destructive) { _ in }
        ])
    }
}
```
