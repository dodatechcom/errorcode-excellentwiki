---
title: "State Derivation Error"
description: "Fix Compose state derivation patterns for complex computed values"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Computed values from multiple states produce stale or incorrect results

## Common Causes

- derivedStateOf not triggering on state change
- Multiple state sources not properly combined
- Computed value caching incorrectly
- State derivation causing infinite recomposition

## Fixes

- Use derivedStateOf for state derived from other state
- Ensure source states actually change
- Use snapshotFlow for side-effect derivations
- Profile to verify recomposition count

## Code Example

```kotlin
// Derived state from multiple sources
val isLoading by remember { derivedStateOf { uiState is UiState.Loading } }
val hasData by remember { derivedStateOf { uiState is UiState.Success } }
val errorMessage by remember { 
    derivedStateOf { 
        (uiState as? UiState.Error)?.message 
    }
}

// Combined derived state:
val canSubmit by remember {
    derivedStateOf {
        email.isNotBlank() && password.length >= 8 && !isLoading
    }
}
```

# derivedStateOf: reduces recomposition
# Use when computation is expensive
# snapshotFlow: for side-effect derivations
# Profile with Layout Inspector
