---
title: "[Solution] Go Dial TCP Connection Refused — Runtime Error Fix"
description: "Fix Go dial tcp connection refused errors. Troubleshoot network connectivity, port availability, and service availability."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Dial TCP: Connection Refused

The error `dial tcp: connection refused` occurs when your Go program attempts to establish a TCP connection to a host and port, but the target host actively rejects the connection. The target service is not listening on the expected port.

## Description

A connection refused error means the TCP three-way handshake failed because no process is listening on the destination port. Unlike a timeout (which suggests the host is unreachable or slow), a refused connection indicates the host is reachable but the service is down or misconfigured.

This is one of the most common network errors in Go microservices, database connections, and API integrations.

## Common Causes

- **Service not running** — the target process has not started or has crashed
- **Wrong port number** — the application is listening on a different port than expected
- **Firewall blocking** — local or remote firewall dropping connections
- **Bind address mismatch** — service bound to `127.0.0.1` but client connects to external IP

## How to Fix

### Fix 1: Verify the service is running

```bash
# Check if the service is listening
ss -tlnp | grep :8080
# or
netstat -tlnp | grep :8080
```

### Fix 2: Use connection retry with backoff

```go
func connectWithRetry(addr string, maxRetries int) (net.Conn, error) {
    var conn net.Conn
    var err error
    for i := 0; i < maxRetries; i++ {
        conn, err = net.DialTimeout("tcp", addr, 5*time.Second)
        if err == nil {
            return conn, nil
        }
        time.Sleep(time.Duration(i+1) * time.Second)
    }
    return nil, fmt.Errorf("failed after %d retries: %w", maxRetries, err)
}
```

### Fix 3: Validate the address before connecting

```go
func validateAddress(addr string) error {
    host, port, err := net.SplitHostPort(addr)
    if err != nil {
        return fmt.Errorf("invalid address: %w", err)
    }
    if host == "" {
        return fmt.Errorf("host cannot be empty")
    }
    if port == "" {
        return fmt.Errorf("port cannot be empty")
    }
    return nil
}
```

### Fix 4: Use context with timeout for connections

```go
func connect(ctx context.Context, addr string) (net.Conn, error) {
    dialer := &net.Dialer{Timeout: 5 * time.Second}
    return dialer.DialContext(ctx, "tcp", addr)
}
```

## Examples

```go
package main

import (
    "fmt"
    "net"
)

func main() {
    conn, err := net.Dial("tcp", "localhost:9999")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer conn.Close()
}
```

Output:
```
dial tcp 127.0.0.1:9999: connection refused
```

## Related Errors

- [net-dial]({{< relref "/languages/go/net-dial" >}}) — general TCP dial failures.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP-level timeouts.
- [dns-resolve]({{< relref "/languages/go/dns-resolve" >}}) — DNS resolution failures before connection.
