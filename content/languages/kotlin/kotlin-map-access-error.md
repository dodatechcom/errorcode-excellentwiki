---
title: "[Solution] Kotlin Map Access Error — Null Key/Value and NoSuchElementException"
description: "Fix Kotlin map access errors including NoSuchElementException and null key/value issues. Learn safe map access patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1004
---

## Common Causes

- Using `map.getValue(key)` when key is absent (throws `NoSuchElementException`)
- Attempting to read from `emptyMap()` with non-null expectation
- Null key insertion then lookup with non-null type
- Key type mismatch after type erasure (e.g., mixed Int vs Long keys)

```kotlin
val map = mapOf("a" to 1, "b" to 2)
val value: Int = map.getValue("c")  // NoSuchElementException
```

## How to Fix

**1. Use safe access operators**

```kotlin
// WRONG: Unsafe access
val value = map["key"]!!

// CORRECT: Safe access with defaults
val value = map["key"] ?: defaultValue
```

**2. Use getOrElse or getOrDefault**

```kotlin
val value = map.getOrElse("missing") { 42 }
val value = map.getOrDefault("missing", 42)
```

**3. Check containsKey before getValue**

```kotlin
if (map.containsKey("key")) {
    val value = map.getValue("key")
}
```

**4. Use getOrPut for mutable maps**

```kotlin
val cache = mutableMapOf<String, Int>()
val value = cache.getOrPut("key") { computeExpensiveValue() }
```

**5. Handle null keys explicitly**

```kotlin
val map: Map<String?, Int> = mapOf(null to 0, "key" to 1)
val nullValue = map[null]  // 0
```

## Examples

```kotlin
// Example 1: Destructuring map entries
val map = mapOf("name" to "Alice", "age" to "30")
val (name, age) = map.entries.first()

// Example 2: Filter and transform
val scores = mapOf("Alice" to 90, "Bob" to 65, "Charlie" to 80)
val passing = scores.filter { it.value >= 70 }

// Example 3: Grouping with fold
val words = listOf("apple", "banana", "avocado", "blueberry")
val grouped = words.groupingBy { it.first() }.eachCount()
// {a=2, b=2}
```

## Related Errors

- [NullPointerException](nullpointer-kotlin) — null dereference
- [IndexOutOfBoundsException](indexoutofboundsexception) — index out of range
- [NoSuchElementException](nosuchelement-kotlin) — element not found
