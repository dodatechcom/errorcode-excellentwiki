---
title: "[Solution] Go TLS Certificate Not Standards Compliant Fix"
description: "Fix Go tls certificate is not standards compliant error. Configure valid TLS certificates, use trusted CAs, and handle certificate chain issues."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# TLS Certificate Not Standards Compliant Fix

The `tls: certificate is not standards compliant` error occurs when a TLS certificate fails to meet the standards required by Go's crypto/tls package.

## Description

Go enforces strict TLS certificate validation. A certificate is rejected if it uses deprecated algorithms, has invalid key sizes, or doesn't conform to RFC 5280 and related standards. This error is stricter than many other TLS implementations.

Common scenarios:

- **Self-signed certificate with weak key** — using RSA keys smaller than 1024 bits.
- **SHA-1 signed certificate** — Go rejects SHA-1 signatures.
- **Missing required extensions** — certificate lacks Subject Alternative Names.
- **Expired certificate** — certificate has passed its validity period.
- **Untrusted certificate chain** — intermediate CA not in system trust store.

## Common Causes

```go
// Cause 1: Connecting to server with weak certificate
func main() {
    resp, err := https.Get("https://weak-cert.example.com")
    // Error: tls: certificate is not standards compliant
    _ = resp
    _ = err
}

// Cause 2: Custom TLS config with wrong min version
func main() {
    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                MinVersion: tls.VersionSSL30, // deprecated, rejected
            },
        },
    }
    _, err := client.Get("https://api.example.com")
    _ = err
}

// Cause 3: Self-signed cert with SHA-1
func generateBadCert() {
    template := &x509.Certificate{
        SignatureAlgorithm: x509.SHA1WithRSA, // deprecated
    }
    // Go rejects SHA-1 signed certificates
}

// Cause 4: Server presenting cert with wrong key usage
func main() {
    tlsConfig := &tls.Config{
        InsecureSkipVerify: false,
    }
    // Server cert doesn't have ServerAuth key usage
}
```

## How to Fix

### Fix 1: Use TLS 1.2+ with strong cipher suites

```go
client := &http.Client{
    Transport: &http.Transport{
        TLSClientConfig: &tls.Config{
            MinVersion: tls.VersionTLS12,
            CipherSuites: []uint16{
                tls.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384,
                tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
            },
        },
    },
}
```

### Fix 2: Generate certificates with SHA-256 and valid key sizes

```go
template := &x509.Certificate{
    SerialNumber: big.NewInt(1),
    NotBefore:    time.Now(),
    NotAfter:     time.Now().Add(365 * 24 * time.Hour),
    KeyUsage:     x509.KeyUsageDigitalSignature,
    ExtKeyUsage:  []x509.ExtKeyUsage{x509.ExtKeyUsageServerAuth},
}

key, _ := rsa.GenerateKey(rand.Reader, 2048)
certDER, _ := x509.CreateCertificate(rand.Reader, template, template, &key.PublicKey, key)
```

### Fix 3: Add custom CA to trust store

```go
caCert, _ := os.ReadFile("ca.pem")
caCertPool := x509.NewCertPool()
caCertPool.AppendCertsFromPEM(caCert)

client := &http.Client{
    Transport: &http.Transport{
        TLSClientConfig: &tls.Config{
            RootCAs: caCertPool,
        },
    },
}
```

### Fix 4: Skip verification for development only

```go
// Development only — never in production
client := &http.Client{
    Transport: &http.Transport{
        TLSClientConfig: &tls.Config{
            InsecureSkipVerify: true,
        },
    },
}
```

## Examples

```go
// This triggers: tls: certificate is not standards compliant
package main

import (
    "crypto/tls"
    "log"
    "net/http"
)

func main() {
    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                MinVersion: tls.VersionTLS10, // deprecated
            },
        },
    }
    _, err := client.Get("https://api.example.com")
    if err != nil {
        log.Fatal(err)
    }
}
```

## Related Errors

- [dns-resolve]({{< relref "/languages/go/dns-resolve" >}}) — DNS lookup failure before TLS.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP request timeout.
- [net-http-close]({{< relref "/languages/go/net-http-close" >}}) — TLS handshake timeout.
