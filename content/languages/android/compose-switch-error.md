---
title: "Switch Toggle Error"
description: "Fix Material 3 Switch and toggle component errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Switch does not toggle or display correct state

## Common Causes

- Switch not reflecting checked state
- onCheckedChange not triggering
- Switch thumb color not customizable
- Switch in list not properly aligned

## Fixes

- Use checked state with onCheckedChange
- Connect to ViewModel for state management
- Use SwitchDefaults for custom colors
- Align with ListItem for proper spacing

## Code Example

```kotlin
var checked by remember { mutableStateOf(false) }

Switch(
    checked = checked,
    onCheckedChange = { checked = it }
)

// In a list:
ListItem(
    headlineContent = { Text("Dark Mode") },
    trailingContent = {
        Switch(
            checked = darkMode,
            onCheckedChange = { viewModel.setDarkMode(it) }
        )
    }
)
```

# Switch: toggle component
# checked: current state
# onCheckedChange: state change callback
# SwitchDefaults: theme-aware defaults
