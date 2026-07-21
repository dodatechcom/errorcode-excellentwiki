---
title: "[Solution] OpenSSL Untrusted Root Error"
description: "Fix OpenSSL untrusted root error. Resolve root certificate trust issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Untrusted Root Error

The root CA certificate is not in the trust store. The certificate chain cannot be verified.

## Common Causes

- Root CA is not installed in trust store
- Custom CA was used but not trusted
- Trust store is outdated

## How to Fix

### Solution 1

```bash
openssl verify -CAfile ca.pem cert.pem
```

### Solution 2

```bash
update-ca-certificates
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
