---
title: "Material3 TextField Error"
description: "Fix Material 3 TextField and OutlinedTextField errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
TextField does not display correctly or handle input properly

## Common Causes

- TextField value not updating
- Label and placeholder not showing
- Error state not displaying
- Keyboard actions not configured

## Fixes

- Use onValueChange to update state
- Set label and placeholder parameters
- Use isError parameter for error state
- Configure keyboardOptions and keyboardActions

## Code Example

```kotlin
OutlinedTextField(
    value = text,
    onValueChange = { text = it },
    label = { Text("Email") },
    placeholder = { Text("Enter your email") },
    isError = emailError != null,
    supportingText = {
        emailError?.let { Text(it, color = MaterialTheme.colorScheme.error) }
    },
    keyboardOptions = KeyboardOptions(
        keyboardType = KeyboardType.Email,
        imeAction = ImeAction.Next
    ),
    keyboardActions = KeyboardActions(
        onNext = { focusManager.moveFocus(FocusDirection.Down) }
    ),
    singleLine = true,
    modifier = Modifier.fillMaxWidth()
)
```

# OutlinedTextField: outlined border
# TextField: filled background
# isError: shows error styling
# supportingText: error or helper text
