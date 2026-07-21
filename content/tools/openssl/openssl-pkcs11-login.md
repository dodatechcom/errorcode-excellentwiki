---
title: "[Solution] OpenSSL PKCS11 Login Error"
description: "Fix OpenSSL PKCS11 login error. Resolve PKCS#11 authentication issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL PKCS11 Login Error

The PKCS#11 login fails. The PIN is wrong or the token is locked.

## Common Causes

- PIN is wrong
- Token is locked after too many attempts
- Login type is wrong

## How to Fix

### Solution 1

```bash
pkcs11-tool --login --module /path/to/pkcs11.so --list-slots
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
