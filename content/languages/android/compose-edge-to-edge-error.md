---
title: "Edge to Edge Error"
description: "Fix Compose edge-to-edge rendering and system bar transparency errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Edge-to-edge rendering causes content to overlap with system bars

## Common Causes

- enableEdgeToEdge() not called in Activity
- System bars not transparent
- Content not padded for transparent bars
- Light/dark status bar icons not set

## Fixes

- Call enableEdgeToEdge() before setContent
- Use Scaffold for automatic edge-to-edge handling
- Apply WindowInsets padding to content
- Use SystemBarStyle for icon color

## Code Example

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge(
            statusBarStyle = SystemBarStyle.auto(
                lightScrim = Color.TRANSPARENT,
                darkScrim = Color.TRANSPARENT
            )
        )
        super.onCreate(savedInstanceState)
        setContent {
            MyTheme {
                Scaffold { paddingValues ->
                    // Content properly padded
                    HomeScreen(modifier = Modifier.padding(paddingValues))
                }
            }
        }
    }
}
```

# enableEdgeToEdge: makes system bars transparent
# Scaffold: handles padding for transparent bars
# Test both light and dark modes
