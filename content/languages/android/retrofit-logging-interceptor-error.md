---
title: "Retrofit Logging Error"
description: "Fix Retrofit logging interceptor configuration and log level errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Retrofit logging interceptor produces no output or too much output

## Common Causes

- HttpLoggingInterceptor not added to OkHttpClient
- Log level set to NONE blocking all logs
- Body logging causing OOM on large responses
- Interceptor added to wrong interceptor list

## Fixes

- Add HttpLoggingInterceptor to OkHttpClient builder
- Set appropriate log level for environment
- Use BODY level only in debug builds
- Use application interceptor for request logging

## Code Example

```kotlin
val loggingInterceptor = HttpLoggingInterceptor().apply {
    level = if (BuildConfig.DEBUG) {
        HttpLoggingInterceptor.Level.BODY
    } else {
        HttpLoggingInterceptor.Level.NONE
    }
}

val client = OkHttpClient.Builder()
    .addInterceptor(loggingInterceptor)
    .addInterceptor(authInterceptor)
    .build()
```

# Levels: NONE, BASIC, HEADERS, BODY
# Use BODY for full request/response
# Disable in production to avoid data leaks
