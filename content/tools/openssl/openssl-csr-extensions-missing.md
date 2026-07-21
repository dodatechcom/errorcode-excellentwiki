---
title: "[Solution] OpenSSL CSR Extensions Missing Error"
description: "Fix OpenSSL CSR extensions missing error. Resolve CSR extension issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL CSR Extensions Missing Error

The CSR does not contain the required extensions (SAN, key usage, etc.).

## Common Causes

- Extensions were not included in CSR config
- SAN was not specified
- Key usage extension is missing

## How to Fix

### Solution 1

```bash
openssl req -in csr.pem -noout -text | grep -A1 'Subject Alternative Name'
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
