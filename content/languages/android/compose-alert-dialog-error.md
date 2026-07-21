---
title: "AlertDialog Button Error"
description: "Fix Compose AlertDialog button positioning and styling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
AlertDialog buttons not properly positioned or styled

## Common Causes

- Dialog buttons reversed (confirm on left)
- Button text not matching expected labels
- Dialog not dismissing on button click
- Dialog content scrolling not working

## Fixes

- Use confirmButton and dismissButton correctly
- Style buttons with MaterialTheme
- Dismiss dialog in button click handlers
- Wrap long content in scrollable Column

## Code Example

```kotlin
AlertDialog(
    onDismissRequest = { showDialog = false },
    icon = { Icon(Icons.Default.Warning, null) },
    title = { Text("Confirm Action") },
    text = {
        // Scrollable content
        Column {
            Text("This action cannot be undone.")
            Text("Are you sure you want to proceed?")
        }
    },
    confirmButton = {
        TextButton(
            onClick = {
                viewModel.confirm()
                showDialog = false
            }
        ) {
            Text("Confirm")
        }
    },
    dismissButton = {
        TextButton(onClick = { showDialog = false }) {
            Text("Cancel")
        }
    }
)
```

# confirmButton: right/bottom button
# dismissButton: left/top button
# icon: optional icon above title
# text: scrollable content area
