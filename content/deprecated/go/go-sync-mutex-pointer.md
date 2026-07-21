---
title: "[Solution] Deprecated Function Migration: sync.Mutex value to pointer receiver"
description: "Migrate from deprecated sync.Mutex value semantics to pointer receiver."
deprecated_function: "func (m SafeMap) Get()"
replacement_function: "func (m *SafeMap) Get()"
languages: ["go"]
deprecated_since: "Go 1.0+"
---

# [Solution] Deprecated Function Migration: sync.Mutex value to pointer receiver

The `func (m SafeMap) Get()` has been deprecated in favor of `func (m *SafeMap) Get()`.

## Migration Guide

Mutex must not be copied after first use

sync.Mutex must not be copied.

## Before (Deprecated)

```go
func (m SafeMap) Get(key string) string {
    m.mu.Lock()
    defer m.mu.Unlock()
    return m.data[key]
}
```

## After (Modern)

```go
func (m *SafeMap) Get(key string) string {
    m.mu.Lock()
    defer m.mu.Unlock()
    return m.data[key]
}
```

## Key Differences

- Mutex must not be copied
- Use pointer receiver
