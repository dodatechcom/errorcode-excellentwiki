---
title: "[Solution] Go DNS Resolution Failure Fix"
description: "Fix Go dial tcp lookup no such host error. Configure DNS servers, handle DNS failures, and use custom resolvers."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["dns", "resolve", "lookup", "network", "tcp", "runtime"]
weight: 5
---

# DNS Resolution Failure Fix

The `dial tcp: lookup: no such host` error occurs when Go cannot resolve a domain name to an IP address.

## Description

When making outbound HTTP or TCP connections, Go uses the system's DNS resolver (or a custom one) to translate hostnames to IP addresses. If the DNS server is unreachable, the hostname doesn't exist, or DNS configuration is wrong, the lookup fails.

Common scenarios:

- **Hostname doesn't exist** — typo in the domain name.
- **DNS server unreachable** — corporate firewall blocking DNS.
- **Network not connected** — running in an environment without internet.
- **Custom DNS not configured** — Docker container or k8s pod with wrong resolv.conf.

## Common Causes

```go
// Cause 1: Typo in hostname
resp, err := http.Get("https://examle.com") // should be example.com

// Cause 2: DNS not available in container
func main() {
    // In Docker without DNS
    resp, err := http.Get("https://api.service.local")
    if err != nil {
        log.Fatal(err) // no such host
    }
}

// Cause 3: Network not connected
func main() {
    resp, err := http.Get("https://www.google.com")
    // Fails if no network
}

// Cause 4: Custom resolver not configured
func main() {
    resolver := &net.Resolver{
        PreferGo: true,
    }
    // Using default when custom is needed
    addrs, err := resolver.LookupHost(context.Background(), "internal.service")
    _ = addrs
    _ = err
}
```

## How to Fix

### Fix 1: Configure custom DNS resolver

```go
func main() {
    dialer := &net.Dialer{
        Resolver: &net.Resolver{
            PreferGo: true,
            Dial: func(ctx context.Context, network, address string) (net.Conn, error) {
                d := net.Dialer{}
                return d.DialContext(ctx, "udp", "8.8.8.8:53")
            },
        },
    }
    transport := &http.Transport{
        DialContext: dialer.DialContext,
    }
    client := &http.Client{Transport: transport}
    resp, err := client.Get("https://api.example.com")
    _ = resp
    _ = err
}
```

### Fix 2: Validate hostname before connecting

```go
func isValidHost(host string) bool {
    _, err := net.LookupHost(host)
    return err == nil
}

func main() {
    host := "api.example.com"
    if !isValidHost(host) {
        log.Fatal("DNS lookup failed for:", host)
    }
}
```

### Fix 3: Retry with backoff

```go
func fetchWithRetry(url string, maxRetries int) (*http.Response, error) {
    var lastErr error
    for i := 0; i < maxRetries; i++ {
        resp, err := http.Get(url)
        if err == nil {
            return resp, nil
        }
        lastErr = err
        time.Sleep(time.Duration(i+1) * time.Second)
    }
    return nil, lastErr
}
```

### Fix 4: Set DNS in Docker/Kubernetes

```yaml
# docker-compose.yml
services:
  app:
    dns:
      - 8.8.8.8
      - 8.8.4.4
```

## Examples

```go
// This triggers: dial tcp: lookup nonexistent.invalid: no such host
package main

import (
    "log"
    "net/http"
)

func main() {
    resp, err := http.Get("https://nonexistent.invalid")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
}
```

## Related Errors

- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused after DNS resolves.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — request times out.
- [tls-cert]({{< relref "/languages/go/tls-cert" >}}) — TLS handshake fails.
