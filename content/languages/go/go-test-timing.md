---
title: "[Solution] Go test timing error — Testing Error Fix"
description: "Fix Go test timing issues."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test timing errors

Tests with time-dependent logic can be flaky.

## How to Fix

### Fix 1: Use time.After for timeouts

```go
func TestWithTimeout(t *testing.T) {
    done := make(chan bool)
    go func() {
        doWork()
        done <- true
    }()
    select {
    case <-done:
        // success
    case <-time.After(5 * time.Second):
        t.Fatal("test timed out")
    }
}
```

### Fix 2: Inject time for testing

```go
type Clock interface {
    Now() time.Time
}

type RealClock struct{}
func (RealClock) Now() time.Time { return time.Now() }
```

## Related Errors

- [test-timeout]({{< relref "/languages/go/test-timeout" >}}) — test timeout.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutine leak.
