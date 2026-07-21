---
title: "Card Configuration Error"
description: "Fix Material 3 Card and elevation configuration errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Card does not display with correct elevation, shape, or colors

## Common Causes

- Card elevation not showing shadow
- Card shape not matching theme
- Card onClick not triggering
- Card colors not customizable

## Fixes

- Use CardDefaults.elevatedCardColors for custom colors
- Set shape in CardDefaults.shape
- Use onClick parameter for clickable cards
- Configure elevation with CardDefaults.elevatedCardElevation

## Code Example

```kotlin
Card(
    onClick = { onClick() },
    modifier = Modifier.fillMaxWidth(),
    shape = RoundedCornerShape(16.dp),
    colors = CardDefaults.cardColors(
        containerColor = MaterialTheme.colorScheme.surface
    ),
    elevation = CardDefaults.cardElevation(
        defaultElevation = 4.dp,
        pressedElevation = 8.dp
    )
) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Card Title", style = MaterialTheme.typography.titleMedium)
        Text("Card content goes here")
    }
}
```

# Card: elevated card
# OutlinedCard: bordered card
# FilledCard: filled background
# CardDefaults: theme-aware defaults
