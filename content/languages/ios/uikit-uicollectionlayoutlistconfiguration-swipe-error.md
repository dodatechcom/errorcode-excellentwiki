---
title: "[Solution] UIKit UICollectionLayoutListConfiguration Swipe Error"
description: "Fix UICollectionLayoutListConfiguration swipe action configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UICollectionLayoutListConfiguration Swipe Error

Swipe action configuration errors occur when the swipe actions conflict with the list style, when action titles are empty, or when the trailing swipe configuration provider returns nil.

## Common Causes
- Swipe actions incompatible with list style
- Action titles empty or too long
- Configuration provider returns nil
- Swipe conflict with other gestures

## How to Fix
1. Ensure swipe actions are compatible with list style
2. Provide descriptive action titles
3. Always return a valid configuration
4. Test swipe gesture conflicts

```swift
var config = UICollectionLayoutListConfiguration(appearance: .plain)
config.trailingSwipeActionsConfigurationProvider = { indexPath in
    let delete = UIContextualAction(style: .destructive, title: "Delete") { _, _, completion in
        completion(true)
    }
    return UISwipeActionsConfiguration(actions: [delete])
}
```

## Examples
```swift
// Full swipe to delete:
config.trailingSwipeActionsConfigurationProvider = { indexPath in
    let delete = UIContextualAction(style: .destructive, title: "Delete") { _, _, completion in
        self.deleteItem(at: indexPath)
        completion(true)
    }
    let config = UISwipeActionsConfiguration(actions: [delete])
    config.performsFirstActionWithFullSwipe = true
    return config
}
```
