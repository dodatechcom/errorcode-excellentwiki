---
title: "[Solution] Deprecated Function Migration: SharedPreferences to DataStore"
description: "Migrate from deprecated SharedPreferences to DataStore."
deprecated_function: "SharedPreferences"
replacement_function: "DataStore"
languages: ["android"]
deprecated_since: "AndroidX DataStore"
---

# [Solution] Deprecated Function Migration: SharedPreferences to DataStore

The `SharedPreferences` has been deprecated in favor of `DataStore`.

## Migration Guide

DataStore is async and type-safe.

## Before (Deprecated)

```android
val prefs = getSharedPreferences("name", MODE_PRIVATE)
prefs.edit().putString("key", "value").apply()
```

## After (Modern)

```android
val dataStore = context.createDataStore(name = "prefs")
suspend fun save(key: String, value: String) {
    dataStore.edit { it[stringPreferencesKey(key)] = value }
}
```

## Key Differences

- DataStore is async and type-safe
