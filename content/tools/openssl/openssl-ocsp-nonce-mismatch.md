---
title: "[Solution] OpenSSL OCSP Nonce Mismatch Error"
description: "Fix OpenSSL OCSP nonce mismatch error. Resolve OCSP nonce verification issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL OCSP Nonce Mismatch Error

The OCSP response nonce does not match the request nonce. Replay attack protection triggered.

## Common Causes

- Nonce in response does not match request
- OCSP proxy modified nonce
- Replay attack detected

## How to Fix

### Solution 1

```bash
openssl ocsp -issuer ca.pem -cert cert.pem -url http://ocsp.example.com -nonce
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
