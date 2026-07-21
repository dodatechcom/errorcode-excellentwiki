---
title: "[Solution] SwiftUI .inspector Modifier Error"
description: "Fix SwiftUI .inspector modifier sidebar inspector panel errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .inspector Modifier Error

Inspector modifier errors occur when the inspector is not properly configured, when the inspector does not show, or when the inspector does not match the design.

## Common Causes
- Inspector not configured
- Inspector does not show
- Inspector not matching design
- Inspector not updating with content

## How to Fix
1. Configure inspector properly
2. Ensure inspector shows
3. Match design specifications
4. Update inspector with content

```swift
struct ContentView: View {
    @State private var showInspector = false

    var body: some View {
        Text("Hello")
            .inspector(isPresented: $showInspector) {
                Text("Inspector Content")
            }
    }
}
```

## Examples
```swift
// With custom width
.inspector(isPresented: $showInspector) {
    Text("Inspector")
}
.inspectorColumnWidth(min: 200, ideal: 300, max: 400)

// Toggle inspector
Button("Toggle Inspector") {
    showInspector.toggle()
}
```
