---
title: "[Solution] Go testing: short mode — Testing Error Fix"
description: "Fix Go testing in short mode."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# testing: short mode

When running `go test -short`, external tests and long-running tests should be skipped.

## How to Fix

```go
func TestExternalAPI(t *testing.T) {
    if testing.Short() {
        t.Skip("skipping external test in short mode")
    }
    // test code
}
```

## Related Errors

- [test-timeout]({{< relref "/languages/go/test-timeout" >}}) — test timeout.
- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
