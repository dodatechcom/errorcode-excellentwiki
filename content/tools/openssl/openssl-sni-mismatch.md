---
title: "[Solution] OpenSSL SNI Mismatch Error"
description: "Fix OpenSSL SNI mismatch error. Resolve Server Name Indication issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL SNI Mismatch Error

The SNI hostname does not match the server certificate. The server returns the wrong certificate.

## Common Causes

- SNI hostname does not match any certificate on server
- Server does not support SNI
- Default certificate is returned

## How to Fix

### Solution 1

```bash
openssl s_client -connect host:443 -servername hostname
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
