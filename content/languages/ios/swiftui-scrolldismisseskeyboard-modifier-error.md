---
title: "[Solution] SwiftUI .scrollDismissesKeyboard Modifier Error"
description: "Fix SwiftUI .scrollDismissesKeyboard modifier keyboard dismissal errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .scrollDismissesKeyboard Modifier Error

ScrollDismissesKeyboard modifier errors occur when the keyboard is not properly dismissed, when the dismissal conflicts with scroll behavior, or when the dismissal does not match the design.

## Common Causes
- Keyboard not dismissed
- Dismissal conflicts with scroll
- Dismissal not matching design
- Dismissal not updating with content

## How to Fix
1. Dismiss keyboard properly
2. Ensure dismissal is compatible with scroll
3. Match design specifications
4. Update dismissal with content

```swift
struct ContentView: View {
    var body: some View {
        List {
            ForEach(0..<20) { i in
                TextField("Item \(i)", text: $text)
            }
        }
        .scrollDismissesKeyboard(.interactively)
    }
}
```

## Examples
```swift
// Immediately
.scrollDismissesKeyboard(.immediately)

// Interactively
.scrollDismissesKeyboard(.interactively)

// Automatically
.scrollDismissesKeyboard(.automatic)
```
