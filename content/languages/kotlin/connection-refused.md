---
title: "[Solution] Kotlin ConnectException — Connection Refused Fix"
description: "Fix Kotlin ConnectException when network connection is refused. Check server availability, port numbers, and firewall settings."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ConnectException — Connection Refused Fix

A `ConnectException` is thrown when a connection attempt is refused by the remote host. The server may be down, the port may be wrong, or a firewall may be blocking the connection.

## Description

This is a subclass of `SocketException` (which extends `IOException`). It indicates the TCP SYN packet was rejected (RST) or no service is listening on the target port.

Common scenarios:

- **Server not running** — target process not started.
- **Wrong port number** — connecting to incorrect port.
- **Firewall blocking** — network rules prevent connection.
- **Server overloaded** — too many connections, server rejects new ones.
- **DNS resolves but service unavailable** — hostname correct but service down.

## Common Causes

```kotlin
// Cause 1: Server not running
val socket = Socket("localhost", 8080)  // ConnectException: Connection refused

// Cause 2: Wrong port
val socket = Socket("localhost", 9999)  // ConnectException: wrong port

// Cause 3: Firewall blocking
val socket = Socket("10.0.0.1", 80)  // ConnectException: firewall blocking

// Cause 4: Server not ready yet
// Server starting asynchronously
val socket = Socket("localhost", 8080)  // ConnectException: server not ready
```

## Solutions

### Fix 1: Verify server is running

```kotlin
// Wrong — assume server is running
val socket = Socket("localhost", 8080)

// Correct — check connectivity first
fun isServerAvailable(host: String, port: Int, timeout: Int = 3000): Boolean {
    return try {
        Socket().use { socket ->
            socket.connect(InetSocketAddress(host, port), timeout)
            true
        }
    } catch (e: Exception) {
        false
    }
}

if (isServerAvailable("localhost", 8080)) {
    val socket = Socket("localhost", 8080)
} else {
    println("Server not available")
}
```

### Fix 2: Add retry logic with backoff

```kotlin
// Wrong — single attempt
val socket = Socket("localhost", 8080)

// Correct — retry with exponential backoff
suspend fun connectWithRetry(host: String, port: Int, maxRetries: Int = 5): Socket {
    var delay = 1000L
    repeat(maxRetries) { attempt ->
        try {
            return Socket(host, port)
        } catch (e: ConnectException) {
            println("Connection attempt ${attempt + 1} failed, retrying in ${delay}ms...")
            delay(delay)
            delay = (delay * 2).coerceAtMost(30_000)
        }
    }
    throw ConnectException("Failed to connect after $maxRetries attempts")
}
```

### Fix 3: Use proper timeout settings

```kotlin
// Wrong — no timeout, hangs forever
val socket = Socket("localhost", 8080)

// Correct — set connection timeout
val socket = Socket()
socket.connect(InetSocketAddress("localhost", 8080), 5000)  // 5 second timeout
```

### Fix 4: Use higher-level HTTP clients

```kotlin
// Wrong — raw socket connection
val socket = Socket("localhost", 8080)

// Correct — HTTP client with built-in retry and timeout
val client = HttpClient {
    install(HttpTimeout) {
        requestTimeoutMillis = 5000
        connectTimeoutMillis = 3000
    }
}
```

## Examples

```kotlin
import java.net.*

fun main() {
    val host = "localhost"
    val port = 8080

    try {
        val socket = Socket(host, port)
        println("Connected to $host:$port")
        socket.close()
    } catch (e: ConnectException) {
        println("Connection refused: ${e.message}")
        println("Make sure the server is running on $host:$port")
    }
}
```

## Related Errors

- [SocketTimeoutException]({{< relref "/languages/kotlin/socket-timeout" >}}) — connection timed out.
- [IOException]({{< relref "/languages/kotlin/io-exception" >}}) — general I/O error.
- [UnknownHostException]({{< relref "/languages/kotlin/runtime-exception" >}}) — DNS resolution failed.
