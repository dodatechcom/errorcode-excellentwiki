---
title: "[Solution] SwiftUI @FocusState Error"
description: "Fix SwiftUI @FocusState keyboard focus management errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @FocusState Error

FocusState errors occur when the focus state is not properly managed, when the focus is not set on the correct field, or when the focus state does not update with view changes.

## Common Causes
- Focus state not properly bound
- Focus set on wrong field
- Focus state not updating with view changes
- Focus state type mismatch

## How to Fix
1. Bind focus state to the correct field
2. Set focus state using the binding
3. Update focus state with view changes
4. Use correct focus state type

```swift
struct ContentView: View {
    @FocusState private var isUsernameFocused: Bool

    var body: some View {
        TextField("Username", text: $username)
            .focused($isUsernameFocused)
        Button("Focus") { isUsernameFocused = true }
    }
}
```

## Examples
```swift
// Multiple focus states:
enum Field: Hashable {
    case username, password, email
}

@FocusState private var focusedField: Field?

TextField("Username", text: $username)
    .focused($focusedField, equals: .username)
TextField("Password", text: $password)
    .focused($focusedField, equals: .password)

Button("Submit") { focusedField = nil }
```
