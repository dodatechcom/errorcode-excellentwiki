---
title: "[Solution] Go test mock HTTP server error — Testing Error Fix"
description: "Fix Go test mock HTTP server setup."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test mock HTTP server errors

Mock HTTP servers need proper setup and cleanup in tests.

## How to Fix

### Fix 1: Use httptest.NewServer

```go
func TestWithMockServer(t *testing.T) {
    ts := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "hello")
    }))
    defer ts.Close()

    resp, err := http.Get(ts.URL)
    // test response
}
```

## Related Errors

- [http-server-closed]({{< relref "/languages/go/http-server-closed" >}}) — server closed.
- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
