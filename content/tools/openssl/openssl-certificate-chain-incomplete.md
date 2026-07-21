---
title: "[Solution] OpenSSL Certificate Chain Incomplete Error"
description: "Fix OpenSSL certificate chain incomplete error. Resolve missing intermediate certificates."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Certificate Chain Incomplete Error

The certificate chain is incomplete. Intermediate or root certificates are missing.

## Common Causes

- Intermediate certificate is missing
- Root certificate is not in the chain
- Chain is not properly ordered

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
