---
title: "[Solution] Deprecated Function Migration: manual slice growth to slices.Grow"
description: "Migrate from deprecated manual slice capacity management to slices.Grow in Go."
deprecated_function: "make([]T, 0, n)"
replacement_function: "slices.Grow(s, n)"
languages: ["go"]
deprecated_since: "Go 1.21+"
---

# [Solution] Deprecated Function Migration: manual slice growth to slices.Grow

The `make([]T, 0, n)` has been deprecated in favor of `slices.Grow(s, n)`.

## Migration Guide

slices.Grow pre-allocates capacity for a slice, making append operations more efficient.

## Before (Deprecated)

```go
result := make([]int, 0, len(input))
for _, v := range input {
    if v > 0 {
        result = append(result, v)
    }
}
```

## After (Modern)

```go
import "slices"

result := slices.Grow([]int{}, len(input))
for _, v := range input {
    if v > 0 {
        result = append(result, v)
    }
}
```

## Key Differences

- slices.Grow pre-allocates capacity
- Cleaner than make with capacity
- Available in slices package (Go 1.21+)
