---
title: "[Solution] Go Goroutine Leak — Runtime Error Fix"
description: "Fix Go goroutine leaks. Ensure goroutines exit when done, use context for cancellation, and monitor goroutine count."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Goroutine Leak — Runtime Error Fix

A goroutine leak occurs when goroutines are started but never exit, consuming memory and potentially other resources indefinitely.

## Description

Goroutines are lightweight, but they are not free. Each goroutine uses at least 2-8 KB of stack memory. When goroutines are leaked — blocked on a channel that will never receive or send, or stuck in an infinite loop — they accumulate and consume increasing amounts of memory.

Common scenarios:

- **Blocked on channel send/receive** — channel has no receiver/sender and isn't closed.
- **Missing context cancellation** — goroutine doesn't respect context cancellation.
- **Infinite loop without exit condition** — goroutine runs forever.
- **Mutex held forever** — goroutine acquires a lock and never releases it.

## Common Causes

```go
// Cause 1: Blocked on channel with no receiver
func leak() {
    ch := make(chan int)
    go func() {
        ch <- 1 // Blocks forever — no one is reading
    }()
}

// Cause 2: No context cancellation
func worker() {
    for {
        result := <-fetchData() // Blocks if channel is empty
        process(result)
    }
    // No way to stop this goroutine
}

// Cause 3: Infinite loop
func stuck() {
    for {
        // Never exits
    }
}

// Cause 4: HTTP handler goroutine leak
func handler(w http.ResponseWriter, r *http.Request) {
    ch := make(chan string, 1)
    go func() {
        ch <- slowOperation() // May block if slowOperation hangs
    }()
    select {
    case result := <-ch:
        w.Write([]byte(result))
    case <-r.Context().Done():
        // Request cancelled, but goroutine is still running
    }
}
```

## How to Fix

### Fix 1: Use context for goroutine cancellation

```go
// Wrong — no way to stop the goroutine
func worker(data <-chan int) {
    for v := range data {
        process(v)
    }
}

// Correct — respect context cancellation
func worker(ctx context.Context, data <-chan int) {
    for {
        select {
        case <-ctx.Done():
            return
        case v, ok := <-data:
            if !ok {
                return
            }
            process(v)
        }
    }
}
```

### Fix 2: Always have a receiver for channel sends

```go
// Wrong — goroutine blocks forever
go func() {
    ch <- result
}()

// Correct — ensure someone is listening
go func() {
    select {
    case ch <- result:
    case <-ctx.Done():
        return
    }
}()
```

### Fix 3: Close channels when done sending

```go
// Wrong — reader blocks forever
go func() {
    for v := range ch {
        process(v)
    }
}()

// Correct — close channel when sending is done
go func() {
    for _, v := range data {
        ch <- v
    }
    close(ch)
}()
```

### Fix 4: Monitor goroutine count

```go
import "runtime"

func monitorGoroutines() {
    ticker := time.NewTicker(time.Second)
    for range ticker.C {
        fmt.Printf("Goroutines: %d\n", runtime.NumGoroutine())
    }
}

// In main or test setup
go monitorGoroutines()
```

### Fix 5: Use WaitGroups for proper shutdown

```go
func main() {
    var wg sync.WaitGroup
    ctx, cancel := context.WithCancel(context.Background())
    defer cancel()

    for i := 0; i < 10; i++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            for {
                select {
                case <-ctx.Done():
                    return
                default:
                    process(id)
                }
            }
        }(i)
    }

    // Signal all goroutines to stop
    cancel()
    wg.Wait()
}
```

## Examples

```go
// This creates a goroutine leak (runs forever, accumulating memory)
package main

func main() {
    for i := 0; i < 100000; i++ {
        go func() {
            ch := make(chan int)
            <-ch // Blocks forever
        }()
    }
    select {} // Block main goroutine
}
```

## Related Errors

- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked.
- [channel-closed]({{< relref "/languages/go/channel-closed" >}}) — sending on a closed channel.
- [out-of-memory]({{< relref "/languages/go/out-of-memory" >}}) — leaked goroutines consume memory.
