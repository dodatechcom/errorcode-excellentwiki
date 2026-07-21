---
title: "[Solution] OpenSSL /dev/urandom Not Available Error"
description: "Fix OpenSSL /dev/urandom not available error. Resolve random device issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL /dev/urandom Not Available Error

/dev/urandom is not available on the system. OpenSSL cannot read random data.

## Common Causes

- /dev/urandom does not exist
- Device permissions are wrong
- Kernel does not provide /dev/urandom

## How to Fix

### Solution 1

```bash
ls -la /dev/urandom
```

### Solution 2

```bash
mknod /dev/urandom c 1 9
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
