---
title: "Glide Memory Cache Error"
description: "Fix Glide memory cache configuration and OutOfMemoryError issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Glide causes OutOfMemoryError or displays stale images from memory cache

## Common Causes

- Memory cache size too large for device
- Disk cache interfering with memory cache
- ImageView recycled while Glide loading
- Crossfade not clearing previous image

## Fixes

- Configure Glide memory cache size appropriately
- Use skipMemoryCache() for one-time images
- Use placeholder during load
- Clear Glide cache on low memory

## Code Example

```kotlin
// Custom Glide module with memory cache config
@GlideModule
class MyAppGlideModule : AppGlideModule() {
    override fun applyOptions(context: Context, builder: GlideBuilder) {
        val memoryCacheSize = (Runtime.getRuntime().maxMemory() / 8).toInt()
        builder.setMemoryCache(LruResourceCache(memoryCacheSize.toLong()))
    }
}

// Skip cache for specific load:
Glide.with(context)
    .load(url)
    .skipMemoryCache(true)
    .into(imageView)

// Clear cache on memory pressure:
Glide.get(context).clearMemory()
```

# Glide caches: memory (RAM) and disk (storage)
# skipMemoryCache(true) for unique images
# clearMemory() in onTrimMemory() callback
