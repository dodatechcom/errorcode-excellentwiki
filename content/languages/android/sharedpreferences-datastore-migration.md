---
title: "SharedPreferences to DataStore Migration"
description: "Migrate from SharedPreferences to DataStore for modern Android development"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App uses legacy SharedPreferences and needs migration to DataStore

## Common Causes

- SharedPreferences type-unsafe
- No error handling for data corruption
- Does not support coroutine/Flow natively
- Performance issues with large data sets

## Fixes

- Migrate to Preferences DataStore for simple key-value
- Migrate to Proto DataStore for typed objects
- Use dataStore extension property on Context
- Handle migration from SharedPreferences to DataStore

## Code Example

```kotlin
// Preferences DataStore (simple key-value)
val Context.dataStore by preferencesDataStore(name = "settings")

// Define keys
object PreferencesKeys {
    val DARK_MODE = booleanPreferencesKey("dark_mode")
    val USERNAME = stringPreferencesKey("username")
}

// Read
val darkMode: Flow<Boolean> = context.dataStore.data
    .map { prefs -> prefs[PreferencesKeys.DARK_MODE] ?: false }

// Write
suspend fun setDarkMode(enabled: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[PreferencesKeys.DARK_MODE] = enabled
    }
}
```

# DataStore advantages over SharedPreferences:
# - Thread-safe with coroutines
# - Type-safe with Proto DataStore
# - Rollback on corruption
# - No ANR risk
