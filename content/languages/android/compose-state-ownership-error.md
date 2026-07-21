---
title: "State Ownership Error"
description: "Fix Compose state ownership and single source of truth architecture errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Multiple composables own the same state causing inconsistencies

## Common Causes

- Same state duplicated in multiple composables
- State updated in one place but not reflected elsewhere
- Hoisted state not reaching all required composables
- State mutation scattered across component tree

## Fixes

- Lift state to highest common ancestor
- Use single ViewModel for shared state
- Pass state down through composable parameters
- Never duplicate state across components

## Code Example

```kotlin
// WRONG: state duplicated
@Composable
fun ParentA() {
    var text by remember { mutableStateOf("") }  // Duplicate!
}
@Composable
fun ParentB() {
    var text by remember { mutableStateOf("") }  // Different state!
}

// CORRECT: single source
@Composable
fun Parent() {
    var text by remember { mutableStateOf("") }  // Single source
    ChildA(text = text)
    ChildB(text = text)
}

// Or use ViewModel for complex state:
@Composable
fun Screen(viewModel: MyViewModel = hiltViewModel()) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    // Single source of truth
}
```

# Single source of truth
# Lift state to common ancestor
# ViewModel for shared state
# Never duplicate state
