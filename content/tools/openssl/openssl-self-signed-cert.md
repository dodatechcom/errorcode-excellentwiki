---
title: "[Solution] OpenSSL Self-Signed Certificate Error"
description: "Fix OpenSSL self-signed certificate error. Resolve self-signed certificate trust issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Self-Signed Certificate Error

The certificate is self-signed and not trusted by clients. Browsers and clients reject the connection.

## Common Causes

- Certificate was signed by its own key
- CA certificate is not in trust store
- Self-signed cert used in production

## How to Fix

### Solution 1

```bash
openssl x509 -in cert.pem -noout -issuer -subject
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
