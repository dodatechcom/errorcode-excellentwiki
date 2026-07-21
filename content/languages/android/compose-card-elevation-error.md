---
title: "Card Elevation Error"
description: "Fix Material 3 Card elevation and shadow rendering errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Card shadow not visible or elevation not responding to interaction

## Common Causes

- Card elevation not showing shadow
- Elevation not changing on press
- Card shape affecting shadow rendering
- Elevation values too subtle to see

## Fixes

- Use CardDefaults.elevatedCardElevation for custom shadows
- Set pressedElevation for interactive feedback
- Ensure card has proper shape for shadows
- Use higher elevation values for visible shadows

## Code Example

```kotlin
Card(
    onClick = { onClick() },
    elevation = CardDefaults.cardElevation(
        defaultElevation = 2.dp,
        pressedElevation = 8.dp,
        focusedElevation = 4.dp
    ),
    colors = CardDefaults.cardColors(
        containerColor = MaterialTheme.colorScheme.surface
    ),
    shape = RoundedCornerShape(12.dp)
) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Card with elevation", style = MaterialTheme.typography.titleMedium)
    }
}
```

# defaultElevation: resting shadow
# pressedElevation: pressed state shadow
# focusedElevation: focused state shadow
# disabledElevation: disabled state shadow
