---
title: "[Solution] OpenSSL OCSP Response Expired Error"
description: "Fix OpenSSL OCSP response expired error. Resolve OCSP response freshness issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL OCSP Response Expired Error

The OCSP response has expired. The response thisUpdate is too old.

## Common Causes

- OCSP response was cached too long
- OCSP responder produces infrequent updates
- Response validity period is short

## How to Fix

### Solution 1

```bash
openssl ocsp -issuer ca.pem -cert cert.pem -url http://ocsp.example.com
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
