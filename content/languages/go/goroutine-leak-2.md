---
title: "[Solution] Go Goroutine Leak — Runtime Error Fix"
description: "Fix Go goroutine leaks by ensuring goroutines complete, channels are closed, and contexts are canceled. Detect and prevent stuck goroutines."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["goroutine", "leak", "concurrency", "memory", "runtime", "channel"]
weight: 5
---

# Goroutine Leak — Runtime Error Fix

A goroutine leak occurs when goroutines are spawned but never terminate, consuming memory and potentially other resources indefinitely.

## Description

Goroutines are lightweight, but leaked goroutines accumulate over time, increasing memory usage and potentially causing application slowdowns or crashes. Unlike deadlocks (which panic immediately), goroutine leaks silently grow until resources are exhausted.

Common scenarios:

- **Blocked channel operation** — goroutine waiting to send/receive on a channel that has no partner.
- **Missing context cancellation** — goroutine watching a context that is never canceled.
- **Infinite loop without exit** — goroutine looping forever with no break condition.
- **Forgotten goroutine** — fire-and-forget `go` without tracking completion.

## Common Causes

```go
// Cause 1: Blocked on channel with no receiver
func leak() {
    ch := make(chan int)
    go func() {
        ch <- 1 // blocks forever — no one reads
    }()
}

// Cause 2: Missing context cancellation
func fetch(ctx context.Context) {
    go func() {
        for {
            select {
            case <-ctx.Done():
                return
            default:
                // work
            }
        }
    }()
    // Context never canceled
}

// Cause 3: Infinite loop without exit
func monitor() {
    go func() {
        for {
            time.Sleep(time.Second)
            // no way to stop
        }
    }()
}

// Cause 4: Goroutine waiting on unbuffered channel
func process() {
    done := make(chan struct{})
    go func() {
        <-done // waits forever if nobody signals
    }()
}
```

## How to Fix

### Fix 1: Use context with cancel

```go
func worker(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            fmt.Println("worker stopped:", ctx.Err())
            return
        default:
            doWork()
        }
    }
}

func main() {
    ctx, cancel := context.WithCancel(context.Background())
    go worker(ctx)

    time.Sleep(time.Second)
    cancel() // stops the goroutine
}
```

### Fix 2: Always have matching senders/receivers

```go
// Wrong
func leak() {
    ch := make(chan int)
    go func() { ch <- 1 }()
}

// Correct — buffered channel or matching receiver
func noLeak() {
    ch := make(chan int, 1)
    go func() { ch <- 1 }()
    <-ch
}
```

### Fix 3: Use WaitGroup to track goroutines

```go
func main() {
    var wg sync.WaitGroup
    for i := 0; i < 5; i++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            process(id)
        }(i)
    }
    wg.Wait() // wait for all goroutines
}
```

### Fix 4: Use done channel for goroutine control

```go
func worker(done <-chan struct{}) {
    for {
        select {
        case <-done:
            return
        default:
            doWork()
        }
    }
}

func main() {
    done := make(chan struct{})
    go worker(done)
    time.Sleep(time.Second)
    close(done)
}
```

## Examples

```go
// This creates a goroutine leak (blocks forever)
package main

import "time"

func main() {
    ch := make(chan int)
    go func() {
        val := <-ch // blocks if nothing sent
        _ = val
    }()
    time.Sleep(time.Second)
}
```

## Related Errors

- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked (panics immediately).
- [channel-closed]({{< relref "/languages/go/channel-closed" >}}) — sending on a closed channel.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — memory exhausted from accumulated leaked goroutines.
