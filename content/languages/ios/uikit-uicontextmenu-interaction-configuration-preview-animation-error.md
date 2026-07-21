---
title: "[Solution] UIKit UIContextMenu Interaction Configuration Preview Animation Error"
description: "Fix UIContextMenuInteraction preview animation configuration and timing errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Configuration Preview Animation Error

Preview animation errors occur when the animation is not properly configured, when the animation conflicts with the menu, or when the animation does not complete properly.

## Common Causes
- Animation not configured
- Animation conflicts with menu
- Animation not completing
- Animation duration incorrect

## How to Fix
1. Configure animation properly
2. Ensure animation does not conflict with menu
3. Handle animation completion
4. Set correct animation duration

```swift
func interaction(_ interaction: UIContextMenuInteraction, willPerformPreviewActionForMenuWith configuration: UIContextMenuConfiguration, animator: UIContextMenuInteractionAnimating) {
    animator.addCompletion {
        self.navigateToDetail()
    }
}
```

## Examples
```swift
// Animation with custom timing:
func interaction(_ interaction: UIContextMenuInteraction, willPerformPreviewActionForMenuWith configuration: UIContextMenuConfiguration, animator: UIContextMenuInteractionAnimating) {
    animator.preferredCommitStyle = .pop
    animator.addCompletion {
        UIView.animate(withDuration: 0.3) {
            self.view.alpha = 1.0
        }
    }
}
```
