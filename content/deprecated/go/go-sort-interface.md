---
title: "[Solution] Deprecated Function Migration: sort.Interface to slices.SortFunc"
description: "Migrate from deprecated sort.Interface to slices.SortFunc in Go."
deprecated_function: "sort.Interface (Len, Less, Swap)"
replacement_function: "slices.SortFunc()"
languages: ["go"]
deprecated_since: "Go 1.21+"
---

# [Solution] Deprecated Function Migration: sort.Interface to slices.SortFunc

The `sort.Interface (Len, Less, Swap)` has been deprecated in favor of `slices.SortFunc()`.

## Migration Guide

slices.SortFunc is more concise than implementing the sort.Interface.

## Before (Deprecated)

```go
type ByName []User

func (u ByName) Len() int           { return len(u) }
func (u ByName) Less(i, j int) bool { return u[i].Name < u[j].Name }
func (u ByName) Swap(i, j int)      { u[i], u[j] = u[j], u[i] }

sort.Sort(ByName(users))
```

## After (Modern)

```go
import "slices"

slices.SortFunc(users, func(a, b User) int {
    return cmp.Compare(a.Name, b.Name)
})
```

## Key Differences

- No need to implement 3 methods
- SortFunc takes a comparison function
- More concise and less boilerplate
- Uses cmp.Compare for natural ordering
