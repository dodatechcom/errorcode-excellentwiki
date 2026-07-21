---
title: "[Solution] SwiftUI @Query Property Wrapper Error"
description: "Fix SwiftUI @Query property wrapper SwiftData query errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI @Query Property Wrapper Error

Query property wrapper errors occur when the query is not properly configured, when the query does not fetch data, or when the query does not update with model changes.

## Common Causes
- Query not configured
- Query does not fetch data
- Query not updating
- Model not registered

## How to Fix
1. Configure query properly
2. Ensure query fetches data
3. Update query with model changes
4. Register model

```swift
struct ContentView: View {
    @Query private var items: [Item]

    var body: some View {
        List(items) { item in
            Text(item.name)
        }
    }
}
```

## Examples
```swift
// With sort descriptor
@Query(sort: \Item.name) private var items: [Item]

// With predicate
@Query(filter: #Predicate<Item> { $0.isActive }) private var items: [Item]

// With animation
@Query(sort: \Item.name, animation: .default) private var items: [Item]
```
