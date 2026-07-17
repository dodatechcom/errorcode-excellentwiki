---
title: "[Solution] Go Deadlock — All Goroutines Asleep Fix"
description: "Fix Go deadlock: all goroutines are asleep. Ensure channels are properly closed, goroutines can make progress, and avoid blocking sends."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# All Goroutines Asleep — Deadlock Fix

A deadlock occurs when all goroutines in a program are blocked and none can make progress. The Go runtime detects this and panics with `fatal error: all goroutines are asleep - deadlock!`.

## Description

Go's runtime has a built-in deadlock detector. When every goroutine is blocked (on channel operations, locks, or system calls), the runtime assumes this is unintended and panics. This is a development aid — production programs should avoid reaching this state.

Common scenarios:

- **Unbuffered channel with no goroutine on the other side** — send or receive blocks forever.
- **Closing a channel twice** — double close panics, but blocking on close is also problematic.
- **All goroutines waiting on each other** — circular dependency.
- **Main goroutine blocked** — main program waits on a channel with no sender.

## Common Causes

```go
// Cause 1: Unbuffered channel with no receiver
func main() {
    ch := make(chan int)
    ch <- 1 // Blocks — no goroutine is reading
}

// Cause 2: Reading from empty channel with no sender
func main() {
    ch := make(chan int)
    <-ch // Blocks — no goroutine is writing
}

// Cause 3: Circular wait between goroutines
func main() {
    ch1 := make(chan int)
    ch2 := make(chan int)

    go func() {
        <-ch1   // Wait for ch1
        ch2 <- 1 // Then send to ch2
    }()

    <-ch2   // Main waits for ch2 — but the goroutine is waiting for ch1
    ch1 <- 1 // Never reached
}

// Cause 4: All goroutines blocked on mutex
func main() {
    var mu sync.Mutex
    mu.Lock()
    go func() {
        mu.Lock() // Blocks — main holds the lock
        defer mu.Unlock()
    }()
    mu.Unlock() // Never reached
}
```

## How to Fix

### Fix 1: Use buffered channels to prevent blocking

```go
// Wrong — unbuffered channel blocks
func main() {
    ch := make(chan int)
    ch <- 1 // Blocks
}

// Correct — buffered channel allows send without receiver
func main() {
    ch := make(chan int, 1)
    ch <- 1 // Succeeds immediately
    fmt.Println(<-ch)
}
```

### Fix 2: Always have matching senders and receivers

```go
// Wrong — no goroutine reading
func main() {
    ch := make(chan int)
    ch <- 1
}

// Correct — goroutine reads what main sends
func main() {
    ch := make(chan int)
    go func() {
        v := <-ch
        fmt.Println(v)
    }()
    ch <- 1
}
```

### Fix 3: Break circular dependencies

```go
// Wrong — circular wait
ch1 := make(chan int)
ch2 := make(chan int)

go func() {
    <-ch1
    ch2 <- 1
}()

<-ch2
ch1 <- 1

// Correct — use goroutines for both sides
ch1 := make(chan int)
ch2 := make(chan int)

go func() {
    <-ch1
    ch2 <- 1
}()

go func() {
    <-ch2
    ch1 <- 1
}()

// Use timeout to detect deadlock
select {
case <-ch2:
case <-time.After(time.Second):
    fmt.Println("timeout")
}
```

### Fix 4: Use select with timeout for potentially blocking operations

```go
// Wrong — may block forever
result := <-ch

// Correct — timeout prevents deadlock
select {
case result = <-ch:
    fmt.Println("received:", result)
case <-time.After(5 * time.Second):
    fmt.Println("timeout waiting for channel")
}
```

### Fix 5: Run with race detector

```bash
go run -race main.go
go test -race ./...
```

### Fix 6: Use context with timeout

```go
// Wrong — no timeout
result := <-ch

// Correct — context timeout
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

select {
case result = <-ch:
case <-ctx.Done():
    fmt.Println("timeout:", ctx.Err())
}
```

## Examples

```go
// This triggers: fatal error: all goroutines are asleep - deadlock!
package main

func main() {
    ch := make(chan int)
    ch <- 1
}
```

## Related Errors

- [channel-closed]({{< relref "/languages/go/channel-closed" >}}) — sending on a closed channel.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutines stuck but not all asleep.
- [sync-mutex]({{< relref "/languages/go/sync-mutex" >}}) — RWMutex not locked when accessed.
