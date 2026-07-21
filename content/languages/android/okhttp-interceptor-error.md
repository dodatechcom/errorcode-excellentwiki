---
title: "OkHttp Interceptor Error"
description: "Fix OkHttp interceptor chain errors and logging configuration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
OkHttp interceptors cause request failures or infinite loops

## Common Causes

- Interceptor calling proceed() multiple times
- Interceptor modifying request in loop
- Same interceptor added twice causing duplication
- Application interceptor vs network interceptor confused

## Fixes

- Call proceed() exactly once per interceptor
- Check for recursive interceptor calls
- Use addInterceptor for app-level, addNetworkInterceptor for network-level
- Ensure interceptor does not deadlock on synchronized blocks

## Code Example

```kotlin
val client = OkHttpClient.Builder()
    // Application interceptor (once per request)
    .addInterceptor(HttpLoggingInterceptor().apply {
        level = HttpLoggingInterceptor.Level.BODY
    })
    // Network interceptor (once per network call)
    .addNetworkInterceptor { chain ->
        val response = chain.proceed(chain.request())
        response.newBuilder()
            .header("Cache-Control", "no-cache")
            .build()
    }
    .build()
```

# Application interceptors: retry, auth, logging
# Network interceptors: cache headers, response manipulation
