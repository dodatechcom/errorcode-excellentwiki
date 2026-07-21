---
title: "Clickable Modifier Error"
description: "Fix Compose clickable modifier for handling click events"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Click events not being handled correctly or click area not matching expected size

## Common Causes

- Click not triggering on composable
- Click area too small or too large
- Click interfering with child composables
- Click not working with enabled state

## Fixes

- Use clickable modifier for click handling
- Use combinedClickable for multiple click types
- Use enabled parameter for conditional clicks
- Test click area and event propagation

## Code Example

```kotlin
Modifier.clickable { onClick() }

// With enabled state:
Modifier.clickable(
    enabled = isEnabled,
    onClick = { onClick() }
)

// Multiple click types:
Modifier.combinedClickable(
    onClick = { onClick() },
    onLongClick = { onLongClick() },
    onDoubleClick = { onDoubleClick() }
)
```

# clickable: single click# combinedClickable: multiple click types# enabled: conditional click# Test event propagation
