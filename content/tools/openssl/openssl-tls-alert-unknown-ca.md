---
title: "[Solution] OpenSSL TLS Alert Unknown CA Error"
description: "Fix OpenSSL TLS alert unknown CA error. Resolve unknown CA certificate issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL TLS Alert Unknown CA Error

The peer rejects the certificate because the issuing CA is not in its trust store.

## Common Causes

- Client does not trust the server CA
- Intermediate CA is not installed
- Self-signed CA is not trusted

## How to Fix

### Solution 1

```bash
openssl s_client -connect host:443 -CAfile ca.pem
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
