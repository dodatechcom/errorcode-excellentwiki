---
title: "Focus Modifier Error"
description: "Fix Compose focus modifier for keyboard and programmatic focus management"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable not receiving focus correctly or focus behavior not matching expected

## Common Causes

- Focus not moving between composables
- Programmatic focus not working
- Focus indicators not appearing
- Focus request not being honored

## Fixes

- Use focusRequester for programmatic focus
- Use focusable modifier for focusable composables
- Use onKeyEvent for keyboard input
- Test focus traversal with Tab key

## Code Example

```kotlin
val focusRequester = rememberFocusRequester()

Modifier
    .focusRequester(focusRequester)
    .focusable()
    .onKeyEvent { event ->
        if (event.key == Key.DirectionRight && event.type == KeyEventType.KeyDown) {
            // Handle key event
            true
        } else false
    }

// Programmatic focus:
LaunchedEffect(Unit) {
    focusRequester.requestFocus()
}
```

# focusRequester: programmatic focus# focusable: makes composable focusable# onKeyEvent: keyboard input# request.requestFocus(): request focus
