---
title: "Paging Library Error"
description: "Fix Android Paging 3 library errors for infinite scroll lists"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Paging 3 library fails to load pages or displays incorrect data

## Common Causes

- PagingSource not properly implemented
- Pager not configured with correct PagingConfig
- LoadResult not returning correct page data
- PagingData not collected properly in UI

## Fixes

- Implement PagingSource with load() method
- Configure PagingConfig with pageSize
- Return LoadResult.Page with correct data and prevKey/nextKey
- Collect pagingData in lifecycle scope

## Code Example

```kotlin
class MyPagingSource(private val api: ApiService) : PagingSource<Int, Item>() {
    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, Item> {
        val page = params.key ?: 1
        return try {
            val response = api.getItems(page, params.loadSize)
            LoadResult.Page(
                data = response.items,
                prevKey = if (page == 1) null else page - 1,
                nextKey = if (response.items.isEmpty()) null else page + 1
            )
        } catch (e: Exception) {
            LoadResult.Error(e)
        }
    }

    override fun getRefreshKey(state: PagingState<Int, Item>): Int? {
        return state.anchorPosition?.let { state.closestPageToPosition(it)?.prevKey?.plus(1) }
    }
}

// In ViewModel:
val pager = Pager(PagingConfig(pageSize = 20)) {
    MyPagingSource(api)
}.flow.cachedIn(viewModelScope)
```

# Paging 3 components:
# PagingSource: loads data
# Pager: creates Flow<PagingData>
# PagingDataAdapter: displays in RecyclerView
# collectAsLazyPagingItems() for Compose
