---
title: "[Solution] SwiftUI @FocusedBinding Property Wrapper Error"
description: "Fix SwiftUI @FocusedBinding property wrapper focus state binding errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @FocusedBinding Property Wrapper Error

FocusedBinding errors occur when the binding is not properly established, when the binding does not update, or when the binding does not match the focus state.

## Common Causes
- Binding not established
- Binding not updating
- Binding does not match focus state
- Focus state not shared

## How to Fix
1. Establish binding properly
2. Ensure binding updates
3. Match binding to focus state
4. Share focus state

```swift
struct ContentView: View {
    @FocusState private var isFocused: Bool

    var body: some View {
        VStack {
            TextField("Enter", text: $text)
                .focused($isFocused)
            Button("Focus") { isFocused = true }
        }
    }
}
```

## Examples
```swift
// Boolean focus binding
@FocusState private var isFocused: Bool

// Enum focus binding
@FocusState private var focusedField: Field?

// Programmatic focus
isFocused = true
focusedField = .email

// Clear focus
isFocused = false
focusedField = nil
```
