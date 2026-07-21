---
title: "Data Storage Security Error"
description: "Fix Android data storage security errors for sensitive information"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Sensitive data stored insecurely causing potential security vulnerabilities

## Common Causes

- Storing passwords in SharedPreferences plain text
- Logging sensitive data in production
- Caching sensitive data in external storage
- Using MODE_WORLD_READABLE for files

## Fixes

- Use EncryptedSharedPreferences for sensitive data
- Never log sensitive data in release builds
- Store sensitive data only in internal storage
- Use MODE_PRIVATE for all file operations

## Code Example

```kotlin
// EncryptedSharedPreferences
val masterKey = MasterKey.Builder(context)
    .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
    .build()

val encryptedPrefs = EncryptedSharedPreferences.create(
    context,
    "secret_prefs",
    masterKey,
    PrefKeyEncryptionScheme.AES256_SIV,
    PrefValueEncryptionScheme.AES256_GCM
)

encryptedPrefs.edit().putString("token", secretToken).apply()
```

# Never store passwords in SharedPreferences
# Use EncryptedSharedPreferences for tokens
# Use Android Keystore for cryptographic keys
# Use biometric prompt for user authentication
