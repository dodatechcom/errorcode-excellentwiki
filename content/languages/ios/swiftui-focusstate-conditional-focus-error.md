---
title: "[Solution] SwiftUI @FocusState Conditional Focus Error"
description: "Fix SwiftUI @FocusState conditional focus binding errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @FocusState Conditional Focus Error

Conditional focus errors occur when the focus condition is not properly evaluated, when the condition conflicts with view state, or when the condition does not update.

## Common Causes
- Focus condition not evaluated
- Condition conflicts with view state
- Condition not updating
- Condition not reflecting user input

## How to Fix
1. Evaluate focus condition properly
2. Ensure condition is compatible with view state
3. Update condition
4. Reflect user input in condition

```swift
struct ContentView: View {
    @FocusState private var isFocused: Bool
    @State private var text = ""

    var body: some View {
        VStack {
            TextField("Enter", text: $text)
                .focused($isFocused, equals: text.isEmpty)
        }
    }
}
```

## Examples
```swift
// Focus on validation error:
.focused($isFocused, equals: hasError)

// Focus on first empty field:
.focused($focusedField, equals: .email)

// Focus based on count:
.focused($isFocused, equals: items.count == 0)
```
