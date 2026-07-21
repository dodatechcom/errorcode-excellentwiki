---
title: "Compose Screenshot Test Error"
description: "Fix Compose screenshot and visual regression testing configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose screenshot tests produce incorrect images or fail to compare correctly

## Common Causes

- Screenshot not capturing full composable
- Screenshot comparison threshold too strict
- Theme not applied in screenshot test
- Font scaling affecting screenshot comparison

## Fixes

- Use captureToImage for composable screenshots
- Set comparison threshold appropriately
- Apply theme in test setContent
- Use Robolectric for consistent rendering

## Code Example

```kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun screenshot() {
    composeTestRule.setContent {
        MyTheme {
            MyScreen()
        }
    }

    // Capture screenshot
    val bitmap = composeTestRule.onRoot()
        .captureToImage()
        .toArgbImageBitmap()

    // Save or compare
    assertAgainstGolden("screenshot", bitmap)
}
```

# captureToImage: capture composable as ImageBitmap
# Use Robolectric for consistent device rendering
# Set comparison threshold for visual diffs
# Store golden screenshots for comparison
