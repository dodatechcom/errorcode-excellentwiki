---
title: "Switch Trailing Error"
description: "Fix Material 3 Switch placement in trailing content of ListItem"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Switch in ListItem trailing content does not align or respond correctly

## Common Causes

- Switch not vertically centered with headline
- Switch click area overlapping with ListItem click
- Switch state not updating when ListItem is clicked
- Multiple Switches in list interfering

## Fixes

- Use proper ListItem slot for Switch
- Separate ListItem click from Switch click
- Use individual state for each Switch
- Test Switch interaction independently

## Code Example

```kotlin
// Switch in trailing content
ListItem(
    headlineContent = { Text("Enable Feature") },
    supportingContent = { Text("Description") },
    trailingContent = {
        Switch(
            checked = featureEnabled,
            onCheckedChange = { viewModel.setFeatureEnabled(it) }
        )
    }
)

// Multiple switches in list:
Column {
    items(settings) { setting ->
        ListItem(
            headlineContent = { Text(setting.name) },
            trailingContent = {
                Switch(
                    checked = setting.enabled,
                    onCheckedChange = { viewModel.toggleSetting(setting.id) }
                )
            }
        )
    }
}
```

# Use trailingContent for Switch slot
# Individual state per Switch
# Separate click handlers for ListItem and Switch
# Test both click areas independently
