---
title: "[Solution] SwiftUI ForEach Index Out of Range Error"
description: "Fix ForEach index out of range errors in SwiftUI List and VStack."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI ForEach Index Out of Range Error

ForEach index errors occur when accessing array elements by index without checking bounds, or when the data source changes during iteration.

## Common Causes
- Array index accessed without bounds checking
- Data source modified during ForEach iteration
- Off-by-one error in range-based ForEach
- Array emptied while view is displaying

## How to Fix
1. Always check array bounds before accessing elements
2. Use ForEach with Identifiable conformance instead of indices
3. Use safe subscript extension
4. Handle empty data sources gracefully

```swift
// Safe subscript extension:
extension Array {
    subscript(safe index: Int) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}

// Safe usage:
ForEach(items.indices, id: \.self) { index in
    if let item = items[safe: index] {
        Text(item.name)
    }
}
```

## Examples
```swift
// Better: Use Identifiable with ForEach
struct Item: Identifiable {
    let id = UUID()
    let name: String
}

// Safe iteration:
ForEach(items) { item in
    Text(item.name)
}

// If using indices:
if !items.isEmpty {
    ForEach(0..<items.count, id: \.self) { index in
        Text(items[index].name)
    }
}
```
