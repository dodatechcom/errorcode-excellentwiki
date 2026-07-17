---
title: "[Solution] Go TLS Certificate Error Fix"
description: "Fix Go tls: certificate is not standards compliant error. Configure TLS properly, use valid certificates, and disable verification for testing only."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# TLS: Certificate Is Not Standards Compliant — Fix

A TLS certificate error occurs when the server presents a certificate that doesn't meet TLS standards, or the client's TLS configuration rejects it.

## Description

Go's `crypto/tls` package enforces strict certificate validation by default. When a server presents an invalid, expired, self-signed, or non-compliant certificate, the TLS handshake fails with an error like `tls: certificate is not standards compliant`.

Common scenarios:

- **Expired certificate** — server certificate has passed its expiry date.
- **Self-signed certificate** — not signed by a trusted CA.
- **Hostname mismatch** — certificate CN/SAN doesn't match the hostname.
- **Missing intermediate certificates** — server doesn't send the full chain.
- **Weak TLS version or cipher** — server uses deprecated TLS 1.0 or weak ciphers.

## Common Causes

```go
// Cause 1: Connecting to server with expired cert
resp, err := http.Get("https://expired.example.com")

// Cause 2: Self-signed certificate in development
resp, err := http.Get("https://localhost:8443")

// Cause 3: Certificate hostname mismatch
// Certificate is for "*.example.com" but connecting to "test.other.com"
resp, err := http.Get("https://test.other.com")

// Cause 4: Weak TLS configuration
tlsConfig := &tls.Config{
    MinVersion: tls.VersionTLS10, // Deprecated, weak
}
```

## How to Fix

### Fix 1: Skip certificate verification for development (NOT for production)

```go
// Wrong — skips ALL verification (insecure in production)
tr := &http.Transport{
    TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
}
client := &http.Client{Transport: tr}
resp, err := client.Get("https://localhost:8443")

// Correct — only for development/testing
// Add a build tag or environment check
if os.Getenv("ENV") == "development" {
    tr := &http.Transport{
        TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    client = &http.Client{Transport: tr}
}
```

### Fix 2: Use proper certificates in production

```go
// Correct — load CA certificate
caCert, err := os.ReadFile("ca.pem")
if err != nil {
    log.Fatal(err)
}

caCertPool := x509.NewCertPool()
caCertPool.AppendCertsFromPEM(caCert)

tr := &http.Transport{
    TLSClientConfig: &tls.Config{
        RootCAs:    caCertPool,
        MinVersion: tls.VersionTLS12,
    },
}
client := &http.Client{Transport: tr}
```

### Fix 3: Regenerate expired or invalid certificates

```bash
# Generate self-signed cert for development
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# Generate with SAN for localhost
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes \
    -subj "/CN=localhost" \
    -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"
```

### Fix 4: Configure TLS with proper minimum version

```go
// Wrong — allows weak TLS versions
config := &tls.Config{
    MinVersion: tls.VersionTLS10,
}

// Correct — require TLS 1.2 or higher
config := &tls.Config{
    MinVersion: tls.VersionTLS12,
    CipherSuites: []uint16{
        tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
        tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
    },
}
```

### Fix 5: Use system certificate pool

```go
import "crypto/tls"

// Correct — use system roots
config := &tls.Config{
    RootCAs: nil, // nil means use system certificates
}
```

## Examples

```go
// This triggers: tls: certificate is not standards compliant
package main

import (
    "crypto/tls"
    "fmt"
    "net/http"
)

func main() {
    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                MinVersion: tls.VersionTLS10,
            },
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

- [dns-resolve]({{< relref "/languages/go/dns-resolve" >}}) — DNS resolution failure before TLS.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP client timeout.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused.
