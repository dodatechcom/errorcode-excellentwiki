---
title: "[Solution] Go TLS Handshake Timeout Fix"
description: "Fix Go net/http TLS handshake timeout error. Configure TLS settings, check certificates, and handle slow TLS negotiations."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Net/HTTP: TLS Handshake Timeout — Fix

A TLS handshake timeout occurs when the TLS negotiation between client and server takes too long to complete.

## Description

Go's HTTP client has a `TLSHandshakeTimeout` in the transport configuration. When the TLS handshake (certificate exchange, key negotiation) exceeds this timeout, the connection fails. The default timeout is typically 10 seconds.

Common scenarios:

- **Slow server** — server takes too long to respond to TLS ClientHello.
- **Certificate issues** — server sends invalid or large certificate chain.
- **Network latency** — high latency slows TLS negotiation.
- **Version mismatch** — client and server disagree on TLS version.

## Common Causes

```go
// Cause 1: Default TLS timeout too short
transport := &http.Transport{
    TLSHandshakeTimeout: 1 * time.Second, // Too short
}
client := &http.Client{Transport: transport}
resp, err := client.Get("https://slow-server.com")

// Cause 2: Large certificate chain
// Server sends many intermediate certificates
client := &http.Client{
    Transport: &http.Transport{
        TLSHandshakeTimeout: 2 * time.Second,
    },
}

// Cause 3: TLS version negotiation failure
// Server only supports TLS 1.0, client requires 1.2

// Cause 4: Network latency causing slow handshake
client := &http.Client{
    Transport: &http.Transport{
        TLSHandshakeTimeout: 5 * time.Second,
    },
}
```

## How to Fix

### Fix 1: Increase TLS handshake timeout

```go
// Wrong — too short for high-latency connections
transport := &http.Transport{
    TLSHandshakeTimeout: 1 * time.Second,
}

// Correct — increase timeout
transport := &http.Transport{
    TLSHandshakeTimeout: 10 * time.Second,
}
client := &http.Client{Transport: transport}
```

### Fix 2: Configure TLS to skip problematic steps

```go
// For internal/testing connections
transport := &http.Transport{
    TLSClientConfig: &tls.Config{
        InsecureSkipVerify: true, // Skip certificate verification
        MinVersion:         tls.VersionTLS12,
    },
    TLSHandshakeTimeout: 10 * time.Second,
}
client := &http.Client{Transport: transport}
```

### Fix 3: Use connection pooling

```go
// Correct — reuse connections to avoid repeated handshakes
transport := &http.Transport{
    TLSHandshakeTimeout:   10 * time.Second,
    MaxIdleConns:          100,
    MaxIdleConnsPerHost:   10,
    IdleConnTimeout:       90 * time.Second,
    TLSClientConfig: &tls.Config{
        MinVersion: tls.VersionTLS12,
    },
}
client := &http.Client{Transport: transport}
```

### Fix 4: Pre-warm connections

```go
// Correct — establish connections before using them
func warmUpTransport(addr string) error {
    conn, err := tls.DialWithDialer(
        &net.Dialer{Timeout: 5 * time.Second},
        "tcp", addr,
        &tls.Config{MinVersion: tls.VersionTLS12},
    )
    if err != nil {
        return err
    }
    conn.Close()
    return nil
}
```

### Fix 5: Set appropriate TLS version

```go
// Wrong — may negotiate slow TLS version
transport := &http.Transport{
    TLSClientConfig: &tls.Config{
        MinVersion: tls.VersionTLS10,
    },
}

// Correct — require modern TLS
transport := &http.Transport{
    TLSClientConfig: &tls.Config{
        MinVersion: tls.VersionTLS12,
        CipherSuites: []uint16{
            tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
            tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
        },
    },
}
```

## Examples

```go
// This triggers: net/http: TLS handshake timeout
package main

import (
    "crypto/tls"
    "fmt"
    "net/http"
    "time"
)

func main() {
    client := &http.Client{
        Transport: &http.Transport{
            TLSHandshakeTimeout: 1 * time.Second,
        },
    }
    resp, err := client.Get("https://example.com")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer resp.Body.Close()
}
```

## Related Errors

- [tls-cert]({{< relref "/languages/go/tls-cert" >}}) — TLS certificate validation error.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — overall HTTP client timeout.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection refused.
