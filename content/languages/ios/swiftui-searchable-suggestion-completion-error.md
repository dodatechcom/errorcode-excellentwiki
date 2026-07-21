---
title: "[Solution] SwiftUI .searchable Suggestion Completion Error"
description: "Fix SwiftUI searchable suggestion completion configuration errors in iOS."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# SwiftUI .searchable Suggestion Completion Error

Suggestion completion fails when the search completion is not properly connected to the suggestion, when the suggestion text does not match available results, or when the suggestion is not dismissed after selection.

## Common Causes
- Search completion not connected to suggestion
- Suggestion text mismatch with results
- Suggestion not dismissed after selection
- Multiple suggestions with same completion

## How to Fix
1. Connect searchCompletion to suggestion text
2. Ensure suggestion text matches results
3. Dismiss suggestions after selection
4. Use unique completion values

```swift
.searchable(text: $searchText, prompt: "Search")
.searchSuggestions {
    ForEach(suggestions, id: \.self) { suggestion in
        Text(suggestion).searchCompletion(suggestion)
    }
}
```

## Examples
```swift
// Dynamic suggestions:
.searchable(text: $searchText)
.searchSuggestions {
    if searchText.isEmpty {
        ForEach(recentSearches, id: \.self) { recent in
            Label(recent, systemImage: "clock.arrow.circlepath")
                .searchCompletion(recent)
        }
    } else {
        ForEach(filteredSuggestions, id: \.self) { suggestion in
            Text(suggestion).searchCompletion(suggestion)
        }
    }
}
```
