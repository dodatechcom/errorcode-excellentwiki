---
title: "[Solution] Deprecated Function Migration: manual goroutine sync to sync.WaitGroup"
description: "Migrate from deprecated manual synchronization to sync.WaitGroup."
deprecated_function: "Manual channel synchronization"
replacement_function: "sync.WaitGroup"
languages: ["go"]
deprecated_since: "Go 1.0+"
---

# [Solution] Deprecated Function Migration: manual goroutine sync to sync.WaitGroup

The `Manual channel synchronization` has been deprecated in favor of `sync.WaitGroup`.

## Migration Guide

WaitGroup is cleaner for waiting on goroutines

Manual synchronization with channels is verbose. WaitGroup provides a simpler API.

## Before (Deprecated)

```go
done := make(chan bool)
go func() {
    doWork()
    done <- true
}()
<-done
```

## After (Modern)

```go
var wg sync.WaitGroup
wg.Add(1)
go func() {
    defer wg.Done()
    doWork()
}()
wg.Wait()
```

## Key Differences

- WaitGroup.Add to set counter
- WaitGroup.Done to decrement
- WaitGroup.Wait to block until zero
- defer wg.Done() is idiomatic
