---
title: "[Solution] Deprecated Function Migration: sync.Once with init to sync.OnceFunc"
description: "Migrate from deprecated sync.Once pattern to sync.OnceFunc."
deprecated_function: "var once sync.Once
once.Do(func() { })"
replacement_function: "sync.OnceFunc(func() { })"
languages: ["go"]
deprecated_since: "Go 1.21+"
---

# [Solution] Deprecated Function Migration: sync.Once with init to sync.OnceFunc

The `var once sync.Once
once.Do(func() { })` has been deprecated in favor of `sync.OnceFunc(func() { })`.

## Migration Guide

sync.OnceFunc is simpler.

## Before (Deprecated)

```go
var once sync.Once
func init() {
    once.Do(func() {
        // init
    })
}
```

## After (Modern)

```go
var initOnce = sync.OnceFunc(func() {
    // init
})
```

## Key Differences

- sync.OnceFunc is simpler
