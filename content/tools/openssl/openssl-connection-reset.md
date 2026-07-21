---
title: "[Solution] OpenSSL Connection Reset Error"
description: "Fix OpenSSL connection reset error. Resolve TCP connection reset issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Connection Reset Error

The connection is reset by the peer. The TCP connection is forcibly closed.

## Common Causes

- Peer reset the connection
- Firewall dropped the connection
- Server crashed during TLS handshake

## How to Fix

### Solution 1

```bash
openssl s_client -connect host:443
```

### Solution 2

```bash
tcpdump -i any port 443
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
