---
title: "Clickable Modifier Error"
description: "Fix Compose clickable modifier and gesture detection errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Clickable modifier not working or conflicting with parent gestures

## Common Causes

- clickable modifier not responding to taps
- Long click not detected
- Clickable conflicting with scroll gestures
- Disabled state not properly handled

## Fixes

- Ensure clickable modifier is on the correct element
- Use combinedClickable for both click and long click
- Let scroll handle first in LazyColumn
- Use enabled parameter to control clickability

## Code Example

```kotlin
// Basic click
Text(
    text = "Click me",
    modifier = Modifier.clickable { onClick() }
)

// Long click
Box(
    modifier = Modifier.combinedClickable(
        onClick = { onClick() },
        onLongClick = { onLongClick() }
    )
)

// Disabled state
Button(
    onClick = { onSubmit() },
    enabled = isFormValid
) {
    Text("Submit")
}
```

# clickable: basic tap detection
# combinedClickable: tap and long press
# Use enabled parameter for disabled state
# Let parent handle scroll gestures
