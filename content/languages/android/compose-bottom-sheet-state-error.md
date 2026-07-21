---
title: "BottomSheet State Error"
description: "Fix Compose BottomSheet state management and partial expansion errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
BottomSheet does not partially expand or state changes cause incorrect behavior

## Common Causes

- Sheet state not initialized with correct skipPartiallyExpanded
- Sheet dismisses unexpectedly on state change
- Partial expansion not working with certain content heights
- Sheet state not resetting after dismiss

## Fixes

- Configure sheetState with skipPartiallyExpanded properly
- Use anchor sheet to content height
- Manage showSheet state correctly
- Reset sheet state before showing again

## Code Example

```kotlin
val sheetState = rememberModalBottomSheetState(
    skipPartiallyExpanded = false
)

if (showBottomSheet) {
    ModalBottomSheet(
        onDismissRequest = { showBottomSheet = false },
        sheetState = sheetState
    ) {
        // Sheet content
        Column(modifier = Modifier.padding(16.dp)) {
            Text("Bottom Sheet Content")
            LazyColumn { /* content */ }
        }
    }
}

// Programmatically expand:
LaunchedEffect(Unit) {
    sheetState.expand()
}
```

# skipPartiallyExpanded: skip half-expanded state
# sheetState.expand(): programmatically expand
# sheetState.partialExpand(): partially expand
# sheetState.hide(): hide sheet
