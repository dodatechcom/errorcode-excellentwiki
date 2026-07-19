---
title: "[Solution] Go test parallel race condition — Testing Error Fix"
description: "Fix Go test parallel race condition."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test parallel race condition

Parallel tests with shared state cause race conditions.

## How to Fix

### Fix 1: Isolate test state

```go
func TestParallel(t *testing.T) {
    t.Parallel()
    // Use only local variables, no shared state
    localData := make(map[string]int)
    localData["key"] = 42
}
```

## Related Errors

- [race-condition]({{< relref "/languages/go/race-condition" >}}) — race condition.
- [concurrent-map]({{< relref "/languages/go/concurrent-map" >}}) — concurrent map.
