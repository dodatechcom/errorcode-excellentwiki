---
title: "[Solution] OpenSSL Digital Signature in Email Error"
description: "Fix OpenSSL digital signature in email error. Resolve S/MIME email signature issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Digital Signature in Email Error

The digital signature on the email cannot be verified. The signer certificate is not trusted.

## Common Causes

- Signer certificate is not trusted
- Signature is corrupted
- Signer certificate is expired

## How to Fix

### Solution 1

```bash
openssl smime -verify -in signed.pem -CAfile ca.pem
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
