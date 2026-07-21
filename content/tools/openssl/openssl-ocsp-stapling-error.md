---
title: "[Solution] OpenSSL OCSP Stapling Error"
description: "Fix OpenSSL OCSP stapling errors when online certificate status protocol fails"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL OCSP Stapling Error

OCSP stapling errors occur when the server cannot provide a valid OCSP response during TLS handshake.

## Common Causes

- OCSP responder unreachable
- OCSP response expired
- Server not configured for stapling
- Certificate missing OCSP responder URI

## Common Error Messages

```
error:14095124:SSL routines:ssl3_get_cert_status:tlsv1 alert certificate revoked
```

## How to Fix

### 1. Test OCSP Stapling

```bash
openssl s_client -connect example.com:443 -status 2>&1 | grep "OCSP"
```

### 2. Check OCSP Responder

```bash
openssl ocsp -issuer issuer.pem -cert cert.pem -url http://ocsp.example.com -resp_text
```

### 3. Configure OCSP Stapling

```bash
# Nginx configuration
ssl_stapling on;
ssl_stapling_verify on;
```

## Examples

```bash
openssl s_client -connect example.com:443 -tlsextdebug 2>&1 | grep OCSP
```
