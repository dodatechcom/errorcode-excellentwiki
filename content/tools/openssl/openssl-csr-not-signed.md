---
title: "[Solution] OpenSSL CSR Not Signed Error"
description: "Fix OpenSSL CSR not signed error. Resolve unsigned CSR issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL CSR Not Signed Error

The CSR is not signed. It was created without a private key or the signing step was skipped.

## Common Causes

- CSR was created without -newkey
- CSR signing was skipped
- CSR was generated as unsigned

## How to Fix

### Solution 1

```bash
openssl req -in csr.pem -noout -verify
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
