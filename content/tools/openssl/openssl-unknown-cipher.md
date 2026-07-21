---
title: "[Solution] OpenSSL Unknown Cipher Error"
description: "Fix OpenSSL unknown cipher error. Resolve unrecognized cipher algorithm issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Unknown Cipher Error

The specified cipher algorithm is not recognized. The cipher name is wrong or not compiled in.

## Common Causes

- Cipher name is misspelled
- Cipher is not compiled into OpenSSL
- Cipher was removed in newer version

## How to Fix

### Solution 1

```bash
openssl ciphers -v 'ALL'
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
