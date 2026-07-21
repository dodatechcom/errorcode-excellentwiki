---
title: "[Solution] OpenSSL Certificate Verify Failed Error"
description: "Fix OpenSSL certificate verify failed error. Resolve certificate chain verification issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Certificate Verify Failed Error

The certificate chain verification fails. The certificate is not trusted or the chain is broken.

## Common Causes

- Certificate is not signed by trusted CA
- Chain is incomplete
- Certificate is expired

## How to Fix

### Solution 1

```bash
openssl verify -CAfile ca.pem cert.pem
```

### Solution 2

```bash
openssl verify -untrusted intermediate.pem -CAfile root.pem cert.pem
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
