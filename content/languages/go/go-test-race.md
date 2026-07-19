---
title: "[Solution] Go test -race data race — Testing Error Fix"
description: "Fix Go test race condition."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test -race data race

Data races detected by `-race` during testing must be fixed for reliable test results.

## How to Fix

### Fix 1: Use test helper with mutex

```go
type testHelper struct {
    mu   sync.Mutex
    data map[string]string
}

func (h *testHelper) Get(key string) string {
    h.mu.Lock()
    defer h.mu.Unlock()
    return h.data[key]
}
```

## Related Errors

- [race-condition]({{< relref "/languages/go/race-condition" >}}) — race condition.
- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
