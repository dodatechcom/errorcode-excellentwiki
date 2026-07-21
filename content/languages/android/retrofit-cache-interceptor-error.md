---
title: "Retrofit Cache Interceptor Error"
description: "Fix Retrofit cache interceptor for offline support and stale data handling"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit caching does not provide offline support or returns stale data

## Common Causes

- Cache not configured on OkHttpClient
- Server Cache-Control headers not overridden
- Offline cache not forcing cache read
- Cache size too small for response data

## Fixes

- Configure Cache directory and size on OkHttpClient
- Add interceptor to force cache when offline
- Override Cache-Control headers with interceptor
- Use appropriate cache size for data volume

## Code Example

```kotlin
val cacheSize = 10L * 1024 * 1024  // 10 MB
val cache = Cache(context.cacheDir, cacheSize)

val client = OkHttpClient.Builder()
    .cache(cache)
    .addInterceptor { chain ->
        var request = chain.request()
        if (!isNetworkAvailable()) {
            request = request.newBuilder()
                .cacheControl(CacheControl.FORCE_CACHE)
                .build()
        }
        chain.proceed(request)
    }
    .addNetworkInterceptor { chain ->
        val response = chain.proceed(chain.request())
        response.newBuilder()
            .header("Cache-Control", "public, max-age=300")
            .build()
    }
    .build()
```

# Cache: directory + size
# FORCE_CACHE: use cache even if stale
# max-age: cache duration in seconds
