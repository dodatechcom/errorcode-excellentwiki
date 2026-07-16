---
title: "[Solution] Kotlin SocketTimeoutException — Socket Timeout Fix"
description: "Fix Kotlin SocketTimeoutException when a network operation takes too long. Increase timeouts, use async operations, and handle slow networks."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["sockettimeoutexception", "timeout", "socket", "network", "slow"]
weight: 5
---

# SocketTimeoutException — Socket Timeout Fix

A `SocketTimeoutException` is thrown when a socket operation (read or write) exceeds the configured timeout. The connection was established but the operation took too long.

## Description

This is a subclass of `InterruptedIOException`. It occurs when data transfer is too slow, the server is slow to respond, or the network is congested. Unlike `ConnectException` (connection refused), this means the connection was made but timed out during data transfer.

Common scenarios:

- **Slow server response** — server takes too long to process request.
- **Large data transfer** — reading/writing too much data.
- **Network congestion** — slow or unreliable network.
- **Deadlock on server** — server stuck, never responds.

## Common Causes

```kotlin
// Cause 1: Read timeout exceeded
val socket = Socket("server", 8080)
socket.soTimeout = 1000  // 1 second timeout
val input = socket.getInputStream()
input.read()  // SocketTimeoutException if no data within 1 second

// Cause 2: Slow server response
val url = URL("https://slow-server.com/api")
val connection = url.openConnection()
connection.connectTimeout = 5000
connection.readTimeout = 3000  // SocketTimeoutException
val data = connection.getInputStream().readBytes()

// Cause 3: Large data transfer
val socket = Socket("server", 8080)
socket.soTimeout = 100
socket.getInputStream().readBytes()  // Timeout on large data

// Cause 4: Network congestion
// On slow mobile network, even fast servers may timeout
```

## Solutions

### Fix 1: Increase timeout for legitimate slow operations

```kotlin
// Wrong — timeout too short
val connection = url.openConnection()
connection.readTimeout = 100  // 100ms too short for API

// Correct — appropriate timeout
val connection = url.openConnection()
connection.readTimeout = 30_000  // 30 seconds for API
```

### Fix 2: Use async operations with cancellation

```kotlin
// Wrong — blocking with short timeout
val socket = Socket("server", 8080)
socket.soTimeout = 1000
val data = socket.getInputStream().readBytes()

// Correct — async with timeout and cancellation
val job = launch(Dispatchers.IO) {
    val socket = Socket("server", 8080)
    socket.soTimeout = 10_000
    val data = socket.getInputStream().readBytes()
}
// Cancel if taking too long
delay(15_000)
if (job.isActive) {
    job.cancel()
    println("Operation timed out")
}
```

### Fix 3: Use streaming for large data

```kotlin
// Wrong — read everything into memory
val data = url.openStream().readBytes()  // May timeout on large files

// Correct — stream in chunks
url.openStream().use { stream ->
    val buffer = ByteArray(8192)
    while (true) {
        val bytesRead = stream.read(buffer)
        if (bytesRead == -1) break
        processChunk(buffer.copyOf(bytesRead))
    }
}
```

### Fix 4: Implement retry with timeout handling

```kotlin
suspend fun fetchWithRetry(url: String, maxRetries: Int = 3): ByteArray? {
    repeat(maxRetries) { attempt ->
        try {
            return withContext(Dispatchers.IO) {
                URL(url).readBytes()
            }
        } catch (e: SocketTimeoutException) {
            println("Attempt ${attempt + 1} timed out")
            if (attempt < maxRetries - 1) {
                delay(1000L * (attempt + 1))
            }
        }
    }
    return null
}
```

## Examples

```kotlin
import java.net.*

fun main() {
    val url = URL("https://httpbin.org/delay/5")

    try {
        val connection = url.openConnection() as HttpURLConnection
        connection.connectTimeout = 5000
        connection.readTimeout = 10_000

        val data = connection.inputStream.bufferedReader().readText()
        println("Response: ${data.take(100)}")
    } catch (e: SocketTimeoutException) {
        println("Request timed out: ${e.message}")
    } finally {
        // Clean up
    }
}
```

## Related Errors

- [ConnectException]({{< relref "/languages/kotlin/connection-refused" >}}) — connection refused by server.
- [IOException]({{< relref "/languages/kotlin/io-exception" >}}) — general I/O error.
- [SSLHandshakeException]({{< relref "/languages/kotlin/ssl-handshake" >}}) — SSL/TLS handshake failed.
