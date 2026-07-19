---
title: "[Solution] Go broken pipe — Network Error Fix"
description: "Fix Go broken pipe error. Handle EPIPE signals when writing to closed connections."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# broken pipe

The error `write broken pipe` (EPIPE) occurs when you write to a pipe or socket whose read end has been closed.

## Common Causes

- **Client disconnected** — writing to a closed HTTP connection
- **Pipe reader closed** — the read end of an `os.Pipe` was closed

## How to Fix

### Fix 1: Check for broken pipe before writing

```go
func writeSafely(conn net.Conn, data []byte) error {
    conn.SetWriteDeadline(time.Now().Add(5 * time.Second))
    _, err := conn.Write(data)
    if errors.Is(err, syscall.EPIPE) {
        return fmt.Errorf("connection closed by peer")
    }
    return err
}
```

### Fix 2: Use signal.Ignore for SIGPIPE

```go
func init() { signal.Ignore(syscall.SIGPIPE) }
```

## Examples

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    r, w, _ := os.Pipe()
    r.Close()
    _, err := w.Write([]byte("hello"))
    fmt.Println(err)
}
```

Output:
```
write |1: broken pipe
```

## Related Errors

- [connection-reset]({{< relref "/languages/go/connection-reset" >}}) — connection reset.
- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
