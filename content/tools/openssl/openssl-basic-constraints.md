---
title: "[Solution] OpenSSL Basic Constraints Error"
description: "Fix OpenSSL basic constraints error. Resolve basic constraints extension issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Basic Constraints Error

The basic constraints are missing or wrong. A CA certificate does not have CA:true, or a leaf cert has CA:true.

## Common Causes

- CA certificate missing CA:TRUE
- Leaf certificate has CA:TRUE
- Path length constraint is exceeded

## How to Fix

### Solution 1

```bash
openssl x509 -in cert.pem -noout -text | grep -A1 'Basic Constraints'
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
