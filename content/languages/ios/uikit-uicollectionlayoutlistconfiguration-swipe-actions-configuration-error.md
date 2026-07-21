---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Swipe Actions Configuration Error"
description: "Fix UICollectionLayoutListConfiguration swipe actions configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Swipe Actions Configuration Error

Swipe actions configuration errors occur when the swipe actions are not properly configured, when the actions conflict with the cell content, or when the actions do not update properly.

## Common Causes
- Actions not configured
- Actions conflict with content
- Actions not updating
- Actions not matching design

## How to Fix
1. Configure actions properly
2. Ensure actions do not conflict with content
3. Update actions dynamically
4. Match design specifications

```swift
var config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
config.trailingSwipeActionsConfigurationProvider = { indexPath in
    let deleteAction = UIContextualAction(style: .destructive, title: "Delete") { _, _, _ in
        print("Delete")
    }
    return UISwipeActionsConfiguration(actions: [deleteAction])
}
```

## Examples
```swift
// Swipe actions with multiple options:
config.trailingSwipeActionsConfigurationProvider = { indexPath in
    let deleteAction = UIContextualAction(style: .destructive, title: "Delete") { _, _, _ in
        print("Delete")
    }
    deleteAction.backgroundColor = .systemRed
    deleteAction.image = UIImage(systemName: "trash")

    let archiveAction = UIContextualAction(style: .normal, title: "Archive") { _, _, _ in
        print("Archive")
    }
    archiveAction.backgroundColor = .systemBlue
    archiveAction.image = UIImage(systemName: "archivebox")

    return UISwipeActionsConfiguration(actions: [deleteAction, archiveAction])
}
```
