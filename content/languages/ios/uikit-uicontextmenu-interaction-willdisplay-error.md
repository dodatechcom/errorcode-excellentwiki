---
title: "[Solution] UIKit UIContextMenu Interaction WillDisplay Error"
description: "Fix UIContextMenuInteraction willDisplay delegate method configuration errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction WillDisplay Error

willDisplay errors occur when the delegate method is not properly implemented, when the menu is modified after display, or when the analytics tracking conflicts with menu display.

## Common Causes
- Delegate method not implemented
- Menu modified after willDisplay is called
- Analytics tracking interfering with display
- Menu configuration changes during display

## How to Fix
1. Implement willDisplay delegate method
2. Avoid modifying menu after display
3. Keep analytics tracking non-blocking
4. Ensure menu configuration is final before display

```swift
func interaction(_ interaction: UIContextMenuInteraction, willDisplay menu: UIMenu, for configuration: UIContextMenuConfiguration) {
    // Track analytics
    analytics.track(.menuOpened)
    // Do not modify menu here
}
```

## Examples
```swift
// willDisplay with preview customization:
func interaction(_ interaction: UIContextMenuInteraction, willDisplay menu: UIMenu, for configuration: UIContextMenuConfiguration) {
    // Configure menu appearance
    menu.preferredDisplayOrder = [.inline]
    // Log event
    print("Menu displayed for configuration: \(String(describing: configuration.identifier))")
}
```
