---
title: "[Solution] SwiftUI .popover Modifier Error"
description: "Fix SwiftUI .popover modifier popover presentation errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .popover Modifier Error

Popover modifier errors occur when the popover is not properly positioned, when the popover does not dismiss, or when the popover conflicts with the view hierarchy.

## Common Causes
- Popover not positioned
- Popover does not dismiss
- Popover conflicts with hierarchy
- Popover not matching design

## How to Fix
1. Position popover properly
2. Ensure popover dismisses
3. Ensure popover is compatible with hierarchy
4. Match design specifications

```swift
struct ContentView: View {
    @State private var showPopover = false

    var body: some View {
        Button("Show Popover") { showPopover = true }
            .popover(isPresented: $showPopover) {
                Text("Popover Content")
            }
    }
}
```

## Examples
```swift
// With arrow edge:
.popover(isPresented: $showPopover, arrowEdge: .top) {
    Text("Popover")
}

// With custom size:
.popover(isPresented: $showPopover) {
    Text("Popover")
        .frame(width: 200, height: 100)
}

// With attachment:
.popover(isPresented: $showPopover, attachmentAnchor: .rect(.bounds)) {
    Text("Popover")
}
```
