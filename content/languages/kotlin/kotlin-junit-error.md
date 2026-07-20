---
title: "[Solution] Kotlin JUnit 5 Error — Parameterized Test and Lifecycle"
description: "Fix Kotlin JUnit 5 errors including parameterized tests and test instance lifecycle. Learn correct JUnit 5 integration with Kotlin."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1016
---

## Common Causes

- Missing JUnit 5 dependencies for Kotlin test runner
- Using JUnit 4 `@RunWith` with JUnit 5 engine
- `@ParameterizedTest` missing `@MethodSource` or `@CsvSource`
- `@TestInstance(Lifecycle.PER_CLASS)` conflicts with Kotlin companion object

```kotlin
// Missing parameterized source
@ParameterizedTest
fun testWithValues(input: String) {
    assertNotNull(input)
    // No @MethodSource or @ValueSource — test won't run
}
```

## How to Fix

**1. Add correct JUnit 5 dependencies**

```kotlin
// build.gradle.kts
dependencies {
    testImplementation(kotlin("test"))
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
    testImplementation("org.junit.jupiter:junit-jupiter-params:5.10.0")
}
tasks.test { useJUnitPlatform() }
```

**2. Use @ValueSource or @MethodSource correctly**

```kotlin
@ParameterizedTest
@ValueSource(strings = ["Alice", "Bob", "Charlie"])
fun testNameLength(name: String) {
    assertTrue(name.length >= 3)
}

@ParameterizedTest
@MethodSource("provideTestData")
fun testWithMethod(input: Int) {
    assertTrue(input > 0)
}

companion object {
    @JvmStatic
    fun provideTestData() = listOf(1, 2, 3, 4, 5)
}
```

**3. Use Lifecycle.PER_CLASS for shared state**

```kotlin
@TestInstance(Lifecycle.PER_CLASS)
class MyTest {
    private lateinit var service: Service

    @BeforeAll
    fun setup() {
        service = Service()
    }

    @Test
    fun test1() {
        assertNotNull(service)
    }
}
```

**4. Use Kotlin-specific test extensions**

```kotlin
@TestFactory
fun dynamicTests(): Stream<DynamicTest> {
    return listOf(1, 2, 3).stream().map { DynamicTest.dynamicTest("Test $it") {
        assertTrue(it > 0)
    }}
}
```

## Examples

```kotlin
// Example 1: Complete parameterized test
@ParameterizedTest
@CsvSource(
    "1, 2, 3",
    "10, 20, 30",
    "-1, 1, 0"
)
fun testAddition(a: Int, b: Int, expected: Int) {
    assertEquals(expected, a + b)
}

// Example 2: Nested test classes
@Nested
inner class ValidationTests {
    @Test
    fun `valid email passes`() {
        assertTrue(Validator.isValidEmail("a@b.com"))
    }

    @Test
    fun `invalid email fails`() {
        assertFalse(Validator.isValidEmail("not-email"))
    }
}

// Example 3: Timeout extension
@Test
@Timeout(5)
fun testWithTimeout() {
    slowOperation()
}
```

## Related Errors

- [kotlin.test error](kotlin-test-error) — assertion errors
- [MockK error](kotlin-mockk-error) — mock verification
- [ClassCastException](classcastexception-kotlin) — type cast failed
