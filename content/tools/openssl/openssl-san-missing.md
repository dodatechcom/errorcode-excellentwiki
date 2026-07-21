---
title: "[Solution] OpenSSL SAN Missing Error"
description: "Fix OpenSSL SAN missing error. Resolve Subject Alternative Name issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL SAN Missing Error

The certificate does not have a Subject Alternative Name (SAN) extension. Modern TLS requires SAN.

## Common Causes

- SAN extension was not included when generating cert
- Only CN is set without SAN
- SAN is empty

## How to Fix

### Solution 1

```bash
openssl x509 -in cert.pem -noout -text | grep -A1 'Subject Alternative Name'
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
