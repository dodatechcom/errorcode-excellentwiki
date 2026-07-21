---
title: "[Solution] OpenSSL CA Unique Subject Error"
description: "Fix OpenSSL CA unique subject error. Resolve duplicate certificate subject issues."
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL CA Unique Subject Error

The CA rejects the certificate because the subject already exists and unique_subject is set.

## Common Causes

- Subject already exists in CA database
- unique_subject = yes in config
- Certificate was already issued

## How to Fix

### Solution 1

```bash
cat /etc/ssl/ca/index.txt | grep '/CN=myhost'
```

## Related Pages

- [OpenSSL Certificate Errors]({{< relref "/tools/openssl/openssl-unable-to-load-certificate" >}})
- [OpenSSL Key Errors]({{< relref "/tools/openssl/openssl-unable-to-load-private-key" >}})
- [OpenSSL TLS Errors]({{< relref "/tools/openssl/openssl-ssl-handshake-failure" >}})
