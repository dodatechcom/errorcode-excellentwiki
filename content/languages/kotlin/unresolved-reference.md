---
title: "[Solution] Kotlin Unresolved Reference — Name Not Found Fix"
description: "Fix Kotlin unresolved reference errors. Check imports, spelling, visibility, and ensure the referenced symbol exists."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["unresolved-reference", "import", "symbol", "compile", "name"]
weight: 5
---

# Unresolved Reference — Name Not Found Fix

An unresolved reference error occurs at compile time when Kotlin cannot find the referenced variable, function, class, or property. This is one of the most common compile errors in Kotlin.

## Description

Kotlin must be able to resolve every name you use to a declared symbol. If the name doesn't exist, isn't imported, or isn't visible, the compiler reports an unresolved reference error.

Common scenarios:

- **Typo in name** — misspelled variable or function name.
- **Missing import** — using a class without importing it.
- **Wrong visibility** — accessing private member from outside.
- **Extension function not in scope** — calling extension without import.
- **Wrong package** — class in different package without import.

## Common Causes

```kotlin
// Cause 1: Typo
val result = procesData("hello")  // Unresolved reference: procesData (typo)

// Cause 2: Missing import
val date = LocalDate.now()  // Unresolved reference: LocalDate (not imported)

// Cause 3: Wrong visibility
class Secret {
    private fun hidden() {}
}
Secret().hidden()  // Unresolved reference: hidden (private)

// Cause 4: Extension function not imported
// In file utils.kt:
fun String.isPalindrome(): Boolean = this == this.reversed()

// In main.kt:
"hello".isPalindrome()  // Unresolved reference if not imported
```

## Solutions

### Fix 1: Check spelling

```kotlin
// Wrong
val result = procesData("hello")

// Correct
val result = processData("hello")
```

### Fix 2: Add missing imports

```kotlin
// Wrong
val date = LocalDate.now()

// Correct
import java.time.LocalDate
val date = LocalDate.now()

// Or use wildcard import
import java.time.*
```

### Fix 3: Make members accessible

```kotlin
// Wrong — private member
class Secret {
    private fun hidden() {}
}

// Correct — change visibility
class Secret {
    fun hidden() {}  // public
}

// Or use internal for module-level access
class Secret {
    internal fun hidden() {}  // accessible within module
}
```

### Fix 4: Import extension functions

```kotlin
// In utils.kt
package com.example.utils
fun String.isPalindrome(): Boolean = this == this.reversed()

// In main.kt
import com.example.utils.isPalindrome
fun main() {
    println("racecar".isPalindrome())  // Works
}
```

## Examples

```kotlin
// Common unresolved reference fixes

// 1. Check if class exists in current scope
// val x = MyClass  // Is MyClass declared or imported?

// 2. Check package
// val x = com.example.MyClass  // Full qualified name

// 3. Check visibility
// Is the member public, internal, or private?

// 4. Check if extension function needs import
// import com.example.utils.myExtension
```

## Related Errors

- [Type mismatch]({{< relref "/languages/kotlin/type-mismatch" >}}) — type incompatibility.
- [ClassNotFoundException]({{< relref "/languages/kotlin/class-not-found" >}}) — class not found at runtime.
- [NoSuchMethodException]({{< relref "/languages/kotlin/no-such-method" >}}) — method not found.
