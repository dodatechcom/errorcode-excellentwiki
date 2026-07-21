---
title: "[Solution] UIKit UIContextMenu Interaction DidEnd Error"
description: "Fix UIContextMenuInteraction didEnd delegate method cleanup errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction DidEnd Error

didEnd cleanup errors occur when resources are not properly released, when the state is not reset after menu dismissal, or when the cleanup conflicts with other interactions.

## Common Causes
- Resources not released after dismissal
- State not reset after menu closes
- Cleanup conflicting with other interactions
- Delegate method not called due to deallocation

## How to Fix
1. Release resources in didEnd delegate
2. Reset state after menu dismissal
3. Ensure cleanup does not conflict with other interactions
4. Maintain strong reference to delegate

```swift
func interaction(_ interaction: UIContextMenuInteraction, willEndFor configuration: UIContextMenuConfiguration, animator: UIContextMenuInteractionAnimating?) {
    // Reset state
    selectedItem = nil
    // Release resources
    temporaryData = nil
}
```

## Examples
```swift
// Complete interaction lifecycle:
func interaction(_ interaction: UIContextMenuInteraction, willDisplay menu: UIMenu, for configuration: UIContextMenuConfiguration) {
    isMenuShowing = true
}

func interaction(_ interaction: UIContextMenuInteraction, willEndFor configuration: UIContextMenuConfiguration, animator: UIContextMenuInteractionAnimating?) {
    animator?.addCompletion {
        self.isMenuShowing = false
        self.selectedItem = nil
    }
}
```
