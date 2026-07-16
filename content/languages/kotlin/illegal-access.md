---
title: "[Solution] Kotlin IllegalAccessException — Access Modifier Fix"
description: "Fix Kotlin IllegalAccessException when trying to access private or restricted members. Use public APIs, setAccessible, or redesign the access pattern."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["illegalaccessexception", "reflection", "private", "access", "modifier"]
weight: 5
---

# IllegalAccessException — Access Modifier Fix

An `IllegalAccessException` is thrown when a reflection operation cannot access a field, method, or constructor due to visibility restrictions.

## Description

Java/Kotlin has access modifiers (`public`, `private`, `protected`, `internal`) that control visibility. When reflection tries to access a private member, the JVM throws `IllegalAccessException`. This is a checked exception in Java.

Common scenarios:

- **Accessing private field** — `getDeclaredField()` without `setAccessible(true)`.
- **Calling private method** — reflection bypassing access control.
- **Instantiating private constructor** — creating instances of utility classes.
- **Module system restrictions** — Java 9+ module access control.

## Common Causes

```kotlin
// Cause 1: Accessing private field
class Secret {
    private val password: String = "hidden"
}
val field = Secret::class.java.getDeclaredField("password")
field.get(instance)  // IllegalAccessException

// Cause 2: Calling private method
class Service {
    private fun internalProcess(): String = "result"
}
val method = Service::class.java.getDeclaredMethod("internalProcess")
method.invoke(instance)  // IllegalAccessException

// Cause 3: Accessing final field
class Constants {
    val value: String = "constant"
}
val field = Constants::class.java.getDeclaredField("value")
field.set(instance, "new")  // IllegalAccessException (final field)

// Cause 4: Accessing across module boundaries
// In module A:
class InternalClass { fun doWork() {} }
// In module B (different module):
// May throw IllegalAccessException
```

## Solutions

### Fix 1: Use setAccessible(true) for reflection

```kotlin
// Wrong
val field = MyClass::class.java.getDeclaredField("privateField")
field.get(instance)  // IllegalAccessException

// Correct
val field = MyClass::class.java.getDeclaredField("privateField")
field.isAccessible = true
val value = field.get(instance)  // Works
```

### Fix 2: Use public APIs instead of reflection

```kotlin
// Wrong — accessing private field via reflection
class User(private var _name: String) {
    // No public getter
}
val field = User::class.java.getDeclaredField("_name")
field.isAccessible = true
val name = field.get(user) as String

// Correct — add a public getter
class User(private var _name: String) {
    val name: String get() = _name
}
val name = user.name
```

### Fix 3: Use Kotlin reflection with visibility handling

```kotlin
import kotlin.reflect.full.memberProperties

// Correct — Kotlin reflection with isAccessible
val property = User::class.memberProperties.find { it.name == "name" }
property?.let {
    it.isAccessible = true
    val value = it.get(user)
}
```

### Fix 4: Redesign to avoid reflection

```kotlin
// Wrong — utility class with private constructor, accessed via reflection
class Utils private constructor() {
    companion object {
        fun create(): Utils = Utils()
    }
}

// Correct — use companion object or object declaration
object Utils {
    fun doWork() = "done"
}
```

## Examples

```kotlin
class Database {
    private val connectionString: String = "jdbc:localhost/db"

    private fun connect(): String = "Connected"
}

fun main() {
    val db = Database()

    // These work with setAccessible
    val field = Database::class.java.getDeclaredField("connectionString")
    field.isAccessible = true
    println(field.get(db))

    val method = Database::class.java.getDeclaredMethod("connect")
    method.isAccessible = true
    println(method.invoke(db))
}
```

## Related Errors

- [NoSuchFieldException]({{< relref "/languages/kotlin/no-such-field" >}}) — field not found in class.
- [NoSuchMethodException]({{< relref "/languages/kotlin/no-such-method" >}}) — method not found in class.
- [InvocationTargetException]({{< relref "/languages/kotlin/invocation-target" >}}) — exception thrown by reflected method.
