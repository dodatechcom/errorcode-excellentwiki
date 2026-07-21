---
title: "WindowInsets Error"
description: "Fix Compose WindowInsets handling and system bar padding errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Content hidden behind system bars or insets not properly applied

## Common Causes

- WindowInsets not consumed properly
- Content overlapping status or navigation bar
- Padding not applied to correct composable
- Insets different for foldable devices

## Fixes

- Use WindowInsets.systemBars for status and nav bars
- Apply padding with WindowInsets.asPaddingValues()
- Use Scaffold for automatic insets handling
- Test on devices with different display cutouts

## Code Example

```kotlin
// Scaffold handles insets automatically
Scaffold { paddingValues ->
    // paddingValues includes system bar padding
    Column(modifier = Modifier.padding(paddingValues)) {
        Text("Content below status bar")
    }
}

// Manual insets:
Box(
    modifier = Modifier
        .fillMaxSize()
        .windowInsetsPadding(WindowInsets.systemBars)
) {
    Text("Content with system bar insets")
}

// Specific inset:
Modifier.windowInsetsPadding(WindowInsets.navigationBars)
```

# WindowInsets.systemBars: status + navigation
# WindowInsets.navigationBars: nav bar only
# WindowInsets.statusBars: status bar only
# Scaffold handles insets by default
