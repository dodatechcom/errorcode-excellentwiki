---
title: "[Solution] Go http: Server closed — Network Error Fix"
description: "Fix Go http: Server closed error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# http: Server closed

The error `http: Server closed` occurs when you try to serve after the server has been closed.

## How to Fix

### Fix 1: Check for ErrServerClosed

```go
if err := server.Serve(listener); err != http.ErrServerClosed {
    log.Fatal(err)
}
```

## Examples

```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    server := &http.Server{Addr: ":8080"}
    server.Close()
    err := server.ListenAndServe()
    fmt.Println(err)
}
```

Output:
```
http: Server closed
```

## Related Errors

- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
- [http-timeout]({{< relref "/languages/go/http-timeout" >}}) — HTTP timeout.
