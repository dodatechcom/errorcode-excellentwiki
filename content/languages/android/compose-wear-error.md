---
title: "Wear OS Compose Error"
description: "Fix Wear OS Compose and WearableAppWidget configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Wear OS Compose app does not display or function correctly on wearable

## Common Causes

- Wear Compose dependencies not added
- ScalingLazyColumn not configured for small screen
- Tile service not rendering
- Complication not updating

## Fixes

- Add wear-compose dependencies
- Use ScalingLazyColumn for Wear lists
- Implement TileService for watch face tiles
- Use Canvas for custom Wear rendering

## Code Example

```kotlin
dependencies {
    implementation "androidx.wear.compose:compose-material:1.3.0"
    implementation "androidx.wear.compose:compose-foundation:1.3.0"
}

// Wear list:
ScalingLazyColumn {
    items(items) { item ->
        Text(
            text = item.name,
            modifier = Modifier.fillMaxWidth()
        )
    }
}
```

# Wear Compose for Wear OS apps
# ScalingLazyColumn: optimized for round screens
# TileService: for watch face tiles
# ComplicationDataSource: for watch complications
