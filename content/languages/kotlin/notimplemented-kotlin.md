---
title: "[Solution] Kotlin NotImplementedError — Not Implemented Fix"
description: "Fix Kotlin NotImplementedError when calling unimplemented functions. Learn how to handle abstract methods and placeholder implementations."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["notimplementederror", "abstract", "interface", "placeholder", "kotlin"]
weight: 5
---

# NotImplementedError — Not Implemented

A `NotImplementedError` is thrown when you call a function that hasn't been implemented yet.

## Description

Kotlin uses `TODO()` and `throw NotImplementedError()` to mark unimplemented code. These are placeholders that crash at runtime if called before implementation.

Common causes:

- **Abstract method called** — invoking abstract method directly
- **`TODO()` called** — placeholder not yet replaced
- **Interface default not implemented** — missing required implementation
- **Stub function** — temporary placeholder left in code

## Common Causes

```kotlin
// Cause 1: TODO() called
fun processData(data: Any) {
    TODO("Not yet implemented")
}

// Cause 2: NotImplementedError thrown
interface Repository {
    fun getAll(): List<Any>
}

class StubRepository : Repository {
    override fun getAll(): List<Any> {
        throw NotImplementedError()
    }
}

// Cause 3: Abstract method
abstract class Shape {
    abstract fun area(): Double
}

class Circle : Shape() {
    override fun area(): Double {
        TODO("Calculate circle area")
    }
}

// Cause 4: Default interface method
interface Plugin {
    fun execute(): String
}

class MyPlugin : Plugin {
    override fun execute(): String {
        TODO("Implement plugin")
    }
}
```

## How to Fix

### Fix 1: Implement the function

```kotlin
// Wrong
fun processData(data: Any) {
    TODO("Not yet implemented")
}

// Correct
fun processData(data: Any) {
    // Actual implementation
    println("Processing: $data")
}
```

### Fix 2: Provide default implementation

```kotlin
// Wrong
interface Repository {
    fun getAll(): List<Any>
}

// Correct
interface Repository {
    fun getAll(): List<Any> = emptyList()
}
```

### Fix 3: Use sealed classes with exhaustive when

```kotlin
// Wrong
sealed class Result {
    class Success : Result()
    class Error : Result()
}

fun handle(result: Result) {
    when (result) {
        is Result.Success -> TODO()
        is Result.Error -> TODO()
    }
}

// Correct
fun handle(result: Result) {
    when (result) {
        is Result.Success -> println("Success")
        is Result.Error -> println("Error")
    }
}
```

### Fix 4: Use check for required state

```kotlin
// Wrong
class Cache {
    var data: Map<String, Any>? = null
    fun get(key: String): Any {
        return data!![key]!!  // May throw if data is null
    }
}

// Correct
class Cache {
    var data: Map<String, Any> = emptyMap()
    fun get(key: String): Any? {
        return data[key]
    }
}
```

## Examples

```kotlin
// Example 1: Proper abstract implementation
abstract class Animal {
    abstract fun makeSound(): String
}

class Dog : Animal() {
    override fun makeSound() = "Woof!"
}

class Cat : Animal() {
    override fun makeSound() = "Meow!"
}

// Example 2: Interface with default
interface Logger {
    fun log(message: String) {
        println("[LOG] $message")
    }
}
```

## Related Errors

- [UnsupportedOperationException]({{< relref "/languages/kotlin/unsupported-operation" >}}) — operation not supported
- [ClassCastException]({{< relref "/languages/kotlin/typecast-kotlin" >}}) — wrong type cast
- [AbstractMethodError]({{< relref "/languages/kotlin/invocation-target" >}}) — abstract method called
