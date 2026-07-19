---
title: "[Solution] Go connection reset by peer — Network Error Fix"
description: "Fix Go connection reset by peer error. Handle TCP RST signals."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# connection reset by peer

The error `read tcp ...: read: connection reset by peer` occurs when the remote side sends a TCP RST packet.

## Common Causes

- **Server crashed or restarted** — the remote process exited
- **Firewall timeout** — an intermediate device killed the connection
- **HTTP keep-alive stale** — reusing a closed connection

## How to Fix

### Fix 1: Retry on reset

```go
for i := 0; i < maxRetries; i++ {
    resp, err := client.Do(req)
    if err == nil { return resp, nil }
    if !errors.Is(err, syscall.ECONNRESET) { return nil, err }
    time.Sleep(time.Duration(i+1) * 100 * time.Millisecond)
}
```

### Fix 2: Disable HTTP keep-alive

```go
client := &http.Client{
    Transport: &http.Transport{ DisableKeepAlives: true },
}
```

## Examples

```go
package main

import (
    "fmt"
    "net"
    "time"
)

func main() {
    conn, err := net.DialTimeout("tcp", "example.com:80", 5*time.Second)
    if err != nil { fmt.Println(err); return }
    defer conn.Close()
    conn.SetDeadline(time.Now().Add(2 * time.Second))
    _, err = conn.Write([]byte("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"))
    fmt.Println(err)
}
```

## Related Errors

- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
- [broken-pipe]({{< relref "/languages/go/broken-pipe" >}}) — broken pipe.
