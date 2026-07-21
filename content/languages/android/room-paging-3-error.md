---
title: "Room Paging 3 Invalidation Error"
description: "Fix Room and Paging 3 integration with invalidation tracker errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Paging 3 with Room does not refresh when data changes

## Common Causes

- InvalidationTracker not monitoring correct table
- PagingSource not invalidated on data change
- cachedIn not properly configured
- PagingConfig.pageSize too large

## Fixes

- Room automatically invalidates on table changes
- Ensure PagingSource returns correct type
- Use cachedIn(viewModelScope) for sharing
- Set appropriate pageSize in PagingConfig

## Code Example

```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM users ORDER BY created_at DESC")
    fun getAllUsersPaged(): PagingSource<Int, User>
}

// In ViewModel:
val usersPager = Pager(
    config = PagingConfig(
        pageSize = 20,
        enablePlaceholders = false,
        prefetchDistance = 5
    )
) {
    userDao.getAllUsersPaged()
}.flow.cachedIn(viewModelScope)

// In Compose:
val lazyItems = usersPager.collectAsLazyPagingItems()
```

# Room PagingSource auto-invalidates on data change
# cachedIn shares paging data across collectors
# pageSize: items per page
# prefetchDistance: how far ahead to prefetch
