---
title: "Animation Test Error"
description: "Fix Compose animation testing for verifying animation behavior in tests"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Animation tests not waiting for animation completion or assertions failing

## Common Causes

- Test not waiting for animation to complete
- Animation assertion failing because of timing
- Test not controlling animation speed
- Animation state not accessible in test

## Fixes

- Use mainClock for animation timing
- Use advanceClockBy() for manual control
- Use animateTo() for animation assertions
- Control animation speed in tests

## Code Example

```kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun testAnimation() {
    composeTestRule.mainClock.autoAdvance = false
    
    composeTestRule.setContent {
        AnimatedContent(targetState = isVisible) {
            if (it) Text("Visible") else Text("Hidden")
        }
    }
    
    // Advance animation
    composeTestRule.mainClock.advanceTimeBy(500)
    composeTestRule.waitForIdle()
    
    composeTestRule.onNodeWithText("Visible")
        .assertIsDisplayed()
}
```

# mainClock: animation timing control# autoAdvance: manual animation control# advanceTimeBy: advance animation time# waitForIdle: composition sync
