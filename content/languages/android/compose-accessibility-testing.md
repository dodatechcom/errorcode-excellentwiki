---
title: "Compose Accessibility Testing Error"
description: "Fix Compose accessibility testing configuration and tool errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose accessibility tests do not detect issues or produce false positives

## Common Causes

- Accessibility test not finding issues
- Semantics tree not matching expectations
- Test not verifying all interactive elements
- Accessibility rule not properly configured

## Fixes

- Enable accessibility testing in Compose test
- Use onNodeWithContentDescription for image tests
- Verify all interactive elements have descriptions
- Test with real accessibility services

## Code Example

```kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun accessibilityCheck() {
    composeTestRule.setContent {
        MyScreen()
    }

    // Check all images have content descriptions
    composeTestRule.onAllNodes(isImage())
        .fetchSemanticsNodes()
        .forEach { node ->
            assertNotNull(node.config.getOrNull(SemanticsProperties.ContentDescription))
        }

    // Check all buttons are labeled
    composeTestRule.onAllNodes(hasClickAction())
        .fetchSemanticsNodes()
        .forEach { node ->
            assertNotNull(node.config.getOrNull(SemanticsProperties.ContentDescription))
        }
}
```

# Test all images have content descriptions
# Test all clickable elements are labeled
# Test color contrast meets WCAG standards
# Use real TalkBack for manual testing
