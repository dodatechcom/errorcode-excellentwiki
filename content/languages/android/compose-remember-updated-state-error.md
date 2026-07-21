---
title: "RememberUpdatedState Error"
description: "Fix Compose rememberUpdatedState and stale reference errors in long-running effects"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Long-running composable effects use stale values from initial composition

## Common Causes

- Lambda capturing stale value from first composition
- Timer or animation using old callback
- Effect not updating when parameters change
- rememberUpdatedState not being used

## Fixes

- Use rememberUpdatedState for changing values in effects
- Add dependency keys to effects that should restart
- Use lambda with rememberUpdatedState for callbacks
- Verify effect re-runs when expected

## Code Example

```kotlin
@Composable
fun Timer(onTimeout: () -> Unit) {
    val currentOnTimeout by rememberUpdatedState(onTimeout)

    LaunchedEffect(Unit) {
        delay(5000)
        currentOnTimeout()  // Uses latest onTimeout, not initial
    }
}

// Without rememberUpdatedState, onTimeout would be stale!
// With:
@Composable
fun LocationTracker(onLocation: (Location) -> Unit) {
    val currentOnLocation by rememberUpdatedState(onLocation)

    DisposableEffect(Unit) {
        val callback = object : LocationCallback() {
            override fun onResult(result: LocationResult) {
                result.lastLocation?.let { currentOnLocation(it) }
            }
        }
        // ... register callback
        onDispose { /* cleanup */ }
    }
}
```

# rememberUpdatedState: keep value fresh in long effects
# Use for callbacks in LaunchedEffect/DisposableEffect
# Prevents stale lambda captures
