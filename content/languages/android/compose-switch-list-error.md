---
title: "Switch List Item Error"
description: "Fix Material 3 Switch in ListItem with proper alignment and state"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Switch in ListItem does not align properly or state management fails

## Common Causes

- Switch not aligned with text in ListItem
- Switch state not updating when toggled
- Multiple switches interfering with each other
- Switch label not showing

## Fixes

- Use trailingContent slot for Switch in ListItem
- Use individual MutableState for each switch
- Connect to ViewModel for state management
- Add label above or beside switch

## Code Example

```kotlin
ListItem(
    headlineContent = { Text("Notifications") },
    supportingContent = { Text("Enable push notifications") },
    trailingContent = {
        Switch(
            checked = notificationsEnabled,
            onCheckedChange = { viewModel.setNotifications(it) }
        )
    }
)

// Multiple switches:
ListItem(
    headlineContent = { Text("Dark Mode") },
    trailingContent = {
        Switch(
            checked = darkMode,
            onCheckedChange = { viewModel.setDarkMode(it) }
        )
    }
)
ListItem(
    headlineContent = { Text("Auto-sync") },
    trailingContent = {
        Switch(
            checked = autoSync,
            onCheckedChange = { viewModel.setAutoSync(it) }
        )
    }
)
```

# Use trailingContent for Switch in ListItem
# Individual state for each Switch
# Connect to ViewModel for persistence
