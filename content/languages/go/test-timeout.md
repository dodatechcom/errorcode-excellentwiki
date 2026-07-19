---
title: "[Solution] Go test timeout — Testing Error Fix"
description: "Fix Go test timeout."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test timeout

The error `panic: test timed out after 10m0s` occurs when a test takes longer than allowed.

## How to Fix

### Fix 1: Set test timeout

```bash
go test -timeout 30s ./...
```

### Fix 2: Use context with timeout

```go
func TestWithTimeout(t *testing.T) {
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    result, err := doWork(ctx)
    if err != nil { t.Fatal(err) }
    _ = result
}
```

## Related Errors

- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — goroutine deadlock.
