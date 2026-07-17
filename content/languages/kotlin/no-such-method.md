---
title: "[Solution] Kotlin NoSuchMethodException — Method Not Found Fix"
description: "Fix Kotlin NoSuchMethodException when a method cannot be found via reflection. Verify method names, parameter types, and use compile-time calls."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# NoSuchMethodException — Method Not Found Fix

A `NoSuchMethodException` is thrown when a method cannot be found via reflection. This occurs when using `getMethod()` or `getDeclaredMethod()` with incorrect method names or parameter types.

## Description

Reflection-based method lookup requires the exact method name and parameter types. Kotlin compiles properties to getter/setter methods, and companion objects to static methods, which can differ from the source names.

Common scenarios:

- **Wrong method name** — typo or incorrect casing in reflection call.
- **Wrong parameter types** — Kotlin types compile to different JVM types.
- **Companion object methods** — accessed differently via reflection.
- **Extension functions** — compiled as static methods with different signatures.

## Common Causes

```kotlin
// Cause 1: Wrong method name
val method = MyClass::class.java.getMethod("doWork")  // Method is actually named "performWork"

// Cause 2: Wrong parameter types
val method = MyClass::class.java.getMethod("process", String::class.java)
// Actual signature: process(Int, String)

// Cause 3: Kotlin property vs Java getter
class User(val name: String)
val method = User::class.java.getMethod("getName")  // Works (Kotlin generates getName())
val method = User::class.java.getMethod("name")  // NoSuchMethodException

// Cause 4: Extension function compiled as static
fun MyClass.extension() {}
val method = MyClass::class.java.getMethod("extension")  // NoSuchMethodException
```

## Solutions

### Fix 1: Use compile-time method references

```kotlin
// Wrong — string-based reflection
val method = MyClass::class.java.getMethod("process", String::class.java)

// Correct — compile-time safe
val method = MyClass::process
method.call(instance, "data")
```

### Fix 2: Check JVM method signatures

```kotlin
// Kotlin properties compile to getter methods
class User(val name: String, var age: Int)
// JVM methods: getName(), getAge(), setAge(Int)

// Wrong
val method = User::class.java.getMethod("name")

// Correct
val method = User::class.java.getMethod("getName")
```

### Fix 3: List available methods for debugging

```kotlin
// Debug: list all methods
val methods = MyClass::class.java.methods
methods.forEach { println("${it.name}(${it.parameterTypes.joinToString()})") }
```

### Fix 4: Use KFunction for Kotlin-native reflection

```kotlin
import kotlin.reflect.full.memberFunctions

// Correct — use Kotlin reflection
val method = MyClass::class.memberFunctions.find { it.name == "process" }
method?.call(instance, "data")
```

## Examples

```kotlin
class Calculator {
    fun add(a: Int, b: Int): Int = a + b
    fun multiply(a: Int, b: Int): Int = a * b
}

fun main() {
    val calc = Calculator()

    // Wrong
    // val method = Calculator::class.java.getMethod("add", Int::class.java, Int::class.java)

    // Correct
    val method = Calculator::class.java.getMethod("add", Int::class.java, Int::class.java)
    val result = method.invoke(calc, 2, 3) as Int
    println(result)  // 5
}
```

## Related Errors

- [ClassNotFoundException]({{< relref "/languages/kotlin/class-not-found" >}}) — class not found in classpath.
- [NoSuchFieldException]({{< relref "/languages/kotlin/no-such-field" >}}) — field not found in class.
- [IllegalAccessException]({{< relref "/languages/kotlin/illegal-access" >}}) — cannot access private method.
