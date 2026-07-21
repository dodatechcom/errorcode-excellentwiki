---
title: "[Solution] OpenSSL SSL_ERROR_WANT_WRITE Error"
description: "Fix OpenSSL SSL_ERROR_WANT_WRITE error. Resolve non-blocking TLS write issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL SSL_ERROR_WANT_WRITE Error

The TLS operation needs to write data but the socket would block. The operation is non-blocking.

## Common Causes

- Non-blocking socket send buffer is full
- TLS record cannot be sent
- Need to retry after buffer frees

## How to Fix

### Solution 1

```bash
openssl s_client -connect host:443
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
