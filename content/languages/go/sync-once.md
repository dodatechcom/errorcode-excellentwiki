---
title: "[Solution] Go sync: once.Do called twice — Concurrency Error Fix"
description: "Fix Go sync.Once usage error."
languages: ["go"]
error-types: ["concurrency-error"]
severities: ["error"]
weight: 5
---

# sync: once.Do called twice

`sync.Once` is designed to execute a function exactly once. Calling it multiple times is fine, but the function only runs once.

## How to Fix

```go
var once sync.Once
var config *Config

func GetConfig() *Config {
    once.Do(func() {
        config = loadConfig()
    })
    return config
}
```

## Related Errors

- [sync-mutex]({{< relref "/languages/go/sync-mutex" >}}) — mutex deadlock.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked.
