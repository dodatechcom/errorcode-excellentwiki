---
title: "[Solution] SwiftUI .alert Modifier Error"
description: "Fix SwiftUI .alert modifier alert presentation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .alert Modifier Error

Alert modifier errors occur when the alert is not properly configured, when the alert does not dismiss, or when the alert actions do not work.

## Common Causes
- Alert not configured
- Alert does not dismiss
- Actions do not work
- Alert not matching design

## How to Fix
1. Configure alert properly
2. Ensure alert dismisses
3. Ensure actions work
4. Match design specifications

```swift
struct ContentView: View {
    @State private var showAlert = false

    var body: some View {
        Button("Show Alert") { showAlert = true }
            .alert("Title", isPresented: $showAlert) {
                Button("OK") { }
            } message: {
                Text("Message")
            }
    }
}
```

## Examples
```swift
// With destructive:
.alert("Delete Item", isPresented: $showAlert) {
    Button("Delete", role: .destructive) { deleteItem() }
    Button("Cancel", role: .cancel) { }
} message: {
    Text("Are you sure?")
}

// With TextField:
.alert("Rename", isPresented: $showAlert) {
    TextField("Name", text: $newName)
    Button("Save") { saveName() }
    Button("Cancel", role: .cancel) { }
}
```
