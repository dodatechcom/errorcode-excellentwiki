---
title: "Switch Disabled State Error"
description: "Fix Material 3 Switch disabled state and color configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Switch does not properly indicate disabled state or custom colors

## Common Causes

- Disabled Switch not visually distinct
- Switch thumb color not customizable
- Switch track color not matching design
- Switch animation not smooth

## Fixes

- Use enabled parameter for disabled state
- Use SwitchDefaults for custom colors
- Test disabled state visual appearance
- Ensure smooth animation with state

## Code Example

```kotlin
Switch(
    checked = isChecked,
    onCheckedChange = { isChecked = it },
    enabled = isEditable,  // Disable when not editable
    colors = SwitchDefaults.colors(
        checkedThumbColor = MaterialTheme.colorScheme.primary,
        checkedTrackColor = MaterialTheme.colorScheme.primaryContainer,
        uncheckedThumbColor = MaterialTheme.colorScheme.surfaceVariant,
        uncheckedTrackColor = MaterialTheme.colorScheme.surfaceVariant,
        disabledCheckedThumbColor = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.38f),
        disabledCheckedTrackColor = MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.38f)
    )
)
```

# enabled: false for disabled state
# SwitchDefaults.colors(): theme colors
# checkedThumbColor/uncheckedThumbColor
# disabled colors for disabled state
