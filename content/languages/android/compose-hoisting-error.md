---
title: "Compose State Hoisting Error"
description: "Fix state hoisting errors in Jetpack Compose for reusable composable components"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable component does not update because state is not properly hoisted

## Common Causes

- State held inside composable instead of being hoisted
- onValueChange callback not properly wired
- Remember inside child when state should be parent-owned
- MutableState not passed down as parameter

## Fixes

- Lift state up to parent composable
- Pass value and onValueChange as separate params
- Use remember in parent, not child
- Follow state hoisting pattern: state down, events up

## Code Example

```kotlin
// WRONG: state inside child
@Composable
fun MyTextField() {
    var text by remember { mutableStateOf("") }  // Not hoisted
    TextField(value = text, onValueChange = { text = it })
}

// CORRECT: state hoisted to parent
@Composable
fun MyTextField(
    value: String,
    onValueChange: (String) -> Unit
) {
    TextField(value = value, onValueChange = onValueChange)
}

// Parent holds state:
@Composable
fun ParentScreen() {
    var text by remember { mutableStateOf("") }
    MyTextField(value = text, onValueChange = { text = it })
}
```

# State hoisting pattern:
# State goes DOWN to child
# Events go UP from child to parent
# Child is stateless and reusable
