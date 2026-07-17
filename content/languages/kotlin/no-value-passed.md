---
title: "[Solution] Kotlin No Value Passed for Parameter — Missing Argument Fix"
description: "Fix Kotlin no value passed for parameter errors. Provide all required arguments, use default values, and check function signatures."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

# No Value Passed for Parameter — Missing Argument Fix

A "No value passed for parameter" error occurs at compile time when you call a function without providing all required arguments. Kotlin requires all non-default parameters to be explicitly provided.

## Description

Kotlin functions can have required parameters (no default value) and optional parameters (with default values). If a parameter has no default value and you don't provide it, the compiler reports this error.

Common scenarios:

- **Forgot required parameter** — function requires 3 args, you passed 2.
- **Named arguments skipped** — using named args but missing required ones.
- **Constructor missing arguments** — data class constructor requires fields.
- **Java method with no defaults** — calling Java method that needs all args.

## Common Causes

```kotlin
// Cause 1: Missing required parameter
fun greet(name: String, greeting: String) {
    println("$greeting, $name!")
}
greet("Alice")  // No value passed for parameter 'greeting'

// Cause 2: Constructor missing fields
data class User(val name: String, val age: Int, val email: String)
val user = User("Alice", 30)  // No value passed for parameter 'email'

// Cause 3: Named arguments skipping required
fun configure(host: String, port: Int, debug: Boolean) {}
configure(port = 8080, debug = true)  // No value passed for 'host'

// Cause 4: Default values not used properly
fun process(data: String, retries: Int = 3, timeout: Long = 1000) {}
process(timeout = 5000)  // No value passed for 'data'
```

## Solutions

### Fix 1: Provide all required arguments

```kotlin
// Wrong
greet("Alice")

// Correct
greet("Alice", "Hello")

// Or use named arguments
greet(name = "Alice", greeting = "Hello")
```

### Fix 2: Add default values to parameters

```kotlin
// Wrong — all parameters required
fun greet(name: String, greeting: String) {
    println("$greeting, $name!")
}

// Correct — greeting has default
fun greet(name: String, greeting: String = "Hello") {
    println("$greeting, $name!")
}
greet("Alice")  // Works, uses default "Hello"
```

### Fix 3: Provide all constructor arguments

```kotlin
// Wrong
data class User(val name: String, val age: Int, val email: String)
val user = User("Alice", 30)

// Correct
val user = User("Alice", 30, "alice@example.com")

// Or use named arguments
val user = User(name = "Alice", age = 30, email = "alice@example.com")
```

### Fix 4: Use named arguments to clarify

```kotlin
// Wrong — positional arguments, easy to mix up
fun configure(host: String, port: Int, debug: Boolean) {}
configure("localhost", 8080, true)

// Correct — named arguments are clearer
configure(
    host = "localhost",
    port = 8080,
    debug = true
)
```

## Examples

```kotlin
data class ServerConfig(
    val host: String,
    val port: Int = 8080,
    val debug: Boolean = false,
    val maxConnections: Int = 100
)

fun main() {
    // All required args
    val config1 = ServerConfig(host = "localhost")

    // With optional args
    val config2 = ServerConfig(
        host = "production.example.com",
        port = 443,
        debug = true
    )

    // Error: No value passed for 'host'
    // val config3 = ServerConfig(port = 8080)
}
```

## Related Errors

- [Type mismatch]({{< relref "/languages/kotlin/type-mismatch" >}}) — wrong argument type.
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid argument value.
- [Unresolved reference]({{< relref "/languages/kotlin/unresolved-reference" >}}) — function not found.
