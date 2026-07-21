---
title: "Compose Keyboard Error"
description: "Fix Compose keyboard handling and IME adjustment errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Keyboard covers input fields or does not dismiss when expected

## Common Causes

- Keyboard overlapping text fields
- IME padding not applied to content
- Keyboard not dismissing on background tap
- TextField not receiving focus correctly

## Fixes

- Use imePadding() for IME-aware layout
- Wrap content in Scaffold or imePadding
- Use focusRequester for explicit focus
- Use clickable to clear focus on background

## Code Example

```kotlin
// Scaffold provides IME padding
Scaffold { paddingValues ->
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(paddingValues)
            .imePadding()  // Handles keyboard overlap
    ) {
        OutlinedTextField(
            value = text,
            onValueChange = { text = it },
            modifier = Modifier.fillMaxWidth()
        )
    }
}

// Dismiss keyboard on background tap
Box(
    modifier = Modifier
        .fillMaxSize()
        .pointerInput(Unit) {
            detectTapGestures { focusManager.clearFocus() }
        }
)
```

# imePadding(): padding for keyboard
# focusManager.clearFocus(): dismiss keyboard
# Scaffold: handles system bars and IME
