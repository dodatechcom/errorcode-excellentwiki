---
title: "LazyColumn Performance Error"
description: "Fix LazyColumn performance optimization and item recycling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn scrolls slowly or janks because of performance issues

## Common Causes

- Items too complex causing slow rendering
- Images not cached causing network calls during scroll
- Layout calculations too expensive
- Item recomposition happening too frequently

## Fixes

- Simplify item composable layout
- Use Coil/Glide for image caching
- Use fixed item heights when possible
- Use key for stable item identity

## Code Example

```kotlin
LazyColumn(
    modifier = Modifier.fillMaxSize()
) {
    items(items, key = { it.id }) { item ->
        // Keep item composable simple
        Row(
            modifier = Modifier.fillMaxWidth().padding(8.dp)
        ) {
            AsyncImage(
                model = item.imageUrl,
                contentDescription = null,
                modifier = Modifier.size(48.dp)
            )
            Column(modifier = Modifier.weight(1f)) {
                Text(item.title, maxLines = 1)
                Text(item.subtitle, maxLines = 2)
            }
        }
    }
}
```

# Simple item layouts for performance
# Image caching with Coil/Glide
# Fixed item heights for better recycling
# key parameter for stable items
