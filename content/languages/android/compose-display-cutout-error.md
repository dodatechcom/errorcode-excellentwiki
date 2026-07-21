---
title: "Display Cutout Error"
description: "Fix Compose display cutout and notch handling errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Content overlaps with camera cutout or display notch

## Common Causes

- Cutout area not properly accounted for
- Content rendering behind camera punch-hole
- Landscape mode cutout different from portrait
- Cutout handling not consistent across devices

## Fixes

- Use WindowInsets.displayCutout for cutout area
- Apply cutout padding to root composable
- Test on devices with different cutout styles
- Use Scaffold for automatic cutout handling

## Code Example

```kotlin
// Display cutout insets
Box(
    modifier = Modifier
        .fillMaxSize()
        .windowInsetsPadding(WindowInsets.displayCutout)
) {
    // Content avoids cutout area
}

// Or in Scaffold:
Scaffold { paddingValues ->
    // paddingValues includes cutout insets
    LazyColumn(contentPadding = paddingValues) {
        items(list) { item -> ListItem(item) }
    }
}
```

# WindowInsets.displayCutout: camera cutout area
# Scaffold includes cutout in padding
# Test on devices: Pixel 7 Pro, Galaxy S24, etc.
