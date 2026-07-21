---
title: "[Solution] Deprecated Function Migration: sort.Sort to slices.Sort"
description: "Migrate from deprecated sort.Sort to slices.Sort."
deprecated_function: "sort.Sort(Sortable(data))"
replacement_function: "slices.Sort(data)"
languages: ["go"]
deprecated_since: "Go 1.21+"
---

# [Solution] Deprecated Function Migration: sort.Sort to slices.Sort

The `sort.Sort(Sortable(data))` has been deprecated in favor of `slices.Sort(data)`.

## Migration Guide

slices.Sort is simpler.

## Before (Deprecated)

```go
type ByName []User
func (a ByName) Len() int { return len(a) }
```

## After (Modern)

```go
import "slices"
slices.SortFunc(users, func(a, b User) int {
    return cmp.Compare(a.Name, b.Name)
})
```

## Key Differences

- slices.SortFunc is simpler
