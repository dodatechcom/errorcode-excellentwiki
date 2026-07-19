---
title: "[Solution] Go connection refused — Network Error Fix"
description: "Fix Go connection refused error. Ensure the target server is running."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# connection refused

The error `dial tcp [::1]:PORT: connect: connection refused` occurs when nothing is listening on the target address.

## Common Causes

- **Server not running** — the target service is not started
- **Wrong port** — connecting to the wrong port
- **Firewall blocking** — firewall rejecting connections

## How to Fix

### Fix 1: Verify the server is running

```bash
netstat -tlnp | grep :8080
```

### Fix 2: Add retry with backoff

```go
func dialWithRetry(addr string, maxRetries int) (net.Conn, error) {
    for i := 0; i < maxRetries; i++ {
        conn, err := net.DialTimeout("tcp", addr, 5*time.Second)
        if err == nil { return conn, nil }
        time.Sleep(time.Duration(1<<uint(i)) * time.Second)
    }
    return nil, fmt.Errorf("failed after %d retries", maxRetries)
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
    conn, err := net.Dial("tcp", "localhost:19999")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer conn.Close()
}
```

Output:
```
dial tcp [::1]:19999: connect: connection refused
```

## Related Errors

- [connection-reset]({{< relref "/languages/go/connection-reset" >}}) — connection reset.
- [broken-pipe]({{< relref "/languages/go/broken-pipe" >}}) — broken pipe.
