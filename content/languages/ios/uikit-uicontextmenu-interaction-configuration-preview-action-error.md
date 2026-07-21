---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Action Error"
description: "Fix UIContextMenuInteraction configuration preview action handling errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Action Error

Preview action errors occur when the preview action is not properly handled, when the action conflicts with the menu, or when the action does not perform the expected operation.

## Common Causes
- Preview action not properly handled
- Action conflicts with menu
- Action not performing expected operation
- Action handler not implemented

## How to Fix
1. Handle preview action properly
2. Ensure action does not conflict with menu
3. Implement action handler correctly
4. Test action with different scenarios

```swift
func interaction(_ interaction: UIContextMenuInteraction, willPerformPreviewActionForMenuWith configuration: UIContextMenuConfiguration, animator: UIContextMenuInteractionAnimating) {
    animator.addCompletion {
        self.navigateToDetail()
    }
}
```

## Examples
```swift
// Preview action with custom handling:
func interaction(_ interaction: UIContextMenuInteraction, willPerformPreviewActionForMenuWith configuration: UIContextMenuConfiguration, animator: UIContextMenuInteractionAnimating) {
    if let indexPath = configuration.identifier as? IndexPath {
        animator.preferredCommitStyle = .pop
        animator.addCompletion {
            let detailVC = self.detailViewController(for: indexPath)
            self.navigationController?.pushViewController(detailVC, animated: true)
        }
    }
}
```
