---
title: "LazyColumn Key Error"
description: "Fix LazyColumn key errors causing incorrect item composition in Jetpack Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn items display incorrectly or retain stale state due to missing or wrong keys

## Common Causes

- Using index as key instead of unique identifier
- Key not unique across items
- Missing key entirely causing state reuse
- Key changes during recomposition

## Fixes

- Use stable unique ID as key, not list index
- Ensure key is truly unique for each item
- Add key parameter to items() call
- Use itemsIndexed with correct key lambda

## Code Example

```kotlin
// WRONG: using index
LazyColumn {
    items(list.size) { index ->
        ItemRow(list[index])  // State reused on reorder
    }
}

// CORRECT: using unique key
LazyColumn {
    items(list, key = { it.id }) { item ->
        ItemRow(item)  // State correctly tracked
    }
}
```

# Always provide stable keys
# Keys should not change during item lifetime
# Use database ID, UUID, or stable unique value
