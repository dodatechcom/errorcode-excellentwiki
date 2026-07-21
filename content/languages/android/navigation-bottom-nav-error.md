---
title: "Bottom Navigation Error"
description: "Fix Android Navigation bottom navigation view integration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Bottom navigation does not switch fragments correctly with Navigation component

## Common Causes

- BottomNavigationView not connected to NavController
- Fragment transaction not using Navigation
- Back stack not properly managed with bottom nav
- Menu item ID does not match fragment destination ID

## Fixes

- Use NavigationUI.setupWithNavController()
- Ensure menu item IDs match nav graph destination IDs
- Use NavigationUI.onNavDestinationSelected for menu
- Configure popUpTo for bottom navigation items

## Code Example

```kotlin
val navHostFragment = supportFragmentManager
    .findFragmentById(R.id.nav_host_fragment) as NavHostFragment
val navController = navHostFragment.navController

// Connect bottom nav to navigation
binding.bottomNav.setupWithNavController(navController)

// Or for manual handling:
binding.bottomNav.setOnItemSelectedListener { item ->
    NavigationUI.onNavDestinationSelected(item, navController)
}
```

<!-- Menu IDs must match nav graph destination IDs -->
<menu>
    <item android:id="@+id/homeFragment" android:title="Home" />
    <item android:id="@+id/searchFragment" android:title="Search" />
    <item android:id="@+id/profileFragment" android:title="Profile" />
</menu>
