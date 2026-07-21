---
title: "Coil LazyColumn Image Error"
description: "Fix Coil image loading in LazyColumn performance and flickering issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Images in LazyColumn flicker or load incorrectly when scrolling

## Common Causes

- Image not remembered across recompositions
- Coil not configured for LazyColumn performance
- Image request key not stable
- Placeholder shown briefly during scroll

## Fixes

- Use AsyncImage with stable model key
- Configure Coil memory and disk cache
- Use crossfade for smooth transitions
- Provide stable keys for list items

## Code Example

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        AsyncImage(
            model = ImageRequest.Builder(LocalContext.current)
                .data(item.imageUrl)
                .crossfade(true)
                .memoryCacheKey("item_${item.id}")  // Stable key
                .build(),
            contentDescription = null,
            contentScale = ContentScale.Crop,
            placeholder = painterResource(R.drawable.placeholder),
            modifier = Modifier.fillMaxWidth().height(200.dp)
        )
    }
}
```

# Use stable keys for LazyColumn items
# Configure Coil cache in Application class
# Use crossfade for smooth transitions
