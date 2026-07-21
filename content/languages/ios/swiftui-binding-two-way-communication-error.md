---
title: "[Solution] SwiftUI @Binding Two-Way Communication Error"
description: "Fix SwiftUI @Binding two-way data flow communication errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @Binding Two-Way Communication Error

Binding communication errors occur when the binding is not properly established, when the binding path is incorrect, or when the binding does not update properly.

## Common Causes
- Binding not established
- Binding path incorrect
- Binding not updating
- Binding type mismatch

## How to Fix
1. Establish binding properly
2. Use correct binding path
3. Ensure binding updates
4. Check binding type

```swift
struct ChildView: View {
    @Binding var text: String

    var body: some View {
        TextField("Enter text", text: $text)
    }
}

struct ParentView: View {
    @State private var text = ""
    var body: some View {
        ChildView(text: $text)
    }
}
```

## Examples
```swift
// Binding with transform:
struct ChildView: View {
    @Binding var isOn: Bool

    var body: some View {
        Toggle("Toggle", isOn: $isOn)
    }
}

struct ParentView: View {
    @State private var setting = 0
    var body: some View {
        ChildView(isOn: Binding(
            get: { setting != 0 },
            set: { setting = $0 ? 1 : 0 }
        ))
    }
}
```
