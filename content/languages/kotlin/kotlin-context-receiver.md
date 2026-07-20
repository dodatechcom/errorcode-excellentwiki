---
title: "[Solution] Kotlin Context Receiver Resolution Ambiguity"
description: "Fix Kotlin context receiver resolution ambiguity. Learn correct context receiver usage and disambiguation strategies."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1038
---

## What This Error Means

Context receivers (Kotlin 1.6.20+) provide implicit context to functions. Resolution ambiguity occurs when multiple context receivers define the same member name, or when context receiver order matters for resolution.

## Common Causes

- Two context receivers defining same-named function
- Context receiver type conflicts with explicit parameter
- Context receiver not resolved due to wrong import
- Conflicting extension functions on different context receivers

```kotlin
context(Logger, Transaction)
fun process() {
    log("hello")  // Ambiguous: Logger.log or Transaction.log?
}
```

## How to Fix

**1. Use explicit receiver qualification**

```kotlin
context(Logger, Transaction)
fun process() {
    this@Logger.log("hello")   // Explicit
    this@Transaction.log("hello")  // Explicit
}
```

**2. Rename conflicting functions**

```kotlin
// WRONG: Both have log()
interface Logger { fun log(message: String) }
interface Transaction { fun log(message: String) }

// CORRECT: Unique names
interface Logger { fun logMessage(message: String) }
interface Transaction { fun logTransaction(message: String) }
```

**3. Use context with unique types**

```kotlin
@JvmInline
value class LoggerContext(val name: String)

@JvmInline
value class TxContext(val id: String)

context(LoggerContext, TxContext)
fun process() {
    // No ambiguity — different types
}
```

**4. Order context receivers explicitly**

```kotlin
// First receiver has priority for same-name functions
context(A, B)  // A's functions are resolved first
fun compute() { ... }
```

## Examples

```kotlin
// Example 1: Context receiver for DSL scope
context(DurationFormatter)
fun Duration.format(): String {
    return formatDuration(this)  // Resolves from DurationFormatter
}

// Example 2: Multiple context receivers
interface AuthContext { val currentUser: User }
interface DbContext { suspend fun query(sql: String): ResultSet }

context(AuthContext, DbContext)
suspend fun getUserOrders(): List<Order> {
    val user = currentUser  // From AuthContext
    return query("SELECT * FROM orders WHERE user_id = ${user.id}")  // From DbContext
}

// Example 3: Context receiver with class
class Config(val debug: Boolean)

context(Config)
fun logDebug(message: String) {
    if (debug) println("[DEBUG] $message")
}

// Usage
with(Config(debug = true)) {
    logDebug("Starting application")
}
```

## Related Errors

- [Extension error](extension-error) — extension function issue
- [DSL builder error](kotlin-dsl-builder-error) — builder scope
- [Operator overload](kotlin-operator-overload) — operator issues
