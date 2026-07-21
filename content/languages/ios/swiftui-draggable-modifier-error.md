---
title: "[Solution] SwiftUI .draggable Modifier Error"
description: "Fix SwiftUI .draggable modifier drag and drop source errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .draggable Modifier Error

Draggable modifier errors occur when the drag source is not properly configured, when the drag does not start, or when the drag data is not properly encoded.

## Common Causes
- Drag source not configured
- Drag does not start
- Drag data not encoded
- Drag not matching design

## How to Fix
1. Configure drag source properly
2. Ensure drag starts
3. Encode drag data properly
4. Match design specifications

```swift
struct ContentView: View {
    var body: some View {
        Text("Drag me")
            .draggable("Draggable text")
    }
}
```

## Examples
```swift
// With custom data:
Text("Drag me")
    .draggable(MyItem(name: "item"))

// With preview:
Text("Drag me")
    .draggable("Data", preview: {
        Text("Custom Preview")
            .padding()
            .background(.red)
    })

// With Transferable:
Text("Drag me")
    .draggable(MyTransferable(data: data))
```
