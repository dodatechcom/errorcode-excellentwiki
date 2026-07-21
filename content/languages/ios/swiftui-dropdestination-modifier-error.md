---
title: "[Solution] SwiftUI .dropDestination Modifier Error"
description: "Fix SwiftUI .dropDestination modifier drag and drop destination errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .dropDestination Modifier Error

DropDestination modifier errors occur when the drop destination is not properly configured, when the drop is not accepted, or when the drop data is not properly decoded.

## Common Causes
- Drop destination not configured
- Drop not accepted
- Drop data not decoded
- Drop not matching design

## How to Fix
1. Configure drop destination properly
2. Accept drop properly
3. Decode drop data properly
4. Match design specifications

```swift
struct ContentView: View {
    var body: some View {
        Text("Drop here")
            .dropDestination(for: String.self) { items, location in
                print(items)
                return true
            }
    }
}
```

## Examples
```swift
// With validation:
.dropDestination(for: String.self) { items, location in
    guard items.count > 0 else { return false }
    handleDrop(items)
    return true
}

// With custom type:
.dropDestination(for: MyItem.self) { items, location in
    handleItems(items)
    return true
}

// With isTargeted:
.dropDestination(for: String.self) { items, location in
    true
} isTargeted: { isTargeted in
    isTargeted ? .blue : .gray
}
```
