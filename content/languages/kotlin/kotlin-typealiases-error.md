---
title: "[Solution] Kotlin Typealias Recursive Expansion and Import Conflict"
description: "Fix Kotlin typealias recursive expansion and import conflicts. Learn correct typealias usage and resolution rules."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1039
---

## What This Error Means

Typealias errors occur when a typealias creates a circular reference, conflicts with imports from different packages, or when the compiler cannot resolve the underlying type at compile time.

## Common Causes

- Circular typealias references (`typealias A = B` / `typealias B = A`)
- Two typealiases with same name from different packages
- Typealias for platform type causing null-safety issues
- Typealias in KMP not matching across all source sets

```kotlin
// Circular reference — compiler error
typealias NodeList = List<Node>
typealias Node = NodeList  // Recursive, unresolvable
```

## How to Fix

**1. Break circular typealias references**

```kotlin
// WRONG: Circular
typealias Tree = Node
typealias Node = Tree

// CORRECT: Use actual types
typealias Tree = List<Node>
data class Node(val value: String, val children: List<Node>)
```

**2. Use explicit imports to resolve conflicts**

```kotlin
import com.packageA.Result as ResultA
import com.packageB.Result as ResultB

// Use qualified names when needed
val a: ResultA = ResultA.success()
val b: ResultB = ResultB.ok()
```

**3. Verify typealias resolution in KMP source sets**

```kotlin
// commonMain
expect class PlatformResult

// jvmMain
actual typealias PlatformResult = java.io.File

// jsMain
actual typealias PlatformResult = File  // JS File
```

**4. Use fully qualified name when typealias is ambiguous**

```kotlin
package com.example

typealias MyList = List<String>

// If another MyList exists from import
val items: com.example.MyList = listOf("a", "b")
```

## Examples

```kotlin
// Example 1: Function type alias
typealias Predicate<T> = (T) -> Boolean
typealias ErrorHandler = (Exception) -> Unit

fun <T> filter(items: List<T>, predicate: Predicate<T>): List<T> {
    return items.filter(predicate)
}

// Example 2: Typealias for complex nested types
typealias Matrix<T> = List<List<T>>
typealias UserMap = Map<Long, Map<String, Any>>

// Example 3: Generic typealias
typealias Result<T> = Either<Error, T>

suspend fun <T> safeCall(block: suspend () -> T): Result<T> {
    return try {
        Either.Right(block())
    } catch (e: Exception) {
        Either.Left(Error(e.message ?: "Unknown error"))
    }
}
```

## Related Errors

- [Inline class error](inline-class-error) — value class issue
- [Expect/actual error](expect-actual-error) — expect/actual mismatch
- [Unresolved reference](unresolved-reference) — type not found
