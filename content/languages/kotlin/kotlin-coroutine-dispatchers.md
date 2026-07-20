---
title: "[Solution] Kotlin Coroutine Dispatcher Selection Error"
description: "Fix Kotlin coroutine dispatcher errors including IO on Main, wrong thread context. Learn correct dispatcher usage patterns."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1011
---

## What This Error Means

Wrong dispatcher selection causes thread safety violations, UI freezes, or unexpected thread context. Using `Dispatchers.Main` for blocking work or `Dispatchers.IO` for UI operations are common mistakes.

## Common Causes

- Blocking I/O on `Dispatchers.Main` (freezes UI)
- UI updates from `Dispatchers.IO` (crashes on Android)
- Using `Dispatchers.Default` for blocking I/O
- Creating new dispatchers instead of reusing existing ones

```kotlin
// WRONG: Blocking I/O on Main
viewModelScope.launch(Dispatchers.Main) {
    val data = database.query()  // Blocks UI thread
}
```

## How to Fix

**1. Use the correct dispatcher for each task**

```kotlin
// CORRECT: Dispatchers for each concern
viewModelScope.launch(Dispatchers.IO) {
    val data = repository.fetch()  // Network on IO
    withContext(Dispatchers.Main) {
        _uiState.value = data  // UI update on Main
    }
}
```

**2. Use Dispatchers.Default for CPU-bound work**

```kotlin
val sorted = withContext(Dispatchers.Default) {
    hugeList.parallelSort()  // CPU-intensive
}
```

**3. Use TestDispatcher in tests**

```kotlin
@Test
fun testWithDispatcher() = runTest {
    val testDispatcher = UnconfinedTestDispatcher(testScheduler)
    val repository = FakeRepository(dispatcher = testDispatcher)
    repository.fetch()
}
```

**4. Inject dispatchers for testability**

```kotlin
class MyViewModel(
    private val dispatcher: CoroutineDispatcher = Dispatchers.IO
) : ViewModel() {
    fun loadData() = viewModelScope.launch(dispatcher) {
        // Easily swappable in tests
    }
}
```

## Examples

```kotlin
// Example 1: Complete dispatcher usage pattern
class UserRepository(private val ioDispatcher: CoroutineDispatcher) {
    suspend fun getUsers(): List<User> = withContext(ioDispatcher) {
        api.fetchUsers()
    }
}

// Example 2: Confined dispatcher for sequential work
val singleThreadDispatcher = Executors.newSingleThreadDispatcher().asCoroutineDispatcher()

// Example 3: Limited dispatcher for rate limiting
val limitedDispatcher = Dispatchers.IO.limitedParallelism(4)
```

## Related Errors

- [CancellationException](cancellationexception-kotlin) — coroutine cancelled
- [Channel error](kotlin-channel-error) — channel communication error
- [Flow backpressure error](kotlin-flow-backpressure) — flow emission issue
