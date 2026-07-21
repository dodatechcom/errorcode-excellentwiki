---
title: "[Solution] OpenSSL PKCS11 Sign Error"
description: "Fix OpenSSL PKCS11 sign error. Resolve PKCS#11 signing issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL PKCS11 Sign Error

The PKCS#11 signing operation fails. The key is not on the token or the mechanism is unsupported.

## Common Causes

- Key is not on the token
- Mechanism is not supported
- Token is not logged in

## How to Fix

### Solution 1

```bash
pkcs11-tool --module /path/to/pkcs11.so --list-objects --type privkey
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
