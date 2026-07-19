---
title: "[Solution] Go DNS lookup failure — Network Error Fix"
description: "Fix Go DNS lookup failure error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# DNS lookup failure

The error `lookup example.com on 127.0.0.53:53: no such host` occurs when DNS resolution fails.

## Common Causes

- **DNS server down** — configured DNS server is unreachable
- **Domain doesn't exist** — typo in hostname
- **Network issue** — no network connectivity

## How to Fix

### Fix 1: Use custom resolver

```go
r := &net.Resolver{
    PreferGo: true,
    Dial: func(ctx context.Context, network, address string) (net.Conn, error) {
        d := net.Dialer{Timeout: 5 * time.Second}
        return d.DialContext(ctx, "udp", "8.8.8.8:53")
    },
}
ips, err := r.LookupHost(ctx, "example.com")
```

## Related Errors

- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
- [net-dial-timeout]({{< relref "/languages/go/net-dial-timeout" >}}) — dial timeout.
