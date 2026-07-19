---
title: "[Solution] Go test: parallel test issues — Testing Error Fix"
description: "Fix Go parallel test problems."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# parallel test issues

`t.Parallel()` allows tests to run concurrently, which can cause shared state problems.

## How to Fix

### Fix 1: Use t.Cleanup for shared resources

```go
func TestWithDB(t *testing.T) {
    t.Parallel()
    db := setupTestDB(t)
    t.Cleanup(func() { db.Close() })
    // test code
}
```

### Fix 2: Use unique test data

```go
func TestUnique(t *testing.T) {
    t.Parallel()
    key := fmt.Sprintf("test-%d", time.Now().UnixNano())
    // use unique key
}
```

## Related Errors

- [race-condition]({{< relref "/languages/go/race-condition" >}}) — race condition.
- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
