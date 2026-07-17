---
title: "[Solution] Go TLS Handshake Timeout Fix"
description: "Fix Go net/http TLS handshake timeout error. Configure TLS settings, check certificates, and handle network issues during handshake."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# TLS Handshake Timeout Fix

The `net/http: TLS handshake timeout` error occurs when the TLS handshake between client and server takes longer than the configured timeout.

## Description

TLS handshake involves certificate exchange, key negotiation, and cipher suite agreement. This process can be slow due to network latency, large certificate chains, or server performance issues. Go's `http.Transport` has a `TLSHandshakeTimeout` that defaults to 10 seconds. If the handshake doesn't complete in time, the connection is closed.

Common scenarios:

- **Large certificate chain** — server presents many intermediate certificates.
- **Slow server** — server CPU-bound during key exchange.
- **Network congestion** — high latency on TLS negotiation.
- **Certificate revocation check** — server performing CRL/OCSP checks.
- **Client certificate requested** — mutual TLS adds extra round trips.

## Common Causes

```go
// Cause 1: Default timeout too short for slow networks
func main() {
    client := &http.Client{
        Transport: &http.Transport{
            TLSHandshakeTimeout: 2 * time.Second, // too short
        },
    }
    _, err := client.Get("https://slow-tls-server.example.com")
}

// Cause 2: Client certificate negotiation slow
func main() {
    cert, _ := tls.LoadX509KeyPair("client.crt", "client.key")
    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                Certificates: []tls.Certificate{cert},
            },
            TLSHandshakeTimeout: 5 * time.Second,
        },
    }
}

// Cause 3: Server presenting invalid certificate
func main() {
    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                InsecureSkipVerify: false,
            },
        },
    }
    // Server cert validation may delay handshake
}

// Cause 4: No keepalive, re-handshaking every request
func main() {
    transport := &http.Transport{
        DisableKeepAlives: true, // forces new TLS handshake per request
    }
    client := &http.Client{Transport: transport}
}
```

## How to Fix

### Fix 1: Increase TLS handshake timeout

```go
client := &http.Client{
    Transport: &http.Transport{
        TLSHandshakeTimeout: 30 * time.Second,
    },
}
```

### Fix 2: Use connection pooling with keepalive

```go
client := &http.Client{
    Transport: &http.Transport{
        MaxIdleConns:        100,
        MaxIdleConnsPerHost: 10,
        IdleConnTimeout:     90 * time.Second,
        TLSHandshakeTimeout: 10 * time.Second,
    },
}
```

### Fix 3: Pre-load root certificates

```go
func main() {
    caCert, _ := os.ReadFile("ca-bundle.crt")
    caCertPool := x509.NewCertPool()
    caCertPool.AppendCertsFromPEM(caCert)

    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                RootCAs: caCertPool,
            },
        },
    }
}
```

### Fix 4: Use InsecureSkipVerify for development

```go
// Development only
client := &http.Client{
    Transport: &http.Transport{
        TLSClientConfig: &tls.Config{
            InsecureSkipVerify: true,
        },
        TLSHandshakeTimeout: 5 * time.Second,
    },
}
```

## Examples

```go
// This triggers: net/http: TLS handshake timeout
package main

import (
    "fmt"
    "net/http"
    "time"
)

func main() {
    client := &http.Client{
        Transport: &http.Transport{
            TLSHandshakeTimeout: 1 * time.Millisecond,
        },
    }
    _, err := client.Get("https://www.google.com")
    fmt.Println(err) // TLS handshake timeout
}
```

## Related Errors

- [tls-cert]({{< relref "/languages/go/tls-cert" >}}) — certificate not standards compliant.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — general HTTP request timeout.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused.
