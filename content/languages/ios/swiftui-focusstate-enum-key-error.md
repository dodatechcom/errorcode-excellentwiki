---
title: "[Solution] SwiftUI @FocusState Enum Key Error"
description: "Fix SwiftUI @FocusState enum-based focus management errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @FocusState Enum Key Error

Enum-based focus errors occur when the focus state enum is not properly defined, when the enum cases do not match the fields, or when the focus state does not update with view changes.

## Common Causes
- Enum not properly defined
- Enum cases do not match fields
- Focus state not updating
- Focus state type mismatch

## How to Fix
1. Define enum with Hashable conformance
2. Bind each field to its enum case
3. Set focus state using enum cases
4. Clear focus by setting to nil

```swift
enum Field: Hashable {
    case name, email, phone
}

struct FormView: View {
    @FocusState private var focusedField: Field?
    @State private var name = ""

    var body: some View {
        TextField("Name", text: $name)
            .focused($focusedField, equals: .name)
    }
}
```

## Examples
```swift
// Sequential field navigation:
func submitField(_ field: Field) {
    switch field {
    case .name: focusedField = .email
    case .email: focusedField = .phone
    case .phone: focusedField = nil
    }
}
```
