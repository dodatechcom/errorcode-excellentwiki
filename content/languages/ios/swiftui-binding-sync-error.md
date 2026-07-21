---
title: "[Solution] SwiftUI @Binding Sync Error"
description: "Fix SwiftUI @Binding synchronization issues between parent and child views."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @Binding Sync Error

@Binding fails to sync when the binding source is not properly connected, when the parent view is recreated, or when the binding is captured incorrectly in closures.

## Common Causes
- Binding not connected to @State in parent
- Parent view recreated losing state
- Binding captured in escaping closure
- Two-way binding not updating both sides

## How to Fix
1. Ensure parent uses @State or @Binding for the bound value
2. Pass $ prefix for two-way bindings
3. Avoid capturing bindings in escaping closures
4. Use @StateObject for reference type state

```swift
// Parent with state:
struct Parent: View {
    @State private var name = ""
    var body: some View {
        Child(name: $name) // Two-way binding
    }
}

// Child with binding:
struct Child: View {
    @Binding var name: String
    var body: some View {
        TextField("Name", text: $name)
    }
}
```

## Examples
```swift
// Binding chain example:
struct FormView: View {
    @State private var username = ""
    @State private var isValid = false

    var body: some View {
        VStack {
            UsernameField(username: $username, isValid: $isValid)
            SubmitButton(isEnabled: isValid)
        }
    }
}

struct UsernameField: View {
    @Binding var username: String
    @Binding var isValid: Bool

    var body: some View {
        TextField("Username", text: $username)
            .onChange(of: username) { newValue in
                isValid = newValue.count >= 3
            }
    }
}
```
