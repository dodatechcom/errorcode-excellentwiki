---
title: "Coroutine Test Dispatcher Error"
description: "Fix Kotlin coroutines test dispatcher and runTest errors in Android tests"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Coroutine tests hang, run forever, or produce timing-sensitive failures

## Common Causes

- runTest not used for coroutine tests
- TestCoroutineDispatcher not advancing time
- Dispatchers.setMain not called in test setup
- Unconfined vs StandardTestDispatcher confusion

## Fixes

- Use runTest for coroutine test blocks
- Use advanceUntilIdle() to complete all pending
- Call Dispatchers.setMain in @Before
- Use StandardTestDispatcher for precise control

## Code Example

```kotlin
@Before
fun setup() {
    Dispatchers.setMain(StandardTestDispatcher())
}

@After
fun tearDown() {
    Dispatchers.resetMain()
}

@Test
fun `test loading then success`() = runTest {
    val viewModel = MyViewModel(testRepository)

    // Initial state
    assertEquals(UiState.Loading, viewModel.uiState.value)

    // Advance time to complete coroutine
    advanceUntilIdle()

    // Final state
    assertIs<UiState.Success>(viewModel.uiState.value)
}
```

# runTest: automatically handles coroutine testing
# StandardTestDispatcher: manual time control
# UnconfinedTestDispatcher: immediate execution
# advanceUntilIdle(): complete all pending work
