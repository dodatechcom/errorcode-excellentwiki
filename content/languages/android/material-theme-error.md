---
title: "Material Theme Error"
description: "Fix Material Design theme and MaterialYou dynamic color errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Material Design components do not display correct theme colors or styles

## Common Causes

- Material theme not applied as app theme
- Dynamic color not working on API 31+
- Theme attributes not matching expected values
- Material3 components using Material2 theme

## Fixes

- Set Theme.Material3.DayNight as app theme
- Check API level for dynamic color support
- Use Material theme attributes instead of hardcoded colors
- Use MaterialTheme composable in Compose

## Code Example

```kotlin
<!-- res/values/themes.xml -->
<style name="Theme.MyApp" parent="Theme.Material3.DayNight.NoActionBar">
    <item name="colorPrimary">@color/purple_500</item>
    <item name="colorOnPrimary">@color/white</item>
</style>

// Compose:
MaterialTheme(
    colorScheme = if (isSystemInDarkTheme()) darkColorScheme()
    else lightColorScheme(),
    typography = Typography(),
    content = content
)
```

# For dynamic color (API 31+):
val dynamicColor = Build.VERSION.SDK_INT >= Build.VERSION_CODES.S
if (dynamicColor) {
    val context = dynamicColorContext(this)
    MaterialTheme(colorScheme = dynamicLightColorScheme(context))
}
