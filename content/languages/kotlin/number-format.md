---
title: "[Solution] Kotlin NumberFormatException — String to Number Fix"
description: "Fix Kotlin NumberFormatException when parsing strings to numbers. Validate input, use toIntOrNull, and handle non-numeric characters."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["numberformatexception", "parse", "int", "double", "string"]
weight: 5
---

# NumberFormatException — String to Number Fix

A `NumberFormatException` is thrown when attempting to convert a string to a number and the string does not contain a parsable number.

## Description

This is a subclass of `IllegalArgumentException`. It occurs when `toInt()`, `toLong()`, `toDouble()`, or similar parsing functions receive a string that cannot be parsed as a number.

Common scenarios:

- **Non-numeric characters in string** — `"abc".toInt()`.
- **Empty or blank string** — `"".toInt()`.
- **Overflow** — number too large for the target type.
- **Decimal in integer parser** — `"3.14".toInt()`.

## Common Causes

```kotlin
// Cause 1: Non-numeric string
val num = "abc".toInt()  // NumberFormatException

// Cause 2: Empty string
val num = "".toInt()  // NumberFormatException

// Cause 3: Decimal in integer parser
val num = "3.14".toInt()  // NumberFormatException

// Cause 4: Number too large
val num = "99999999999999999999".toLong()  // NumberFormatException

// Cause 5: Whitespace in string
val num = "  42  ".toInt()  // NumberFormatException (spaces not trimmed)
```

## Solutions

### Fix 1: Use `toIntOrNull` for safe parsing

```kotlin
// Wrong
val num = "abc".toInt()  // NumberFormatException

// Correct
val num = "abc".toIntOrNull()  // Returns null
val num = "42".toIntOrNull()   // Returns 42
```

### Fix 2: Trim and validate before parsing

```kotlin
// Wrong
val input = getUserInput()
val num = input.toInt()  // May throw

// Correct
val input = getUserInput()
val num = input.trim().toIntOrNull()
if (num != null) {
    // Use num
} else {
    println("Invalid number: $input")
}
```

### Fix 3: Use default values with Elvis operator

```kotlin
// Wrong
val config = mapOf("port" to "8080")
val port = config["port"]!!.toInt()  // NumberFormatException if not a number

// Correct
val port = config["port"]?.toIntOrNull() ?: 3000
```

### Fix 4: Parse decimals properly

```kotlin
// Wrong
val pi = "3.14".toInt()  // NumberFormatException

// Correct
val pi = "3.14".toDouble()  // 3.14
val piInt = "3.14".toIntOrNull()  // null (can't parse decimal as Int)
val piRounded = "3.14".toDoubleOrNull()?.toInt()  // 3
```

## Examples

```kotlin
fun main() {
    val inputs = listOf("42", "abc", "3.14", "", "  10  ", "99999999999999999999")

    for (input in inputs) {
        val result = input.trim().toIntOrNull()
        println("'$input' -> $result")
    }
    // '42' -> 42
    // 'abc' -> null
    // '3.14' -> null
    // '' -> null
    // '  10  ' -> null (spaces cause failure)
    // '99999999999999999999' -> null
}
```

## Related Errors

- [IllegalArgumentException]({{< relref "/languages/kotlin/illegal-argument" >}}) — parent class of NumberFormatException.
- [ArithmeticException]({{< relref "/languages/kotlin/runtime-exception" >}}) — division by zero or overflow during arithmetic.
- [ClassCastException]({{< relref "/languages/kotlin/class-cast" >}}) — wrong type cast at runtime.
