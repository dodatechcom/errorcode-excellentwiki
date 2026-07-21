---
title: "Compose Padding Structure Error"
description: "Fix Jetpack Compose padding and spacing structural errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Padding values applied incorrectly causing visual layout issues

## Common Causes

- Padding applied outside of background instead of inside
- Nested padding causing double spacing
- WindowInsets not properly consumed
- Scaffold padding not applied to content

## Fixes

- Apply padding inside modifier chain before background
- Use paddingValues from Scaffold directly
- Consume WindowInsets with contentPadding
- Use Arrangement for Column/Row spacing

## Code Example

```kotlin
// Scaffold provides padding values
Scaffold { paddingValues ->
    LazyColumn(
        modifier = Modifier.padding(paddingValues),
        contentPadding = PaddingValues(16.dp)
    ) {
        items(list) { item ->
            ItemRow(item, modifier = Modifier.padding(horizontal = 16.dp))
        }
    }
}

// Window insets:
LazyColumn(
    contentPadding = WindowInsets.systemBars.asPaddingValues()
) { ... }
```

# paddingValues from Scaffold handles system bars
# contentPadding for LazyColumn/Column first/last spacing
# item modifier padding for between-item spacing
