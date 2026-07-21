---
title: "Network Retry Strategy Error"
description: "Implement proper network retry strategy with exponential backoff in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Network requests fail without proper retry or retry too aggressively

## Common Causes

- No retry logic for transient network failures
- Retry immediately without backoff causing network storm
- Retry count not limited causing infinite loop
- Retry not distinguishing between retryable and permanent errors

## Fixes

- Implement exponential backoff with jitter
- Limit retry count per request
- Only retry on 5xx and network errors, not 4xx
- Use OkHttp interceptor for retry logic

## Code Example

```kotlin
class RetryInterceptor(private val maxRetries: Int = 3) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        var lastException: IOException? = null
        repeat(maxRetries) { attempt ->
            try {
                return chain.proceed(chain.request())
            } catch (e: IOException) {
                lastException = e
                val delayMs = (1000L * 2).coerceAtMost(30000L) * (attempt + 1)
                Thread.sleep(delayMs + Random.nextLong(0, 500))
            }
        }
        throw lastException ?: IOException("Request failed after $maxRetries retries")
    }
}
```

# Exponential backoff: 1s, 2s, 4s, 8s...
# Add jitter to prevent thundering herd
# Only retry on transient errors (5xx, timeout)
