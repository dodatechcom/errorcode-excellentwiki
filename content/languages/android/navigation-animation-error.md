---
title: "Navigation Animation Error"
description: "Fix Navigation component enter/exit animation configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Fragment transitions do not animate correctly with Navigation component

## Common Causes

- Animation resource not found
- Animation defined in wrong resource directory
- NavOptions animation not applied
- Shared element transition not working

## Fixes

- Define animations in res/anim/ directory
- Use navOptions with anim builder
- Configure shared element with sharedElement parameters
- Test animations on real device

## Code Example

```kotlin
// Navigation with animations:
val action = HomeFragmentDirections.actionHomeToDetail(itemId)
val navOptions = navOptions {
    anim {
        enter = R.anim.slide_in_right
        exit = R.anim.slide_out_left
        popEnter = R.anim.slide_in_left
        popExit = R.anim.slide_out_right
    }
}
findNavController().navigate(action, navOptions)

// res/anim/slide_in_right.xml:
<set xmlns:android="http://schemas.android.com/apk/res/android">
    <translate android:fromXDelta="100%" android:toXDelta="0%"
        android:duration="300" />
</set>
```

# Animations in res/anim/ directory
# enter: new fragment entering
# exit: old fragment leaving
# popEnter/popExit: back navigation
