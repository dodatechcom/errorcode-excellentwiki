---
title: "CompositionLocal Error"
description: "Fix CompositionLocal and dependency propagation errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
CompositionLocal values not properly provided or consumed across composable tree

## Common Causes

- CompositionLocal not provided at correct level
- LocalComposition value returning default error
- CompositionLocal not propagating to nested composables
- Multiple CompositionLocals conflicting

## Fixes

- Provide CompositionLocal at highest needed level
- Use CompositionLocalProvider to set values
- Access with LocalComposition.current in children
- Use unique CompositionLocal names per type

## Code Example

```kotlin
// Define CompositionLocal
val LocalUserColor = staticCompositionLocalOf { Color.Gray }

// Provide value
@Composable
fun AppTheme(userColor: Color) {
    CompositionLocalProvider(LocalUserColor provides userColor) {
        MyApp()
    }
}

// Consume value
@Composable
fun UserAvatar() {
    val color = LocalUserColor.current
    Box(modifier = Modifier.background(color))
}
```

# staticCompositionLocalOf: value rarely changes
# compositionLocalOf: value may change
# provides: sets value in tree
# current: reads value from tree
