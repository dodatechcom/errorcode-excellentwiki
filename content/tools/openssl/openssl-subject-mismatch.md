---
title: "[Solution] OpenSSL Subject Mismatch Error"
description: "Fix OpenSSL subject mismatch error. Resolve certificate subject verification issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Subject Mismatch Error

The certificate subject does not match the expected name. Hostname verification fails.

## Common Causes

- Certificate CN does not match hostname
- SAN does not include the hostname
- Wrong certificate for the domain

## How to Fix

### Solution 1

```bash
openssl x509 -in cert.pem -noout -subject
```

### Solution 2

```bash
openssl x509 -in cert.pem -noout -text | grep 'Subject Alternative Name'
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
