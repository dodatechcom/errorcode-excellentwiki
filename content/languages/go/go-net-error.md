---
title: "[Solution] Go net Error — How to Fix"
description: "Fix Go net errors. Handle TCP/UDP connections, DNS resolution, timeouts, and network configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go net Error

Fix Go net errors. Handle TCP/UDP connections, DNS resolution, timeouts, and network configuration.

## Why It Happens

- Connection is refused because the target port is not listening
- DNS resolution fails because of network configuration issues
- Connection times out because of too short timeout settings
- Connection is reset because the server closed the connection

## Common Error Messages

```
dial tcp: connection refused
```
```
lookup: no such host
```
```
i/o timeout
```
```
connection reset by peer
```

## How to Fix It

### Solution 1: Create TCP connection with timeout

```go
conn, err := net.DialTimeout("tcp", "host:8080", 5*time.Second)
if err != nil { log.Fatal(err) }
defer conn.Close()
```

### Solution 2: Configure DNS resolution

```go
resolver := &net.Resolver{
    PreferGo: true,
    Dial: func(ctx context.Context, network, address string) (net.Conn, error) {
        return net.Dial("udp", "8.8.8.8:53")
    },
}
addrs, _ := resolver.LookupHost(ctx, "example.com")
```

### Solution 3: Set connection deadlines

```go
conn, _ := net.Dial("tcp", "host:8080")
conn.SetDeadline(time.Now().Add(5 * time.Second))
conn.SetReadDeadline(time.Now().Add(30 * time.Second))
conn.SetWriteDeadline(time.Now().Add(30 * time.Second))
```

### Solution 4: Handle connection reuse

```go
client := &http.Client{
    Transport: &http.Transport{
        MaxIdleConns:        100,
        MaxIdleConnsPerHost: 10,
        IdleConnTimeout:     90 * time.Second,
    },
}
```

## Common Scenarios

- Connection to database is refused because the port is wrong
- DNS resolution fails because the resolver is not reachable
- HTTP client connections are not being reused causing high latency

## Prevent It

- Use net.DialTimeout for connections with timeouts
- Configure custom DNS resolver for reliable resolution
- Tune http.Transport settings for connection reuse
