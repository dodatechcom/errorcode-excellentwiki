---
title: "[Solution] UIKit UIContextMenu Configuration Identifier Error"
description: "Fix UIContextMenuConfiguration identifier assignment and lookup errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Configuration Identifier Error

Context menu identifier errors occur when identifiers are not unique, when the identifier is used for tracking but not properly assigned, or when the identifier does not match between configuration and actions.

## Common Causes
- Identifier is nil when tracking is needed
- Identifiers not unique across menu instances
- Identifier type mismatch
- Identifier lost during view reuse

## How to Fix
1. Assign unique identifiers for tracking
2. Use IndexPath or UUID for reliable identification
3. Store identifier in configuration
4. Verify identifier matches in action handler

```swift
func interaction(_ interaction: UIContextMenuInteraction, configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
    let indexPath = collectionView.indexPathForItem(at: location)
    return UIContextMenuConfiguration(identifier: indexPath, previewProvider: nil) { _ in
        let delete = UIAction(title: "Delete") { [weak self] _ in
            self?.deleteItem(at: indexPath)
        }
        return UIMenu(children: [delete])
    }
}
```

## Examples
```swift
// Identifier with tracking:
func interaction(_ interaction: UIContextMenuInteraction, willDisplay menu: UIMenu, for configuration: UIContextMenuConfiguration) {
    if let indexPath = configuration.identifier as? IndexPath {
        analytics.track(.contextMenuOpened, properties: ["row": indexPath.row])
    }
}
```
