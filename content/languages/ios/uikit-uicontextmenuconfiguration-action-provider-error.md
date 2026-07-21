---
title: "[Solution] UIKit UIContextMenuConfiguration Action Provider Error"
description: "Fix UIContextMenuConfiguration action provider closure errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenuConfiguration Action Provider Error

Action provider errors occur when the closure returns nil, when the menu contains invalid actions, or when the actions conflict with the preview provider.

## Common Causes
- Action provider returns nil or empty menu
- Actions have duplicate identifiers
- Actions conflict with preview interaction
- Actions not properly enabled or disabled

## How to Fix
1. Return valid UIMenu from action provider
2. Ensure action identifiers are unique
3. Test actions with preview interaction
4. Configure action state properly

```swift
return UIContextMenuConfiguration(identifier: nil, previewProvider: nil) { _ in
    let share = UIAction(title: "Share", image: UIImage(systemName: "square.and.arrow.up")) { _ in }
    let delete = UIAction(title: "Delete", image: UIImage(systemName: "trash"), attributes: .destructive) { _ in }
    return UIMenu(children: [share, delete])
}
```

## Examples
```swift
// Action provider with submenu:
return UIContextMenuConfiguration(identifier: indexPath, previewProvider: nil) { _ in
    let copy = UIAction(title: "Copy") { _ in }
    let paste = UIAction(title: "Paste") { _ in }
    let clipboard = UIMenu(title: "Clipboard", children: [copy, paste])
    let delete = UIAction(title: "Delete", attributes: .destructive) { _ in }
    return UIMenu(children: [clipboard, delete])
}
```
