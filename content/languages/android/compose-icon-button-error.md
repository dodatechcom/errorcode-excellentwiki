---
title: "IconButton Sizing Error"
description: "Fix Material 3 IconButton and FAB sizing and click handling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
IconButton or FAB does not have correct size or click area

## Common Causes

- IconButton touch area too small
- FAB not showing icon centered
- IconButton not triggering click
- ExtendedFAB text not showing

## Fixes

- Use minimumInteractiveComponentSize for touch target
- Use contentAlignment for icon centering
- Set onClick on IconButton or FAB
- Use ExtendedFAB for text + icon

## Code Example

```kotlin
// Standard FAB
FloatingActionButton(
    onClick = { onClick() },
    containerColor = MaterialTheme.colorScheme.primary
) {
    Icon(Icons.Default.Add, contentDescription = "Add")
}

// Extended FAB
ExtendedFloatingActionButton(
    onClick = { onClick() },
    icon = { Icon(Icons.Default.Edit, null) },
    text = { Text("Compose") }
)

// Icon Button
IconButton(
    onClick = { onClick() },
    modifier = Modifier.minimumInteractiveComponentSize()
) {
    Icon(Icons.Default.MoreVert, contentDescription = "Menu")
}
```

# FAB: floating action button
# ExtendedFAB: FAB with text
# IconButton: icon-only button
# minimumInteractiveComponentSize: 48dp touch target
