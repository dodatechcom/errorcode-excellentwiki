---
title: "[Solution] Go net/http: request canceled — Network Error Fix"
description: "Fix Go request canceled error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# net/http: request canceled

The error `net/http: request canceled (Client.Timeout exceeded while reading body)` occurs when the client timeout fires before the response is complete.

## How to Fix

### Fix 1: Increase client timeout

```go
client := &http.Client{Timeout: 60 * time.Second}
```

### Fix 2: Use per-request context

```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
resp, err := client.Do(req)
```

## Related Errors

- [http-timeout]({{< relref "/languages/go/http-timeout" >}}) — HTTP timeout.
- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — context deadline.
