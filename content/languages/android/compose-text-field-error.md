---
title: "Compose TextField Error"
description: "Fix Material 3 TextField and OutlinedTextField state management errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
TextField does not properly handle text input or state updates

## Common Causes

- TextField value not updating on text change
- TextField not clearing after submission
- Keyboard not showing when TextField focused
- TextField error state not displaying

## Fixes

- Use onValueChange to update state
- Clear text state after successful submission
- Use focusRequester for programmatic focus
- Use isError and supportingText for errors

## Code Example

```kotlin
var text by remember { mutableStateOf("") }
var error by remember { mutableStateOf<String?>(null) }

OutlinedTextField(
    value = text,
    onValueChange = { 
        text = it
        error = null  // Clear error on input
    },
    label = { Text("Email") },
    isError = error != null,
    supportingText = {
        error?.let { Text(it, color = MaterialTheme.colorScheme.error) }
    },
    keyboardOptions = KeyboardOptions(
        keyboardType = KeyboardType.Email,
        imeAction = ImeAction.Next
    ),
    singleLine = true,
    modifier = Modifier.fillMaxWidth()
)
```

# value: current text
# onValueChange: update on text change
# isError: show error state
# supportingText: error or helper text
