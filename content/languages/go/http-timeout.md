---
title: "[Solution] HTTP Context Deadline Exceeded Fix"
description: "Fix Go HTTP timeout errors when context deadline is exceeded. Set appropriate timeouts, use context.WithTimeout, and handle deadline errors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HTTP Context Deadline Exceeded

The `net/http` client times out when a request takes longer than the configured deadline. This happens when the server is slow, the network is congested, or the timeout is set too aggressively. Go's `http.Client` has a default timeout of 0 (no timeout), so requests can hang indefinitely.

## Common Causes

```go
// Cause 1: Default client has no timeout
resp, err := http.Get("https://slow-api.example.com")
// hangs indefinitely if server is slow

// Cause 2: Timeout too short
client := &http.Client{Timeout: 100 * time.Millisecond}
resp, err := client.Get("https://api.example.com/data")
// deadline exceeded — API needs 200ms

// Cause 3: No context with deadline
req, _ := http.NewRequest("GET", url, nil)
// no timeout set on request or client

// Cause 4: TLS handshake takes too long
// Client timeout includes DNS + TCP + TLS + server response

// Cause 5: Response body read times out
resp, err := client.Get(url)
body, err := io.ReadAll(resp.Body) // read may timeout
```

## How to Fix

### Fix 1: Set proper client timeout

```go
import (
    "net/http"
    "time"
)

var client = &http.Client{
    Timeout: 30 * time.Second, // total timeout for entire request
}

func fetchData(url string) ([]byte, error) {
    resp, err := client.Get(url)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    return io.ReadAll(resp.Body)
}
```

### Fix 2: Use context for per-request timeout

```go
func fetchDataWithContext(ctx context.Context, url string) ([]byte, error) {
    ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    defer cancel()

    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    return io.ReadAll(resp.Body)
}
```

### Fix 3: Use transport-level timeouts for fine control

```go
client := &http.Client{
    Transport: &http.Transport{
        DialContext: (&net.Dialer{
            Timeout:   5 * time.Second,  // TCP connection
            KeepAlive: 30 * time.Second,
        }).DialContext,
        TLSHandshakeTimeout:   5 * time.Second,
        ResponseHeaderTimeout: 10 * time.Second,
        ExpectContinueTimeout: 1 * time.Second,
    },
    Timeout: 30 * time.Second,
}
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "io"
    "log"
    "net/http"
    "time"
)

func main() {
    client := &http.Client{Timeout: 10 * time.Second}

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    req, err := http.NewRequestWithContext(ctx, "GET", "https://httpbin.org/delay/2", nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Do(req)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()

    body, _ := io.ReadAll(resp.Body)
    fmt.Println(string(body))
}
```

## Related Errors

- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — generic context timeout
- [grpc-timeout]({{< relref "/languages/go/grpc-timeout" >}}) — gRPC deadline exceeded
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP dial timeout
