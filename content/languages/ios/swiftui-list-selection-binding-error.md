---
title: "[Solution] SwiftUI List Selection Binding Error"
description: "Fix SwiftUI List selection binding not working correctly in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI List Selection Binding Error

List selection binding fails when the binding type does not match the selection parameter or when the selection is not properly managed in the parent view.

## Common Causes
- Binding type mismatch with List selection
- Using selection with non-Identifiable data
- Multiple selection mode not configured
- Selection not persisted in parent view state

## How to Fix
1. Ensure binding type matches List data type
2. Use Identifiable conformance for selection
3. Configure multiple selection with .selection modifier
4. Store selection in @State or @Binding

```swift
// Single selection:
@State private var selected: Item.ID?

List(items, selection: $selected) { item in
    Text(item.name)
}

// Multiple selection:
@State private var selected = Set<Item.ID>()

List(items, selection: $selected) { item in
    Text(item.name)
}
```

## Examples
```swift
// List with selection management:
struct ContentView: View {
    let items = ["One", "Two", "Three"]
    @State private var selection: String?

    var body: some View {
        NavigationStack {
            List(items, id: \.self, selection: $selection) { item in
                Text(item)
            }
            .toolbar {
                EditButton()
            }
        }
    }
}
```
