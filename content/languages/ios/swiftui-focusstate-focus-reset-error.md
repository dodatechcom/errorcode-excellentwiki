---
title: "[Solution] SwiftUI @FocusState Focus Reset Error"
description: "Fix SwiftUI @FocusState focus reset and cleanup errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @FocusState Focus Reset Error

Focus reset errors occur when the focus is not properly reset, when the reset conflicts with view lifecycle, or when the reset does not clear all focused fields.

## Common Causes
- Focus not properly reset
- Reset conflicts with view lifecycle
- Reset does not clear all fields
- Reset not triggered

## How to Fix
1. Reset focus properly
2. Ensure reset is compatible with lifecycle
3. Clear all focused fields
4. Trigger reset appropriately

```swift
struct ContentView: View {
    @FocusState private var isFocused: Bool
    @State private var text = ""

    var body: some View {
        VStack {
            TextField("Enter", text: $text)
                .focused($isFocused)
            Button("Submit") {
                isFocused = false
            }
        }
        .onDisappear {
            isFocused = false
        }
    }
}
```

## Examples
```swift
// Reset on submit:
.onSubmit {
    isFocused = false
}

// Reset on navigation:
.navigationDestination(isPresented: $showDetail) {
    DetailView()
        .onAppear { isFocused = false }
}

// Reset all fields:
func resetFocus() {
    focusedField = nil
}
```
