---
title: "Compose Test Animation Error"
description: "Fix Compose test animation control and transition verification errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose tests fail because of animations not completing or transitioning

## Common Causes

- Test asserting during animation
- Animation spec affecting test timing
- Transition not reaching final state
- Infinite animation blocking test completion

## Fixes

- Use mainClock.autoAdvance = false for manual control
- Advance clock past animation duration
- Use waitForIdle to let animations complete
- Disable animations in test configuration

## Code Example

```kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun testAnimation() {
    composeTestRule.mainClock.autoAdvance = false

    composeTestRule.setContent {
        AnimatedVisibility(visible = isVisible) {
            Text("Animated content")
        }
    }

    // Trigger animation
    isVisible = true

    // Advance past animation
    composeTestRule.mainClock.advanceTimeBy(500)
    composeTestRule.waitForIdle()

    // Assert final state
    composeTestRule.onNodeWithText("Animated content")
        .assertIsDisplayed()
}
```

# autoAdvance: control clock manually
# advanceTimeBy: advance past animation
# waitForIdle: let pending work complete
# Or use composeTestRule.mainClock.advanceTimeByFrame()
