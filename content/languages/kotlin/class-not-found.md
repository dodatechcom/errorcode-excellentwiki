---
title: "[Solution] Kotlin ClassNotFoundException — Class Loading Fix"
description: "Fix Kotlin ClassNotFoundException when a class cannot be found at runtime. Check classpath, dependencies, and class names."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ClassNotFoundException — Class Loading Fix

A `ClassNotFoundException` is thrown when an application tries to load a class through its string name using `Class.forName()`, `ClassLoader.loadClass()`, or `ClassLoader.findSystemClass()`, but the class is not found in the classpath.

## Description

This is a checked exception in Java, commonly seen in Kotlin when using reflection, serialization frameworks, or dynamic class loading. The class name string may be wrong, or the JAR/dependency may be missing from the classpath.

Common scenarios:

- **Missing dependency** — library JAR not included in build.
- **Wrong class name string** — typo in reflection-based class loading.
- **ProGuard/R8 obfuscation** — class renamed during minification.
- **Classloader isolation** — class exists in different classloader.

## Common Causes

```kotlin
// Cause 1: Reflection with wrong class name
val clazz = Class.forName("com.example.MyClas")  // Typo, ClassNotFoundException

// Cause 2: Missing dependency
// If Gson is not in classpath:
val clazz = Class.forName("com.google.gson.Gson")  // ClassNotFoundException

// Cause 3: ProGuard obfuscation
// Class renamed to a.b.c during minification
val clazz = Class.forName("com.example.MyClass")  // ClassNotFoundException

// Cause 4: Wrong classloader
val clazz = Class.forName("com.example.MyClass", true, myClassLoader)
```

## Solutions

### Fix 1: Verify class name is correct

```kotlin
// Wrong
val clazz = Class.forName("com.example.MyServce")  // Typo

// Correct
val clazz = Class.forName("com.example.MyService")
```

### Fix 2: Check dependencies are included

```kotlin
// Ensure dependency is in build.gradle.kts
// dependencies {
//     implementation("com.google.code.gson:gson:2.10.1")
// }

// Then the class will be available
val gson = Gson()  // Works if Gson is in classpath
```

### Fix 3: Use KClass instead of string-based reflection

```kotlin
// Wrong — string-based, error-prone
val clazz = Class.forName("com.example.MyClass")

// Correct — compile-time safe
val clazz = MyClass::class.java
val kclazz = MyClass::class
```

### Fix 4: Keep classes from obfuscation

```kotlin
// In proguard-rules.pro:
// -keep class com.example.MyClass { *; }
// -keep class com.example.** { *; }

// Or use @Keep annotation (Android)
// @Keep
// class MyClass
```

## Examples

```kotlin
fun main() {
    // Safe class loading with error handling
    val className = "kotlin.String"
    try {
        val clazz = Class.forName(className)
        println("Found: ${clazz.name}")
    } catch (e: ClassNotFoundException) {
        println("Class not found: $className")
    }

    // Prefer KClass for known types
    val stringClass = String::class
    println("Kotlin class: $stringClass")
    println("Java class: ${stringClass.java}")
}
```

## Related Errors

- [NoSuchMethodException]({{< relref "/languages/kotlin/no-such-method" >}}) — method not found in class.
- [NoSuchFieldException]({{< relref "/languages/kotlin/no-such-field" >}}) — field not found in class.
- [InvocationTargetException]({{< relref "/languages/kotlin/invocation-target" >}}) — exception thrown by reflected method.
