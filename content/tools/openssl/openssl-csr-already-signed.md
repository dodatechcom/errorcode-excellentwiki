---
title: "[Solution] OpenSSL CSR Already Signed Error"
description: "Fix OpenSSL CSR already signed error. Resolve already-signed CSR issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL CSR Already Signed Error

The CSR has already been signed. A CSR should only be signed once by the requestor.

## Common Causes

- CSR was signed twice
- CSR has a self-signature that is invalid
- CSR was modified after signing

## How to Fix

### Solution 1

```bash
openssl req -in csr.pem -noout -verify
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
