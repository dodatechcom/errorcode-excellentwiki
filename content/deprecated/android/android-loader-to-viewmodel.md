---
title: "[Solution] Deprecated Function Migration: Loader to ViewModel + Repository"
description: "Migrate from deprecated Loader API to ViewModel with Repository pattern."
deprecated_function: "CursorLoader / AsyncTaskLoader"
replacement_function: "ViewModel + Repository"
languages: ["kotlin"]
deprecated_since: "Architecture Components"
---

# [Solution] Deprecated Function Migration: Loader to ViewModel + Repository

The `CursorLoader / AsyncTaskLoader` has been deprecated in favor of `ViewModel + Repository`.

## Migration Guide

Loaders are lifecycle-unaware. ViewModel + Repository provides lifecycle-aware data loading.

## Before (Deprecated)

```kotlin
public class MyLoader extends AsyncTaskLoader<List<Item>> {
    public MyLoader(Context context) { super(context); }
    @Override
    public List<Item> loadInBackground() {
        return database.getItems();
    }
}
getLoaderManager().initLoader(0, null, this);
```

## After (Modern)

```kotlin
class ItemRepository(private val db: AppDatabase) {
    suspend fun getItems(): List<Item> = db.itemDao().getAll()
}

class ItemViewModel(private val repo: ItemRepository) : ViewModel() {
    private val _items = MutableStateFlow<List<Item>>(emptyList())
    val items: StateFlow<List<Item>> = _items

    fun loadItems() {
        viewModelScope.launch {
            _items.value = repo.getItems()
        }
    }
}
```

## Key Differences

- ViewModel survives configuration changes
- Repository abstracts data sources
- Flow/LiveData for lifecycle-aware updates
- Coroutines for async operations
