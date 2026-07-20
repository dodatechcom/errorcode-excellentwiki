---
title: "[Solution] TLS Handshake Failure Fix"
description: "Fix TLS handshake failures in Go. Handle certificate validation, cipher suites, and protocol versions."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# TLS Handshake Failure

The TLS handshake fails in Go when the client and server cannot agree on protocol versions, cipher suites, or certificate chains. This is common with custom CAs, mutual TLS (mTLS), or servers that require specific TLS versions.

## Common Causes

```go
// Cause 1: Certificate signed by unknown CA
// tls: certificate signed by unknown authority

// Cause 2: TLS version mismatch
// Server requires TLS 1.3, client only supports TLS 1.2

// Cause 3: Client certificate not provided (mTLS)
// tls: bad certificate

// Cause 4: Hostname verification fails
// tls: cannot validate certificate for 10.0.0.1

// Cause 5: Cipher suite not supported
// tls: no supported transport
```

## How to Fix

### Fix 1: Configure TLS with custom CA

```go
import (
    "crypto/tls"
    "crypto/x509"
    "io/ioutil"
    "net/http"
)

func tlsClient() *http.Client {
    caCert, _ := ioutil.ReadFile("ca.pem")
    caPool := x509.NewCertPool()
    caPool.AppendCertsFromPEM(caCert)

    return &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                RootCAs:    caPool,
                MinVersion: tls.VersionTLS12,
            },
        },
    }
}
```

### Fix 2: Configure mutual TLS (mTLS)

```go
func mtlsClient() (*http.Client, error) {
    cert, err := tls.LoadX509KeyPair("client.crt", "client.key")
    if err != nil {
        return nil, err
    }

    caCert, _ := ioutil.ReadFile("ca.pem")
    caPool := x509.NewCertPool()
    caPool.AppendCertsFromPEM(caCert)

    return &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                Certificates: []tls.Certificate{cert},
                RootCAs:      caPool,
            },
        },
    }, nil
}
```

### Fix 3: Skip verification for development only

```go
// WARNING: Do not use in production
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

    caPool := x509.NewCertPool()
    caPool.AppendCertsFromPEM(caCert)

    client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{RootCAs: caPool},
        },
    }

    resp, err := client.Get("https://secure.example.com/api")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()

    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println(string(body))
}
```

## Related Errors

- [go-x509-error]({{< relref "/languages/go/go-x509-error" >}}) — X.509 certificate verification
- [go-ssh-error]({{< relref "/languages/go/go-ssh-error" >}}) — SSH handshake similar process
- [go-pkcs-error]({{< relref "/languages/go/go-pkcs-error" >}}) — PKCS#12 certificate loading
