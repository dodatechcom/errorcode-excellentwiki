---
title: "[Solution] Go send on nil channel — Concurrency Error Fix"
description: "Fix Go send on nil channel."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# send on nil channel

The error `panic: send on nil channel` occurs when you attempt to send on a nil channel.

## Common Causes

- **Uninitialized channel** — `var ch chan int` defaults to nil
- **Failed initialization** — function returned nil channel

## How to Fix

### Fix 1: Always initialize channels

```go
ch := make(chan int) // not var ch chan int
```

### Fix 2: Check for nil in select

```go
for ch1 != nil || ch2 != nil {
    select {
    case v, ok := <-ch1:
        if !ok { ch1 = nil; continue }
        out <- v
    case v, ok := <-ch2:
        if !ok { ch2 = nil; continue }
        out <- v
    }
}
```

## Examples

```go
package main

func main() {
    var ch chan int
    ch <- 1
}
```

Output:
```
panic: send on nil channel
```

## Related Errors

- [channel-closed]({{< relref "/languages/go/channel-closed" >}}) — send on closed channel.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — all goroutines blocked.
