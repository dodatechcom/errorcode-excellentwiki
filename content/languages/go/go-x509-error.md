---
title: "[Solution] crypto/x509 Certificate Error Fix"
description: "Fix Go x509 certificate errors. Handle certificate validation, chain verification, and format issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# crypto/x509 Certificate Error

The `crypto/x509` package fails during certificate verification when the certificate is expired, signed by an unknown CA, the hostname does not match the certificate CN/SAN, or the certificate chain is incomplete. X.509 errors are common in TLS clients connecting to services with self-signed or corporate CA certificates.

## Common Causes

```go
// Cause 1: Unknown CA — self-signed cert not trusted
resp, err := http.Get("https://self-signed.example.com")
// x509: certificate signed by unknown authority

// Cause 2: Hostname mismatch
// Certificate CN=api.example.com, connecting to 192.168.1.1
// x509: cannot validate certificate for 192.168.1.1

// Cause 3: Expired certificate
// Certificate valid: 2020-01-01 to 2021-01-01
// x509: certificate has expired

// Cause 4: Intermediate certificate missing
// Server only sends leaf cert, not the full chain
// x509: certificate signed by unknown authority

// Cause 5: System certificate pool missing root CA
// Custom Docker image with minimal CA bundle
// x509: certificate signed by unknown authority
```

## How to Fix

### Fix 1: Add custom CA certificate to TLS config

```go
import (
    "crypto/tls"
    "crypto/x509"
    "io/ioutil"
    "net/http"
)

func customHTTPClient(caCertPath string) (*http.Client, error) {
    caCert, err := ioutil.ReadFile(caCertPath)
    if err != nil {
        return nil, err
    }

    caCertPool := x509.NewCertPool()
    if !caCertPool.AppendCertsFromPEM(caCert) {
        return nil, fmt.Errorf("failed to parse CA certificate")
    }

    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                RootCAs: caCertPool,
            },
        },
    }
    return client, nil
}
```

### Fix 2: Skip verification for development only

```go
// WARNING: Do not use in production
client := &http.Client{
    Transport: &http.Transport{
        TLSClientConfig: &tls.Config{
            InsecureSkipVerify: true, // skip hostname and CA verification
        },
    },
}
```

### Fix 3: Verify certificate chain properly

```go
func verifyCert(certPEM, caPEM []byte) error {
    caCertPool := x509.NewCertPool()
    caCertPool.AppendCertsFromPEM(caPEM)

    block, _ := pem.Decode(certPEM)
    cert, err := x509.ParseCertificate(block.Bytes)
    if err != nil {
        return err
    }

    opts := x509.VerifyOptions{
        Roots:     caCertPool,
        KeyUsages: []x509.ExtKeyUsage{x509.ExtKeyUsageClientAuth},
    }

    _, err = cert.Verify(opts)
    return err
}
```

## Examples

```go
package main

import (
    "crypto/tls"
    "crypto/x509"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
)

func main() {
    caCert, err := ioutil.ReadFile("ca.pem")
    if err != nil {
        log.Fatal(err)
    }

    caCertPool := x509.NewCertPool()
    caCertPool.AppendCertsFromPEM(caCert)

    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                RootCAs: caCertPool,
            },
        },
    }

    resp, err := client.Get("https://api.example.com/secure")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println(string(body))
}
```

## Related Errors

- [tls-handshake]({{< relref "/languages/go/tls-handshake-error" >}}) — TLS handshake fails at transport level
- [go-pkcs-error]({{< relref "/languages/go/go-pkcs-error" >}}) — PKCS#12 certificate loading fails
- [go-crypto-error]({{< relref "/languages/go/go-crypto-error" >}}) — general crypto operation failures
