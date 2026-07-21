---
title: "[Solution] SwiftUI .searchable Placement Error"
description: "Fix SwiftUI searchable bar placement configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .searchable Placement Error

Searchable placement errors occur when the search bar is not properly positioned, when the placement conflicts with other toolbar items, or when the placement is not available on the current iOS version.

## Common Causes
- Search bar not positioned correctly
- Placement conflicts with toolbar items
- Placement not available on iOS version
- Multiple searchable modifiers conflicting

## How to Fix
1. Ensure searchable is in navigation context
2. Place searchable after other modifiers
3. Check iOS version compatibility
4. Use only one searchable per navigation stack

```swift
NavigationStack {
    List {
        ForEach(items) { item in
            Text(item.name)
        }
    }
    .searchable(text: $searchText)
}
```

## Examples
```swift
// Searchable with placement:
NavigationStack {
    List {
        ForEach(items) { item in
            Text(item.name)
        }
    }
    .searchable(text: $searchText, placement: .navigationBarDrawer(displayMode: .always))
}
```
