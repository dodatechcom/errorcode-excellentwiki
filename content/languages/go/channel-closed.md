---
title: "[Solution] Go Send on Closed Channel — Runtime Error Fix"
description: "Fix Go send on closed channel panic. Learn proper channel lifecycle management, close patterns, and safe channel communication."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Send on Closed Channel — Runtime Error

The error `panic: send on closed channel` occurs when you attempt to send a value to a channel that has already been closed. In Go, sending to a closed channel is a fatal runtime error that cannot be recovered in the same goroutine.

## Description

Channels in Go are typed conduits for communicating between goroutines. Once a channel is closed, it cannot accept new values. Attempting to send to a closed channel panics immediately. Unlike receiving from a closed channel (which returns the zero value), sending has no graceful fallback.

This is a common bug in concurrent programs where one goroutine closes a channel while another is still trying to send values.

## Common Causes

- **Closing a channel twice** — calling `close(ch)` more than once on the same channel
- **Sending after close** — one goroutine closes the channel while another is still sending
- **Race condition on close** — unsynchronized close and send operations
- **Missing coordination** — no signal that all senders are done before closing

## How to Fix

### Fix 1: Only the sender should close the channel

```go
// Rule: only the sender should close a channel
func producer(ch chan<- int) {
    defer close(ch) // only the sender closes
    for i := 0; i < 10; i++ {
        ch <- i
    }
}
```

### Fix 2: Use sync.WaitGroup to coordinate

```go
func main() {
    ch := make(chan int)
    var wg sync.WaitGroup

    wg.Add(1)
    go func() {
        defer wg.Done()
        for i := 0; i < 10; i++ {
            ch <- i
        }
    }()

    go func() {
        wg.Wait()
        close(ch) // close after all senders are done
    }()

    for v := range ch {
        fmt.Println(v)
    }
}
```

### Fix 3: Use a done channel to signal stop

```go
func worker(done <-chan struct{}, data <-chan int) {
    for {
        select {
        case <-done:
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

### Fix 4: Protect close with a sync.Once

```go
type SafeChannel struct {
    ch   chan int
    once sync.Once
}

func (sc *SafeChannel) Close() {
    sc.once.Do(func() {
        close(sc.ch)
    })
}
```

## Examples

```go
package main

import "fmt"

func main() {
    ch := make(chan int, 5)
    close(ch)

    // This will panic
    ch <- 1
}
```

Output:
```
panic: send on closed channel
```

## Related Errors

- [deadlock]({{< relref "/languages/go/deadlock" >}}) — goroutines blocked waiting on channel operations.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines stuck on unclosed channels.
- [concurrent-map]({{< relref "/languages/go/concurrent-map" >}}) — concurrent map access without synchronization.
