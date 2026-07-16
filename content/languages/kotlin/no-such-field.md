---
title: "[Solution] Kotlin NoSuchFieldException — Field Not Found Fix"
description: "Fix Kotlin NoSuchFieldException when accessing a field via reflection. Verify field names, use properties, and check visibility."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nosuchfieldexception", "reflection", "field", "property"]
weight: 5
---

# NoSuchFieldException — Field Not Found Fix

A `NoSuchFieldException` is thrown when a field cannot be found via reflection using `getField()` or `getDeclaredField()`. This occurs with incorrect field names or when accessing private fields without proper setup.

## Description

Kotlin properties compile to JVM fields with specific naming conventions. Backing fields may have different names than the source property, and synthetic fields exist for delegation and nullable types.

Common scenarios:

- **Wrong field name** — typos or incorrect JVM name.
- **Accessing private field** — requires `getDeclaredField()` and `setAccessible(true)`.
- **Synthetic backing fields** — `$delegate` fields for delegated properties.
- **Companion object fields** — accessed through the companion class.

## Common Causes

```kotlin
// Cause 1: Wrong field name
val field = MyClass::class.java.getDeclaredField("myField")  // Actual name: my_field

// Cause 2: Using getField for private field
class Secret {
    private val password: String = "hidden"
}
val field = Secret::class.java.getField("password")  // NoSuchFieldException (private)

// Cause 3: Backing field name mismatch
class User {
    val name: String = "Alice"  // Backing field is actually "name"
}
val field = User::class.java.getDeclaredField("_name")  // NoSuchFieldException

// Cause 4: Delegated property has different field name
class MyDelegate {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): String = "delegated"
}
class Host {
    val delegated: String by MyDelegate()
}
val field = Host::class.java.getDeclaredField("delegated")  // NoSuchFieldException
```

## Solutions

### Fix 1: Use Kotlin properties instead of field reflection

```kotlin
// Wrong — reflection-based field access
val field = MyClass::class.java.getDeclaredField("name")
field.isAccessible = true
val value = field.get(instance)

// Correct — use Kotlin property access
val value = instance.name
```

### Fix 2: Use getDeclaredField for private fields

```kotlin
// Wrong
val field = MyClass::class.java.getField("privateField")  // NoSuchFieldException

// Correct
val field = MyClass::class.java.getDeclaredField("privateField")
field.isAccessible = true
val value = field.get(instance)
```

### Fix 3: Use KProperty for Kotlin reflection

```kotlin
import kotlin.reflect.full.memberProperties

// Correct — Kotlin reflection
val property = MyClass::class.memberProperties.find { it.name == "name" }
property?.let {
    it.isAccessible = true
    val value = it.get(instance)
}
```

### Fix 4: List all declared fields for debugging

```kotlin
// Debug: list all fields
val fields = MyClass::class.java.declaredFields
fields.forEach { println("${it.name}: ${it.type}") }
```

## Examples

```kotlin
class Config(val host: String, private val secret: String) {
    val port: Int = 8080
}

fun main() {
    val config = Config("localhost", "key123")

    // Correct — use properties
    println(config.host)
    println(config.port)

    // If reflection is necessary
    val secretField = Config::class.java.getDeclaredField("secret")
    secretField.isAccessible = true
    println(secretField.get(config))  // key123
}
```

## Related Errors

- [ClassNotFoundException]({{< relref "/languages/kotlin/class-not-found" >}}) — class not found in classpath.
- [NoSuchMethodException]({{< relref "/languages/kotlin/no-such-method" >}}) — method not found in class.
- [IllegalAccessException]({{< relref "/languages/kotlin/illegal-access" >}}) — cannot access private member.
