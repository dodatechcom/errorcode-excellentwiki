---
title: "Gesture Test Error"
description: "Fix Compose gesture testing for automated gesture simulation and verification"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Gesture tests not simulating gestures correctly or assertions failing

## Common Causes

- Gesture not being simulated in test
- Gesture assertion not matching expected result
- Test timing issue with gesture
- Gesture not triggering expected behavior

## Fixes

- Use performTouchInput for gesture simulation
- Use awaitGesture() for complex gestures
- Use assertHasClickAction for click verification
- Test gesture sequence order

## Code Example

```kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun testGesture() {
    composeTestRule.setContent {
        MyComposable()
    }
    
    // Click gesture
    composeTestRule.onNodeWithTag("button")
        .performTouchInput { click() }
    
    // Long press
    composeTestRule.onNodeWithTag("item")
        .performTouchInput { longClick() }
    
    // Swipe gesture
    composeTestRule.onNodeWithTag("swipeable")
        .performTouchInput {
            swipe(
                start = centerLeft,
                end = centerRight,
                durationMillis = 300
            )
        }
    
    composeTestRule.waitForIdle()
}
```

# performTouchInput: gesture simulation# click/longClick/swipe: gesture types# awaitGesture: complex gesture sequences# waitForIdle: composition sync
