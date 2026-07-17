---
title: "[Solution] Go Connection Refused Error Fix"
description: "Fix Go dial tcp connect: connection refused error. Check server status, verify port, and handle connection errors with retry logic."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Dial TCP: Connect: Connection Refused — Fix

A connection refused error occurs when your Go program tries to connect to a TCP port where no service is listening.

## Description

When you dial a TCP address and no process is listening on that port, the operating system returns a "connection refused" (RST packet). Go reports this as `dial tcp [ip]:port: connect: connection refused`.

Common scenarios:

- **Server not running** — connecting to a port where nothing is listening.
- **Wrong port number** — server is on a different port.
- **Server crashed** — was running but has terminated.
- **Firewall blocking** — firewall drops connections without sending RST.
- **Server backlog full** — too many pending connections.

## Common Causes

```go
// Cause 1: Server not running
resp, err := http.Get("http://localhost:8080/api")
// dial tcp 127.0.0.1:8080: connect: connection refused

// Cause 2: Wrong port
resp, err := http.Get("http://localhost:3000/api")
// Server actually runs on port 5000

// Cause 3: Server crashed between checks
if isServerRunning() {
    resp, err := http.Get("http://localhost:8080/api") // May fail if server crashed
}

// Cause 4: Connection to wrong host
resp, err := http.Get("http://192.168.1.999:8080/api")
// Host doesn't exist or is unreachable
```

## How to Fix

### Fix 1: Check if server is reachable before connecting

```go
// Wrong — assumes server is up
resp, err := http.Get("http://localhost:8080/api")

// Correct — check first
func isServerUp(addr string, timeout time.Duration) bool {
    conn, err := net.DialTimeout("tcp", addr, timeout)
    if err != nil {
        return false
    }
    conn.Close()
    return true
}

if isServerUp("localhost:8080", 2*time.Second) {
    resp, err := http.Get("http://localhost:8080/api")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
} else {
    fmt.Println("server is not running")
}
```

### Fix 2: Use retry with exponential backoff

```go
func fetchWithRetry(url string, maxRetries int) (*http.Response, error) {
    var lastErr error
    for i := 0; i < maxRetries; i++ {
        resp, err := http.Get(url)
        if err == nil {
            return resp, nil
        }
        lastErr = err
        wait := time.Duration(1<<uint(i)) * time.Second
        log.Printf("attempt %d failed: %v, retrying in %v", i+1, err, wait)
        time.Sleep(wait)
    }
    return nil, lastErr
}
```

### Fix 3: Handle connection errors in HTTP handlers

```go
func proxyHandler(w http.ResponseWriter, r *http.Request) {
    resp, err := http.Get("http://backend:8080" + r.URL.Path)
    if err != nil {
        if opErr, ok := err.(*net.OpError); ok {
            if opErr.Err.Error() == "connect: connection refused" {
                http.Error(w, "backend unavailable", http.StatusBadGateway)
                return
            }
        }
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    defer resp.Body.Close()
    io.Copy(w, resp.Body)
}
```

### Fix 4: Use timeout on dial

```go
// Wrong — no timeout, may hang
conn, err := net.Dial("tcp", "remote-host:8080")

// Correct — use timeout
conn, err := net.DialTimeout("tcp", "remote-host:8080", 5*time.Second)
if err != nil {
    log.Printf("connection failed: %v", err)
}
```

### Fix 5: Verify port with net.LookupPort

```go
// Correct — verify the port number
port, err := net.LookupPort("tcp", "8080")
if err != nil {
    log.Printf("invalid port: %v", err)
}
fmt.Printf("port: %d\n", port)
```

## Examples

```go
// This triggers: dial tcp 127.0.0.1:9999: connect: connection refused
package main

import (
    "fmt"
    "net/http"
)

func main() {
    resp, err := http.Get("http://127.0.0.1:9999/api")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer resp.Body.Close()
}
```

## Related Errors

- [http-listen]({{< relref "/languages/go/http-listen" >}}) — address already in use when starting server.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP client timeout.
- [dns-resolve]({{< relref "/languages/go/dns-resolve" >}}) — DNS resolution failure.
