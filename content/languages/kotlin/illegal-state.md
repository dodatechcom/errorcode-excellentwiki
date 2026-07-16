---
title: "[Solution] Kotlin IllegalStateException — Invalid Object State Fix"
description: "Fix Kotlin IllegalStateException when an object is not in the correct state for an operation. Use state checks, builders, and proper initialization."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["illegalsateexception", "state", "initialization", "check"]
weight: 5
---

# IllegalStateException — Invalid Object State Fix

An `IllegalStateException` is thrown when a method has been invoked on an object that is not in an appropriate state. Unlike `IllegalArgumentException` (bad input), this signals bad internal state.

## Description

This exception indicates the object's internal state doesn't support the requested operation. It's commonly thrown by frameworks, coroutines, and lifecycle-aware components when operations happen in the wrong order.

Common scenarios:

- **Accessing a resource before initialization** — reading from an unclosed stream.
- **Calling methods in wrong order** — starting before building, closing twice.
- **Coroutine scope already cancelled** — launching in a dead scope.
- **Fragment not attached to activity** — accessing context too early or too late.

## Common Causes

```kotlin
// Cause 1: Operating on uninitialized object
class Connection {
    private var socket: Socket? = null
    fun send(data: String) {
        if (socket == null) throw IllegalStateException("Connection not initialized")
        socket!!.send(data)
    }
}

// Cause 2: Starting an already-started component
class Server {
    private var running = false
    fun start() {
        if (running) throw IllegalStateException("Server already running")
        running = true
    }
}

// Cause 3: Accessing coroutine scope after cancellation
suspend fun fetchData(scope: CoroutineScope) {
    scope.cancel()
    launch(scope) { ... }  // IllegalStateException
}

// Cause 4: Using Fragment before/after lifecycle
class MyFragment : Fragment() {
    fun doWork() {
        val ctx = requireContext()  // IllegalStateException if not attached
    }
}
```

## Solutions

### Fix 1: Use `check` for state validation

```kotlin
// Wrong
fun process() {
    if (!initialized) throw IllegalStateException("Not initialized")
    // ...
}

// Correct
fun process() {
    check(initialized) { "Processor must be initialized before calling process()" }
    // ...
}
```

### Fix 2: Use sealed state machines

```kotlin
// Wrong — boolean flags are error-prone
class Player {
    private var isPlaying = false
    private var isPaused = false
    fun play() {
        if (isPlaying) throw IllegalStateException("Already playing")
        isPlaying = true
    }
}

// Correct — sealed class enforces valid states
sealed class PlayerState {
    object Idle : PlayerState()
    object Playing : PlayerState()
    object Paused : PlayerState()
}

class Player {
    private var state: PlayerState = PlayerState.Idle
    fun play() {
        state = when (state) {
            is PlayerState.Idle -> PlayerState.Playing
            is PlayerState.Paused -> PlayerState.Playing
            is PlayerState.Playing -> throw IllegalStateException("Already playing")
        }
    }
}
```

### Fix 3: Initialize lazily with safe defaults

```kotlin
// Wrong
class Service {
    private lateinit var database: Database
    fun query(sql: String): Result {
        return database.execute(sql)  // IllegalStateException if not initialized
    }
}

// Correct — use lazy initialization
class Service {
    private val database: Database by lazy { Database.connect() }
    fun query(sql: String): Result {
        return database.execute(sql)
    }
}
```

### Fix 4: Use builder pattern to ensure correct order

```kotlin
// Wrong — easy to forget steps
class HttpRequest {
    var url: String? = null
    var method: String? = null
    fun build(): HttpRequest {
        if (url == null) throw IllegalStateException("URL not set")
        return this
    }
}

// Correct — builder enforces required fields
class HttpRequest private constructor(val url: String, val method: String) {
    class Builder {
        private var url: String = ""
        private var method: String = "GET"
        fun url(url: String) = apply { this.url = url }
        fun method(method: String) = apply { this.method = method }
        fun build(): HttpRequest {
            require(url.isNotBlank()) { "URL is required" }
            return HttpRequest(url, method)
        }
    }
}
```

## Examples

```kotlin
fun main() {
    val connection = Connection()
    // connection.send("hello")  // IllegalStateException: not initialized

    connection.connect()
    connection.send("hello")  // Works after initialization
}
```

## Related Errors

- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid argument value, not object state.
- [UnsupportedOperationException]({{< relref "/languages/kotlin/unsupported-operation" >}}) — operation not supported by the object.
- [CancellationException]({{< relref "/languages/kotlin/cancellation-exception" >}}) — coroutine was cancelled.
