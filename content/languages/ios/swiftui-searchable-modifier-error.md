---
title: "[Solution] SwiftUI .searchable Modifier Error"
description: "Fix SwiftUI .searchable modifier search field and suggestion errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .searchable Modifier Error

Searchable modifier errors occur when the search field is not properly configured, when suggestions are not displayed, or when the search does not filter content.

## Common Causes
- Search field not configured
- Suggestions not displayed
- Search does not filter content
- Search not clearing properly

## How to Fix
1. Configure search field properly
2. Display suggestions correctly
3. Filter content based on search
4. Clear search properly

```swift
struct ContentView: View {
    @State private var searchText = ""
    @State private var items: [Item] = []

    var body: some View {
        List(items) { item in
            Text(item.name)
        }
        .searchable(text: $searchText)
    }
}
```

## Examples
```swift
// With suggestions:
.searchable(text: $searchText, suggestions: {
    Text("Suggestion 1").searchCompletion("suggestion1")
    Text("Suggestion 2").searchCompletion("suggestion2")
})

// With prompt:
.searchable(text: $searchText, prompt: "Search items")

// Autocorrection disabled:
.searchable(text: $searchText, autocorrectionDisabled: true)
```
