---
title: "[Solution] OpenSSL NPN Not Supported Error"
description: "Fix OpenSSL NPN not supported error. Resolve Next Protocol Negotiation deprecation issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL NPN Not Supported Error

NPN is not supported. NPN has been replaced by ALPN in modern TLS.

## Common Causes

- NPN is deprecated and removed
- OpenSSL version does not support NPN
- Server does not support NPN

## How to Fix

### Solution 1

```bash
openssl s_client -connect host:443 -alpn h2
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
