---
title: "Chip Selection Error"
description: "Fix Material 3 Chip and FilterChip selection errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Chips do not select or filter correctly in Compose

## Common Causes

- FilterChip not toggling selection
- ChipGroup not managing selection state
- AssistChip click not working
- Chip icon not displaying

## Fixes

- Use selected parameter for FilterChip
- Manage selection state with MutableState
- Set onClick for AssistChip
- Use leadingIcon for chip icon

## Code Example

```kotlin
// Filter Chip
var selected by remember { mutableStateOf(false) }
FilterChip(
    selected = selected,
    onClick = { selected = !selected },
    label = { Text("Filter") },
    leadingIcon = if (selected) {
        { Icon(Icons.Default.Check, null) }
    } else null
)

// Assist Chip
AssistChip(
    onClick = { /* action */ },
    label = { Text("Assist") },
    leadingIcon = { Icon(Icons.Default.Add, null) }
)
```

# FilterChip: toggleable selection chip
# AssistChip: action chip with icon
# InputChip: editable chip with trailing icon
# SuggestionChip: clickable suggestion
