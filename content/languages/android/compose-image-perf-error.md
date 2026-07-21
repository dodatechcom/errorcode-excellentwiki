---
title: "Compose Image Performance Error"
description: "Fix Compose image loading and display performance issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Images in Compose cause jank or memory issues during loading

## Common Causes

- Loading full-resolution images without downsampling
- Image not cached properly across recompositions
- Multiple images loading simultaneously on scroll
- Coil/Glide not configured for memory efficiency

## Fixes

- Use AsyncImage with crossfade for smooth loading
- Configure Coil memory and disk cache
- Use contentScale to fit images to container
- Set placeholder during load to prevent layout shift

## Code Example

```kotlin
AsyncImage(
    model = ImageRequest.Builder(context)
        .data(imageUrl)
        .crossfade(true)
        .memoryCachePolicy(CachePolicy.ENABLED)
        .diskCachePolicy(CachePolicy.ENABLED)
        .build(),
    contentDescription = null,
    contentScale = ContentScale.Crop,
    placeholder = painterResource(R.drawable.placeholder),
    modifier = Modifier
        .fillMaxWidth()
        .height(200.dp)
)
```

# Use Coil/Glide for automatic downsampling
# Enable memory and disk caching
# Use placeholder to prevent layout shift
