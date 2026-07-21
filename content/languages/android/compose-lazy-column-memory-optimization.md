---
title: "LazyColumn Memory Error"
description: "Fix LazyColumn memory usage and prevent out-of-memory errors with large lists"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn causes out-of-memory errors when displaying large datasets

## Common Causes

- Memory usage growing with scroll position
- Images not being recycled from memory
- Large dataset causing OOM crash
- LazyColumn holding references to off-screen items

## Fixes

- Use key for proper item recycling
- Implement image caching with Coil
- Paginate data instead of loading all at once
- Use Paging library for large datasets

## Code Example

```kotlin
// Use Paging 3 for large datasets
val items: Flow<PagingData<Item>> = pager.flow

LazyColumn {
    items(items) { item -> ItemRow(item) }
}

// Or paginate manually:
LaunchedEffect(Unit) { viewModel.loadMore() }
```

# Paging 3 for automatic pagination# Coil for image caching and recycling# key for proper item identity# Paginate data loading
