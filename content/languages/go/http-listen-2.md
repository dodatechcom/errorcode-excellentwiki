---
title: "[Solution] Go HTTP Listen Address Already in Use Fix"
description: "Fix Go listen tcp bind address already in use error. Handle port reuse, use SO_REUSEADDR, and properly shut down servers."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# HTTP Listen — Address Already in Use Fix

The `listen tcp: bind: address already in use` error occurs when a Go program tries to start an HTTP server on a port that is already occupied.

## Description

Each TCP port can only be bound by one process at a time (unless `SO_REUSEADDR` or `SO_REUSEPORT` is configured). When a Go HTTP server starts with `http.ListenAndServe`, it binds to the specified port. If another process or a previous instance of the same program is already using that port, the bind fails.

Common scenarios:

- **Server not properly shut down** — previous instance still running after restart.
- **Port in TIME_WAIT state** — TCP connection hasn't fully closed after server stop.
- **Multiple server instances** — two copies of the program running simultaneously.
- **Port reserved by another service** — OS or another application using the same port.

## Common Causes

```go
// Cause 1: Server not gracefully shut down
func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
    // Previous instance may still hold port 8080
}

// Cause 2: Port in TIME_WAIT state
func main() {
    // Restart immediately after crash
    // Old connection may still be in TIME_WAIT
    log.Fatal(http.ListenAndServe(":8080", nil))
}

// Cause 3: Multiple goroutines starting servers
func main() {
    for i := 0; i < 3; i++ {
        go func() {
            http.ListenAndServe(":8080", nil) // only first succeeds
        }()
    }
}

// Cause 4: Testing with fixed port
func TestServer(t *testing.T) {
    go http.ListenAndServe(":8080", nil)
    go http.ListenAndServe(":8080", nil) // fails
}
```

## How to Fix

### Fix 1: Gracefully shut down the server

```go
func main() {
    server := &http.Server{Addr: ":8080", Handler: nil}

    go func() {
        sigint := make(chan os.Signal, 1)
        signal.Notify(sigint, os.Interrupt)
        <-sigint
        server.Shutdown(context.Background())
    }()

    log.Fatal(server.ListenAndServe())
}
```

### Fix 2: Use port 0 for dynamic port assignment (testing)

```go
func startServer(t *testing.T) string {
    listener, err := net.Listen("tcp", ":0")
    if err != nil {
        t.Fatal(err)
    }
    go http.Serve(listener, nil)
    return listener.Addr().String()
}
```

### Fix 3: Allow address reuse with SO_REUSEADDR

```go
func listenAndServe(addr string, handler http.Handler) error {
    ln, err := net.Listen("tcp", addr)
    if err != nil {
        // Try with reuse
        return http.ListenAndServe(addr, handler)
    }
    return http.Serve(ln, handler)
}
```

### Fix 4: Find and kill the existing process

```bash
# Find process using port 8080
lsof -i :8080
# or
ss -tlnp | grep 8080
# Then kill it
kill -9 <PID>
```

## Examples

```go
// This triggers: listen tcp :8080: bind: address already in use
package main

import (
    "log"
    "net/http"
)

func main() {
    // If another process is on :8080, this panics
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

## Related Errors

- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused when connecting.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP request times out.
- [context-canceled]({{< relref "/languages/go/context-canceled" >}}) — context canceled during operation.
