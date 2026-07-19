---
title: "[Solution] Go test JSON output — Testing Error Fix"
description: "Fix Go test JSON output for CI/CD."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test JSON output

Use `-json` flag for machine-readable test output.

## How to Fix

```bash
go test -json ./...
```

### Fix 1: Parse JSON output

```go
type TestEvent struct {
    Time    time.Time `json:"Time"`
    Action  string    `json:"Action"`
    Package string    `json:"Package"`
    Test    string    `json:"Test"`
    Output  string    `json:"Output"`
}
```

## Related Errors

- [json-syntax-error]({{< relref "/languages/go/json-syntax-error" >}}) — JSON syntax.
- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
