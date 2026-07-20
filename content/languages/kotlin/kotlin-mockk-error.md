---
title: "[Solution] Kotlin MockK Verification Error — Relaxed Mock and Slot Capture"
description: "Fix Kotlin MockK verification errors. Learn correct mock setup, relaxed mocks, and slot capture patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1017
---

## Common Causes

- Verification failure: expected call was never made
- `Relaxed mock` returning unexpected defaults causing silent failures
- Slot capture on non-matching invocation
- Using `every` on a `relaxed` mock without `verify` afterwards
- Co-variant return type mismatch in mock setup

```kotlin
val mock = mockk<Repository>()
every { mock.getUser() } returns User("Alice")
verify { mock.getUser() }  // Fails if getUser() was never called
```

## How to Fix

**1. Use verify with correct parameters**

```kotlin
// WRONG: Verify without order
verify { mock.save(any()) }

// CORRECT: Verify with exact parameters
verify { mock.save(expectedUser) }
```

**2. Use slot for argument capture**

```kotlin
val slot = slot<User>()
verify { mock.save(capture(slot)) }
assertEquals("Alice", slot.captured.name)
```

**3. Use relaxed mock carefully**

```kotlin
// Relaxed mock auto-stubs all methods
val mock = mockk<Repository>(relaxed = true)

// Better: explicit stubbing
val mock = mockk<Repository>()
every { mock.getUser() } returns defaultUser
```

**4. Use coEvery for suspend functions**

```kotlin
val mock = mockk<Repository>()
coEvery { mock.fetchUser() } returns User("Alice")

coVerify { mock.fetchUser() }
```

## Examples

```kotlin
// Example 1: Complete mock with verification
class UserServiceTest {
    private val repository = mockk<Repository>()
    private val service = UserService(repository)

    @Test
    fun testSaveUser() = runTest {
        val user = User("Alice", 30)
        coEvery { repository.save(user) } just Runs

        service.saveUser(user)

        coVerify(exactly = 1) { repository.save(user) }
    }
}

// Example 2: Slot capture with multiple arguments
val nameSlot = slot<String>()
val ageSlot = slot<Int>()
verify { mock.create(capture(nameSlot), capture(ageSlot)) }

// Example 3: Ordered verification
verifyOrder {
    mock.connect()
    mock.authenticate()
    mock.fetch()
}
```

## Related Errors

- [MockK private mocking](kotlin-mockk-private) — private function mocking
- [kotlin.test error](kotlin-test-error) — assertion errors
- [JUnit error](kotlin-junit-error) — JUnit lifecycle
