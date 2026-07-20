---
title: "[Solution] Kotlin MockK Private Function Mocking and Spy"
description: "Fix Kotlin MockK private function mocking errors. Learn correct patterns for mocking private members and using spyk."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1018
---

## Common Causes

- Attempting to mock private functions without MockK agent/inline support
- `spyk` on a class with private constructors
- Private method mocking returning unexpected values
- MockK inline agent not configured for final classes

```kotlin
// May fail without MockK agent configuration
val spy = spyk(MyClass())
every { spy.privateMethod() } returns "mocked"  // Compilation error
```

## How to Fix

**1. Configure MockK agent for final/private classes**

```kotlin
// build.gradle.kts
dependencies {
    testImplementation("io.mockk:mockk:1.13.8")
}
tasks.withType<Test> {
    jvmArgs("--add-opens", "java.base/java.lang=ALL-UNNAMED")
}
```

**2. Use mockkObject for companion object mocking**

```kotlin
mockkObject(MyCompanion)
every { MyCompanion.create() } returns mockInstance
// ... test ...
unmockkObject(MyCompanion)
```

**3. Use spyk with partial mocking**

```kotlin
val spy = spyk(MyClass())
every { spy.privateMethod() } returns "stubbed"
// Other methods call real implementation
```

**4. Restructure for testability instead of mocking private**

```kotlin
// WRONG: Mocking private methods
class Service {
    private fun validate(input: String): Boolean { ... }
}

// CORRECT: Make validation testable
class Service(private val validator: Validator = Validator()) {
    fun process(input: String) {
        require(validator.isValid(input))
    }
}
```

## Examples

```kotlin
// Example 1: MockK with inline classes
@JvmInline
value class UserId(val value: Long)

class UserService {
    fun getUserName(id: UserId): String = "User-${id.value}"
}

val mock = mockk<UserService>()
every { mock.getUserName(UserId(1L)) } returns "Alice"

// Example 2: Mocking extension functions
val mockFn = mockk<(String) -> Int>()
every { mockFn("hello") } returns 5

// Example 3: Answer-based mocking
val mock = mockk<Repository>()
every { mock.getUser(any()) } answers { User(firstArg()) }
```

## Related Errors

- [MockK verification error](kotlin-mockk-error) — mock verification
- [kotlin.test error](kotlin-test-error) — assertion errors
- [Inline class error](inline-class-error) — value class issue
