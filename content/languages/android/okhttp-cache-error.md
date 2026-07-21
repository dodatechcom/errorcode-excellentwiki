---
title: "OkHttp Cache Error"
description: "Fix OkHttp cache configuration and cache hit/miss errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
OkHttp caching does not work as expected causing unnecessary network calls

## Common Causes

- Cache size too small for responses
- Server response not cacheable (no-cache header)
- Cache directory not writable
- POST requests not cached by default

## Fixes

- Set appropriate cache size (10MB recommended)
- Check server Cache-Control headers
- Ensure cache directory is writable
- Use interceptors to force cache for specific endpoints

## Code Example

```kotlin
val cacheSize = 10L * 1024 * 1024  // 10 MB
val cache = Cache(context.cacheDir, cacheSize)

val client = OkHttpClient.Builder()
    .cache(cache)
    .addInterceptor { chain ->
        val request = chain.request()
            .newBuilder()
            .cacheControl(CacheControl.FORCE_CACHE)
            .build()
        chain.proceed(request)
    }
    .build()
```

# Check cache status:
val response = client.newCall(request).execute()
Log.d("Cache", response.cacheResponse?.toString() ?: "NO CACHE")
Log.d("Network", response.networkResponse?.toString() ?: "NO NETWORK")
