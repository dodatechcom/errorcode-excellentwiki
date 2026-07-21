---
title: "[Solution] OpenSSL Issuer Not Found Error"
description: "Fix OpenSSL issuer not found error. Resolve certificate issuer reference issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Issuer Not Found Error

The issuer of the certificate cannot be found. The issuer certificate is not available.

## Common Causes

- Issuer certificate is not in the chain
- Issuer CA is not installed
- Certificate chain is broken

## How to Fix

### Solution 1

```bash
openssl x509 -in cert.pem -noout -issuer
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
