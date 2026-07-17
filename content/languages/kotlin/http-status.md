---
title: "[Solution] Kotlin HttpStatusCodeException — HTTP Status Fix"
description: "Fix Kotlin HttpStatusCodeException when HTTP requests return error status codes. Handle 4xx/5xx responses, check URLs, and implement retry logic."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# HttpStatusCodeException — HTTP Status Fix

An `HttpStatusCodeException` is thrown when an HTTP request returns an error status code (4xx or 5xx). This is common with OkHttp, Ktor, and other HTTP clients.

## Description

HTTP status codes indicate the result of the request:
- **4xx Client Error** — bad request, unauthorized, not found.
- **5xx Server Error** — internal server error, service unavailable.

Common scenarios:

- **404 Not Found** — resource doesn't exist.
- **401 Unauthorized** — missing or invalid authentication.
- **403 Forbidden** — insufficient permissions.
- **500 Internal Server Error** — server-side failure.
- **429 Too Many Requests** — rate limiting.

## Common Causes

```kotlin
// Cause 1: Resource not found
val response = client.get("https://api.example.com/users/999")
// 404 Not Found

// Cause 2: Missing authentication
val response = client.get("https://api.example.com/protected")
// 401 Unauthorized

// Cause 3: Server error
val response = client.post("https://api.example.com/data") {
    setBody(invalidData)
}
// 500 Internal Server Error

// Cause 4: Rate limiting
repeat(100) {
    client.get("https://api.example.com/data")
}
// 429 Too Many Requests
```

## Solutions

### Fix 1: Handle specific status codes

```kotlin
// Wrong — no status code handling
val response = client.get("https://api.example.com/data")
val data = response.bodyAsText()  // May contain error

// Correct — check status code
val response = client.get("https://api.example.com/data")
when (response.status) {
    HttpStatusCode.OK -> {
        val data = response.bodyAsText()
        process(data)
    }
    HttpStatusCode.NotFound -> println("Resource not found")
    HttpStatusCode.Unauthorized -> println("Authentication required")
    HttpStatusCode.InternalServerError -> println("Server error")
    else -> println("Unexpected status: ${response.status}")
}
```

### Fix 2: Use try-catch with error body

```kotlin
// Wrong — ignoring error responses
val response = client.get(url)

// Correct — handle error responses
val response = client.get(url)
if (!response.status.isSuccess()) {
    val errorBody = response.bodyAsText()
    println("HTTP ${response.status.value}: $errorBody")
}
```

### Fix 3: Implement retry with backoff

```kotlin
// Wrong — single attempt
val response = client.get(url)

// Correct — retry on transient errors
suspend fun fetchWithRetry(url: String, maxRetries: Int = 3): String {
    repeat(maxRetries) { attempt ->
        val response = client.get(url)
        if (response.status.isSuccess()) {
            return response.bodyAsText()
        }
        if (response.status.value in 500..599) {
            delay(1000L * (attempt + 1))  // Exponential backoff
        } else {
            throw HttpStatusCodeException(response.status)
        }
    }
    throw HttpStatusCodeException(HttpStatusCode.InternalServerError)
}
```

### Fix 4: Configure timeouts

```kotlin
// Wrong — default timeout
val client = HttpClient {
    install(HttpTimeout) {
        requestTimeoutMillis = null  // No timeout
    }
}

// Correct — appropriate timeouts
val client = HttpClient {
    install(HttpTimeout) {
        requestTimeoutMillis = 30_000
        connectTimeoutMillis = 10_000
        socketTimeoutMillis = 10_000
    }
}
```

## Examples

```kotlin
import io.ktor.client.*
import io.ktor.client.call.*
import io.ktor.client.engine.okhttp.*
import io.ktor.client.plugins.*
import io.ktor.client.request.*
import io.ktor.http.*

fun main() = runBlocking {
    val client = HttpClient(OkHttp) {
        install(HttpTimeout) {
            requestTimeoutMillis = 10_000
        }
    }

    try {
        val response = client.get("https://httpbin.org/status/404")
        println("Status: ${response.status}")
    } catch (e: Exception) {
        println("Request failed: ${e.message}")
    } finally {
        client.close()
    }
}
```

## Related Errors

- [ConnectException]({{< relref "/languages/kotlin/connection-refused" >}}) — connection refused.
- [SocketTimeoutException]({{< relref "/languages/kotlin/socket-timeout" >}}) — request timed out.
- [IOException]({{< relref "/languages/kotlin/io-exception" >}}) — general I/O error.
