---
title: "Material3 Button Error"
description: "Fix Material 3 button styling and click handling errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Material 3 buttons do not display correct styles or respond to clicks

## Common Causes

- Button content color not matching theme
- OutlinedButton vs Button not distinguished
- Click handler not triggering
- Button state not updating after click

## Fixes

- Use Button, OutlinedButton, or TextButton for correct styles
- Set colors parameter for custom button colors
- Use onClick lambda for click handling
- Manage button state with remember and mutableStateOf

## Code Example

```kotlin
// Regular Button
Button(
    onClick = { viewModel.submit() },
    colors = ButtonDefaults.buttonColors(
        containerColor = MaterialTheme.colorScheme.primary
    )
) {
    Text("Submit")
}

// Outlined Button
OutlinedButton(onClick = { /* click */ }) {
    Text("Cancel")
}

// Text Button
TextButton(onClick = { /* click */ }) {
    Text("Learn More")
}
```

# Button: filled
# OutlinedButton: bordered
# TextButton: text only
# FilledTonalButton: filled with tone
