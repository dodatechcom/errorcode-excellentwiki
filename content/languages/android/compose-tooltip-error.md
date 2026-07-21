---
title: "Tooltip Display Error"
description: "Fix Compose Tooltip and popup display errors in Material 3"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Tooltip does not show on long press or hover

## Common Causes

- TooltipBox not properly configured
- Tooltip not appearing on user interaction
- Tooltip position not following anchor
- Tooltip not dismissing automatically

## Fixes

- Use TooltipBox with plainTooltip or richTooltip
- Configure tooltipState for manual or auto control
- Place tooltip near anchor element
- Handle tooltip lifecycle with tooltipState

## Code Example

```kotlin
TooltipBox(
    positionProvider = TooltipDefaults.rememberPlainTooltipPositionProvider(),
    tooltip = {
        PlainTooltip { Text("Edit item") }
    },
    state = rememberTooltipState()
) {
    IconButton(onClick = { /* edit */ }) {
        Icon(Icons.Default.Edit, "Edit")
    }
}

// Rich tooltip:
TooltipBox(
    positionProvider = TooltipDefaults.rememberRichTooltipPositionProvider(),
    tooltip = {
        RichTooltip(title = { Text("Settings") }) {
            Text("Configure app preferences here")
        }
    },
    state = rememberTooltipState()
) {
    // Anchor content
}
```

# plainTooltip: simple text tooltip
# richTooltip: title + description
# tooltipState.show(): manually show
# tooltipState.dismiss(): manually dismiss
