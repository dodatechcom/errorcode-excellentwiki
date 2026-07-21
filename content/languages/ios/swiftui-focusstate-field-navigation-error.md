---
title: "[Solution] SwiftUI @FocusState Field Navigation Error"
description: "Fix SwiftUI @FocusState field-to-field navigation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @FocusState Field Navigation Error

Field navigation errors occur when the focus does not move correctly between fields, when the navigation conflicts with user input, or when the navigation does not follow the expected order.

## Common Causes
- Focus does not move between fields
- Navigation conflicts with input
- Navigation does not follow order
- Navigation not triggered

## How to Fix
1. Move focus between fields properly
2. Ensure navigation is compatible with input
3. Follow expected order
4. Trigger navigation appropriately

```swift
enum Field: Hashable {
    case name, email, phone
}

struct FormView: View {
    @FocusState private var focusedField: Field?
    @State private var name = ""
    @State private var email = ""

    var body: some View {
        VStack {
            TextField("Name", text: $name)
                .focused($focusedField, equals: .name)
                .onSubmit { focusedField = .email }
            TextField("Email", text: $email)
                .focused($focusedField, equals: .email)
                .onSubmit { focusedField = nil }
        }
    }
}
```

## Examples
```swift
// Return key navigation:
.onSubmit {
    switch focusedField {
    case .name: focusedField = .email
    case .email: focusedField = .phone
    case .phone: focusedField = nil
    default: break
    }
}

// Tab key navigation:
.keyboardType(.next)
```
