---
title: "[Solution] Deprecated Function Migration: manual type assertion to type switch"
description: "Migrate from verbose type assertions to type switch in Go."
deprecated_function: "x.(Type) with ok check"
replacement_function: "switch v := x.(type)"
languages: ["go"]
deprecated_since: "Go 1.0+"
---

# [Solution] Deprecated Function Migration: manual type assertion to type switch

The `x.(Type) with ok check` has been deprecated in favor of `switch v := x.(type)`.

## Migration Guide

Type switch provides cleaner syntax for multiple type checks.

## Before (Deprecated)

```go
func process(x interface{}) {
    if s, ok := x.(string); ok {
        fmt.Println("String:", s)
    } else if i, ok := x.(int); ok {
        fmt.Println("Int:", i)
    }
}
```

## After (Modern)

```go
func process(x interface{}) {
    switch v := x.(type) {
    case string:
        fmt.Println("String:", v)
    case int:
        fmt.Println("Int:", v)
    default:
        fmt.Println("Unknown type")
    }
}
```

## Key Differences

- Type switch uses comma-ok pattern
- Variable v is the typed value
- Cleaner than multiple if-else chains
