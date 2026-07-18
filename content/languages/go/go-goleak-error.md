---
title: "[Solution] Go Goroutine Leak Error — How to Fix"
description: "Fix Go goroutine leak errors. Handle test goroutine detection, resource cleanup, and leak prevention patterns."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Goroutine Leak Error

Fix Go goroutine leak errors. Handle test goroutine detection, resource cleanup, and leak prevention patterns.

## Why It Happens

- Goroutines spawned by code under test are not cleaned up after test completes
- HTTP servers or database connections are not closed causing leaked goroutines
- Context cancellation does not stop all child goroutines
- Ticker or timer goroutines are not stopped after use

## Common Error Messages

```
goleak: leaked goroutine
```
```
goleak: found unexpected goroutines
```
```
goroutine leak detected after test
```
```
FAIL: goroutines leaked
```

## How to Fix It

### Solution 1: Use goleak in tests

```go
import "go.uber.org/goleak"
func TestMain(m *testing.M) {
    goleak.VerifyTestMain(m)
}
func TestSomething(t *testing.T) {
    defer goleak.VerifyNone(t)
}
```

### Solution 2: Ignore known goroutines

```go
func TestWithKnownLeaks(t *testing.T) {
    defer goleak.VerifyNone(t,
        goleak.IgnoreTopFunction("go.opencensus.io/stats/view.(*worker).start"),
    )
}
```

### Solution 3: Clean up goroutines properly

```go
ticker := time.NewTicker(time.Second)
defer ticker.Stop()
ctx, cancel := context.WithCancel(context.Background())
defer cancel()
go func() {
    for {
        select {
        case <-ctx.Done(): return
        case t := <-ticker.C: process(t)
        }
    }
}()
```

### Solution 4: Close resources that spawn goroutines

```go
server := httptest.NewServer(handler)
defer server.Close()
ln, _ := net.Listen("tcp", ":0")
defer ln.Close()
```

## Common Scenarios

- A test detects leaked goroutines from HTTP client connections not being closed
- A background ticker goroutine leaks because Stop is never called
- A goroutine spawned by context.AfterFunc leaks because the stop function is not called

## Prevent It

- Use goleak.VerifyTestMain or goleak.VerifyNone in every test package
- Always defer Stop on tickers and Close on resources that spawn goroutines
- Use context cancellation to signal background goroutines to stop
