---
title: "Compose Accessibility Test Error"
description: "Fix Compose accessibility testing with semantics tree verification"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Accessibility tests fail because semantics tree does not match expectations

## Common Causes

- onNodeWithContentDescription not finding elements
- Semantics tree not matching expected structure
- Test not verifying content description
- Accessibility action not registered in test

## Fixes

- Use onNodeWithContentDescription for image tests
- Verify semantics properties with assertHasClickAction
- Use onNode with semantics matcher
- Test semantic properties in Compose tests

## Code Example

```kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun accessibility() {
    composeTestRule.setContent {
        MyScreen()
    }

    // Verify content description exists
    composeTestRule.onNodeWithContentDescription("Settings icon")
        .assertExists()
        .assertHasClickAction()

    // Verify text content
    composeTestRule.onNodeWithText("Submit")
        .assertIsDisplayed()
        .assertHasClickAction()

    // Verify custom semantics
    composeTestRule.onNode(
        hasText("Progress") and hasContentDescription("75%")
    ).assertExists()
}
```

# onNodeWithContentDescription: find by description
# assertHasClickAction: verify clickable
# assertIsEnabled/isDisabled: verify state
