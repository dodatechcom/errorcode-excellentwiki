---
title: "[Solution] OpenSSL CA New Certs Dir Error"
description: "Fix OpenSSL CA new certs dir error. Resolve CA output directory issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL CA New Certs Dir Error

The new_certs_dir does not exist or is not writable. Issued certificates cannot be stored.

## Common Causes

- new_certs_dir does not exist
- Directory is not writable
- Directory is full

## How to Fix

### Solution 1

```bash
ls -la /etc/ssl/ca/newcerts/
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
