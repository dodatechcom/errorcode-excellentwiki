---
title: "[Solution] SwiftUI ForEach Identifiable Conformance Error"
description: "Fix ForEach missing Identifiable conformance errors in SwiftUI."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI ForEach Identifiable Conformance Error

ForEach requires elements to conform to Identifiable or provide an explicit id parameter. Missing conformance causes a compiler error.

## Common Causes
- Model type does not conform to Identifiable
- Using ForEach without id parameter on non-Identifiable types
- Duplicate identifiers in the data array
- Using wrong key path for id

## How to Fix
1. Make model conform to Identifiable protocol
2. Provide id parameter to ForEach using a key path
3. Ensure id values are unique across all elements
4. Use UUID() for auto-generated unique identifiers

```swift
// Model conforming to Identifiable:
struct Item: Identifiable {
    let id = UUID()
    let name: String
}

// Usage:
ForEach(items) { item in
    Text(item.name)
}
```

## Examples
```swift
// Multiple ways to use ForEach:
// 1. With Identifiable:
ForEach(items) { item in Text(item.name) }

// 2. With explicit id:
ForEach(items, id: \.self) { item in Text(item) }

// 3. With key path:
ForEach(items, id: \.id) { item in Text(item.name) }

// 4. With Range:
ForEach(0..<5) { index in Text("\(index)") }
```
