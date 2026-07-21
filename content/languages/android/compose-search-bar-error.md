---
title: "SearchBar Configuration Error"
description: "Fix Material 3 SearchBar configuration and expand/collapse errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
SearchBar does not expand, collapse, or handle input correctly

## Common Causes

- SearchBar not expanding on click
- Search results not updating with input
- Active state not properly managed
- Back button not collapsing search

## Fixes

- Use active state to control expansion
- Update results based on query changes
- Handle back press to collapse search
- Use onActiveChange callback for state management

## Code Example

```kotlin
var query by remember { mutableStateOf("") }
var active by remember { mutableStateOf(false) }

SearchBar(
    query = query,
    onQueryChange = { query = it },
    onSearch = { performSearch(query) },
    active = active,
    onActiveChange = { active = it },
    placeholder = { Text("Search...") },
    leadingIcon = { Icon(Icons.Default.Search, null) },
    trailingIcon = {
        if (active) {
            IconButton(onClick = { query = ""; active = false }) {
                Icon(Icons.Default.Close, null)
            }
        }
    }
) {
    // Search suggestions
    searchResults.forEach { result ->
        ListItem(
            headlineContent = { Text(result.title) },
            modifier = Modifier.clickable {
                query = result.title
                active = false
            }
        )
    }
}
```

# SearchBar: Material 3 search component
# active: controls expanded state
# onSearch: triggered on keyboard submit
# onActiveChange: expand/collapse callback
