---
title: "Complex State Hoisting Error"
description: "Fix complex state hoisting patterns in Jetpack Compose multi-level components"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
State does not propagate correctly through deeply nested Compose component hierarchy

## Common Causes

- Intermediate composable not forwarding state
- Callback not properly wired through component tree
- State reset when recomposing parent
- Nested remember calls creating separate state instances

## Fixes

- Hoist state to highest common ancestor
- Pass state and callbacks as parameters at each level
- Use CompositionLocal for deeply nested state
- Avoid remember in intermediate composables

## Code Example

```kotlin
// WRONG: state trapped in intermediate component
@Composable
fun Parent() {
    @Composable
    fun Intermediate() {
        var text by remember { mutableStateOf("") }  // Not accessible!
        Child(text = text)
    }
}

// CORRECT: state hoisted to parent
@Composable
fun Parent() {
    var text by remember { mutableStateOf("") }
    Intermediate(text = text, onTextChange = { text = it })
}

@Composable
fun Intermediate(text: String, onTextChange: (String) -> Unit) {
    Child(text = text, onTextChange = onTextChange)
}

// For deeply nested state, use CompositionLocal:
val LocalAuthState = compositionLocalOf<AuthState> { error("No auth") }
```

# State hoisting: state UP, events DOWN
# CompositionLocal for context-like state
# Avoid state in intermediate composables
