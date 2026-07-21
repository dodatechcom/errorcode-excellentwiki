---
title: "[Solution] OpenSSL SSL_ERROR_ZERO_RETURN Error"
description: "Fix OpenSSL SSL_ERROR_ZERO_RETURN error. Resolve TLS connection closure issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL SSL_ERROR_ZERO_RETURN Error

The peer has sent a close_notify alert. The TLS connection is being cleanly shut down.

## Common Causes

- Peer initiated graceful shutdown
- TLS session is ending normally
- Application should handle closure

## How to Fix

### Solution 1

```bash
openssl s_client -connect host:443
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
