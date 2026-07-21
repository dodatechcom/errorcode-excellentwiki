---
title: "[Solution] SwiftUI ForEach Delete Error"
description: "Fix SwiftUI ForEach deletion animation and data source sync errors."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI ForEach Delete Error

ForEach deletion errors occur when the data source is not properly updated, when the deletion animation conflicts with the view update, or when the id assignment changes after deletion.

## Common Causes
- Data source not updated after deletion
- Animation timing conflicts with data update
- Identifiable IDs regenerated after deletion
- onDelete not implemented on ForEach

## How to Fix
1. Update data source in onDelete handler
2. Use proper animation for deletion
3. Ensure IDs remain stable after deletion
4. Implement onDelete on the ForEach or parent

```swift
// ForEach with deletion:
ForEach(items) { item in
    Text(item.name)
}
.onDelete { indexSet in
    withAnimation {
        items.remove(atOffsets: indexSet)
    }
}
```

## Examples
```swift
// Move and delete:
List {
    ForEach(items) { item in
        Text(item.name)
    }
    .onMove { source, destination in
        items.move(fromOffsets: source, toOffset: destination)
    }
    .onDelete { indexSet in
        items.remove(atOffsets: indexSet)
    }
}
.editing()
```
