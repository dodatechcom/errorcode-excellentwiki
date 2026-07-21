---
title: "Coil Compose Configuration Error"
description: "Fix Coil image loading configuration and memory management errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Coil images do not load or cause memory issues in LazyColumn

## Common Causes

- Coil not configured with crossfade
- Image flickering in LazyColumn scroll
- Memory cache not properly configured
- Image request not using stable key

## Fixes

- Configure Coil with crossfade in Application
- Use stable memoryCacheKey for list items
- Set appropriate image size for container
- Enable disk cache for network images

## Code Example

```kotlin
// Application-level Coil configuration
@GlideModule
class MyAppGlideModule : AppGlideModule() {
    override fun applyOptions(context: Context, builder: GlideBuilder) {
        builder.setMemoryCache(LruResourceCache(20 * 1024 * 1024))
    }
}

// In LazyColumn:
AsyncImage(
    model = ImageRequest.Builder(LocalContext.current)
        .data(item.imageUrl)
        .crossfade(true)
        .memoryCacheKey("item_${item.id}")
        .size(Size.ORIGINAL)
        .build(),
    contentDescription = item.name,
    contentScale = ContentScale.Crop,
    modifier = Modifier.fillMaxWidth().height(200.dp)
)
```

# Crossfade for smooth loading
# memoryCacheKey for stable list item images
# Set image size for memory efficiency
# Use disk cache for network images
