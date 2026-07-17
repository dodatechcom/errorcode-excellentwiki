---
title: "[Solution] Kotlin IllegalArgumentException — Invalid Argument Fix"
description: "Fix Kotlin IllegalArgumentException when passing invalid arguments. Learn how to validate parameters and use require/check functions."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# IllegalArgumentException — Invalid Argument

An `IllegalArgumentException` occurs when a method receives an argument that doesn't meet its requirements.

## Description

Kotlin methods often validate their parameters using `require`, `check`, or manual validation. When arguments are invalid, they throw `IllegalArgumentException` with a descriptive message.

Common causes:

- **Invalid range** — number outside allowed range
- **Null argument** — passing null to non-nullable parameter
- **Invalid format** — string doesn't match expected pattern
- **Business rule violation** — argument violates domain constraints

## Common Causes

```kotlin
// Cause 1: Invalid range
fun setAge(age: Int) {
    require(age in 0..150) { "Invalid age: $age" }
}
setAge(-5)  // IllegalArgumentException

// Cause 2: Null argument
fun processName(name: String) {
    // name is non-nullable
}
processName(null)  // Compilation error, but possible via Java interop

// Cause 3: Invalid format
fun parseDate(date: String) {
    require(date.matches(Regex("\\d{4}-\\d{2}-\\d{2}"))) { "Invalid date format" }
}
parseDate("not-a-date")  // IllegalArgumentException

// Cause 4: Business rule violation
fun withdraw(amount: Double, balance: Double) {
    require(amount > 0) { "Amount must be positive" }
    require(amount <= balance) { "Insufficient funds" }
}
withdraw(100.0, 50.0)  // IllegalArgumentException
```

## How to Fix

### Fix 1: Use `require` for preconditions

```kotlin
// Wrong
fun setAge(age: Int) {
    // No validation
}

// Correct
fun setAge(age: Int) {
    require(age in 0..150) { "Age must be between 0 and 150" }
}
```

### Fix 2: Use `check` for state validation

```kotlin
// Wrong
fun process() {
    // Assumes state is valid
}

// Correct
fun process() {
    check(isInitialized) { "Object not initialized" }
}
```

### Fix 3: Use validation functions

```kotlin
// Wrong
fun createEmail(email: String) {
    // Assumes valid email
}

// Correct
fun createEmail(email: String) {
    require(email.contains("@")) { "Invalid email: $email" }
    require(email.contains(".")) { "Invalid email: $email" }
}
```

### Fix 4: Use sealed classes for results

```kotlin
// Wrong
fun divide(a: Int, b: Int): Int {
    require(b != 0) { "Division by zero" }
    return a / b
}

// Correct
sealed class Result<out T> {
    data class Success<T>(val value: T) : Result<T>()
    data class Error(val message: String) : Result<Nothing>()
}

fun divide(a: Int, b: Int): Result<Int> {
    return if (b != 0) {
        Result.Success(a / b)
    } else {
        Result.Error("Division by zero")
    }
}
```

## Examples

```kotlin
// Example 1: Complete validation
fun create_user(name: String, age: Int, email: String) {
    require(name.isNotBlank()) { "Name cannot be blank" }
    require(age in 0..150) { "Invalid age" }
    require(email.contains("@")) { "Invalid email" }
}

// Example 2: Builder pattern with validation
class UserBuilder {
    private var name: String? = null
    private var age: Int? = null
    
    fun name(name: String) = apply { this.name = name }
    fun age(age: Int) = apply { this.age = age }
    
    fun build(): User {
        val name = this.name ?: throw IllegalArgumentException("Name required")
        val age = this.age ?: throw IllegalArgumentException("Age required")
        require(age in 0..150) { "Invalid age" }
        return User(name, age)
    }
}
```

## Related Errors

- [NullPointerException]({{< relref "/languages/kotlin/nullpointer-kotlin" >}}) — null dereference
- [ClassCastException]({{< relref "/languages/kotlin/typecast-kotlin" >}}) — wrong type cast
- [IndexOutOfBoundsException]({{< relref "/languages/kotlin/index-out-of-bounds" >}}) — index beyond bounds
