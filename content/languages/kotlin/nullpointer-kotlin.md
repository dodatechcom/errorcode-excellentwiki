---
title: "[Solution] Kotlin NullPointerException — Null Safety Fix"
description: "Fix Kotlin NullPointerException with null safety. Learn how to use safe calls, let blocks, and the Elvis operator to handle nullable types."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nullpointerexception", "null-safety", "nullable", "kotlin"]
weight: 5
---

# NullPointerException — Null Safety Fix

A `NullPointerException` occurs when you attempt to dereference a null reference, bypassing Kotlin's null safety system.

## Description

Kotlin's type system distinguishes between nullable and non-nullable types at compile time. However, NPEs can still occur when using the `!!` operator, Java interop, or uninitialized `lateinit` variables.

Common causes:

- **Force unwrap with `!!`** — explicitly allowing null dereference
- **Java interop** — receiving null from Java into non-nullable type
- **Uninitialized `lateinit`** — accessing before assignment
- **Platform types** — null from external sources

## Common Causes

```kotlin
// Cause 1: Force unwrap with !!
val name: String? = null
println(name!!.length)  // NullPointerException

// Cause 2: Java interop returning null
val javaList: JavaList<String> = getJavaList()
val first: String = javaList.get(0)  // NPE if list is null

// Cause 3: Uninitialized lateinit
class User {
    lateinit var name: String
    fun greet() = println("Hello, $name")
}
val user = User()
user.greet()  // UninitializedPropertyAccessException

// Cause 4: Unsafe cast
val data: Any? = null
val str: String = data as String  // ClassCastException/NPE
```

## How to Fix

### Fix 1: Use safe call operator `?.`

```kotlin
// Wrong
val name: String? = null
println(name!!.length)  // NPE

// Correct
println(name?.length)  // null, no exception
```

### Fix 2: Use Elvis operator `?:`

```kotlin
// Wrong
val name: String? = null
val length = name!!.length  // NPE

// Correct
val length = name?.length ?: 0  // 0
```

### Fix 3: Use `let` blocks

```kotlin
// Wrong
val name: String? = getName()
println(name!!.uppercase())  // NPE

// Correct
name?.let {
    println(it.uppercase())
} ?: println("Name is null")
```

### Fix 4: Check `lateinit` before use

```kotlin
// Wrong
class User {
    lateinit var name: String
    fun greet() = println("Hello, $name")
}

// Correct
class User {
    lateinit var name: String
    fun greet() {
        if (::name.isInitialized) {
            println("Hello, $name")
        } else {
            println("Name not set")
        }
    }
}
```

## Examples

```kotlin
// Example 1: Safe null handling
fun processUser(user: User?) {
    user?.let {
        println(it.name)
        it.address?.let { addr ->
            println(addr.city)
        }
    } ?: println("User is null")
}

// Example 2: Default values
val config = mapOf("host" to "localhost")
val port = config["port"]?.toIntOrNull() ?: 8080
```

## Related Errors

- [ClassCastException]({{< relref "/languages/kotlin/class-cast" >}}) — wrong type cast at runtime
- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — invalid argument passed
- [IndexOutOfBoundsException]({{< relref "/languages/kotlin/index-out-of-bounds" >}}) — index beyond collection size
