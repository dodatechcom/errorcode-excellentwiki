---
title: "[Solution] OpenSSL Key Usage Invalid Error"
description: "Fix OpenSSL key usage invalid error. Resolve key usage extension issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Key Usage Invalid Error

The certificate key usage does not include the required usage. TLS or code signing usage is missing.

## Common Causes

- Key usage does not include digitalSignature
- Key usage does not include keyEncipherment
- Extended key usage is wrong

## How to Fix

### Solution 1

```bash
openssl x509 -in cert.pem -noout -text | grep -A1 'Key Usage'
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
