---
title: "[Solution] Go net/http: too many redirects — Network Error Fix"
description: "Fix Go too many redirects error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# net/http: too many redirects

The error `net/http: too many redirects` occurs when a redirect loop is detected.

## How to Fix

### Fix 1: Limit redirects

```go
client := &http.Client{
    CheckRedirect: func(req *http.Request, via []*http.Request) error {
        if len(via) >= 10 {
            return fmt.Errorf("too many redirects")
        }
        return nil
    },
}
```

## Related Errors

- [http-timeout]({{< relref "/languages/go/http-timeout" >}}) — HTTP timeout.
- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
