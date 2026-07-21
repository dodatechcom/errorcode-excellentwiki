---
title: "DataStore Migration Error"
description: "Fix DataStore migration from SharedPreferences with data loss prevention"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DataStore migration loses data or creates duplicate entries

## Common Causes

- SharedPreferences keys not mapped correctly
- Data type conversion during migration failing
- Migration not running on first launch
- Old SharedPreferences file not cleaned up

## Fixes

- Map all SharedPreferences keys to DataStore keys
- Handle type conversion carefully
- Use produceMigrations for automatic migration
- Clean up old SharedPreferences after migration

## Code Example

```kotlin
// Automatic migration from SharedPreferences
val Context.myDataStore by dataStore(
    fileName = "settings.pb",
    serializer = SettingsSerializer,
    produceMigrations = { context ->
        listOf(
            sharedPreferencesMigration(context, "old_prefs_name")
        )
    }
)

// Manual migration:
suspend fun migrateFromPrefs(prefs: SharedPreferences, dataStore: DataStore<Settings>) {
    dataStore.edit { settings ->
        settings[USERNAME] = prefs.getString("username", "") ?: ""
        settings[DARK_MODE] = prefs.getBoolean("dark_mode", false)
    }
    prefs.edit().clear().apply()  // Clean up old prefs
}
```

# sharedPreferencesMigration: automatic migration
# Map old keys to new keys carefully
# Test migration with real data
