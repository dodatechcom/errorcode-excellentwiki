---
title: "[Solution] Deprecated Function Migration: sort.Reverse to slices.SortFunc"
description: "Migrate from deprecated sort.Reverse to slices.SortFunc."
deprecated_function: "sort.Reverse(data)"
replacement_function: "slices.SortFunc(data, reverse)"
languages: ["go"]
deprecated_since: "Go 1.21+"
---

# [Solution] Deprecated Function Migration: sort.Reverse to slices.SortFunc

The `sort.Reverse(data)` has been deprecated in favor of `slices.SortFunc(data, reverse)`.

## Migration Guide

slices.SortFunc is more flexible.

## Before (Deprecated)

```go
sort.Reverse(sort.IntSlice(data))
```

## After (Modern)

```go
slices.SortFunc(data, func(a, b int) int {
    return cmp.Compare(b, a)
})
```

## Key Differences

- slices.SortFunc is more flexible
