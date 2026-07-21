---
title: "[Solution] OpenSSL Smart Card Not Found Error"
description: "Fix OpenSSL smart card not found error. Resolve smart card reader issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Smart Card Not Found Error

The smart card or token is not detected. The reader is not connected or the token is not inserted.

## Common Causes

- Smart card reader is not connected
- Token is not inserted
- pcscd service is not running

## How to Fix

### Solution 1

```bash
pcsc_scan
```

### Solution 2

```bash
pkcs11-tool --list-slots
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
