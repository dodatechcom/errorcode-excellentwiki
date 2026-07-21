---
title: "ModalBottomSheet Behavior Error"
description: "Fix Compose ModalBottomSheet display and dismiss behavior errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ModalBottomSheet does not show or dismiss correctly

## Common Causes

- Sheet not appearing when showSheet = true
- Sheet dismissing unexpectedly on configuration change
- Sheet state not resetting after dismiss
- Drag to dismiss not working

## Fixes

- Use ModalBottomSheet with proper state
- Manage showSheet state correctly
- Reset sheetState before showing again
- Configure sheetState for drag behavior

## Code Example

```kotlin
var showSheet by remember { mutableStateOf(false) }
val sheetState = rememberModalBottomSheetState()

if (showSheet) {
    ModalBottomSheet(
        onDismissRequest = { showSheet = false },
        sheetState = sheetState
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text("Bottom Sheet Content")
            Button(onClick = { showSheet = false }) {
                Text("Close")
            }
        }
    }
}

// Show sheet:
Button(onClick = { showSheet = true }) {
    Text("Show Sheet")
}
```

# ModalBottomSheet: overlay bottom sheet
# sheetState: manage sheet position
# onDismissRequest: handle dismiss
# showSheet: control visibility
