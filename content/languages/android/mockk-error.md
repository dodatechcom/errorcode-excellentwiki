---
title: "MockK Error"
description: "Fix MockK mocking framework errors for Kotlin classes and coroutines"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
MockK fails to mock final classes, suspend functions, or companion objects

## Common Causes

- Final class not mockable without MockK configuration
- Suspend function not properly mocked
- Companion object method not mocked
- every {} block throwing exception

## Fixes

- Use mockk() for final classes (MockK handles this)
- Use coEvery {} for suspend function mocking
- Use mockkStatic() for companion objects
- Use @TestConfiguration for MockK settings

## Code Example

```kotlin
// Mock final class
val mockRepo = mockk<Repository>()

// Mock suspend function
coEvery { mockRepo.getData() } returns listOf(item)

// Mock companion object
mockkStatic(SomeClass.Companion)
every { SomeClass.create() } returns mockInstance

// Mock object
mockkObject(MySingleton)
every { MySingleton.doSomething() } returns result

// Verify calls:
coVerify { mockRepo.getData() }
coVerify(exactly = 2) { mockRepo.saveData(any()) 
```

# MockK: native Kotlin mocking
# coEvery: coroutine mocking
# coVerify: verify coroutine calls
# mockkObject: singleton mocking
