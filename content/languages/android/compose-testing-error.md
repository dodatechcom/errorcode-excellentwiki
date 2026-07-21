---
title: "Compose Testing Error"
description: "Fix Jetpack Compose UI test errors with ComposeTestRule and assertions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose UI tests fail to find nodes or assert content correctly

## Common Causes

- Node not found by semantics matcher
- Test rule not properly configured
- Using wrong assertion method
- Content not loaded when assertion runs

## Fixes

- Use onNodeWithText or onNodeWithTag to find nodes
- Use createComposeRule() in test setup
- Use assertIsDisplayed() before interactions
- Use waitForIdle() or waitUntil for async content

## Code Example

```kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun myTest() {
    composeTestRule.setContent {
        MyComposable()
    }
    composeTestRule.onNodeWithText("Hello")
        .assertIsDisplayed()
    composeTestRule.onNodeWithTag("submitButton")
        .performClick()
    composeTestRule.onNodeWithText("Success")
        .waitUntil(timeoutMillis = 5000) { exists() }
        .assertExists()
}
```

# Use semantic tags for reliable test selection
# Add testTag("name") modifier to test targets
# Run: ./gradlew connectedDebugAndroidTest
