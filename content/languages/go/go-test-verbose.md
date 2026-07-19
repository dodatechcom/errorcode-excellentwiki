---
title: "[Solution] Go test verbose output — Testing Error Fix"
description: "Fix Go test verbose output issues."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test verbose output

Use `-v` flag for detailed test output including pass/fail for each subtest.

## How to Fix

```bash
go test -v ./...
```

### Fix 1: Use subtests for organized output

```go
func TestAdd(t *testing.T) {
    t.Run("positive", func(t *testing.T) {
        if Add(2, 3) != 5 {
            t.Error("expected 5")
        }
    })
    t.Run("negative", func(t *testing.T) {
        if Add(-1, -2) != -3 {
            t.Error("expected -3")
        }
    })
}
```

## Related Errors

- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
- [go-build-error]({{< relref "/languages/go/go-build-error" >}}) — build error.
