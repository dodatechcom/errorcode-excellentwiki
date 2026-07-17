---
title: "[Solution] Kotlin InvocationTargetException — Reflection Invocation Fix"
description: "Fix Kotlin InvocationTargetException when a reflected method throws an exception. Handle the underlying cause and validate inputs."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# InvocationTargetException — Reflection Invocation Fix

An `InvocationTargetException` is thrown when a method invoked via reflection throws an exception. The actual exception is wrapped as the `cause` of the `InvocationTargetException`.

## Description

When you call `Method.invoke()`, any exception thrown by the target method is wrapped in an `InvocationTargetException`. To find the real problem, you need to extract the `cause`. This is a checked exception in Java, commonly seen in Kotlin reflection and framework code.

Common scenarios:

- **Target method throws an exception** — the wrapped exception is the real issue.
- **Constructor throws an exception** — `Constructor.newInstance()` wraps the cause.
- **Framework method invocation** — Spring, Hibernate, etc. use reflection internally.
- **Null argument to non-null parameter** — NPE wrapped in InvocationTargetException.

## Common Causes

```kotlin
// Cause 1: Target method throws exception
class Service {
    fun process(data: String): Int {
        return data.toInt()  // May throw NumberFormatException
    }
}
val method = Service::class.java.getMethod("process", String::class.java)
method.invoke(service, "abc")  // InvocationTargetException wrapping NumberFormatException

// Cause 2: Constructor throws exception
class User(name: String) {
    init {
        require(name.isNotBlank()) { "Name cannot be blank" }
    }
}
val constructor = User::class.java.getConstructor(String::class.java)
constructor.newInstance("")  // InvocationTargetException wrapping IllegalArgumentException

// Cause 3: Null passed to non-null parameter
val method = Service::class.java.getMethod("process", String::class.java)
method.invoke(service, null)  // InvocationTargetException wrapping NPE

// Cause 4: Exception in target method
class Processor {
    fun run(): Unit = throw RuntimeException("Processing failed")
}
```

## Solutions

### Fix 1: Extract the cause from InvocationTargetException

```kotlin
// Wrong — treating InvocationTargetException as the real error
try {
    val method = MyClass::class.java.getMethod("process", String::class.java)
    method.invoke(obj, "data")
} catch (e: InvocationTargetException) {
    println(e.message)  // Doesn't show the real error
}

// Correct — extract the cause
try {
    val method = MyClass::class.java.getMethod("process", String::class.java)
    method.invoke(obj, "data")
} catch (e: InvocationTargetException) {
    val realException = e.cause
    println("Real error: ${realException?.message}")
}
```

### Fix 2: Use KFunction for Kotlin-native reflection

```kotlin
import kotlin.reflect.full.callSafely

// Correct — use Kotlin reflection with safe calls
val function = MyClass::class.memberFunctions.find { it.name == "process" }
val result = function?.callSafely(obj, "data")
when (result) {
    is Result.Success -> println("Result: ${result.value}")
    is Result.Failure -> println("Error: ${result.exception.message}")
}
```

### Fix 3: Handle exceptions in target method directly

```kotlin
// Wrong — exception propagates as InvocationTargetException
class Service {
    fun process(data: String): Int = data.toInt()
}

// Correct — handle in the method itself
class Service {
    fun process(data: String): Int {
        return data.toIntOrNull() ?: throw IllegalArgumentException("Invalid number: $data")
    }
}
```

### Fix 4: Use try-catch with cause chain

```kotlin
try {
    val method = MyClass::class.java.getMethod("process")
    method.invoke(obj)
} catch (e: InvocationTargetException) {
    when (val cause = e.cause) {
        is IllegalArgumentException -> handleInvalid(cause)
        is IOException -> handleIO(cause)
        else -> throw cause ?: e
    }
}
```

## Examples

```kotlin
class Calculator {
    fun divide(a: Int, b: Int): Int {
        if (b == 0) throw ArithmeticException("Division by zero")
        return a / b
    }
}

fun main() {
    val calc = Calculator()
    val method = Calculator::class.java.getMethod("divide", Int::class.java, Int::class.java)

    try {
        val result = method.invoke(calc, 10, 0)
        println(result)
    } catch (e: InvocationTargetException) {
        println("Wrapped: ${e.javaClass.simpleName}")
        println("Real cause: ${e.cause?.javaClass.simpleName}: ${e.cause?.message}")
        // Real cause: ArithmeticException: Division by zero
    }
}
```

## Related Errors

- [ClassNotFoundException]({{< relref "/languages/kotlin/class-not-found" >}}) — class not found in classpath.
- [NoSuchMethodException]({{< relref "/languages/kotlin/no-such-method" >}}) — method not found in class.
- [IllegalAccessException]({{< relref "/languages/kotlin/illegal-access" >}}) — cannot access the method.
