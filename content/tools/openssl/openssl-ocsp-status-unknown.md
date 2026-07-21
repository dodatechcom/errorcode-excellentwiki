---
title: "[Solution] OpenSSL OCSP Status Unknown Error"
description: "Fix OpenSSL OCSP status unknown error. Resolve OCSP responder issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL OCSP Status Unknown Error

The OCSP responder returns an unknown status. The certificate serial number is not in the response.

## Common Causes

- Certificate is not in OCSP database
- OCSP responder is misconfigured
- Serial number format is wrong

## How to Fix

### Solution 1

```bash
openssl ocsp -issuer ca.pem -cert cert.pem -url http://ocsp.example.com
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
