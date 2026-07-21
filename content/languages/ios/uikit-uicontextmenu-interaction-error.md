---
title: "[Solution] UIKit UIContextMenu Interaction Error"
description: "Fix UIContextMenu interaction and preview errors in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Error

Context menu interactions fail when the interaction is not properly configured, when the preview provider returns nil, or when the menu actions conflict with existing gesture recognizers.

## Common Causes
- Context menu interaction not added to view
- Preview provider returns nil
- Menu actions conflict with tap gestures
- Interaction not updated when view hierarchy changes

## How to Fix
1. Add UIContextMenuInteraction to the target view
2. Implement previewProvider to return a valid view
3. Ensure menu actions do not conflict with gestures
4. Update interaction when view content changes

```swift
// Add context menu:
let interaction = UIContextMenuInteraction(delegate: self)
view.addInteraction(interaction)

// Delegate methods:
func interaction(_ interaction: UIContextMenuInteraction, configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(identifier: nil, previewProvider: nil) { _ in
        let delete = UIAction(title: "Delete", image: UIImage(systemName: "trash")) { _ in
            self.deleteItem()
        }
        return UIMenu(title: "", children: [delete])
    }
}
```

## Examples
```swift
// Context menu with preview:
func interaction(_ interaction: UIContextMenuInteraction, configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
    let previewProvider: UIContextMenuContentPreviewProvider = {
        let previewController = PreviewViewController()
        previewController.item = self.currentItem
        return previewController
    }

    return UIContextMenuConfiguration(identifier: nil, previewProvider: previewProvider) { _ in
        let edit = UIAction(title: "Edit", image: UIImage(systemName: "pencil")) { _ in self.editItem() }
        let share = UIAction(title: "Share", image: UIImage(systemName: "square.and.arrow.up")) { _ in self.shareItem() }
        let delete = UIAction(title: "Delete", image: UIImage(systemName: "trash"), attributes: .destructive) { _ in self.deleteItem() }
        return UIMenu(title: "", children: [edit, share, delete])
    }
}
```
