---
title: "SharedPreferences Thread Error"
description: "Fix SharedPreferences threading errors and ANR from disk I/O"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App shows ANR because SharedPreferences writes block main thread

## Common Causes

- commit() called on main thread causing blocking I/O
- Large data written to SharedPreferences on UI thread
- Multiple rapid writes causing disk thrashing
- apply() callback blocking main thread

## Fixes

- Use apply() instead of commit() for async writes
- Move large data to DataStore or Room
- Batch writes to reduce disk I/O
- Never call commit() on main thread

## Code Example

```kotlin
// WRONG: blocks main thread
val editor = sharedPreferences.edit()
editor.putString("key", "value")
editor.commit()  // Returns boolean, blocks!

// CORRECT: async write
val editor = sharedPreferences.edit()
editor.putString("key", "value")
editor.apply()  // Fire and forget

// With callback (API 11+):
editor.apply()
    .registerOnApplicationCallbacks(object : SharedPreferences.OnSharedPreferenceChangeListener {
        override fun onSharedPreferenceChanged(prefs: SharedPreferences?, key: String?) {
            Log.d("Prefs", "$key updated")
        }
    })
```

# apply() - async, no return value
# commit() - synchronous, returns boolean
# Use DataStore for modern replacement
# ANR threshold: 5 seconds on main thread
