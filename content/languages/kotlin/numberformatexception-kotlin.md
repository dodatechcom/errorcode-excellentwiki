---
title: "[Solution] Kotlin NumberFormatException Fix"
description: "Fix Kotlin NumberFormatException when parsing numbers. Learn why number parsing fails and how to handle invalid input."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["numberformatexception", "parsing", "number", "kotlin"]
weight: 5
---

## What This Error Means

A NumberFormatException is thrown when you try to parse a string that does not represent a valid number. This commonly happens with user input or external data.

## Common Causes

- Non-numeric string passed to toInt/toDouble
- Empty string parsing
- Number with locale-specific formatting
- Null value (Java platform type)

## How to Fix

```kotlin
// WRONG: Parsing non-numeric string
val num = "abc".toInt()  // NumberFormatException

// CORRECT: Use toIntOrNull
val num = "abc".toIntOrNull()  // null
```

```kotlin
// WRONG: Parsing empty string
val num = "".toInt()  // NumberFormatException

// CORRECT: Check for empty string
val num = if (str.isNotEmpty()) str.toIntOrNull() else null
```

```kotlin
// WRONG: Parsing decimal as Int
val num = "3.14".toInt()  // NumberFormatException

// CORRECT: Use toDouble
val num = "3.14".toDouble()  // 3.14
```

## Examples

```kotlin
// Example 1: Safe parsing
fun safeToInt(str: String): Int {
    return str.toIntOrNull() ?: 0
}

// Example 2: Parsing with default
val num = input.toIntOrNull() ?: -1

// Example 3: Regex validation before parsing
fun isValidNumber(str: String): Boolean {
    return str.matches(Regex("-?\\d+"))
}
```

## Related Errors

- [IllegalArgumentException](illegalargumentexception) — invalid argument
- [IndexOutOfBoundsException](indexoutofboundsexception) — index out of range
- [ClassCastException](classcastexception-kotlin) — type cast failed
