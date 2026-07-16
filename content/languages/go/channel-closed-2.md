---
title: "[Solution] Go Send on Closed Channel — Runtime Error Fix"
description: "Fix Go send on closed channel panic. Use sync mechanisms to track channel state, and close channels only from the sender."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["channel", "closed", "send", "panic", "concurrency", "runtime"]
weight: 5
---

# Send on Closed Channel — Runtime Error Fix

Sending on a closed channel causes an immediate panic. This is a common concurrency bug in Go programs.

## Description

Once a channel is closed, any attempt to send a value on it panics with `panic: send on closed channel`. Receiving from a closed channel is safe and returns zero values, but sending is not. This typically happens when multiple goroutines try to use a channel after one of them has closed it.

Common scenarios:

- **Multiple senders** — one goroutine closes while others are still sending.
- **Deferred close in sender** — close runs before all sends complete.
- **Close called twice** — double close also panics.
- **Race on close** — goroutine checks if channel is open then closes it, but another sends in between.

## Common Causes

```go
// Cause 1: Multiple goroutines sending after close
func main() {
    ch := make(chan int)
    close(ch)
    ch <- 1 // panic: send on closed channel
}

// Cause 2: Deferred close before sends finish
func producer(ch chan<- int) {
    defer close(ch)
    for i := 0; i < 10; i++ {
        ch <- i
    }
}

func main() {
    ch := make(chan int, 5)
    go producer(ch)
    // Consumer may not read all values before producer returns
}

// Cause 3: Double close
func main() {
    ch := make(chan int)
    close(ch)
    close(ch) // panic: close of closed channel
}

// Cause 4: Race between close and send
func main() {
    ch := make(chan int, 1)
    go func() {
        ch <- 1
        close(ch)
    }()
    ch <- 2 // may panic if channel was closed
}
```

## How to Fix

### Fix 1: Only close from the sender side

```go
// Wrong — consumer closes
go func() {
    for v := range ch {
        process(v)
    }
    close(ch) // wrong: consumer should not close
}()

// Correct — only the producer closes
go func() {
    for i := 0; i < 10; i++ {
        ch <- i
    }
    close(ch)
}()
```

### Fix 2: Use sync.WaitGroup to coordinate close

```go
var wg sync.WaitGroup
ch := make(chan int)

for i := 0; i < 3; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        ch <- id
    }(i)
}

go func() {
    wg.Wait()
    close(ch)
}()
```

### Fix 3: Use recover to handle unexpected panics

```go
func safeSend(ch chan<- int, v int) (ok bool) {
    defer func() {
        if recover() != nil {
            ok = false
        }
    }()
    ch <- v
    return true
}
```

### Fix 4: Use done channel or context to stop sends

```go
ctx, cancel := context.WithCancel(context.Background())
defer cancel()

ch := make(chan int)
go func() {
    for {
        select {
        case ch <- rand.Int():
        case <-ctx.Done():
            close(ch)
            return
        }
    }
}()
```

## Examples

```go
// This triggers: panic: send on closed channel
package main

func main() {
    ch := make(chan int)
    close(ch)
    ch <- 42
}
```

## Related Errors

- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked waiting on each other.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines stuck on channel operations.
- [sync-mutex]({{< relref "/languages/go/sync-mutex" >}}) — mutex locking errors in concurrent code.
