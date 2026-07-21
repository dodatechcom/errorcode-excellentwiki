---
title: "Room Paging Integration Error"
description: "Fix Room and Paging 3 integration errors for paginated database queries"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Room database queries do not paginate correctly with Paging 3 library

## Common Causes

- PagingSource not returning correct page data
- Room query not returning PagingSource
- PagingConfig not configured with Room
- InvalidationTracker not triggering refresh

## Fixes

- Return PagingSource from Room query
- Use PagingConfig with appropriate pageSize
- Room automatically invalidates on data changes
- Use cachedIn for sharing paging data

## Code Example

```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM users ORDER BY name")
    fun getUsersPagingSource(): PagingSource<Int, User>
}

// In ViewModel:
val usersPager = Pager(
    config = PagingConfig(pageSize = 20, enablePlaceholders = false)
) {
    userDao.getUsersPagingSource()
}.flow.cachedIn(viewModelScope)

// In Compose:
val lazyPagingItems = usersPager.collectAsLazyPagingItems()
```

# Room returns PagingSource directly
# Pager creates Flow<PagingData>
# cachedIn(viewModelScope) shares data
