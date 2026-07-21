---
title: "Compose Theme Error"
description: "Fix Jetpack Compose MaterialTheme and custom theme configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom Compose theme does not apply colors or typography correctly

## Common Causes

- MaterialTheme not wrapping entire composable tree
- ColorScheme not created from custom colors
- Typography not provided to MaterialTheme
- Theme composable not called in setContent

## Fixes

- Wrap content with your custom Theme composable
- Create ColorScheme from your custom Color object
- Provide Typography to MaterialTheme
- Call Theme in setContent block

## Code Example

```kotlin
@Composable
fun MyAppTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = lightColorScheme(
            primary = Purple500,
            onPrimary = Color.White,
            background = LightGray
        ),
        typography = Typography(
            bodyLarge = TextStyle(fontSize = 16.sp)
        ),
        content = content
    )
}

// In Activity:
setContent {
    MyAppTheme {
        MainScreen()
    }
}
```

# Define colors.kt with custom Color values
# Create Light and Dark color schemes
# Apply theme in every composable entry point
