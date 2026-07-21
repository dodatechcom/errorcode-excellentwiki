---
title: "Firebase App Check Error"
description: "Fix Firebase App Check configuration and attestation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Firebase App Check prevents API calls because attestation fails

## Common Causes

- App Check not properly initialized
- Device not passing attestation
- Play Integrity or SafetyNet not configured
- APIs not protected by App Check

## Fixes

- Initialize App Check with appropriate provider
- Verify app signing is configured correctly
- Test with debug provider in development
- Enable App Check enforcement on Firebase APIs

## Code Example

```kotlin
// Initialize App Check
val appCheck = FirebaseAppCheck.getInstance()
appCheck.installAppCheckProviderFactory(
    PlayIntegrityAppCheckProviderFactory.getInstance()
)

// For debug builds:
if (BuildConfig.DEBUG) {
    appCheck.installAppCheckProviderFactory(
        DebugAppCheckProviderFactory.getInstance()
    )
}

// Verify App Check token:
val token = FirebaseAppCheck.getInstance().getToken(false)
token.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        Log.d("AppCheck", "Token: ${task.result?.token}")
    }
}
```

# Play Integrity: production attestation
# SafetyNet: legacy attestation (deprecated)
# Debug provider: development testing
# Enable enforcement in Firebase console
