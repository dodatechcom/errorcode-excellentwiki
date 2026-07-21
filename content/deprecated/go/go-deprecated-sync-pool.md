---
title: "[Solution] Deprecated Function Migration: manual pooling to sync.Pool"
description: "Migrate from deprecated manual object pooling to sync.Pool."
deprecated_function: "Manual channel-based pooling"
replacement_function: "sync.Pool"
languages: ["go"]
deprecated_since: "Go 1.3+"
---

# [Solution] Deprecated Function Migration: manual pooling to sync.Pool

The `Manual channel-based pooling` has been deprecated in favor of `sync.Pool`.

## Migration Guide

sync.Pool handles pooling automatically.

## Before (Deprecated)

```go
pool := make(chan *Object, 100)
go func() {
    for i := 0; i < 100; i++ {
        pool <- newObject()
    }
}()
```

## After (Modern)

```go
var pool = sync.Pool{
    New: func() interface{} {
        return newObject()
    },
}
obj := pool.Get().(*Object)
pool.Put(obj)
```

## Key Differences

- sync.Pool manages object reuse
