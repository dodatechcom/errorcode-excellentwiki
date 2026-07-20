---
title: "[Solution] Kotlin Range Error — Overflow, Zero/Negative Step"
description: "Fix Kotlin range progression errors including overflow, zero step, and negative step in reverse progression."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1005
---

## Common Causes

- Step value of 0 in `IntRange.step()` (throws `IllegalArgumentException`)
- Negative step on ascending range (empty range, no error but logic bug)
- `Int.MAX_VALUE` overflow when incrementing past max
- Using `until` when you mean `downTo` or vice versa

```kotlin
val range = 1..10 step 0  // IllegalArgumentException: step must be positive
```

## How to Fix

**1. Validate step values**

```kotlin
fun safeStep(range: IntProgression, step: Int): IntProgression {
    require(step != 0) { "Step cannot be zero" }
    return range.step(step)
}
```

**2. Use long ranges to avoid overflow**

```kotlin
// WRONG: Int overflow
val range = Int.MAX_VALUE - 5..Int.MAX_VALUE + 5  // Silent overflow

// CORRECT: Use Long range
val range = (Int.MAX_VALUE - 5).toLong()..(Int.MAX_VALUE + 5).toLong()
```

**3. Use downTo for reverse progression**

```kotlin
// WRONG: Empty range
for (i in 10..1 step 1) { /* never executes */ }

// CORRECT: Use downTo
for (i in 10 downTo 1) { println(i) }
```

**4. Use coerceIn to bound values**

```kotlin
val safeIndex = rawIndex.coerceIn(0, list.lastIndex)
```

## Examples

```kotlin
// Example 1: Range with step
val evenNumbers = (2..20 step 2).toList()
// [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

// Example 2: Char range
val letters = 'a'..'f'
println(letters.toList())  // [a, b, c, d, e, f]

// Example 3: Using until for half-open range
for (i in 0 until 10) { print("$i ") }  // 0 to 9

// Example 4: Long range for large values
val bigRange = 1_000_000_000L..2_000_000_000L step 50_000_000L
```

## Related Errors

- [ArithmeticException](numberformatexception-kotlin) — arithmetic overflow
- [IllegalArgumentException](illegalargumentexception) — invalid argument
- [IndexOutOfBoundsException](indexoutofboundsexception) — index out of range
