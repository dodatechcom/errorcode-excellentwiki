---
title: "Remote Config Latest Value Error"
description: "Fix Firebase Remote Config latest value and real-time update errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Remote Config does not return latest values after activation

## Common Causes

- Fetch not called before activate
- Caching returning stale values
- Default values overriding fetched values
- Real-time listener not configured for updates

## Fixes

- Call fetchAndActivate() to get latest values
- Use clear() to reset cache
- Verify defaults are not overriding
- Add configUpdateListener for real-time updates

## Code Example

```kotlin
val remoteConfig = Firebase.remoteConfig

// Fetch and activate
remoteConfig.fetchAndActivate()
    .addOnSuccessListener { activated ->
        val value = remoteConfig.getString("feature_flag")
    }

// Real-time updates (new in Firebase 21+)
remoteConfig.addOnConfigUpdateListener(object : ConfigUpdateListener {
    override fun onUpdate(configUpdate: ConfigUpdate) {
        remoteConfig.activate().addOnCompleteListener {
            // Values updated
        }
    }
    override fun onError(error: FirebaseRemoteConfigException) {
        Log.e("Config", "Update error", error)
    }
})
```

# fetchAndActivate: fetch and apply
# activate: apply previously fetched values
# addOnConfigUpdateListener: real-time updates
