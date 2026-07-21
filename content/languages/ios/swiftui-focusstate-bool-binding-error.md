---
title: "[Solution] SwiftUI @FocusState Bool Binding Error"
description: "Fix SwiftUI @FocusState boolean binding focus errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @FocusState Bool Binding Error

Bool binding focus errors occur when the boolean binding is not properly set, when the binding does not reflect focus state, or when the binding conflicts with view state.

## Common Causes
- Boolean binding not set
- Binding does not reflect focus state
- Binding conflicts with view state
- Binding not updating with view changes

## How to Fix
1. Set boolean binding properly
2. Ensure binding reflects focus state
3. Resolve conflicts with view state
4. Update binding with view changes

```swift
struct ContentView: View {
    @FocusState private var isFocused: Bool
    @State private var text = ""

    var body: some View {
        VStack {
            TextField("Enter text", text: $text)
                .focused($isFocused)
            Button("Focus") { isFocused = true }
            Button("Unfocus") { isFocused = false }
        }
    }
}
```

## Examples
```swift
// Auto-focus on appear:
.onAppear { isFocused = true }

// Dismiss keyboard on scroll:
.onTapGesture { isFocused = false }

// Conditional focus:
.focused($isFocused, equals: isEditing)
```
