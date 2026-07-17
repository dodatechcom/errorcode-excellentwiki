---
title: "[Solution] Kotlin IllegalStateException Fix"
description: "Fix Kotlin IllegalStateException when object state is invalid. Learn why state checks fail and how to manage object state."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["illegalstateexception", "state", "check", "kotlin"]
weight: 5
---

## What This Error Means

An IllegalStateException is thrown when a method is invoked at an illegal or inappropriate time, meaning the object is in an invalid state for the requested operation.

## Common Causes

- Calling method before initialization
- Using closed resource
- State machine in wrong state
- Missing required setup

## How to Fix

```kotlin
// WRONG: Using before initialization
class Connection {
    private var socket: Socket? = null
    fun send(data: String) {
        socket!!.write(data)  // IllegalStateException if not connected
    }
}

// CORRECT: Check state before use
class Connection {
    private var socket: Socket? = null
    fun send(data: String) {
        checkNotNull(socket) { "Not connected" }
        socket!!.write(data)
    }
}
```

```kotlin
// WRONG: Using closed resource
val stream = ByteArrayOutputStream()
stream.close()
stream.write(1)  // IllegalStateException

// CORRECT: Check if open
if (!stream.isOpen) {
    // Reopen or handle
}
```

```kotlin
// WRONG: Missing setup
class Builder {
    private var name: String? = null
    fun build(): Product {
        return Product(name!!)  // IllegalStateException if name not set
    }
}

// CORRECT: Use require
class Builder {
    private var name: String? = null
    fun build(): Product {
        requireNotNull(name) { "Name must be set" }
        return Product(name!!)
    }
}
```

## Examples

```kotlin
// Example 1: check function
fun processOrder(order: Order?) {
    check(order != null) { "Order must not be null" }
    // order is smart-cast to Order
}

// Example 2: State machine
class StateMachine {
    var state: State = State.Idle
        private set

    fun start() {
        check(state == State.Idle) { "Can only start from Idle" }
        state = State.Running
    }

    fun stop() {
        check(state == State.Running) { "Can only stop from Running" }
        state = State.Idle
    }
}

// Example 3: Lifecycle
class Lifecycle {
    private var initialized = false

    fun init() {
        initialized = true
    }

    fun doWork() {
        check(initialized) { "Call init() first" }
    }
}
```

## Related Errors

- [IllegalArgumentException](illegalargumentexception) — invalid argument
- [UnsupportedOperationException](unsupportedoperationexception) — operation not supported
- [UninitializedPropertyAccessException](uninitializedproperty) — lateinit not initialized
