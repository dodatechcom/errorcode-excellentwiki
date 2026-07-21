---
title: "State Hoisting Error"
description: "Fix Compose state hoisting pattern for reusable composables"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable not properly hoisting state making it difficult to test or reuse

## Common Causes

- State trapped inside composable making it non-reusable
- Cannot set initial state from parent
- Cannot observe state changes from parent
- Composable not following unidirectional data flow

## Fixes

- Hoist state to parent composable
- Pass state down as parameters
- Pass callbacks for state changes
- Follow unidirectional data flow pattern

## Code Example

```kotlin
// State trapped inside (NOT reusable):
@Composable
fun BadTextField() {
    var text by remember { mutableStateOf("") }
    TextField(value = text, onValueChange = { text = it })
}

// State hoisted (reusable):
@Composable
fun GoodTextField(
    value: String,
    onValueChange: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    TextField(value = value, onValueChange = onValueChange, modifier = modifier)
}
```

# Hoist state to parent# Pass value and onValueChange# Unidirectional data flow# Makes composable reusable and testable
