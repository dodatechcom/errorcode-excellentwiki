---
title: "[Solution] Go net: dial tcp timeout — Network Error Fix"
description: "Fix Go dial timeout error. Configure timeouts and connection parameters."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# net: dial tcp timeout

The error `dial tcp: i/o timeout` occurs when a TCP connection attempt exceeds the timeout.

## Common Causes

- **Network unreachable** — target host is not accessible
- **DNS resolution slow** — DNS lookup taking too long
- **Firewall blocking** — packets being dropped

## How to Fix

### Fix 1: Increase timeout

```go
conn, err := net.DialTimeout("tcp", "example.com:80", 10*time.Second)
```

### Fix 2: Use context with timeout

```go
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
var d net.Dialer
conn, err := d.DialContext(ctx, "tcp", "host:port")
```

## Related Errors

- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
- [context-deadline]({{< relref "/languages/go/context-deadline" >}}) — context deadline.
