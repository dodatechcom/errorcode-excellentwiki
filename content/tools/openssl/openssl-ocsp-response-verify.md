---
title: "[Solution] OpenSSL OCSP Response Verify Error"
description: "Fix OpenSSL OCSP response verify error. Resolve OCSP response verification issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL OCSP Response Verify Error

The OCSP response verification fails. The response is signed by an unknown or untrusted signer.

## Common Causes

- OCSP response signer is not trusted
- Response signature is invalid
- Response is corrupted

## How to Fix

### Solution 1

```bash
openssl ocsp -issuer ca.pem -cert cert.pem -url http://ocsp.example.com -resp_text
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
