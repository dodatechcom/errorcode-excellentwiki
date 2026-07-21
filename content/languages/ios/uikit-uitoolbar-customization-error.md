---
title: "[Solution] UIKit UIToolbar Customization Error"
description: "Fix UIToolbar custom appearance and button configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIToolbar Customization Error

Toolbar customization errors occur when bar button items are not properly configured, when the toolbar style conflicts with navigation requirements, or when custom views do not size correctly.

## Common Causes
- Bar button items not properly initialized
- Custom view sizing issues in toolbar
- Toolbar style conflicting with navigation bar
- Items exceeding toolbar width

## How to Fix
1. Initialize bar button items with proper targets
2. Set custom view sizes correctly
3. Configure toolbar style independently of nav bar
4. Use flexible space to distribute items

```swift
// Toolbar setup:
let flexibleSpace = UIBarButtonItem(barButtonSystemItem: .flexibleSpace, target: nil, action: nil)
let actionButton = UIBarButtonItem(barButtonSystemItem: .action, target: self, action: #selector(share))
let addButton = UIBarButtonItem(barButtonSystemItem: .add, target: self, action: #selector(add))
toolbar.items = [addButton, flexibleSpace, actionButton]
```

## Examples
```swift
// Toolbar with custom view:
let segmentedControl = UISegmentedControl(items: ["First", "Second"])
segmentedControl.selectedSegmentIndex = 0
let segmentedItem = UIBarButtonItem(customView: segmentedControl)
let flexibleSpace = UIBarButtonItem(barButtonSystemItem: .flexibleSpace, target: nil, action: nil)
toolbar.items = [flexibleSpace, segmentedItem, flexibleSpace]
```
