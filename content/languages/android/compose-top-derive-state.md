---
title: "Derived State Error"
description: "Fix Compose derivedStateOf for efficient computed state in recomposition"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Derived state not updating or causing performance issues from incorrect usage

## Common Causes

- derivedStateOf not triggering recomposition
- Using derivedStateOf unnecessarily
- State dependency not correctly specified
- Performance degradation from over-use

## Fixes

- Use derivedStateOf for state derived from other state
- Do not use for simple state transformations
- Ensure correct dependencies
- Use snapshotFlow for side effects from state

## Code Example

```kotlin
// CORRECT: derived from another state
val count by remember { mutableIntStateOf(0) }
val message by remember {
    derivedStateOf { if (count > 0) "Count: $count" else "Empty" }
}

// WRONG: not derived from state, just a transform
val doubled = remember { derivedStateOf { count * 2 } }
// Use: val doubled = count * 2
```

# derivedStateOf: for state-dependent computed values# Do not use for simple transformations# snapshotFlow: for side effects from state# Test recomposition count
