---
title: "[Solution] SwiftUI Alert Confirmation Dialog Error"
description: "Fix SwiftUI alert and confirmation dialog presentation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI Alert Confirmation Dialog Error

Alert and confirmation dialog errors occur when the dialog modifier is placed incorrectly, when the action handlers conflict, or when the dialog tries to present while another dialog is active.

## Common Causes
- Alert modifier not connected to triggering action
- Multiple alerts trying to present simultaneously
- Confirmation dialog not in navigation context
- Dismiss action not properly implemented

## How to Fix
1. Connect alert modifier with isPresented binding
2. Use separate state variables for multiple alerts
3. Place confirmationDialog in navigation context
4. Implement dismiss action correctly

```swift
// Alert with confirmation:
.alert("Delete Item", isPresented: $showDeleteAlert) {
    Button("Cancel", role: .cancel) { }
    Button("Delete", role: .destructive) { deleteItem() }
} message: {
    Text("This action cannot be undone.")
}

// Confirmation dialog:
.confirmationDialog("Choose Action", isPresented: $showActions) {
    Button("Share") { shareItem() }
    Button("Copy") { copyItem() }
    Button("Delete", role: .destructive) { deleteItem() }
}
```

## Examples
```swift
// Multiple alerts:
.alert("Error", isPresented: $showError) {
    Button("OK", role: .cancel) { }
} message: {
    Text(errorMessage)
}
.alert("Success", isPresented: $showSuccess) {
    Button("OK", role: .cancel) { }
} message: {
    Text("Operation completed.")
}
```
