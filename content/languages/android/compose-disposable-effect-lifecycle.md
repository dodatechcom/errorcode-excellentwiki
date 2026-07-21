---
title: "DisposableEffect Lifecycle Error"
description: "Fix DisposableEffect lifecycle integration errors in Compose"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DisposableEffect not properly tied to lifecycle causing leaks

## Common Causes

- DisposableEffect running in wrong lifecycle state
- onDispose not called when expected
- DisposableEffect key not triggering re-setup
- Resource not properly cleaned up

## Fixes

- Use viewLifecycleOwner in Fragments for DisposableEffect
- Always implement onDispose for cleanup
- Use correct key to trigger re-setup
- Clean up all resources in onDispose

## Code Example

```kotlin
@Composable
fun LocationUpdates() {
    val context = LocalContext.current
    val lifecycleOwner = LocalLifecycleOwner.current

    DisposableEffect(lifecycleOwner) {
        val locationClient = LocationServices.getFusedLocationProviderClient(context)
        val callback = object : LocationCallback() {
            override fun onResult(result: LocationResult) { /* handle */ }
        }

        lifecycleOwner.lifecycle.addObserver(object : DefaultLifecycleObserver {
            override fun onStart(owner: LifecycleOwner) {
                locationClient.requestLocationUpdates(locationRequest, callback, Looper.getMainLooper())
            }
            override fun onStop(owner: LifecycleOwner) {
                locationClient.removeLocationUpdates(callback)
            }
        })

        onDispose {
            locationClient.removeLocationUpdates(callback)
        }
    }
}
```

# DisposableEffect: side effect with cleanup
# onDispose: called when leaving composition or key changes
# Use with lifecycleOwner for lifecycle-aware effects
