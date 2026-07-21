---
title: "DataStore Transaction Error"
description: "Fix DataStore transaction and atomic update errors in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DataStore updates are lost or overwritten because of transaction conflicts

## Common Causes

- Multiple coroutines updating same DataStore simultaneously
- edit() transaction not atomic
- State not properly updated after transaction
- Transaction blocked by slow read

## Fixes

- Use edit() for atomic updates
- Update DataStore from single coroutine
- Use data.first() to read current value
- Handle concurrent access with Mutex

## Code Example

```kotlin
// CORRECT: atomic edit
suspend fun updateUsername(newName: String) {
    context.dataStore.edit { prefs ->
        prefs[PreferencesKeys.USERNAME] = newName
    }
}

// Read and update:
suspend fun incrementCounter() {
    context.dataStore.edit { prefs ->
        val current = prefs[COUNTER_KEY] ?: 0
        prefs[COUNTER_KEY] = current + 1
    }
}
```

# edit() is atomic - all or nothing
# Multiple edits may overwrite each other
# Use single coroutine for sequential updates
