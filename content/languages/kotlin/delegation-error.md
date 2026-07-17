---
title: "[Solution] Kotlin Delegation Error Fix"
description: "Fix Kotlin delegation errors. Learn why delegation fails and how to use by keyword properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["delegation", "by", "interface", "kotlin"]
weight: 5
---

## What This Error Means

A delegation error occurs when the by keyword delegation fails. Delegation allows a class to implement an interface by forwarding calls to another object, but can fail due to missing implementation or wrong interface.

## Common Causes

- Delegated class does not implement interface
- Missing method forwarding
- Property delegation issues
- Circular delegation

## How to Fix

```kotlin
// WRONG: Delegated class does not implement interface
interface Logger {
    fun log(message: String)
}

class ConsoleLogger : Logger {
    override fun log(message: String) = println(message)
}

class App(logger: Logger) : Logger by logger
// App delegates Logger to ConsoleLogger

// CORRECT: Ensure delegate implements interface
class App(private val logger: Logger) : Logger by logger {
    // All Logger methods delegated to logger
}
```

```kotlin
// WRONG: Property delegation with wrong type
val count: String by lazy { 0 }  // Type mismatch

// CORRECT: Match types
val count: Int by lazy { 0 }
```

## Examples

```kotlin
// Example 1: Interface delegation
interface Printer {
    fun print(message: String)
}

class ConsolePrinter : Printer {
    override fun print(message: String) = println(message)
}

class App(printer: Printer) : Printer by printer

// Example 2: Lazy delegation
val expensiveValue: String by lazy {
    computeExpensiveValue()
}

// Example 3: Observable delegation
var name: String by Delegates.observable("initial") { _, old, new ->
    println("$old -> $new")
}
```

## Related Errors

- [ClassCastException](classcastexception-kotlin) — type cast failed
- [IllegalArgumentException](illegalargumentexception) — invalid argument
- [IllegalStateException](illegalstateexception-kotlin) — invalid state
