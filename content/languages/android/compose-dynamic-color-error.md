---
title: "Dynamic Color Error"
description: "Fix Material 3 dynamic color configuration and fallback errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Dynamic color (Material You) does not apply or shows wrong colors on Android 12+

## Common Causes

- DynamicColor not checking API level
- ColorScheme not falling back on older devices
- Dynamic color not available on some OEM skins
- Seed color not matching expected palette

## Fixes

- Check Build.VERSION.SDK_INT >= S for dynamic color
- Provide fallback colorScheme for older devices
- Test on multiple OEM devices
- Use dynamicLightColorScheme/dynamicDarkColorScheme

## Code Example

```kotlin
val colorScheme = when {
    Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
        if (isSystemInDarkTheme()) dynamicDarkColorScheme(context)
        else dynamicLightColorScheme(context)
    }
    else -> {
        if (isSystemInDarkTheme()) darkColorScheme()
        else lightColorScheme()
    }
}

MaterialTheme(colorScheme = colorScheme) {
    // Your content
}
```

# dynamicLightColorScheme: Android 12+ light
# dynamicDarkColorScheme: Android 12+ dark
# Fallback for older devices: static colorScheme
# Test on Pixel, Samsung, OnePlus devices
