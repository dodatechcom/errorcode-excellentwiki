---
title: "Ambience Provider Error"
description: "Fix Compose ambient and provider pattern errors for theme-like data passing"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Theme data not reaching child composables or default values causing crashes

## Common Causes

- Ambience not provided in composable tree
- Default value not set for CompositionLocal
- Ambience value too large causing recomposition
- Nested providers not overriding correctly

## Fixes

- Provide ambience at theme level
- Set sensible defaults for CompositionLocal
- Use derivedStateOf for derived theme values
- Test theme switching with all child composables

## Code Example

```kotlin
// Define theme ambience
val LocalDarkTheme = compositionLocalOf { false }
val LocalTypography = compositionLocalOf { Typography() }

// Provide at theme level
@Composable
fun MyTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    CompositionLocalProvider(
        LocalDarkTheme provides darkTheme,
        LocalTypography provides Typography()
    ) {
        MaterialTheme(content = content)
    }
}

// Consume in child
@Composable
fun ThemedText() {
    val isDark = LocalDarkTheme.current
    val typography = LocalTypography.current
    Text(
        text = "Themed",
        style = if (isDark) typography.bodyLarge else typography.bodyMedium
    )
}
```

# compositionLocalOf: value changes trigger recomposition
# staticCompositionLocalOf: value changes don't trigger
# provides: sets value for subtree
# current: reads value
