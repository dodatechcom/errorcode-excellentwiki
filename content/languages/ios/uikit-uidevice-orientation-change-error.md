---
title: "[Solution] UIKit UIDevice Orientation Change Error"
description: "Fix UIDevice orientation change handling errors in iOS apps."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIDevice Orientation Change Error

Orientation change errors occur when the view controller does not properly respond to size class changes, when layout constraints are not updated, or when rotation animations conflict.

## Common Causes
- View controller does not override viewWillTransition
- Constraints not updated for new size class
- Status bar orientation not accounted for
- Auto-layout not properly configured for rotation

## How to Fix
1. Override viewWillTransition(to:with:) for rotation handling
2. Update layout constraints in trait collection changes
3. Use size classes for responsive layouts
4. Test on all device orientations

```swift
// Handle rotation:
override func viewWillTransition(to size: CGSize, with coordinator: UIViewControllerTransitionCoordinator) {
    super.viewWillTransition(to: size, with: coordinator)
    coordinator.animate { context in
        self.updateLayout(for: size)
    }
}
```

## Examples
```swift
// Responsive layout with trait collection:
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    super.traitCollectionDidChange(previousTraitCollection)
    if traitCollection.verticalSizeClass == .compact {
        // Landscape layout
        stackView.axis = .horizontal
    } else {
        // Portrait layout
        stackView.axis = .vertical
    }
}
```
