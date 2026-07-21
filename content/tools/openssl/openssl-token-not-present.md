---
title: "[Solution] OpenSSL Token Not Present Error"
description: "Fix OpenSSL token not present error. Resolve PKCS#11 token detection issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Token Not Present Error

The PKCS#11 token is not present. The token was removed or the slot is not available.

## Common Causes

- Token was removed from reader
- Slot does not contain a token
- Token is locked

## How to Fix

### Solution 1

```bash
pkcs11-tool --list-slots --module /path/to/pkcs11.so
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
