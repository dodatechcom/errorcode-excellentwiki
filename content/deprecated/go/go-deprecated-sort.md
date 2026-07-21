---
title: "[Solution] Deprecated Function Migration: sort.Slice to slices.SortFunc"
description: "Migrate from deprecated sort.Slice to slices.SortFunc."
deprecated_function: "sort.Slice(s, func(i, j int) bool { })"
replacement_function: "slices.SortFunc(s, func(a, b T) int { })"
languages: ["go"]
deprecated_since: "Go 1.21+"
---

# [Solution] Deprecated Function Migration: sort.Slice to slices.SortFunc

The `sort.Slice(s, func(i, j int) bool { })` has been deprecated in favor of `slices.SortFunc(s, func(a, b T) int { })`.

## Migration Guide

slices.SortFunc uses comparison function

sort.Slice uses a boolean less function.

## Before (Deprecated)

```go
sort.Slice(users, func(i, j int) bool {
    return users[i].Name < users[j].Name
})
```

## After (Modern)

```go
import "slices"
import "cmp"
slices.SortFunc(users, func(a, b User) int {
    return cmp.Compare(a.Name, b.Name)
})
```

## Key Differences

- slices.SortFunc uses comparison function
- cmp.Compare for natural ordering
