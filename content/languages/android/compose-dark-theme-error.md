---
title: "Dark Theme Error"
description: "Fix Material 3 dark theme and color scheme switching errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Dark theme does not apply correctly or switches unexpectedly

## Common Causes

- isSystemInDarkTheme() not checking correctly
- Dark and light color schemes swapped
- Theme switching not triggering recomposition
- Dark theme colors not meeting contrast requirements

## Fixes

- Use isSystemInDarkTheme() for automatic switching
- Provide both lightColorScheme and darkColorScheme
- Wrap theme in composition for recomposition
- Test dark theme colors for WCAG compliance

## Code Example

```kotlin
@Composable
fun MyTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        darkTheme -> darkColorScheme(
            primary = Purple200,
            onPrimary = Black,
            background = DarkGray,
            surface = DarkGray
        )
        else -> lightColorScheme(
            primary = Purple500,
            onPrimary = White,
            background = White,
            surface = White
        )
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        content = content
    )
}
```

# isSystemInDarkTheme(): follows system setting
# darkColorScheme: colors for dark theme
# lightColorScheme: colors for light theme
# Test both themes thoroughly
