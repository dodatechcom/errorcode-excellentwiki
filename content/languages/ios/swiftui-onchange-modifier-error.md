---
title: "[Solution] SwiftUI .onChange Modifier Error"
description: "Fix SwiftUI .onChange modifier value observation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .onChange Modifier Error

onChange modifier errors occur when the change is not properly observed, when the change handler is not called, or when the change does not reflect in the UI.

## Common Causes
- Change not observed
- Handler not called
- Change not reflecting in UI
- Incorrect value comparison

## How to Fix
1. Observe change properly
2. Ensure handler is called
3. Reflect change in UI
4. Use correct comparison

```swift
struct ContentView: View {
    @State private var count = 0

    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") { count += 1 }
        }
        .onChange(of: count) { newValue in
            print("Count changed to \(newValue)")
        }
    }
}
```

## Examples
```swift
// Multiple values:
.onChange(of: username) { _ in validateForm() }
.onChange(of: password) { _ in validateForm() }

// Old and new values (iOS 17+):
.onChange(of: count) { oldValue, newValue in
    print("Changed from \(oldValue) to \(newValue)")
}

// Initial value:
.task { await loadData() }
```
