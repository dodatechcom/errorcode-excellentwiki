---
title: "Recomposition Scope Error"
description: "Fix Compose recomposition scope to prevent unnecessary recompositions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Parent recomposition triggering child recomposition when child data unchanged

## Common Causes

- Child recomposing when only sibling changes
- Unnecessary recomposition causing performance issues
- State change propagating too far in tree
- Lambda being recreated causing recomposition

## Fixes

- Move state down to where it is used
- Use derivedStateOf for computed values
- Remember lambda instances with stable inputs
- Test recomposition count with RecompositionLogger

## Code Example

```kotlin
// WRONG: state at parent causes child recomposition
@Composable
fun Parent() {
    var count by remember { mutableStateOf(0) }
    Child(count)  // Child recomposes on count change
    UnrelatedChild()  // Also recomposes unnecessarily
}

// CORRECT: state at child
@Composable
fun Parent() {
    Child()
    UnrelatedChild()
}

@Composable
fun Child() {
    var count by remember { mutableStateOf(0) }
    // Only this Child recomposes
}
```

# Move state to where it is used# derivedStateOf for computed values# Remember lambdas with stable inputs# Use RecompositionLogger to verify
