---
title: "Swipe Gesture Error"
description: "Fix Compose swipe-to-dismiss and horizontal swipe gesture errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Swipe to dismiss does not work or swipes in wrong direction

## Common Causes

- SwipeToDismiss not configured correctly
- Swipe direction restricted incorrectly
- Dismiss action not triggering
- Background not showing during swipe

## Fixes

- Use SwipeToDismiss with proper state
- Set confirmValueChange for dismiss confirmation
- Show background during swipe with animated content
- Handle undo after dismiss

## Code Example

```kotlin
var dismissState = rememberSwipeToDismissBoxState(
    confirmValueChange = { dismissValue ->
        if (dismissValue == SwipeToDismissBoxValue.EndToStart) {
            showUndoSnackbar()
            true
        } else false
    }
)

SwipeToDismissBox(
    state = dismissState,
    backgroundContent = {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(Color.Red)
                .padding(16.dp),
            contentAlignment = Alignment.CenterEnd
        ) {
            Icon(Icons.Default.Delete, "Delete")
        }
    }
) {
    ListItem(item)
}
```

# SwipeToDismissBox: swipe to dismiss
# EndToStart: swipe left to dismiss
# StartToEnd: swipe right to dismiss
# confirmValueChange: confirm before dismiss
