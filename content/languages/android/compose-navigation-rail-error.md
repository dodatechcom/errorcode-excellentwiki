---
title: "NavigationRail Error"
description: "Fix Material 3 NavigationRail configuration and icon display errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
NavigationRail does not display icons correctly or handle selection

## Common Causes

- NavigationRailItem not showing selected state
- Icons not aligned with labels
- NavigationRail not visible on larger screens
- Selected item not matching current destination

## Fixes

- Use NavigationRailItem with selected parameter
- Set icon and label in NavigationRailItem
- Show NavigationRail on tablet and foldable
- Connect to NavController for auto-selection

## Code Example

```kotlin
// Show on medium+ screens
val windowSizeClass = calculateWindowSizeClass(activity)
if (windowSizeClass.widthSizeClass != WindowWidthSizeClass.Compact) {
    NavigationRail {
        NavigationRailItem(
            selected = currentDestination?.id == "home",
            onClick = { navController.navigate("home") },
            icon = { Icon(Icons.Default.Home, null) },
            label = { Text("Home") }
        )
        NavigationRailItem(
            selected = currentDestination?.id == "search",
            onClick = { navController.navigate("search") },
            icon = { Icon(Icons.Default.Search, null) },
            label = { Text("Search") }
        )
    }
}
```

# NavigationRail: side navigation for tablets
# NavigationBarItem: bottom navigation for phones
# Connect to NavController for auto-selection
# Show based on WindowSizeClass
