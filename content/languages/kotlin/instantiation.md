---
title: "[Solution] Kotlin InstantiationException — Object Creation Fix"
description: "Fix Kotlin InstantiationException when unable to instantiate a class. Check for abstract classes, interfaces, and missing constructors."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# InstantiationException — Object Creation Fix

An `InstantiationException` is thrown when a program tries to create an instance of an abstract class, interface, or a class without a no-arg constructor using `Class.newInstance()` or `Constructor.newInstance()`.

## Description

Some classes cannot be instantiated directly:
- **Abstract classes** — must be subclassed first.
- **Interfaces** — must be implemented.
- **Classes without no-arg constructor** — require specific arguments.
- **Kotlin data classes** — require constructor parameters.

Common scenarios:

- **Abstract class via reflection** — `AbstractClass::class.java.newInstance()`.
- **Interface via reflection** — `MyInterface::class.java.newInstance()`.
- **Missing no-arg constructor** — class only has parameterized constructors.
- **Framework instantiation** — DI frameworks may fail to create instances.

## Common Causes

```kotlin
// Cause 1: Abstract class
abstract class Shape {
    abstract fun area(): Double
}
val shape = Shape::class.java.getDeclaredConstructor().newInstance()
// InstantiationException: cannot instantiate abstract class

// Cause 2: Interface
interface Repository {
    fun find(id: String): Any?
}
val repo = Repository::class.java.getDeclaredConstructor().newInstance()
// InstantiationException: cannot instantiate interface

// Cause 3: No no-arg constructor
class User(val name: String, val age: Int)
val user = User::class.java.getDeclaredConstructor().newInstance()
// InstantiationException: no no-arg constructor

// Cause 4: Kotlin object declaration (singleton)
object AppConfig {
    val version = "1.0"
}
// Cannot instantiate: AppConfig::class.java.getDeclaredConstructor().newInstance()
```

## Solutions

### Fix 1: Use concrete implementations

```kotlin
// Wrong — cannot instantiate abstract class
abstract class Shape { abstract fun area(): Double }
val shape = Shape::class.java.newInstance()

// Correct — instantiate concrete subclass
class Circle(val radius: Double) : Shape() {
    override fun area() = Math.PI * radius * radius
}
val circle = Circle(5.0)
```

### Fix 2: Provide no-arg constructor if needed for reflection

```kotlin
// Wrong — no default constructor
class User(val name: String, val age: Int)

// Correct — add default constructor with default values
class User(val name: String = "", val age: Int = 0)

// Or use a secondary constructor
class User(val name: String, val age: Int) {
    constructor() : this("", 0)
}
```

### Fix 3: Use factory functions or companion objects

```kotlin
// Wrong — trying to instantiate interface
interface Repository<T> {
    fun find(id: String): T?
}

// Correct — use factory
class InMemoryRepository<T> : Repository<T> {
    override fun find(id: String): T? = null
}

fun <T> createRepository(): Repository<T> = InMemoryRepository()
```

### Fix 4: Use Kotlin class references directly

```kotlin
// Wrong — reflection-based instantiation
val instance = MyClass::class.java.getDeclaredConstructor().newInstance()

// Correct — direct instantiation
val instance = MyClass()

// Or for DI frameworks, use KClass
val kclass = MyClass::class
```

## Examples

```kotlin
abstract class Logger {
    abstract fun log(message: String)
}

class ConsoleLogger : Logger() {
    override fun log(message: String) = println("[LOG] $message")
}

fun main() {
    // Cannot do: Logger::class.java.newInstance()

    // Correct
    val logger: Logger = ConsoleLogger()
    logger.log("Application started")
}
```

## Related Errors

- [ClassNotFoundException]({{< relref "/languages/kotlin/class-not-found" >}}) — class not found in classpath.
- [NoSuchMethodException]({{< relref "/languages/kotlin/no-such-method" >}}) — constructor not found.
- [IllegalAccessException]({{< relref "/languages/kotlin/illegal-access" >}}) — cannot access constructor.
