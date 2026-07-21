---
title: "Bottom Navigation Animation Error"
description: "Fix BottomNavigationItem animation and label visibility errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Bottom navigation items do not animate correctly or labels disappear

## Common Causes

- Item icon not animating on selection
- Label text not showing for selected item
- Navigation destination not highlighting correct item
- Animation conflicting with Navigation component

## Fixes

- Use Navigation component for automatic item selection
- Set itemIconTint and itemTextColor selectors
- Ensure menu item IDs match nav graph destination
- Avoid manual animation when using Navigation

## Code Example

```kotlin
<!-- BottomNavigationView with Navigation -->
<com.google.android.material.bottomnavigation.BottomNavigationView
    android:id="@+id/bottomNav"
    app:labelVisibilityMode="labeled" />

<!-- Navigation setup -->
val navHostFragment = supportFragmentManager
    .findFragmentById(R.id.nav_host_fragment) as NavHostFragment
val navController = navHostFragment.navController

binding.bottomNav.setupWithNavController(navController)

<!-- Color selector: res/color/bottom_nav_color.xml -->
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:color="@color/selected" android:state_checked="true" />
    <item android:color="@color/unselected" />
</selector>
```

# labelVisibilityMode: "labeled" always shows text
# "selected" shows only selected label
# "unlabeled" never shows labels
# Use setupWithNavController for auto-selection
