---
title: "[Solution] Kotlin Delegated Property Error — Delegate Fix"
description: "Fix Kotlin delegated property errors. Implement operator functions correctly, check delegate compatibility, and handle initialization."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["delegated-property", "delegate", "observable", "vetoable", "lazy"]
weight: 5
---

# Delegated Property Error — Delegate Fix

Delegated property errors occur when a property delegate doesn't implement the required operator functions (`getValue`, `setValue`) or when the delegate is used incorrectly.

## Description

Kotlin's delegated properties allow you to customize property behavior by delegating get/set operations to a separate class. The delegate must implement `operator fun getValue()` and optionally `operator fun setValue()`. Common built-in delegates include `lazy`, `observable`, and `vetoable`.

Common scenarios:

- **Missing getValue operator** — delegate doesn't implement `getValue`.
- **Read-only delegate on var** — using `by` with `val` delegate on `var`.
- **Lazy initialization failure** — exception in lazy initializer.
- **Vetoable rejection** — `vetoable` rejecting a value change.

## Common Causes

```kotlin
// Cause 1: Missing getValue
class MyDelegate {
    // Missing: operator fun getValue(thisRef: Any?, property: KProperty<*>): String
}
class Host {
    val prop: String by MyDelegate()  // Error: getValue() not found
}

// Cause 2: Wrong delegate type
class StringDelegate {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): Int = 42
}
class Host {
    val prop: String by StringDelegate()  // Type mismatch
}

// Cause 3: Lazy initialization exception
val value: String by lazy {
    throw RuntimeException("Init failed")  // Exception on first access
}

// Cause 4: Vetoable rejecting change
val count: Int by vetoable(0) { _, _, new ->
    new > 0  // Rejects negative values
}
```

## Solutions

### Fix 1: Implement required operator functions

```kotlin
// Wrong — missing getValue
class MyDelegate {
    // No getValue implemented
}

// Correct
class MyDelegate {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): String {
        return "delegated value"
    }
}

class Host {
    val prop: String by MyDelegate()
}
```

### Fix 2: Match delegate return type

```kotlin
// Wrong — type mismatch
class IntDelegate {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): String = "text"
}
class Host {
    val prop: Int by IntDelegate()  // IntDelegate returns String but prop is Int
}

// Correct
class IntDelegate {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): Int = 42
}
class Host {
    val prop: Int by IntDelegate()
}
```

### Fix 3: Handle lazy initialization errors

```kotlin
// Wrong — lazy throws on first access
val value: String by lazy {
    riskyOperation()  // May throw
}

// Correct — handle errors
val value: String by lazy {
    runCatching { riskyOperation() }.getOrDefault("default")
}
```

### Fix 4: Use built-in delegates correctly

```kotlin
// lazy — computes value on first access
val expensiveValue: String by lazy {
    println("Computing...")
    "computed"
}

// observable — notifies on change
var name: String by observable("initial") { _, old, new ->
    println("Name changed from $old to $new")
}

// vetoable — can reject changes
var age: Int by vetoable(0) { _, _, new ->
    new in 0..150  // Only allows 0-150
}
```

## Examples

```kotlin
import kotlin.reflect.KProperty

class LoggingDelegate<T>(private val default: T) {
    private var value: T = default

    operator fun getValue(thisRef: Any?, property: KProperty<*>): T {
        println("Getting ${property.name} = $value")
        return value
    }

    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: T) {
        println("Setting ${property.name} from ${this.value} to $value")
        this.value = value
    }
}

class User {
    var name: String by LoggingDelegate("unknown")
    var age: Int by LoggingDelegate(0)
}

fun main() {
    val user = User()
    user.name = "Alice"
    user.age = 30
    println("Name: ${user.name}, Age: ${user.age}")
}
```

## Related Errors

- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid delegate configuration.
- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — delegate in wrong state.
- [UnsupportedOperationException]({{< relref "/languages/kotlin/unsupported-operation" >}}) — delegate operation not supported.
