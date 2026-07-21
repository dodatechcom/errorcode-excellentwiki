---
title: "ViewModel Process Death Error"
description: "Fix ViewModel data loss during process death and app backgrounding"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ViewModel data is lost when app is killed in background and restored

## Common Causes

- State not saved in SavedStateHandle
- Using StateFlow without process death support
- In-memory cache lost on process kill
- Room database data not restored properly

## Fixes

- Use SavedStateHandle for critical state
- Persist important data to database or SharedPreferences
- Use LiveData with SavedStateHandle for auto-restore
- Check for restored state in ViewModel init

## Code Example

```kotlin
class MyViewModel(
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    val query = savedStateHandle.getLiveData<String>("query", "")

    fun saveQuery(q: String) {
        savedStateHandle["query"] = q
    }

    val items: StateFlow<List<Item>> = savedStateHandle
        .getLiveData<List<Item>>("items", emptyList())
        .asFlow()
}
```

# SavedStateHandle survives process death
# Room data persists across process death
# In-memory caches do NOT survive process death
