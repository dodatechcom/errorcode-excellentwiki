---
title: "Preferences DataStore Error"
description: "Fix Preferences DataStore key management and type safety errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Preferences DataStore returns wrong types or fails to read/write values

## Common Causes

- Key type mismatch between read and write
- Default value not provided for missing keys
- DataStore not properly initialized
- Preferences not persisting after app restart

## Fixes

- Ensure key types match: intPreferencesKey, stringPreferencesKey
- Provide default values with ?: operator
- Initialize DataStore as extension property
- Use data.first() for one-time reads

## Code Example

```kotlin
// Define keys
object PrefsKeys {
    val DARK_MODE = booleanPreferencesKey("dark_mode")
    val USERNAME = stringPreferencesKey("username")
    val FONT_SIZE = intPreferencesKey("font_size")
}

// Read with default:
val darkMode: Flow<Boolean> = context.dataStore.data
    .map { prefs -> prefs[PrefsKeys.DARK_MODE] ?: false }

// Read one-time:
val currentName = context.dataStore.data.first()[PrefsKeys.USERNAME] ?: ""

// Write:
suspend fun setDarkMode(enabled: Boolean) {
    context.dataStore.edit { prefs ->
        prefs[PrefsKeys.DARK_MODE] = enabled
    }
}
```

# Boolean, Int, Long, Float, String, StringSet
# Always provide default with ?: operator
# edit() is atomic and thread-safe
