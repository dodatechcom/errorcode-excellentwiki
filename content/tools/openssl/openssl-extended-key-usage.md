---
title: "[Solution] OpenSSL Extended Key Usage Error"
description: "Fix OpenSSL extended key usage error. Resolve EKU extension issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Extended Key Usage Error

The extended key usage does not include the required purpose. TLS server auth EKU is missing.

## Common Causes

- EKU does not include serverAuth
- EKU does not include clientAuth
- EKU OID is not recognized

## How to Fix

### Solution 1

```bash
openssl x509 -in cert.pem -noout -text | grep -A1 'Extended Key Usage'
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
