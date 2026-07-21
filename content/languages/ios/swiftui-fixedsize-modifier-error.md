---
title: "[Solution] SwiftUI .fixedSize Modifier Error"
description: "Fix SwiftUI .fixedSize modifier view intrinsic size override errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .fixedSize Modifier Error

FixedSize modifier errors occur when the size is not properly fixed, when the fixed size conflicts with the parent, or when the fixed size does not match the design.

## Common Causes
- Size not fixed
- Fixed size conflicts with parent
- Fixed size not matching design
- Fixed size not updating

## How to Fix
1. Fix size properly
2. Ensure fixed size is compatible with parent
3. Match design specifications
4. Update fixed size

```swift
struct ContentView: View {
    var body: some View {
        Text("Hello")
            .fixedSize()
    }
}
```

## Examples
```swift
// Fix both
.fixedSize()

// Fix horizontal only
.fixedSize(horizontal: true, vertical: false)

// Fix vertical only
.fixedSize(horizontal: false, vertical: true)

// Combined with frame
.fixedSize()
.frame(width: 200)
```
