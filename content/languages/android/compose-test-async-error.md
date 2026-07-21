---
title: "Compose Test Async Error"
description: "Fix Compose test asynchronous content and coroutine timing errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose tests fail because of asynchronous content loading or coroutine timing

## Common Causes

- Test asserting before content loads
- Coroutine not completing before assertion
- Main dispatcher not set for testing
- Test running before recomposition completes

## Fixes

- Use waitUntil for async content
- Use advanceUntilIdle() in runTest
- Use TestDispatcher for coroutine testing
- Use mainClock.advanceTimeBy() for Compose timing

## Code Example

```kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun loadData() = runTest {
    composeTestRule.setContent {
        MyScreen()
    }

    // Wait for loading to complete
    composeTestRule.waitUntil(timeoutMillis = 5000) {
        composeTestRule.onAllNodesWithText("Loading").fetchSemanticsNodes().isEmpty()
    }

    // Verify content loaded
    composeTestRule.onNodeWithText("Data loaded")
        .assertIsDisplayed()
}
```

# waitUntil: wait for condition
# advanceUntilIdle(): complete all coroutines
# mainClock.advanceTimeBy(): advance Compose time
# TestCoroutineDispatcher for timing control
