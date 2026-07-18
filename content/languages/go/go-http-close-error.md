---
title: "[Solution] Go HTTP Close Error — How to Fix"
description: "Fix Go HTTP connection close errors. Handle keep-alive, connection pool draining, body drain requirements, and server shutdown patterns."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go HTTP Close Error

Fix Go HTTP connection close errors. Handle keep-alive, connection pool draining, body drain requirements, and server shutdown patterns.

## Why It Happens

- Response body is not closed or drained preventing the connection from being returned to the pool
- The server closes connections before clients finish reading the response body
- Connection pool limits are reached because old connections are not being released
- HTTP/1.1 keep-alive connections are closed by the server during graceful shutdown

## Common Error Messages

```
http: response.Write on hijacked connection
```
```
write tcp <addr>: use of closed connection
```
```
http: proxy: connection reset by peer
```
```
net/http: HTTP/1.x transport connection broken
```

## How to Fix It

### Solution 1: Properly close and drain response bodies

```go
resp, err := client.Get(url)
if err != nil { return err }
defer resp.Body.Close()
_, err = io.Copy(io.Discard, resp.Body)
```

### Solution 2: Configure connection pool properly

```go
transport := &http.Transport{
    MaxIdleConns: 200, MaxIdleConnsPerHost: 20,
    IdleConnTimeout: 90 * time.Second,
}
defer transport.CloseIdleConnections()
```

### Solution 3: Handle connection close errors with retry

```go
for attempt := 0; attempt <= maxRetries; attempt++ {
    resp, err := client.Get(url)
    if err != nil && isConnectionError(err) { continue }
    body, _ := io.ReadAll(resp.Body)
    resp.Body.Close()
    return body, nil
}
```

### Solution 4: Gracefully close server connections during shutdown

```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
srv.Shutdown(ctx)
http.DefaultTransport.(*http.Transport).CloseIdleConnections()
```

## Common Scenarios

- A load balancer sees connection errors because clients do not drain response bodies
- An HTTP client exhausts the connection pool because idle connections are never released
- ['During server shutdown, clients receive connection reset errors because the server closes TCP connections']

## Prevent It

- Always close response bodies and drain them with io.Copy(io.Discard, resp.Body) for connection reuse
- Configure MaxIdleConnsPerHost and IdleConnTimeout on http.Transport for proper pool management
- Call transport.CloseIdleConnections() during application shutdown to clean up pooled connections
