---
title: "[Solution] UIKit UIAlertAction Configuration Error"
description: "Fix UIAlertAction configuration errors causing alerts to display incorrectly."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# UIKit UIAlertAction Configuration Error

UIAlertAction configuration issues cause buttons to not appear, wrong styling, or actions not triggering when tapped.

## Common Causes
- Alert controller missing required actions
- Action handler not properly capturing variables
- Alert presented from non-visible view controller
- Action style not matching expected appearance

## How to Fix
1. Always add at least one action to UIAlertController
2. Use proper variable capture in action handlers
3. Present from the topmost view controller
4. Set action style (.default, .cancel, .destructive) appropriately

```swift
// Correct alert setup:
let alert = UIAlertController(title: "Confirm", message: "Are you sure?", preferredStyle: .alert)
alert.addAction(UIAlertAction(title: "Cancel", style: .cancel))
alert.addAction(UIAlertAction(title: "Delete", style: .destructive) { _ in
    self.deleteItem()
})
present(alert, animated: true)
```

## Examples
```swift
// Alert with text field:
let alert = UIAlertController(title: "Add Item", message: nil, preferredStyle: .alert)
alert.addTextField { field in
    field.placeholder = "Item name"
}
alert.addAction(UIAlertAction(title: "Cancel", style: .cancel))
alert.addAction(UIAlertAction(title: "Add", style: .default) { _ in
    let name = alert.textFields?.first?.text ?? ""
    self.addItem(name)
})
present(alert, animated: true)
```
