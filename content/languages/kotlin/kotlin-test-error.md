---
title: "[Solution] Kotlin Test Assertion Error — Expected/Actual Mismatch"
description: "Fix kotlin.test assertion errors. Learn correct assertion patterns and expected/actual comparison in Kotlin multiplatform tests."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1015
---

## What This Error Means

kotlin.test assertion errors occur when the expected value doesn't match the actual result. This is the most common test failure in Kotlin, often caused by incorrect assertions, data class comparison issues, or platform differences in multiplatform tests.

## Common Causes

- Using reference equality instead of structural equality
- Missing `assertEquals` import from `kotlin.test`
- Asserting on mutable state that changed before assertion
- Multiplatform `expect`/`actual` test implementations returning different values

```kotlin
// Reference equality fails
val a = listOf(1, 2)
val b = listOf(1, 2)
assertTrue(a === b)  // False — different instances
```

## How to Fix

**1. Use structural equality assertions**

```kotlin
import kotlin.test.assertEquals

@Test
fun testEquality() {
    val expected = listOf(1, 2, 3)
    val actual = listOf(1, 2, 3)
    assertEquals(expected, actual)  // Structural equality
}
```

**2. Use assertContentEquals for collections**

```kotlin
import kotlin.test.assertContentEquals

@Test
fun testCollections() {
    val expected = intArrayOf(1, 2, 3)
    val actual = intArrayOf(1, 2, 3)
    assertContentEquals(expected, actual)
}
```

**3. Use assertFailsWith for exception testing**

```kotlin
@Test
fun testException() {
    assertFailsWith<IllegalArgumentException> {
        parseInvalidInput("abc")
    }
}
```

**4. Assert null with assertNull**

```kotlin
@Test
fun testNullability() {
    val result = findItem(nonExistentId)
    assertNull(result)
    assertNotNull(existingItem)
}
```

## Examples

```kotlin
// Example 1: Complete test with multiple assertions
@Test
fun testUserCreation() {
    val user = User("Alice", 30)
    assertEquals("Alice", user.name)
    assertEquals(30, user.age)
    assertEquals(user, User("Alice", 30))
}

// Example 2: Testing suspend functions
@Test
fun testFetchData() = runTest {
    val result = repository.fetch()
    assertEquals("expected", result.value)
    assertTrue(result.isSuccess)
}

// Example 3: Soft assertions for multiple checks
@Test
fun testMultiple() {
    val errors = mutableListOf<String>()
    if (actual.name != expected.name) errors.add("name mismatch")
    if (actual.age != expected.age) errors.add("age mismatch")
    assertTrue(errors.isEmpty(), errors.joinToString())
}
```

## Related Errors

- [ClassCastException](classcastexception-kotlin) — type cast failed
- [IllegalArgumentException](illegalargumentexception) — invalid argument
- [UnsupportedOperationException](unsupportedoperationexception) — operation not supported
