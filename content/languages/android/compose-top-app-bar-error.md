---
title: "TopAppBar Configuration Error"
description: "Fix Material 3 TopAppBar and SmallTopAppBar configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
TopAppBar does not display title correctly or navigation icon missing

## Common Causes

- TopAppBar not showing in Scaffold
- Title not updating on navigation
- Navigation icon not triggering back navigation
- TopAppBar scrolling behavior not working

## Fixes

- Use TopAppBar or CenterAlignedTopAppBar in Scaffold
- Set title as composable for dynamic content
- Use navigationIcon with onClick for back
- Add scrollBehavior for collapsing effect

## Code Example

```kotlin
Scaffold(
    topBar = {
        TopAppBar(
            title = { Text("Screen Title") },
            navigationIcon = {
                IconButton(onClick = { navController.popBackStack() }) {
                    Icon(Icons.Default.ArrowBack, "Back")
                }
            },
            actions = {
                IconButton(onClick = { /* settings */ }) {
                    Icon(Icons.Default.Settings, "Settings")
                }
            }
        )
    }
) { paddingValues ->
    // Content with padding
}
```

# TopAppBar: standard top bar
# CenterAlignedTopAppBar: centered title
# MediumTopAppBar: medium collapsed height
# LargeTopAppBar: large collapsed height
