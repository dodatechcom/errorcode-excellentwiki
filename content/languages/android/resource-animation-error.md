---
title: "Resource Animation Error"
description: "Fix Android resource animation errors in anim and animator XML files"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Animation XML resource fails to load or throws inflate exception

## Common Causes

- Animation XML has invalid tag or attribute
- Referenced property does not exist on target view
- Animation duration not specified
- Missing xmlns declaration for custom attributes

## Fixes

- Use correct animation root tag: set, objectAnimator, or animator
- Verify target property name matches view setter
- Set android:duration on all animations
- Add required xmlns declarations

## Code Example

```kotlin
<!-- res/anim/fade_in.xml -->
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android"
     android:duration="300">
    <alpha
        android:fromAlpha="0.0"
        android:toAlpha="1.0"
        android:interpolator="@android:anim/decelerate_interpolator" />
</set>
```

# Load animation
val fadeIn = AnimationUtils.loadAnimation(this, R.anim.fade_in)
view.startAnimation(fadein)
