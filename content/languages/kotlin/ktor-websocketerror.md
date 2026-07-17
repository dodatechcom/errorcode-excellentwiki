---
title: "[Solution] Kotlin Ktor WebSocket Error Fix"
description: "Fix Ktor WebSocket errors. Learn why Ktor WebSocket connections fail and how to handle real-time communication."
languages: ["kotlin"]
severities: ["error"]
error-types: ["network-error"]
tags: ["ktor", "websocket", "real-time", "kotlin"]
weight: 5
---

## What This Error Means

A Ktor WebSocket error occurs when WebSocket connections fail. This can happen due to network issues, protocol mismatches, or server configuration problems.

## Common Causes

- Server not configured for WebSocket
- Wrong WebSocket URL (ws:// vs wss://)
- Connection timeout
- Missing WebSocket plugin

## How to Fix

```kotlin
// WRONG: Using HTTP instead of WebSocket
val client = HttpClient()
client.webSocket("https://api.example.com/ws")  // Wrong protocol

// CORRECT: Use webSocket with proper config
val client = HttpClient {
    install(WebSockets)
}
client.webSocket("wss://api.example.com/ws") {
    send("Hello")
    val message = receive()
}
```

```kotlin
// WRONG: Not handling WebSocket errors
client.webSocket("wss://api.example.com/ws") {
    send("Hello")
    // May throw on disconnect
}

// CORRECT: Handle WebSocket lifecycle
client.webSocket("wss://api.example.com/ws") {
    try {
        send("Hello")
        for (frame in incoming) {
            // Process frames
        }
    } catch (e: Exception) {
        println("WebSocket error: ${e.message}")
    } finally {
        println("WebSocket closed")
    }
}
```

## Examples

```kotlin
// Example 1: Basic WebSocket
val client = HttpClient { install(WebSockets) }

client.webSocket("wss://echo.websocket.org") {
    send("Hello")
    val response = receive() as? Frame.Text
    println(response?.readText())
}

// Example 2: WebSocket server
routing {
    webSocket("/ws") {
        send("Connected")
        for (frame in incoming) {
            if (frame is Frame.Text) {
                send("Echo: ${frame.readText()}")
            }
        }
    }
}

// Example 3: JSON over WebSocket
client.webSocket("wss://api.example.com/ws") {
    val json = Json { ignoreUnknownKeys = true }
    send(Frame.Text(json.encodeToString(message)))
}
```

## Related Errors

- [Ktor request error](ktor-requesterror) — HTTP request failed
- [Ktor routing error](ktor-routingerror) — routing failed
- [Ktor serialization error](ktor-serializationerror) — serialization failed
