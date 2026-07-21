---
title: "[Solution] OpenSSL Self-Signed Cert in Chain Error"
description: "Fix OpenSSL self-signed cert in chain error. Resolve self-signed certificate in chain issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Self-Signed Cert in Chain Error

A self-signed certificate is found in the certificate chain. The chain cannot be verified to a trusted root.

## Common Causes

- Self-signed CA is in the chain
- Root certificate is self-signed and not in trust store
- Chain includes untrusted cert

## How to Fix

### Solution 1

```bash
openssl verify -CAfile ca.pem cert.pem
```

### Solution 2

```bash
openssl s_client -connect host:443 -showcerts
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
