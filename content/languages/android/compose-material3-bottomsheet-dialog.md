---
title: "Material3 BottomSheet Error"
description: "Fix Material 3 BottomSheetScaffold and ModalBottomSheet errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Bottom sheet does not appear, drag, or dismiss correctly in Compose

## Common Causes

- ModalBottomSheet not showing when state changes
- BottomSheetScaffold content obscured
- Sheet state not properly remembered
- Drag gesture conflicting with LazyColumn

## Fixes

- Use ModalBottomSheet with sheetState
- Use rememberModalBottomSheetState to track state
- Manage showSheet state properly
- Use skipPartiallyExpanded for full-screen sheets

## Code Example

```kotlin
var showSheet by remember { mutableStateOf(false) }

if (showSheet) {
    ModalBottomSheet(
        onDismissRequest = { showSheet = false },
        sheetState = rememberModalBottomSheetState(
            skipPartiallyExpanded = true
        )
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text("Bottom Sheet Content")
            LazyColumn { /* content */ }
        }
    }
}

// BottomSheetScaffold:
BottomSheetScaffold(
    sheetContent = { /* sheet */ },
    content = { padding -> /* main content */ }
)
```

# ModalBottomSheet: overlay bottom sheet
# BottomSheetScaffold: integrated bottom sheet
# rememberModalBottomSheetState: track drag state
