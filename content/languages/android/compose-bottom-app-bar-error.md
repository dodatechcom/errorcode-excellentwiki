---
title: "BottomAppBar Error"
description: "Fix Material 3 BottomAppBar and FloatingActionButton positioning errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
BottomAppBar does not display correctly or FAB not positioned properly

## Common Causes

- FAB not embedded in BottomAppBar cutout
- BottomAppBar not visible with Scaffold
- Navigation icon not responding
- BottomAppBar color not matching theme

## Fixes

- Use FloatingActionButton within BottomAppBar
- Connect BottomAppBar to Scaffold
- Set onNavigationClick for navigation icon
- Use BottomAppBarDefaults for theme colors

## Code Example

```kotlin
Scaffold(
    bottomBar = {
        BottomAppBar(
            actions = {
                IconButton(onClick = { /* home */ }) {
                    Icon(Icons.Default.Home, "Home")
                }
                IconButton(onClick = { /* search */ }) {
                    Icon(Icons.Default.Search, "Search")
                }
            },
            floatingActionButton = {
                FloatingActionButton(onClick = { /* add */ }) {
                    Icon(Icons.Default.Add, "Add")
                }
            }
        )
    }
) { paddingValues ->
    // Content
}
```

# BottomAppBar: Material 3 bottom bar
# FAB: embedded in bar cutout
# actions: navigation icons
# Connect to Scaffold for proper layout
