---
title: "[Solution] Go HTTP Client Error — How to Fix"
description: "Fix Go HTTP client errors. Handle client configuration, connection pooling, retries, and timeouts."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go HTTP Client Error

Fix Go HTTP client errors. Handle client configuration, connection pooling, retries, and timeouts.

## Why It Happens

- HTTP client does not have timeouts configured causing hanging requests
- Connection pool is exhausted because of high concurrency
- Client does not follow redirects causing 301/302 errors
- Response body is not closed causing connection leaks

## Common Error Messages

```
http: client connection force-closed
```
```
http: request canceled
```
```
http: no Cookie header
```
```
http: TLS handshake timeout
```

## How to Fix It

### Solution 1: Configure HTTP client

```go
client := &http.Client{
    Timeout: 30 * time.Second,
    Transport: &http.Transport{
        MaxIdleConns:        100,
        MaxIdleConnsPerHost: 10,
        IdleConnTimeout:     90 * time.Second,
    },
}
```

### Solution 2: Handle response body

```go
resp, err := client.Get(url)
if err != nil { return err }
defer resp.Body.Close()
data, err := io.ReadAll(resp.Body)
```

### Solution 3: Follow redirects

```go
// Default client follows up to 10 redirects
client := &http.Client{
    CheckRedirect: func(req *http.Request, via []*http.Request) error {
        if len(via) >= 5 { return fmt.Errorf("too many redirects") }
        return nil
    },
}
```

### Solution 4: Use request context

```go
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
resp, err := client.Do(req)
```

## Common Scenarios

- HTTP client hangs because timeout is not configured
- Connection pool is exhausted causing errors under load
- Response body is not closed causing connection leak

## Prevent It

- Always set a Timeout on http.Client
- Close response body with defer after every request
- Configure Transport pool sizes for your expected concurrency
