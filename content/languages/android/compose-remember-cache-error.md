---
title: "Remember Cache Error"
description: "Fix Compose remember and cache invalidation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
remember() returns stale data or does not re-compute when expected

## Common Causes

- remember key not changing when it should
- remember computing expensive value every recomposition
- rememberSaveable not persisting complex objects
- Multiple remember calls creating inconsistent state

## Fixes

- Use correct key parameters for remember
- Use key() to invalidate cache when needed
- Use Saver for complex rememberSaveable types
- Ensure remember keys are stable and meaningful

## Code Example

```kotlin
// remember with key - recomputes when key changes
val selectedItem = remember(selectedId) {
    items.find { it.id == selectedId }
}

// rememberSaveable with Saver
val nameSaver = Saver<Name, String>(
    save = { "${it.first}|${it.last}" },
    restore = { Name(it.split("|")[0], it.split("|")[1]) }
)
var name by rememberSaveable(stateSaver = nameSaver) {
    mutableStateOf(Name("John", "Doe"))
}

// remember for expensive computation
val processedData = remember(rawData) {
    rawData.map { expensiveTransform(it) }
}
```

# remember(key): recompute when key changes
# remember(): compute once per composition
# rememberSaveable: survives configuration change
# Saver: custom save/restore for complex types
