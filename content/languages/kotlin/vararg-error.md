---
title: "[Solution] Kotlin Vararg Parameter Error Fix"
description: "Fix Kotlin vararg parameter errors. Learn why vararg arguments fail and how to spread arrays properly."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A vararg parameter error occurs when passing arguments to a vararg function incorrectly. Vararg allows passing a variable number of arguments, but the spread operator must be used for arrays.

## Common Causes

- Wrong spread operator syntax
- Mixing vararg with other parameters
- Passing array without spread
- Named argument issues

## How to Fix

```kotlin
// WRONG: Passing array without spread
fun printAll(vararg items: String) {
    items.forEach { println(it) }
}
val array = arrayOf("a", "b", "c")
printAll(array)  // Error: expected vararg

// CORRECT: Use spread operator
printAll(*array)
```

```kotlin
// WRONG: Wrong spread operator
fun process(vararg numbers: Int) = numbers.sum()
val list = listOf(1, 2, 3)
process(list)  // Error

// CORRECT: Convert and spread
process(*list.toIntArray())
```

## Examples

```kotlin
// Example 1: Basic vararg
fun sum(vararg numbers: Int): Int {
    return numbers.sum()
}
sum(1, 2, 3)  // 6

// Example 2: Spread operator
val array = intArrayOf(1, 2, 3)
sum(*array)  // 6

// Example 3: Vararg with other params
fun log(tag: String, vararg messages: String) {
    messages.forEach { println("$tag: $it") }
}
log("APP", "Hello", "World")
```

## Related Errors

- [IllegalArgumentException](illegalargumentexception) — invalid argument
- [IndexOutOfBoundsException](indexoutofboundsexception) — index out of range
- [ClassCastException](classcastexception-kotlin) — type cast failed
