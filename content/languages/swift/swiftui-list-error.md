---
title: "[Solution] Swift SwiftUI List Rendering Error Fix"
description: "Fix Swift SwiftUI List rendering errors. Learn why SwiftUI List fails to render and how to fix common List issues."
languages: ["swift"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A SwiftUI List rendering error occurs when a List view fails to render properly. This can happen due to missing identifiers, unstable data, or incorrect usage of List modifiers.

## Common Causes

- Missing or duplicate Identifiable conformance
- Data changing during render
- Complex views inside List cells
- Missing stable identity for ForEach

## How to Fix

```swift
// WRONG: Missing Identifiable
struct Item {
    let name: String
}
List(items) { item in  // Error: Item doesn't conform to Identifiable
    Text(item.name)
}

// CORRECT: Add Identifiable conformance
struct Item: Identifiable {
    let id = UUID()
    let name: String
}
List(items) { item in
    Text(item.name)
}
```

```swift
// WRONG: Duplicate IDs
struct Item: Identifiable {
    let id = UUID()  // Always unique, but:
}
// If using external ID that may duplicate

// CORRECT: Ensure stable, unique IDs
struct Item: Identifiable {
    let id: Int  // Use unique database ID
    let name: String
}
```

```swift
// WRONG: Complex view in List cell
List(items) { item in
    VStack {
        // Heavy computation here
        Text(item.name)
        Image(uiImage: processImage(item))  // Slow
    }
}

// CORRECT: Keep List cells simple
List(items) { item in
    Text(item.name)
}
```

## Examples

```swift
// Example 1: Basic List
struct ContentView: View {
    let items = ["Apple", "Banana", "Cherry"]

    var body: some View {
        List(items, id: \.self) { item in
            Text(item)
        }
    }
}

// Example 2: List with sections
List {
    Section("Fruits") {
        Text("Apple")
        Text("Banana")
    }
    Section("Vegetables") {
        Text("Carrot")
    }
}

// Example 3: Editable List
@State private var items = ["Item 1", "Item 2", "Item 3"]

List {
    ForEach(items, id: \.self) { item in
        Text(item)
    }
    .onDelete { indexSet in
        items.remove(atOffsets: indexSet)
    }
}
```

## Related Errors

- [SwiftUI state error](swiftui-state-error) — state management issues
- [SwiftUI navigation error](swiftui-navigation-error) — navigation issues
- [Index out of range](index-out-of-range-swift) — array index beyond bounds
