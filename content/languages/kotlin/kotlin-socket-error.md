---
title: "[Solution] Kotlin Socket Connect Timeout, Broken Pipe, Connection Reset"
description: "Fix Kotlin socket errors including connect timeout, broken pipe, and connection reset. Learn robust socket configuration patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1033
---

## What This Error Means

Socket errors in Kotlin occur during TCP connections due to network issues, timeout misconfiguration, or server-side connection drops. These typically manifest as `SocketTimeoutException`, `SocketException`, or `IOException`.

## Common Causes

- Connect timeout too short for high-latency networks
- Broken pipe when writing to a closed socket
- Connection reset by server (RST packet)
- Not setting `soTimeout` for read operations

```kotlin
// Timeout too short
val socket = Socket()
socket.connect(InetSocketAddress("server.com", 8080), 100)  // 100ms too short
```

## How to Fix

**1. Configure appropriate timeouts**

```kotlin
val socket = Socket()
socket.connect(
    InetSocketAddress("server.com", 8080),
    connectTimeout = 5000  // 5 seconds
)
socket.soTimeout = 10000  // 10 seconds read timeout
```

**2. Handle broken pipe with try-catch**

```kotlin
try {
    outputStream.write(data)
    outputStream.flush()
} catch (e: java.io.IOException) {
    if (e.message?.contains("Broken pipe") == true) {
        reconnect()
    }
}
```

**3. Use reconnect logic with exponential backoff**

```kotlin
suspend fun connectWithRetry(
    host: String,
    port: Int,
    maxRetries: Int = 3
): Socket {
    repeat(maxRetries) { attempt ->
        try {
            return Socket(host, port)
        } catch (e: IOException) {
            delay(1000L * (1 shl attempt))  // Exponential backoff
        }
    }
    throw IOException("Failed after $maxRetries attempts")
}
```

**4. Use keepAlive to detect dead connections**

```kotlin
val socket = Socket()
socket.keepAlive = true
socket.tcpNoDelay = true
```

## Examples

```kotlin
// Example 1: Full socket configuration
fun createConfiguredSocket(host: String, port: Int): Socket {
    val socket = Socket()
    socket.apply {
        tcpNoDelay = true
        keepAlive = true
        soTimeout = 30000
        sendBufferSize = 8192
        receiveBufferSize = 8192
    }
    socket.connect(InetSocketAddress(host, port), 10000)
    return socket
}

// Example 2: NIO channel for non-blocking I/O
val channel = SocketChannel.open()
channel.configureBlocking(true)
channel.connect(InetSocketAddress("server.com", 8080))

// Example 3: SSL socket with timeouts
val factory = javax.net.ssl.SSLSocketFactory.getDefault()
val sslSocket = factory.createSocket("server.com", 443) as javax.net.ssl.SSLSocket
sslSocket.soTimeout = 15000
sslSocket.startHandshake()
```

## Related Errors

- [Socket timeout](socket-timeout) — socket timeout
- [Connection refused](connection-refused) — connection refused
- [SSL handshake error](ssl-handshake) — SSL/TLS error
