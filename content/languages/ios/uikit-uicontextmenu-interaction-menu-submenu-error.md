---
title: "[Solution] UIKit UIContextMenu Interaction Menu Submenu Error"
description: "Fix UIContextMenuInteraction submenu configuration and display errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIContextMenu Interaction Menu Submenu Error

Submenu errors occur when the submenu is not properly configured, when the submenu nesting is too deep, or when the submenu does not display correctly.

## Common Causes
- Submenu not configured properly
- Nesting too deep
- Submenu not displaying correctly
- Submenu title not set

## How to Fix
1. Configure submenu with proper title and actions
2. Limit nesting depth
3. Test submenu display
4. Set submenu title for navigation

```swift
let copy = UIAction(title: "Copy") { _ in }
let paste = UIAction(title: "Paste") { _ in }
let clipboard = UIMenu(title: "Clipboard", children: [copy, paste])
let delete = UIAction(title: "Delete", attributes: .destructive) { _ in }
let menu = UIMenu(children: [clipboard, delete])
```

## Examples
```swift
// Nested submenus:
let bold = UIAction(title: "Bold") { _ in }
let italic = UIAction(title: "Italic") { _ in }
let underline = UIAction(title: "Underline") { _ in }
let formatting = UIMenu(title: "Format", image: UIImage(systemName: "textformat"), children: [bold, italic, underline])
let share = UIAction(title: "Share") { _ in }
let menu = UIMenu(children: [formatting, share])
```
