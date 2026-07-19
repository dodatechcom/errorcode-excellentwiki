---
title: "[Solution] ERR_TLS_CERT_ALTNAME_INVALID — Certificate AltName Mismatch Fix"
description: "Fix ERR_TLS_CERT_ALTNAME_INVALID when server certificate doesn't match the hostname."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_TLS_CERT_ALTNAME_INVALID

The server certificate does not include the requested hostname.

## Causes

- Self-signed certificate
- Certificate issued for different domain
- Missing SAN (Subject Alternative Name)

## Development Fix

```javascript
// Skip cert verification (DEVELOPMENT ONLY)
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
```

For production, fix the certificate — never disable verification.
