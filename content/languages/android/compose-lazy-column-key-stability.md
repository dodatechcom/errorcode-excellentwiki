---
title: "LazyColumn Key Stability Error"
description: "Fix LazyColumn key stability for smooth animations and state preservation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn animations glitching because of unstable keys

## Common Causes

- Keys changing during recomposition
- Using index as key causing state reuse
- Items without keys causing full recomposition
- Key not unique across items

## Fixes

- Use stable unique IDs as keys, not indices
- Ensure keys do not change during item lifetime
- Provide keys for all list items
- Use database ID or UUID as key

## Code Example

```kotlin
// WRONG: using index as key (causes issues)
items(list.size) { index ->
    ItemRow(list[index])  // State reused on reorder
}

// CORRECT: using stable unique key
items(list, key = { it.id }) { item ->
    ItemRow(item)  // State correctly tracked
}
```

# Keys must be stable and unique
# Never use index as key
# Use database ID or UUID
# Keys prevent state reuse on reorder
