---
title: "[Solution] Go Connection Refused Error Fix"
description: "Fix Go dial tcp connect connection refused error. Verify server is running, check port bindings, and handle network errors gracefully."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["net", "dial", "connection", "refused", "tcp", "runtime"]
weight: 5
---

# Connection Refused Error Fix

The `dial tcp: connect: connection refused` error occurs when a TCP connection attempt is rejected because no server is listening on the target address.

## Description

When a Go program tries to connect to a TCP address where no process is listening, the OS kernel sends a TCP RST (reset) packet, resulting in `ECONNREFUSED`. This means the target host is reachable, but the specific port has no listener.

Common scenarios:

- **Server not started** — client tries to connect before server is ready.
- **Server crashed** — process died but client still trying to connect.
- **Wrong port** — connecting to incorrect port number.
- **Server not listening on expected interface** — bound to `127.0.0.1` but connecting to `0.0.0.0`.

## Common Causes

```go
// Cause 1: Server not started yet
func main() {
    resp, err := http.Get("http://localhost:8080/api")
    // Server not running on port 8080
}

// Cause 2: Wrong port
func main() {
    resp, err := http.Get("http://localhost:8081/api")
    // Server is on 8080, not 8081
}

// Cause 3: Server bound to different interface
func main() {
    // Server listens on 127.0.0.1:3000
    // Client connects to 0.0.0.0:3000
    resp, err := http.Get("http://192.168.1.100:3000/api")
}

// Cause 4: Server crashed between health check and request
func main() {
    healthCheck() // passes
    // Server crashes here
    makeRequest() // connection refused
}
```

## How to Fix

### Fix 1: Retry with exponential backoff

```go
func connectWithRetry(url string, maxRetries int) (*http.Response, error) {
    var lastErr error
    for i := 0; i < maxRetries; i++ {
        resp, err := http.Get(url)
        if err == nil {
            return resp, nil
        }
        lastErr = err
        time.Sleep(time.Duration(1<<uint(i)) * 100 * time.Millisecond)
    }
    return nil, lastErr
}
```

### Fix 2: Wait for server readiness

```go
func waitForServer(addr string, timeout time.Duration) error {
    deadline := time.Now().Add(timeout)
    for time.Now().Before(deadline) {
        conn, err := net.Dial("tcp", addr)
        if err == nil {
            conn.Close()
            return nil
        }
        time.Sleep(100 * time.Millisecond)
    }
    return fmt.Errorf("server not ready at %s", addr)
}
```

### Fix 3: Verify server binding address

```go
func main() {
    ln, err := net.Listen("tcp", ":8080")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Server listening on:", ln.Addr())
    http.Serve(ln, nil)
}
```

### Fix 4: Use environment variables for addresses

```go
func getServerAddr() string {
    addr := os.Getenv("SERVER_ADDR")
    if addr == "" {
        addr = "localhost:8080"
    }
    return addr
}
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
    _, err := http.Get("http://127.0.0.1:9999")
    fmt.Println(err) // connection refused
}
```

## Related Errors

- [dns-resolve]({{< relref "/languages/go/dns-resolve" >}}) — DNS lookup failure.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — connection established but request times out.
- [http-listen]({{< relref "/languages/go/http-listen" >}}) — port already in use.
