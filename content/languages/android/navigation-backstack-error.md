---
title: "Navigation Back Stack Error"
description: "Fix Android Navigation back stack management and popUpTo errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Navigation back stack behaves unexpectedly with popUpTo and popUpToInclusive

## Common Causes

- popUpTo not removing destinations as expected
- Back button returns to wrong screen
- popUpToInclusive removes start destination
- Multiple back stack entries for same destination

## Fixes

- Verify popUpTo destination ID is correct
- Use popUpToInclusive=true to remove destination entirely
- Use launchSingleTop to avoid duplicate entries
- Configure popUpTo in XML action or programmatically

## Code Example

```kotlin
<!-- XML action with popUpTo -->
<action
    android:id="@+id/action_detail_to_home"
    app:destination="@id/homeFragment"
    app:popUpTo="@id/homeFragment"
    app:popUpToInclusive="true" />

// Programmatic navigation:
navController.navigate(R.id.detailFragment, null,
    navOptions {
        popUpTo(R.id.homeFragment) {
            inclusive = true
        }
        launchSingleTop = true
    })
```

# popUpTo removes destinations from back stack
# popUpToInclusive=true removes the destination itself
# launchSingleTop prevents duplicate entries
