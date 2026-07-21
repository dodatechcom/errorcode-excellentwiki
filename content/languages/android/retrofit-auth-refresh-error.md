---
title: "Retrofit Token Refresh Error"
description: "Fix Retrofit automatic token refresh interceptor with synchronized token update"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Token refresh fails when multiple requests trigger simultaneously causing 401 loop

## Common Causes

- Multiple 401 responses triggering simultaneous refresh
- Token refresh race condition between threads
- Refresh token also expired
- Token storage not thread-safe

## Fixes

- Use Mutex or synchronized block for token refresh
- Queue requests during token refresh
- Handle refresh token expiry separately
- Use AtomicReference for token storage

## Code Example

```kotlin
class AuthInterceptor : Interceptor {
    private val mutex = Mutex()
    private var token: String? = null

    override fun intercept(chain: Interceptor.Chain): Response {
        val request = chain.request().newBuilder()
            .header("Authorization", "Bearer ${token ?: ""}")
            .build()

        val response = chain.proceed(request)

        if (response.code == 401) {
            return runBlocking {
                mutex.withLock {
                    val newToken = refreshToken()
                    token = newToken
                    val newRequest = request.newBuilder()
                        .header("Authorization", "Bearer $newToken")
                        .build()
                    chain.proceed(newRequest)
                }
            }
        }
        return response
    }
}
```

# Mutex prevents concurrent refresh attempts
# Queue requests while refresh is in progress
# Handle both access and refresh token expiry
