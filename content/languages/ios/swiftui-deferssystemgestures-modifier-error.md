---
title: "[Solution] SwiftUI .defersSystemGestures Modifier Error"
description: "Fix SwiftUI .defersSystemGestures modifier system gesture deferral errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .defersSystemGestures Modifier Error

DefersSystemGestures modifier errors occur when gestures are not properly deferred, when the deferral conflicts with custom gestures, or when the deferral does not match the design.

## Common Causes
- Gestures not deferred
- Deferral conflicts with custom gestures
- Deferral not matching design
- Deferral not updating with content

## How to Fix
1. Defer gestures properly
2. Ensure deferral is compatible with custom gestures
3. Match design specifications
4. Update deferral with content

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello")
            .defersSystemGestures(on: .vertical)
    }
}
```

## Examples
```swift
// Defer all gestures
.defersSystemGestures(on: .all)

// Defer horizontal gestures
.defersSystemGestures(on: .horizontal)

// Defer vertical gestures
.defersSystemGestures(on: .vertical)
```
