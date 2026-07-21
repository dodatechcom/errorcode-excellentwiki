---
title: "[Solution] Deprecated Function Migration: verbose nil checks to errors.Is/As"
description: "Migrate from deprecated error comparison to errors.Is and errors.As in Go."
deprecated_function: "err == ErrNotFound"
replacement_function: "errors.Is(err, ErrNotFound)"
languages: ["go"]
deprecated_since: "Go 1.13+"
---

# [Solution] Deprecated Function Migration: verbose nil checks to errors.Is/As

The `err == ErrNotFound` has been deprecated in favor of `errors.Is(err, ErrNotFound)`.

## Migration Guide

errors.Is and errors.As properly unwrap error chains for comparison.

## Before (Deprecated)

```go
if err == ErrNotFound {
    fmt.Println("not found")
}

if err == os.ErrNotExist {
    fmt.Println("file not found")
}
```

## After (Modern)

```go
if errors.Is(err, ErrNotFound) {
    fmt.Println("not found")
}

if errors.Is(err, os.ErrNotExist) {
    fmt.Println("file not found")
}

var pathErr *os.PathError
if errors.As(err, &pathErr) {
    fmt.Println("path:", pathErr.Path)
}
```

## Key Differences

- errors.Is unwraps error chains
- errors.As finds specific error types
- Direct == does not unwrap errors
- Use errors.Is for sentinel errors
