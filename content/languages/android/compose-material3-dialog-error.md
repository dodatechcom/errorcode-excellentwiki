---
title: "Material3 Dialog Error"
description: "Fix Material 3 Dialog and AlertDialog errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Dialog does not show, dismiss, or handle actions correctly

## Common Causes

- Dialog not appearing when state changes
- Dismiss request not closing dialog
- Positive/negative buttons not wired
- Dialog blocking touch events incorrectly

## Fixes

- Use AlertDialog composable with onDismissRequest
- Control visibility with mutableStateOf
- Wire confirmButton and dismissButton
- Use Dialog for custom layouts

## Code Example

```kotlin
var showDialog by remember { mutableStateOf(false) }

if (showDialog) {
    AlertDialog(
        onDismissRequest = { showDialog = false },
        title = { Text("Confirm") },
        text = { Text("Are you sure you want to proceed?") },
        confirmButton = {
            TextButton(onClick = {
                viewModel.confirm()
                showDialog = false
            }) {
                Text("OK")
            }
        },
        dismissButton = {
            TextButton(onClick = { showDialog = false }) {
                Text("Cancel")
            }
        }
    )
}
```

# AlertDialog: pre-built dialog with buttons
# Dialog: custom dialog layout
# onDismissRequest: called when user taps outside
