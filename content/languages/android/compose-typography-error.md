---
title: "Typography Configuration Error"
description: "Fix Material 3 typography configuration and font family errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom typography not applying or font not rendering correctly

## Common Causes

- Typography not passed to MaterialTheme
- Font family not loaded from resources
- TextStyle not overriding default correctly
- Font weight not working as expected

## Fixes

- Pass Typography to MaterialTheme
- Load font with Font(R.font.family_name)
- Override specific text styles in Typography
- Use FontWeight constants for weight

## Code Example

```kotlin
val customTypography = Typography(
    headlineLarge = TextStyle(
        fontFamily = FontFamily.Monospace,
        fontWeight = FontWeight.Bold,
        fontSize = 32.sp,
        lineHeight = 40.sp
    ),
    bodyLarge = TextStyle(
        fontFamily = FontFamily.SansSerif,
        fontWeight = FontWeight.Normal,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.5.sp
    )
)

MaterialTheme(typography = customTypography) {
    // Typography applied to all MaterialText composables
}
```

# Typography styles: displayLarge-Medium-Small,
# headlineLarge-Medium-Small,
# titleLarge-Medium-Small,
# bodyLarge-Medium-Small,
# labelLarge-Medium-Small
