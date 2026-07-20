---
title: "[Solution] Kotlin Comparator Contract Violation"
description: "Fix Kotlin Comparator contract violation and inconsistent compareTo/equals. Learn comparison consistency rules."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1007
---

## Common Causes

- `compareTo` returning inconsistent results (violates transitivity)
- `compareTo` and `equals` returning different truth values
- Sorting with a comparator that does not respect `equals`
- Using `sortWith` with an unstable comparator in parallel contexts

```kotlin
// Violates comparator contract
val comparator = compareBy<String> { if (it.length > 3) 0 else it.length }
// Returns 0 for "cat" and "dog" but also 0 for "apple" vs "cat"
```

## How to Fix

**1. Ensure compareTo is transitive and consistent**

```kotlin
data class Person(val name: String, val age: Int)

// CORRECT: Consistent comparator
val comparator = compareBy<Person> { it.age }
    .thenBy { it.name }
```

**2. Align compareTo with equals**

```kotlin
// WRONG: compareTo and equals disagree
class Bad(val value: Int) : Comparable<Bad> {
    override fun compareTo(other: Bad) = value.compareTo(other.value)
    override fun equals(other: Any?) = other is Bad && other.value == value + 1
}

// CORRECT: Keep consistent
class Good(val value: Int) : Comparable<Good> {
    override fun compareTo(other: Good) = value.compareTo(other.value)
    override fun equals(other: Any?) = other is Good && other.value == value
    override fun hashCode() = value.hashCode()
}
```

**3. Use stable sort for predictable ordering**

```kotlin
val items = listOf("Banana", "apple", "Cherry")
val sorted = items.sortedWith(compareBy(String.CASE_INSENSITIVE_ORDER) { it })
```

**4. Use naturalOrder for enums**

```kotlin
enum class Priority { LOW, MEDIUM, HIGH }
val sorted = priorities.sorted()  // Uses natural enum ordering
```

## Examples

```kotlin
// Example 1: Multi-field comparator
data class Product(val name: String, val price: Double, val rating: Double)

val byPriceAsc = compareBy<Product> { it.price }
    .thenByDescending { it.rating }
    .thenBy { it.name }

val sorted = products.sortedWith(byPriceAsc)

// Example 2: Custom comparator with null handling
val nullsFirst = compareBy<Int?>(nullsFirst()) { it }

// Example 3: Comparator from lambda
val byLength = compareBy<String> { it.length }
val words = listOf("kotlin", "java", "c", "python")
println(words.sortedWith(byLength))  // [c, java, kotlin, python]
```

## Related Errors

- [ClassCastException](classcastexception-kotlin) — type cast failed
- [UnsupportedOperationException](unsupportedoperationexception) — operation not supported
- [IllegalArgumentException](illegalargumentexception) — invalid argument
