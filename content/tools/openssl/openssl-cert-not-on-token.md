---
title: "[Solution] OpenSSL Cert Not On Token Error"
description: "Fix OpenSSL cert not on token error. Resolve PKCS#11 certificate storage issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Cert Not On Token Error

The certificate is not found on the PKCS#11 token.

## Common Causes

- Certificate was never stored on token
- Certificate was deleted
- Wrong slot is being used

## How to Fix

### Solution 1

```bash
pkcs11-tool --module /path/to/pkcs11.so --list-objects --type cert
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
