---
title: "[Solution] SwiftUI .confirmationDialog Modifier Error"
description: "Fix SwiftUI .confirmationDialog modifier action sheet errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .confirmationDialog Modifier Error

ConfirmationDialog modifier errors occur when the dialog is not properly configured, when the actions are not displayed, or when the dialog does not dismiss.

## Common Causes
- Dialog not configured
- Actions not displayed
- Dialog does not dismiss
- Dialog not matching design

## How to Fix
1. Configure dialog properly
2. Display actions correctly
3. Ensure dialog dismisses
4. Match design specifications

```swift
struct ContentView: View {
    @State private var showDialog = false

    var body: some View {
        Button("Show Dialog") { showDialog = true }
            .confirmationDialog("Title", isPresented: $showDialog) {
                Button("Option 1") { }
                Button("Option 2") { }
            }
    }
}
```

## Examples
```swift
// With message:
.confirmationDialog("Title", isPresented: $showDialog, message: Text("Message")) {
    Button("Option 1") { }
}

// With destructive:
.confirmationDialog("Title", isPresented: $showDialog) {
    Button("Delete", role: .destructive) { }
    Button("Cancel", role: .cancel) { }
}

// With cancellation:
.confirmationDialog("Title", isPresented: $showDialog) {
    Button("Option 1") { }
    Button("Cancel", role: .cancel) { }
}
```
