---
title: "[Solution] Go HTTP Client Timeout Error Fix"
description: "Fix Go context deadline exceeded HTTP client timeout. Configure proper timeouts, use context with deadline, and handle slow responses."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["http", "timeout", "client", "context", "deadline"]
weight: 5
---

# Context Deadline Exceeded (Client Timeout) — Fix

An HTTP client timeout error occurs when the client doesn't receive a response within the configured timeout period.

## Description

Go's `http.Client` has a `Timeout` field that limits the total time for a request including dial, TLS handshake, sending the request, and reading the response. When this timeout expires, the error is `context deadline exceeded (Client.Timeout exceeded while awaiting headers)`.

Common scenarios:

- **Server is slow** — takes longer than expected to respond.
- **Network latency** — high latency causes timeouts.
- **DNS resolution slow** — hostname lookup takes too long.
- **Server overloaded** — server accepts connection but doesn't respond.

## Common Causes

```go
// Cause 1: No timeout set (can hang forever)
client := &http.Client{}
resp, err := client.Get("http://slow-server.com")
// May hang indefinitely

// Cause 2: Timeout too short
client := &http.Client{Timeout: 1 * time.Second}
resp, err := client.Get("http://api.example.com/data")
// context deadline exceeded (Client.Timeout exceeded while awaiting headers)

// Cause 3: Server takes too long to respond headers
client := &http.Client{Timeout: 5 * time.Second}
resp, err := client.Get("http://slow-api.com/heavy-query")

// Cause 4: Reading response body takes too long
client := &http.Client{Timeout: 10 * time.Second}
resp, err := client.Get("http://api.example.com/huge-dataset")
// Timeout covers entire request/response cycle
```

## How to Fix

### Fix 1: Set appropriate client timeout

```go
// Wrong — no timeout, may hang forever
client := &http.Client{}

// Correct — set reasonable timeout
client := &http.Client{
    Timeout: 30 * time.Second,
}
resp, err := client.Get("http://api.example.com/data")
```

### Fix 2: Use Transport for fine-grained timeout control

```go
// Correct — separate timeouts for different phases
transport := &http.Transport{
    DialContext: (&net.Dialer{
        Timeout:   5 * time.Second,  // Connection timeout
        KeepAlive: 30 * time.Second,
    }).DialContext,
    TLSHandshakeTimeout:   5 * time.Second,
    ResponseHeaderTimeout: 10 * time.Second,
}

client := &http.Client{
    Transport: transport,
    Timeout:   30 * time.Second, // Overall timeout
}
```

### Fix 3: Use context for per-request timeout

```go
// Wrong — single timeout for all requests
client := &http.Client{Timeout: 5 * time.Second}
for _, url := range urls {
    resp, err := client.Get(url) // Same timeout for all
}

// Correct — per-request timeout
for _, url := range urls {
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
    resp, err := client.Do(req)
    cancel() // Must call cancel to free resources
    if err != nil {
        if ctx.Err() == context.DeadlineExceeded {
            log.Printf("timeout for %s", url)
        }
        continue
    }
    resp.Body.Close()
}
```

### Fix 4: Read response body within timeout

```go
// Wrong — body read may exceed timeout
client := &http.Client{Timeout: 5 * time.Second}
resp, err := client.Get("http://api.example.com/large")
data, _ := io.ReadAll(resp.Body) // May take too long

// Correct — use context for body read
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
req, _ := http.NewRequestWithContext(ctx, "GET", "http://api.example.com/large", nil)
resp, err := client.Do(req)
if err != nil {
    log.Fatal(err)
}
defer resp.Body.Close()

limitedReader := io.LimitReader(resp.Body, 10<<20) // 10MB limit
data, err := io.ReadAll(limitedReader)
```

### Fix 5: Add retry logic for timeout errors

```go
func fetchWithRetry(url string) (*http.Response, error) {
    client := &http.Client{Timeout: 10 * time.Second}
    for i := 0; i < 3; i++ {
        resp, err := client.Get(url)
        if err == nil {
            return resp, nil
        }
        if ctxErr := err; ctxErr != nil {
            log.Printf("attempt %d failed: %v", i+1, err)
            time.Sleep(time.Duration(i+1) * time.Second)
        }
    }
    return nil, fmt.Errorf("all retries failed for %s", url)
}
```

## Examples

```go
// This triggers: context deadline exceeded (Client.Timeout exceeded while awaiting headers)
package main

import (
    "fmt"
    "net/http"
    "time"
)

func main() {
    client := &http.Client{Timeout: 1 * time.Second}
    resp, err := client.Get("http://httpbin.org/delay/5")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer resp.Body.Close()
}
```

## Related Errors

- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — context deadline exceeded.
- [context-canceled]({{< relref "/languages/go/context-canceled" >}}) — context was canceled.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused.
