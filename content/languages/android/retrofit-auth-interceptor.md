---
title: "Retrofit Auth Interceptor Error"
description: "Fix Retrofit authentication interceptor for token-based API authorization"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
API requests fail because authentication token is not properly attached

## Common Causes

- Token interceptor not added to OkHttp builder
- Token not refreshed before expired
- Authorization header format incorrect
- Token stored in non-thread-safe location

## Fixes

- Add auth interceptor to OkHttp OkHttpClient
- Implement token refresh logic in interceptor
- Use Bearer token format: Authorization: Bearer <token>
- Use synchronized access to token storage

## Code Example

```kotlin
class AuthInterceptor(private val tokenProvider: () -> String) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val request = chain.request().newBuilder()
            .addHeader("Authorization", "Bearer ${tokenProvider()}")
            .build()
        return chain.proceed(request)
    }
}

// Usage:
val client = OkHttpClient.Builder()
    .addInterceptor { chain ->
        val token = sharedPreferences.getString("token", "") ?: ""
        val request = chain.request().newBuilder()
            .addHeader("Authorization", "Bearer $token")
            .build()
        chain.proceed(request)
    }
    .build()
```

# For token refresh, use Authenticator:
val client = OkHttpClient.Builder()
    .authenticator(TokenAuthenticator())
    .build()
