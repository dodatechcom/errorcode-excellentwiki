---
title: "[Solution] OpenSSL Key Not On Token Error"
description: "Fix OpenSSL key not on token error. Resolve PKCS#11 key storage issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Key Not On Token Error

The private key is not found on the PKCS#11 token.

## Common Causes

- Key was never generated on token
- Key was deleted
- Wrong slot is being used

## How to Fix

### Solution 1

```bash
pkcs11-tool --module /path/to/pkcs11.so --list-objects --type privkey
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
