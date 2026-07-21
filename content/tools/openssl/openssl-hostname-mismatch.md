---
title: "[Solution] OpenSSL Hostname Mismatch Error"
description: "Fix OpenSSL hostname mismatch error. Resolve certificate hostname verification issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Hostname Mismatch Error

The hostname in the certificate does not match the connected hostname. TLS verification fails.

## Common Causes

- Certificate CN does not match hostname
- SAN does not include the hostname
- Wrong certificate installed on server

## How to Fix

### Solution 1

```bash
openssl x509 -in cert.pem -noout -text | grep -A1 'Subject Alternative Name'
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
