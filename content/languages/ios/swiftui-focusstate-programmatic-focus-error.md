---
title: "[Solution] SwiftUI @FocusState Programmatic Focus Error"
description: "Fix SwiftUI @FocusState programmatic focus control errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @FocusState Programmatic Focus Error

Programmatic focus errors occur when the focus is not properly set programmatically, when the focus command conflicts with user interaction, or when the focus does not update.

## Common Causes
- Focus not set programmatically
- Focus command conflicts with interaction
- Focus not updating
- Focus state not synchronized

## How to Fix
1. Set focus programmatically using binding
2. Ensure focus command is compatible with interaction
3. Update focus state
4. Synchronize focus state

```swift
struct ContentView: View {
    @FocusState private var isFocused: Bool
    @State private var text = ""

    var body: some View {
        VStack {
            TextField("Enter", text: $text)
                .focused($isFocused)
            Button("Focus") {
                isFocused = true
            }
        }
    }
}
```

## Examples
```swift
// Focus with animation:
withAnimation { isFocused = true }

// Delayed focus:
DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
    isFocused = true
}

// Focus based on condition:
.focused($isFocused, equals: text.isEmpty)
```
