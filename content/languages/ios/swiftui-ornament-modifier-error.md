---
title: "[Solution] SwiftUI .ornament Modifier Error"
description: "Fix SwiftUI .ornament modifier floating ornament presentation errors in visionOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .ornament Modifier Error

Ornament modifier errors occur when the ornament is not properly configured, when the ornament conflicts with the scene, or when the ornament does not match the design.

## Common Causes
- Ornament not configured
- Ornament conflicts with scene
- Ornament not matching design
- Ornament not updating with content

## How to Fix
1. Configure ornament properly
2. Ensure ornament is compatible with scene
3. Match design specifications
4. Update ornament with content

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello")
            .ornament(attachmentAnchor: .scene(.trailing), contentAlignment: .leading) {
                Text("Ornament")
                    .padding()
                    .glassBackgroundEffect()
            }
    }
}
```

## Examples
```swift
// With glass background
.ornament(attachmentAnchor: .scene(.trailing)) {
    VStack {
        Button("Action 1") { }
        Button("Action 2") { }
    }
    .padding()
    .glassBackgroundEffect()
}

// With custom offset
.ornament(attachmentAnchor: .scene(.bottom), contentAlignment: .top) {
    Text("Ornament")
}
```
