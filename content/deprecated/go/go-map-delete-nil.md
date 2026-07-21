---
title: "[Solution] Deprecated Function Migration: delete on nil map to pre-initialization"
description: "Migrate from deprecated delete on nil map to map pre-initialization."
deprecated_function: "delete(nilMap, key)"
replacement_function: "make(map[K]V)"
languages: ["go"]
deprecated_since: "Go 1.0+"
---

# [Solution] Deprecated Function Migration: delete on nil map to pre-initialization

The `delete(nilMap, key)` has been deprecated in favor of `make(map[K]V)`.

## Migration Guide

delete on nil map panics; pre-initialize maps

delete on a nil map panics in Go. Always initialize maps before use.

## Before (Deprecated)

```go
var m map[string]int
delete(m, "key")  // panic!
```

## After (Modern)

```go
m := make(map[string]int)
m["key"] = 1
delete(m, "key")  // works

// Or initialize with make
m := make(map[string]int, 10)  // with capacity hint
```

## Key Differences

- delete on nil map panics
- Always initialize maps with make
- make with capacity hint for known size
- Check for nil before operations
