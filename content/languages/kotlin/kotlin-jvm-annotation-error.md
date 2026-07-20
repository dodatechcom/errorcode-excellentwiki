---
title: "[Solution] Kotlin @JvmStatic/@JvmOverloads/@JvmName Misconfiguration"
description: "Fix Kotlin JVM annotation misconfiguration. Learn correct @JvmStatic, @JvmOverloads, @JvmName usage for Java interop."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1028
---

## Common Causes

- @JvmStatic in interface (not allowed until Kotlin 1.6 with limitations)
- @JvmOverloads on function with no default parameters
- @JvmName causing method signature clashes
- Missing @JvmStatic causing `ClassName.Companion.method()` from Java

```kotlin
// WRONG: @JvmOverloads with no defaults
@JvmOverloads
fun process(input: String) { }  // No defaults to generate

// WRONG: @JvmName clash
@JvmName("processInt")
fun process(input: Int) { }

@JvmName("processInt")  // Duplicate JVM name
fun processValue(input: Int) { }
```

## How to Fix

**1. Use @JvmStatic correctly in companion objects**

```kotlin
class MyClass {
    companion object {
        @JvmStatic
        fun create(): MyClass = MyClass()
        // Java: MyClass.create() — no .Companion needed
    }
}
```

**2. Use @JvmOverloads with default parameters**

```kotlin
@JvmOverloads
fun createUser(
    name: String,
    age: Int = 0,
    email: String? = null
) { }
// Generates: createUser(name, age, email), createUser(name, age), createUser(name)
```

**3. Use @JvmName for unique method names**

```kotlin
@file:JvmName("StringUtils")

fun String.isEmail(): Boolean = contains("@")
fun String.isPhone(): Boolean = matches(Regex("\\d{10}"))
// Java: StringUtils.isEmail(str)
```

**4. Use @JvmField for direct field access**

```kotlin
data class Point(@JvmField val x: Int, @JvmField val y: Int)
// Java: point.x instead of point.getX()
```

## Examples

```kotlin
// Example 1: @JvmOverloads with constructors
class Settings @JvmOverloads constructor(
    val width: Int = 100,
    val height: Int = 100,
    val title: String = "Default"
)

// Java: new Settings(), new Settings(200), new Settings(200, 300, "Custom")

// Example 2: @JvmSynthetic to hide from Java
@JvmSynthetic
fun internalApi() { }  // Not visible from Java

// Example 3: @JvmField in sealed class
sealed class Result {
    @JvmField val timestamp = System.currentTimeMillis()
    class Success(val data: String) : Result()
    class Error(val message: String) : Result()
}
```

## Related Errors

- [Inline class error](inline-class-error) — value class issue
- [Inline function error](kotlin-inline-function-error) — inline issues
- [Typealias error](typealias-error) — typealias issue
