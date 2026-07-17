---
title: "[Solution] Go TLS Handshake Failure / Certificate Verify Failed — Runtime Error Fix"
description: "Fix Go TLS handshake failure and certificate verify failed errors. Configure certificates, skip verification for dev, and resolve certificate chain issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# TLS Handshake Failure / Certificate Verify Failed

The error `tls: handshake failure` or `x509: certificate signed by unknown authority` occurs when a TLS/SSL connection cannot be established due to certificate validation failure, protocol mismatch, or missing certificate configuration.

## Description

TLS (Transport Layer Security) requires both client and server to present valid certificates and agree on cipher suites. Handshake failures happen when the certificate chain is invalid, the certificate has expired, the hostname does not match, or the client and server cannot agree on a protocol version.

This is common in Go HTTP clients connecting to HTTPS services with self-signed certificates, expired certs, or incorrect TLS configuration.

## Common Causes

- **Self-signed certificate** — the certificate is not signed by a trusted CA
- **Expired certificate** — the server certificate has passed its validity period
- **Hostname mismatch** — the certificate CN/SAN does not match the connection hostname
- **Wrong TLS version** — client and server support incompatible TLS versions

## How to Fix

### Fix 1: Skip verification for development (not for production)

```go
func insecureClient() *http.Client {
    tr := &http.Transport{
        TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    return &http.Client{Transport: tr}
}
```

### Fix 2: Add custom CA certificates

```go
func customCAClient(caCertPath string) (*http.Client, error) {
    caCert, err := os.ReadFile(caCertPath)
    if err != nil {
        return nil, err
    }
    caCertPool := x509.NewCertPool()
    caCertPool.AppendCertsFromPEM(caCert)

    tr := &http.Transport{
        TLSClientConfig: &tls.Config{RootCAs: caCertPool},
    }
    return &http.Client{Transport: tr}, nil
}
```

### Fix 3: Configure client certificates for mutual TLS

```go
func mtlsClient(certFile, keyFile string) (*http.Client, error) {
    cert, err := tls.LoadX509KeyPair(certFile, keyFile)
    if err != nil {
        return nil, err
    }
    tr := &http.Transport{
        TLSClientConfig: &tls.Config{
            Certificates: []tls.Certificate{cert},
        },
    }
    return &http.Client{Transport: tr}, nil
}
```

### Fix 4: Force TLS 1.2+ for compatibility

```go
tr := &http.Transport{
    TLSClientConfig: &tls.Config{
        MinVersion: tls.VersionTLS12,
    },
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
    resp, err := http.Get("https://self-signed.example.com")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer resp.Body.Close()
}
```

Output:
```
x509: certificate signed by unknown authority
```

## Related Errors

- [tls-cert]({{< relref "/languages/go/tls-cert" >}}) — certificate loading and parsing errors.
- [net-http-timeout]({{< relref "/languages/go/net-http-timeout" >}}) — HTTP request timeouts after successful handshake.
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection failures before TLS negotiation.
