---
title: "LazyColumn RTL Error"
description: "Fix LazyColumn right-to-left layout support for RTL languages"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn items not properly laid out in RTL languages

## Common Causes

- Items not mirrored for RTL layout
- Horizontal padding incorrect in RTL
- Scroll direction reversed in RTL
- Icons and text alignment wrong

## Fixes

- Use start/end instead of left/right for padding
- Ensure composables use RTL-compatible modifiers
- Test with RTL preview mode
- Use LocalLayoutDirection for manual layout

## Code Example

```kotlin
LazyColumn {
    items(items) { item ->
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 16.dp)  // Automatically mirrors for RTL
        ) {
            Icon(Icons.Default.ArrowForward, null)
            Text(item.text)
        }
    }
}
```

# Use start/end padding (auto-mirrors)# Test with RTL preview in Android Studio# LocalLayoutDirection.current for manual check# Compose handles RTL by default
