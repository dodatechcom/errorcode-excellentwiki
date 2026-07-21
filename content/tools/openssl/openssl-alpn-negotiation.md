---
title: "[Solution] OpenSSL ALPN Negotiation Error"
description: "Fix OpenSSL ALPN negotiation error. Resolve Application-Layer Protocol Negotiation issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL ALPN Negotiation Error

ALPN negotiation fails. The client and server cannot agree on an application protocol.

## Common Causes

- Client ALPN list does not overlap with server
- HTTP/2 is required but not negotiated
- ALPN extension is missing

## How to Fix

### Solution 1

```bash
openssl s_client -connect host:443 -alpn h2
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
