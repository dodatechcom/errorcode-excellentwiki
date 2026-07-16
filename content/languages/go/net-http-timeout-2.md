---
title: "[Solution] Go HTTP Request Timeout Fix"
description: "Fix Go HTTP context deadline exceeded error. Set appropriate timeouts, use context cancellation, and handle slow servers gracefully."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["http", "timeout", "deadline", "context", "network", "runtime"]
weight: 5
---

# HTTP Request Timeout Fix

The `context deadline exceeded` error on HTTP requests occurs when a request takes longer than the configured timeout.

## Description

Go's HTTP client has no default timeout (it waits forever). When you set a timeout via `http.Client.Timeout` or `context.WithTimeout`, the request must complete within that duration. If the server is slow, the network is congested, or the server is down, the request times out.

Common scenarios:

- **Slow server response** — API takes longer than expected.
- **Network latency** — high latency on cloud or cross-region connections.
- **DNS resolution slow** — DNS server is unresponsive.
- **TLS handshake slow** — certificate exchange takes too long.
- **No default timeout** — requests hang forever without explicit timeout.

## Common Causes

```go
// Cause 1: No timeout configured (hangs forever)
func main() {
    client := &http.Client{} // no timeout
    resp, err := client.Get("https://slow-api.example.com")
    // May hang indefinitely
}

// Cause 2: Timeout too short
func main() {
    client := &http.Client{
        Timeout: 100 * time.Millisecond, // too short
    }
    resp, err := client.Get("https://api.example.com")
}

// Cause 3: Context timeout too tight
func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 50*time.Millisecond)
    defer cancel()
    req, _ := http.NewRequestWithContext(ctx, "GET", "https://api.example.com", nil)
    resp, err := http.DefaultClient.Do(req)
    _ = resp
    _ = err
}

// Cause 4: No deadline on connection
func main() {
    conn, _ := net.DialTimeout("tcp", "example.com:443", time.Second)
    // No read/write deadline set
    conn.SetReadDeadline(time.Time{}) // no deadline
}
```

## How to Fix

### Fix 1: Set appropriate client timeout

```go
func main() {
    client := &http.Client{
        Timeout: 30 * time.Second,
    }
    resp, err := client.Get("https://api.example.com")
    if err != nil {
        if errors.Is(err, context.DeadlineExceeded) {
            log.Println("request timed out")
        }
        log.Fatal(err)
    }
    defer resp.Body.Close()
}
```

### Fix 2: Use context with timeout for per-request control

```go
func fetchData(url string) ([]byte, error) {
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()

    req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()
    return io.ReadAll(resp.Body)
}
```

### Fix 3: Set per-phase timeouts with transport

```go
client := &http.Client{
    Transport: &http.Transport{
        DialContext: (&net.Dialer{
            Timeout:   5 * time.Second,
            KeepAlive: 30 * time.Second,
        }).DialContext,
        TLSHandshakeTimeout: 5 * time.Second,
        ResponseHeaderTimeout: 10 * time.Second,
    },
}
```

### Fix 4: Use retry with timeout

```go
func fetchWithRetry(url string) (*http.Response, error) {
    for i := 0; i < 3; i++ {
        ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
        req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
        resp, err := http.DefaultClient.Do(req)
        cancel()
        if err == nil {
            return resp, nil
        }
        time.Sleep(time.Duration(i+1) * time.Second)
    }
    return nil, fmt.Errorf("all retries failed")
}
```

## Examples

```go
// This triggers: Get "https://httpbin.org/delay/10": context deadline exceeded
package main

import (
    "fmt"
    "net/http"
    "time"
)

func main() {
    client := &http.Client{Timeout: 1 * time.Millisecond}
    _, err := client.Get("https://httpbin.org/delay/10")
    fmt.Println(err) // context deadline exceeded
}
```

## Related Errors

- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — general context deadline exceeded.
- [context-canceled]({{< relref "/languages/go/context-canceled" >}}) — context explicitly canceled.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused.
