---
title: "[Solution] SwiftUI .onDrop Modifier Error"
description: "Fix SwiftUI .onDrop modifier legacy drag and drop errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .onDrop Modifier Error

OnDrop modifier errors occur when the drop handler is not properly configured, when the drop is not accepted, or when the drop data is not properly loaded.

## Common Causes
- Drop handler not configured
- Drop not accepted
- Drop data not loaded
- Drop not matching design

## How to Fix
1. Configure drop handler properly
2. Accept drop properly
3. Load drop data properly
4. Match design specifications

```swift
struct ContentView: View {
    var body: some View {
        Text("Drop here")
            .onDrop(of: ["public.plain-text"], delegate: DropDelegate())
    }
}
```

## Examples
```swift
// Custom drop delegate:
class DropDelegate: NSObject, UIDropInteractionDelegate {
    func performDrop(_ interaction: UIDropInteraction) -> Bool {
        return true
    }
}

// With proposal:
func dropInteraction(_ interaction: UIDropInteraction, sessionDidUpdate session: UIDropSession) -> UIDropProposal {
    UIDropProposal(operation: .copy)
}
```
