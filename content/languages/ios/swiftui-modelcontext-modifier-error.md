---
title: "[Solution] SwiftUI .modelContext Modifier Error"
description: "Fix SwiftUI .modelContext modifier SwiftData context access errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .modelContext Modifier Error

ModelContext modifier errors occur when the context is not properly accessed, when the context does not save, or when the context does not track changes.

## Common Causes
- Context not accessed
- Context does not save
- Context does not track
- Missing context injection

## How to Fix
1. Access context properly
2. Ensure context saves
3. Track changes in context
4. Inject context

```swift
struct ContentView: View {
    @Environment(\.modelContext) private var context

    var body: some View {
        Button("Add Item") {
            let item = Item(name: "New Item")
            context.insert(item)
        }
    }
}
```

## Examples
```swift
// Insert item
context.insert(item)

// Save changes
try? context.save()

// Delete item
context.delete(item)

// Fetch items
let items = try? context.fetch(FetchDescriptor<Item>())
```
