---
title: "[Solution] context deadline exceeded — HTTP Client Fix"
description: "Fix Go context deadline exceeded errors in HTTP clients. Handle timeouts, cancellation, and context propagation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["context", "timeout", "http", "deadline", "client"]
weight: 5
---

# context deadline exceeded — HTTP Client

This error occurs when an HTTP request made with `http.Client` exceeds its context deadline. The context's timeout or deadline was reached before the server responded.

## What This Error Means

Common error messages:

- `Get "http://api.example.com/data": context deadline exceeded`
- `Post "http://api.example.com/submit": context deadline exceeded`
- `context canceled` (deadline was set but request was explicitly canceled)
- `Get "http://api.example.com": dial tcp 127.0.0.1:80: i/o timeout`

The Go `context.Context` carries deadlines, cancellation signals, and request-scoped values. When the deadline expires, all operations using that context are immediately terminated.

## Common Causes

```go
// Cause 1: No timeout set (default is no deadline — waits forever)
client := &http.Client{}
resp, err := client.Get("https://api.example.com/slow-endpoint")

// Cause 2: Timeout too short
ctx, cancel := context.WithTimeout(context.Background(), 100*time.Millisecond)
defer cancel()
req, _ := http.NewRequestWithContext(ctx, "GET", "https://api.example.com/data", nil)
resp, err := client.Do(req)

// Cause 3: Upstream server is slow
// Server takes 30s, client timeout is 5s

// Cause 4: DNS resolution timeout
// DNS server unreachable, context expires during resolution

// Cause 5: Connection pool exhausted
// All connections in use, new request waits until context expires
```

## How to Fix

### Fix 1: Set appropriate timeouts

```go
client := &http.Client{
    Timeout: 30 * time.Second,
}

resp, err := client.Get("https://api.example.com/data")
if err != nil {
    log.Printf("Request failed: %v", err)
}
defer resp.Body.Close()
```

### Fix 2: Use context with timeout

```go
ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
defer cancel()

req, err := http.NewRequestWithContext(ctx, "GET", "https://api.example.com/data", nil)
if err != nil {
    log.Fatal(err)
}

resp, err := http.DefaultClient.Do(req)
if err != nil {
    if ctx.Err() == context.DeadlineExceeded {
        log.Println("Request timed out")
    }
    log.Fatal(err)
}
defer resp.Body.Close()
```

### Fix 3: Use context with cancellation for user requests

```go
func handler(w http.ResponseWriter, r *http.Request) {
    // Propagate the request context to downstream calls
    ctx := r.Context()

    req, err := http.NewRequestWithContext(ctx, "GET", "https://api.example.com/data", nil)
    if err != nil {
        http.Error(w, err.Error(), 500)
        return
    }

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        if ctx.Err() == context.Canceled {
            log.Println("Client disconnected")
        }
        http.Error(w, "upstream error", 502)
        return
    }
    defer resp.Body.Close()

    io.Copy(w, resp.Body)
}
```

### Fix 4: Configure transport for connection pooling

```go
client := &http.Client{
    Timeout: 30 * time.Second,
    Transport: &http.Transport{
        MaxIdleConns:        100,
        MaxIdleConnsPerHost: 10,
        IdleConnTimeout:     90 * time.Second,
        DialContext: (&net.Dialer{
            Timeout:   5 * time.Second,
            KeepAlive: 30 * time.Second,
        }).DialContext,
    },
}
```

### Fix 5: Add retry with exponential backoff

```go
func doWithRetry(ctx context.Context, client *http.Client, req *http.Request, maxRetries int) (*http.Response, error) {
    for i := 0; i < maxRetries; i++ {
        resp, err := client.Do(req)
        if err == nil {
            return resp, nil
        }
        if i < maxRetries-1 {
            delay := time.Duration(1<<uint(i)) * time.Second
            select {
            case <-time.After(delay):
            case <-ctx.Done():
                return nil, ctx.Err()
            }
        }
    }
    return nil, fmt.Errorf("max retries exceeded")
}
```

## Examples

```
Get "http://localhost:8080/api/users": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
```

```go
// Fix: increase timeout for slow endpoints
client := &http.Client{
    Timeout: 60 * time.Second,
    Transport: &http.Transport{
        ResponseHeaderTimeout: 30 * time.Second,
    },
}
```

## Related Errors

- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — context deadline exceeded
- [context-deadline-2]({{< relref "/languages/go/context-deadline-2" >}}) — context deadline exceeded variant
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP timeout
