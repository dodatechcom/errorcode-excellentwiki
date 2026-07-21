---
title: "[Solution] OpenSSL Certificate Revoked Error"
description: "Fix OpenSSL certificate revoked error. Resolve certificate revocation issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Certificate Revoked Error

The certificate has been revoked by the CA. It should no longer be trusted.

## Common Causes

- Certificate was revoked by CA
- Certificate is in CRL
- OCSP reports revoked status

## How to Fix

### Solution 1

```bash
openssl x509 -in cert.pem -noout -serial
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
