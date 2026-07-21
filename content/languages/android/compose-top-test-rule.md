---
title: "Compose Test Error"
description: "Fix Compose testing with ComposeTestRule for automated UI tests"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose UI tests failing or not finding composables correctly

## Common Causes

- Composable not found in test
- Click action not triggering in test
- Assertion failing because of timing
- Test not waiting for composition

## Fixes

- Use ComposeTestRule for test management
- Use onNodeWithText/onNodeWithTag to find nodes
- Use performClick/performTextInput for actions
- Use waitForIdle() for composition sync

## Code Example

```kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun testMyComposable() {
    composeTestRule.setContent {
        MyComposable()
    }
    
    composeTestRule.onNodeWithText("Hello")
        .assertIsDisplayed()
    
    composeTestRule.onNodeWithTag("submitButton")
        .performClick()
    
    composeTestRule.waitForIdle()
    
    composeTestRule.onNodeWithText("Success")
        .assertIsDisplayed()
}
```

# createComposeRule(): test rule# setContent: set test content# onNode*: find composables# performClick/performTextInput: actions
