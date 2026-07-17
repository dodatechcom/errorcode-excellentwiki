---
title: "[Solution] Go HTTP Listen Address Already in Use Fix"
description: "Fix Go listen tcp bind: address already in use error. Find and kill the process using the port, use SO_REUSEADDR, or pick a different port."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Listen TCP: Bind: Address Already in Use — Fix

This error occurs when your Go program tries to listen on a TCP port that is already in use by another process.

## Description

When you call `net.Listen("tcp", ":8080")` or start an HTTP server, the OS checks if the port is available. If another process (or a previous instance of your program) is already bound to that port, the bind call fails with `bind: address already in use`.

Common scenarios:

- **Previous instance still running** — the old server process didn't shut down cleanly.
- **Another application using the port** — a different service is bound to the same port.
- **TIME_WAIT state** — the port was recently used and is in the TCP TIME_WAIT state.
- **SO_REUSEADDR not set** — the socket option isn't enabled (default in Go is usually fine).

## Common Causes

```go
// Cause 1: Previous instance still running
// Terminal 1: go run server.go (running)
// Terminal 2: go run server.go (fails — port 8080 in use)

// Cause 2: Another process using the port
// If nginx or another service is on port 8080
ln, err := net.Listen("tcp", ":8080")
// err: listen tcp :8080: bind: address already in use

// Cause 3: Rapid restart with SO_REUSEADDR issues
// Server crashes and restarts quickly
// Port may be in TIME_WAIT state

// Cause 4: Multiple goroutines trying to bind
for i := 0; i < 10; i++ {
    go func() {
        ln, err := net.Listen("tcp", ":8080") // Only one succeeds
        if err != nil {
            log.Fatal(err)
        }
        _ = ln
    }()
}
```

## How to Fix

### Fix 1: Find and kill the process using the port

```bash
# Linux/macOS
lsof -i :8080
# or
ss -tlnp | grep 8080
# or
netstat -tlnp | grep 8080

# Kill the process
kill -9 <PID>
```

### Fix 2: Use a different port

```go
// Wrong — hardcoded port
ln, err := net.Listen("tcp", ":8080")

// Correct — try multiple ports or use 0 for random available port
func listenOnAvailablePort() (net.Listener, error) {
    for port := 8080; port < 9000; port++ {
        addr := fmt.Sprintf(":%d", port)
        ln, err := net.Listen("tcp", addr)
        if err == nil {
            return ln, nil
        }
    }
    return nil, fmt.Errorf("no available port found")
}
```

### Fix 3: Set SO_REUSEADDR before binding

```go
// Correct — set socket options
func main() {
    ln, err := net.Listen("tcp", ":8080")
    if err != nil {
        log.Fatal(err)
    }
    defer ln.Close()

    // For raw sockets, set SO_REUSEADDR:
    // Use syscall or golang.org/x/net for SO_REUSEADDR
}
```

### Fix 4: Graceful shutdown

```go
// Wrong — hard kill leaves port in TIME_WAIT
func main() {
    http.ListenAndServe(":8080", nil)
}

// Correct — graceful shutdown
func main() {
    srv := &http.Server{Addr: ":8080"}

    go func() {
        if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
            log.Fatal(err)
        }
    }()

    // Wait for interrupt signal
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    srv.Shutdown(ctx)
}
```

### Fix 5: Use port 0 for tests

```go
// Correct — use random available port for testing
func startTestServer() (string, func()) {
    ln, _ := net.Listen("tcp", ":0")
    addr := ln.Addr().String()

    srv := &http.Server{Handler: handler}
    go srv.Serve(ln)

    return addr, func() {
        srv.Shutdown(context.Background())
    }
}
```

## Examples

```go
// This triggers: listen tcp :8080: bind: address already in use
package main

import "net/http"

func main() {
    // Assume something else is on port 8080
    http.ListenAndServe(":8080", nil)
}
```

## Related Errors

- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused when connecting to a port.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP client timeout.
- [context-canceled]({{< relref "/languages/go/context-canceled" >}}) — context was canceled.
