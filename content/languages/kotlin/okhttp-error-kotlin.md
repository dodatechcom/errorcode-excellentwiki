---
title: "[Solution] Kotlin OkHttp Connection Error Fix"
description: "Fix OkHttp connection errors in Kotlin. Learn why OkHttp requests fail and how to handle HTTP client issues."
languages: ["kotlin"]
severities: ["error"]
error-types: ["network-error"]
weight: 5
---

## What This Error Means

An OkHttp connection error occurs when HTTP requests made with OkHttp fail. This can happen due to network issues, SSL problems, or timeout configuration.

## Common Causes

- Network unreachable
- SSL certificate issues
- Connection timeout
- DNS resolution failure

## How to Fix

```kotlin
// WRONG: Not handling connection errors
val client = OkHttpClient()
val request = Request.Builder().url("https://api.example.com").build()
val response = client.newCall(request).execute()  // May throw

// CORRECT: Handle exceptions
try {
    val client = OkHttpClient()
    val request = Request.Builder().url("https://api.example.com").build()
    val response = client.newCall(request).execute()
    if (response.isSuccessful) {
        val body = response.body?.string()
    }
} catch (e: IOException) {
    println("Connection error: ${e.message}")
}
```

```kotlin
// WRONG: Default timeout too short
val client = OkHttpClient()  // 10s default

// CORRECT: Configure timeouts
val client = OkHttpClient.Builder()
    .connectTimeout(30, TimeUnit.SECONDS)
    .readTimeout(30, TimeUnit.SECONDS)
    .writeTimeout(30, TimeUnit.SECONDS)
    .build()
```

## Examples

```kotlin
// Example 1: Basic OkHttp
val client = OkHttpClient()
val request = Request.Builder()
    .url("https://api.example.com/users")
    .build()

client.newCall(request).enqueue(object : Callback {
    override fun onFailure(call: Call, e: IOException) {
        println("Error: ${e.message}")
    }
    override fun onResponse(call: Call, response: Response) {
        response.body?.string()?.let { println(it) }
    }
})
```

## Related Errors

- [Retrofit Kotlin error](retrofit-kotlin) — Retrofit error
- [Fuel HTTP client error](fuel-error) — Fuel error
- [Ktor request error](ktor-requesterror) — Ktor error
