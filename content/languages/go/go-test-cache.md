---
title: "[Solution] Go test caching error — Testing Error Fix"
description: "Fix Go test caching issues."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test caching issues

Go caches test results. Use `-count=1` to disable caching.

## How to Fix

```bash
go test -count=1 ./...
```

### Fix 1: Use t.Setenv to invalidate cache

```go
func TestWithEnv(t *testing.T) {
    t.Setenv("MY_VAR", "value")
    // test uses env var, cache invalidated
}
```

## Related Errors

- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
- [go-test-short]({{< relref "/languages/go/go-test-short" >}}) — short mode.
