---
title: "[Solution] UIKit UITableViewCell Swipe Action Error"
description: "Fix UITableView swipe-to-delete and swipe action configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UITableViewCell Swipe Action Error

Swipe actions fail to appear when trailingSwipeActionsConfigurationForRowAt is not implemented, when actions have invalid titles, or when the view is in editing mode.

## Common Causes
- delegate method not implemented
- Actions with empty or nil titles
- Swipe actions conflict with editing mode
- Configuration returns nil

## How to Fix
1. Implement trailingSwipeActionsConfigurationForRowAt
2. Provide valid titles for all actions
3. Handle editing mode appropriately
4. Return proper configuration object

```swift
// Swipe actions:
func tableView(_ tableView: UITableView, trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {
    let delete = UIContextualAction(style: .destructive, title: "Delete") { _, _, completion in
        self.deleteItem(at: indexPath)
        completion(true)
    }
    return UISwipeActionsConfiguration(actions: [delete])
}
```

## Examples
```swift
// Multiple swipe actions:
func tableView(_ tableView: UITableView, trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {
    let delete = UIContextualAction(style: .destructive, title: "Delete") { _, _, completion in
        self.delete(at: indexPath)
        completion(true)
    }
    delete.image = UIImage(systemName: "trash")

    let archive = UIContextualAction(style: .normal, title: "Archive") { _, _, completion in
        self.archive(at: indexPath)
        completion(true)
    }
    archive.backgroundColor = .systemBlue
    archive.image = UIImage(systemName: "archivebox")

    return UISwipeActionsConfiguration(actions: [delete, archive])
}
```
