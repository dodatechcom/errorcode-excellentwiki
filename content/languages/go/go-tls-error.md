---
title: "[Solution] Go TLS Error — How to Fix"
description: "Fix Go TLS errors. Handle certificate loading, TLS configuration, and protocol negotiation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go TLS Error

Fix Go TLS errors. Handle certificate loading, TLS configuration, and protocol negotiation.

## Why It Happens

- TLS certificate is not loaded correctly causing handshake failures
- Minimum TLS version is too low causing security warnings
- Client certificate verification is not configured causing mTLS failures
- TLS certificate chain is incomplete causing verification errors

## Common Error Messages

```
tls: bad certificate
```
```
tls: unknown certificate authority
```
```
tls: handshake failure
```
```
tls: protocol version not supported
```

## How to Fix It

### Solution 1: Configure TLS server

```go
cert, _ := tls.LoadX509KeyPair("server.crt", "server.key")
tlsConfig := &tls.Config{
    Certificates: []tls.Certificate{cert},
    MinVersion:   tls.VersionTLS12,
}
ln, _ := tls.Listen("tcp", ":443", tlsConfig)
http.Serve(ln, nil)
```

### Solution 2: Configure mTLS

```go
caCert, _ := os.ReadFile("ca.crt")
caCertPool := x509.NewCertPool()
caCertPool.AppendCertsFromPEM(caCert)
tlsConfig := &tls.Config{
    ClientCAs:  caCertPool,
    ClientAuth: tls.RequireAndVerifyClientCert,
}
```

### Solution 3: Make HTTP client use TLS

```go
client := &http.Client{
    Transport: &http.Transport{
        TLSClientConfig: &tls.Config{
            MinVersion: tls.VersionTLS12,
        },
    },
}
resp, _ := client.Get("https://api.example.com")
```

### Solution 4: Load certificate from embedded

```go
//go:embed certs/server.crt
type certPEM []byte
//go:embed certs/server.key
type keyPEM []byte
func loadCerts() (*tls.Certificate, error) {
    return tls.X509KeyPair(certPEM, keyPEM)
}
```

## Common Scenarios

- TLS handshake fails because certificate is not loaded
- mTLS fails because CA certificate is not configured
- Client rejects server certificate because of protocol version mismatch

## Prevent It

- Load certificates with tls.LoadX509KeyPair
- Configure ClientAuth and ClientCAs for mTLS
- Always set MinVersion to tls.VersionTLS12 or higher
