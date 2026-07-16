---
title: "[Solution] Go DNS Resolution Failed Fix"
description: "Fix Go dial tcp lookup: no such host DNS resolution error. Check DNS settings, hostname spelling, and network connectivity."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["dns", "resolve", "lookup", "network", "hostname"]
weight: 5
---

# Dial TCP: Lookup: No Such Host — DNS Resolution Fix

A DNS resolution failure occurs when Go cannot resolve a hostname to an IP address during a network connection.

## Description

When you dial a hostname (e.g., `http://api.example.com`), Go's net package performs a DNS lookup. If the DNS server cannot find the hostname, the lookup fails with `dial tcp: lookup example.com: no such host`.

Common scenarios:

- **Typo in hostname** — `exmaple.com` instead of `example.com`.
- **DNS server unreachable** — DNS server is down or not configured.
- **Hostname doesn't exist** — the domain hasn't been registered or has expired.
- **Local DNS misconfiguration** — `/etc/resolv.conf` has wrong nameservers.
- **Private/internal hostname** — hostname only resolves on internal DNS.

## Common Causes

```go
// Cause 1: Typo in hostname
resp, err := http.Get("http://exmaple.com") // "exmaple" is wrong

// Cause 2: Non-existent domain
resp, err := http.Get("http://this-domain-does-not-exist-12345.com")

// Cause 3: DNS server not reachable
// If /etc/resolv.conf points to a dead nameserver
resp, err := http.Get("http://example.com")

// Cause 4: Using hostname without DNS configured
// Running in a container without proper DNS setup
resp, err := http.Get("http://internal-service:8080")
```

## How to Fix

### Fix 1: Verify hostname spelling and existence

```go
// Wrong — typo
url := "http://exmaple.com/api"

// Correct — double-check hostname
url := "http://example.com/api"
```

### Fix 2: Use IP address directly for testing

```go
// Wrong — DNS lookup fails
resp, err := http.Get("http://example.com")

// Correct — use IP for testing (bypass DNS)
resp, err := http.Get("http://93.184.216.34")
// Or use Host header
req, _ := http.NewRequest("GET", "http://93.184.216.34/api", nil)
req.Host = "example.com"
resp, err := http.DefaultClient.Do(req)
```

### Fix 3: Handle DNS errors with retry

```go
func fetchWithRetry(url string, maxRetries int) (*http.Response, error) {
    var lastErr error
    for i := 0; i < maxRetries; i++ {
        resp, err := http.Get(url)
        if err == nil {
            return resp, nil
        }
        if strings.Contains(err.Error(), "no such host") {
            lastErr = err
            time.Sleep(time.Duration(i+1) * time.Second)
            continue
        }
        return nil, err
    }
    return nil, lastErr
}
```

### Fix 4: Check DNS configuration

```bash
# Linux/macOS — check resolv.conf
cat /etc/resolv.conf

# Test DNS resolution
nslookup example.com
dig example.com

# Check if DNS server is reachable
ping 8.8.8.8
```

### Fix 5: Configure custom DNS resolver

```go
import "net"

// Use custom DNS resolver
resolver := &net.Resolver{
    PreferGo: true,
    Dial: func(ctx context.Context, network, address string) (net.Conn, error) {
        d := net.Dialer{}
        return d.DialContext(ctx, "udp", "8.8.8.8:53")
    },
}

// Use resolver in a custom transport
transport := &http.Transport{
    DialContext: func(ctx context.Context, network, addr string) (net.Conn, error) {
        host, port, _ := net.SplitHostPort(addr)
        ips, _ := resolver.LookupHost(ctx, host)
        if len(ips) == 0 {
            return nil, fmt.Errorf("no IPs found for %s", host)
        }
        return net.Dial(network, net.JoinHostPort(ips[0], port))
    },
}

client := &http.Client{Transport: transport}
resp, err := client.Get("http://example.com")
```

## Examples

```go
// This triggers: dial tcp: lookup this-does-not-exist.com: no such host
package main

import (
    "fmt"
    "net/http"
)

func main() {
    resp, err := http.Get("http://this-does-not-exist.com")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer resp.Body.Close()
}
```

## Related Errors

- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused when connecting to a port.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP request timeout.
- [tls-cert]({{< relref "/languages/go/tls-cert" >}}) — TLS certificate validation error.
