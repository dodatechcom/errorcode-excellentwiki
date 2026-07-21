---
title: "DataStore Corruption Error"
description: "Fix DataStore file corruption and data loss errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DataStore data is lost or corrupted on app startup or after crash

## Common Causes

- DataStore file corrupted by concurrent writes
- Process death during write operation
- Proto DataStore schema migration missing
- DataStore not handling corruption gracefully

## Fixes

- Handle corruption in DataStore initializer
- Use runCatching for safe data access
- Provide default values for Proto DataStore
- Use DataStore migration from SharedPreferences

## Code Example

```kotlin
// Handle corruption:
val Context.settingsDataStore by dataStore(
    fileName = "settings.pb",
    serializer = SettingsSerializer,
    corruptionHandler = ReplaceFileExceptionHandler(
        Settings.getDefaultInstance()
    )
)

// Migration from SharedPreferences:
val Context.dataStore by dataStore(
    fileName = "settings.pb",
    serializer = SettingsSerializer,
    produceMigrations = { context ->
        listOf(sharedPreferencesMigration(context, "prefs_name"))
    }
)
```

# DataStore handles corruption automatically
# Provide defaultValue for Proto DataStore
# Use migration for SharedPreferences transition
