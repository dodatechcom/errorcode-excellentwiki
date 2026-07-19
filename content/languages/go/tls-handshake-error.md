---
title: "[Solution] Go TLS handshake error — Network Error Fix"
description: "Fix Go TLS handshake error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# TLS handshake error

The error `tls: handshake failure` occurs when the TLS/SSL handshake between client and server fails.

## How to Fix

### Fix 1: Add custom CA certificate

```go
caCert, _ := ioutil.ReadFile("ca.crt")
caCertPool := x509.NewCertPool()
caCertPool.AppendCertsFromPEM(caCert)

client := &http.Client{
    Transport: &http.Transport{
        TLSClientConfig: &tls.Config{ RootCAs: caCertPool },
    },
}
```

## Related Errors

- [connection-refused]({{< relref "/languages/go/connection-refused" >}}) — connection refused.
- [http-timeout]({{< relref "/languages/go/http-timeout" >}}) — HTTP timeout.
