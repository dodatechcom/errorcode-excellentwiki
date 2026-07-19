---
title: "[Solution] Go bind: address already in use — Network Error Fix"
description: "Fix Go bind address already in use error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# bind: address already in use

The error `bind: address already in use` occurs when starting a server on a port already in use.

## How to Fix

### Fix 1: Find and kill the existing process

```bash
lsof -i :8080
kill -9 <PID>
```

### Fix 2: Use a different port

```go
listener, err := net.Listen("tcp", ":0") // let OS assign
```

## Examples

```go
package main

import (
    "fmt"
    "net"
)

func main() {
    l1, _ := net.Listen("tcp", ":8080")
    defer l1.Close()
    l2, err := net.Listen("tcp", ":8080")
    fmt.Println(err)
}
```

Output:
```
listen tcp :8080: bind: address already in use
```

## Related Errors

- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
- [http-server-closed]({{< relref "/languages/go/http-server-closed" >}}) — server closed.
