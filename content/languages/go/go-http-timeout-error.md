---
title: "[Solution] Go HTTP Timeout Error — How to Fix"
description: "Fix Go HTTP timeout errors. Handle dial, TLS handshake, response header, and overall request timeouts with proper context control."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go HTTP Timeout Error

Fix Go HTTP timeout errors. Handle dial, TLS handshake, response header, and overall request timeouts with proper context control.

## Why It Happens

- The HTTP client timeout is set too low for the target service response time
- No context-based timeout is used so the request has no deadline
- DNS resolution is slow but no separate timeout is configured for dial phase
- The server takes longer than client timeout to start sending response headers

## Common Error Messages

```
context deadline exceeded (Client.Timeout or context timeout exceeded)
```
```
dial tcp <addr>: i/o timeout
```
```
TLS handshake timeout
```
```
net/http: timeout awaiting response headers
```

## How to Fix It

### Solution 1: Set layered timeouts for different phases

```go
client := &http.Client{
    Timeout: 30 * time.Second,
    Transport: &http.Transport{
        DialContext: (&net.Dialer{Timeout: 5*time.Second}).DialContext,
        TLSHandshakeTimeout: 10 * time.Second,
        ResponseHeaderTimeout: 10 * time.Second,
    },
}
```

### Solution 2: Use context for per-request timeouts

```go
ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
defer cancel()
req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
resp, err := client.Do(req)
```

### Solution 3: Implement retry with exponential backoff

```go
backoff := 1 * time.Second
for attempt := 0; attempt < 5; attempt++ {
    data, err := fetch(ctx, url)
    if err == nil { return data, nil }
    time.Sleep(backoff)
    backoff = min(backoff*2, 30*time.Second)
}
```

### Solution 4: Adjust timeouts based on operation type

```go
var clients = map[string]*http.Client{
    "fast":      {Timeout: 5*time.Second},
    "slow":      {Timeout: 120*time.Second},
    "streaming": {Timeout: 0},
}
```

## Common Scenarios

- An API gateway times out at 5s but upstream services take 10s to respond
- A file upload client times out because the timeout does not account for upload duration
- A microservice calls multiple endpoints but one slow call causes the entire chain to timeout

## Prevent It

- Set Transport-level timeouts (Dialer, TLSHandshake, ResponseHeader) separately from client-level timeout
- Use per-request context timeouts rather than relying on global client timeout
- Monitor P99 response times and set timeouts to at least 3x the normal response time
