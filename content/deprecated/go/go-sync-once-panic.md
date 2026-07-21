---
title: "[Solution] Deprecated Function Migration: sync.Once with panic recovery to error returns"
description: "Migrate from deprecated panic in sync.Once to error returns."
deprecated_function: "once.Do(func() { panic(...) })"
replacement_function: "Error return pattern"
languages: ["go"]
deprecated_since: "Go 1.0+"
---

# [Solution] Deprecated Function Migration: sync.Once with panic recovery to error returns

The `once.Do(func() { panic(...) })` has been deprecated in favor of `Error return pattern`.

## Migration Guide

Panic in sync.Once is unrecoverable

If sync.Once panics, subsequent calls are blocked. Use error returns instead.

## Before (Deprecated)

```go
var once sync.Once
var config *Config

func loadConfig() {
    once.Do(func() {
        c, err := readConfig()
        if err != nil {
            panic(err)  // blocks all future calls!
        }
        config = c
    })
}
```

## After (Modern)

```go
var once sync.Once
var config *Config
var loadErr error

func loadConfig() error {
    once.Do(func() {
        c, err := readConfig()
        if err != nil {
            loadErr = err
            return
        }
        config = c
    })
    return loadErr
}
```

## Key Differences

- Panic in sync.Once is permanent
- Error return is recoverable
- Store error for later inspection
- Callers can handle the error
