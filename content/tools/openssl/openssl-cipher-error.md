---
title: "[Solution] OpenSSL Cipher Error"
description: "Fix OpenSSL cipher errors when selected cipher suites are not available"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Cipher Error

Cipher errors occur when OpenSSL cannot find or use the specified cipher suite.

## Common Causes

- Cipher disabled by security policy
- OpenSSL compiled without cipher support
- Cipher not supported by remote peer
- Deprecated cipher no longer available

## Common Error Messages

```
error:14094410:SSL routines:ssl3_read_bytes:sslv3 alert handshake failure
```

## How to Fix

### 1. List Available Ciphers

```bash
openssl ciphers -v 'ALL' | head -20
```

### 2. Test Specific Cipher

```bash
openssl s_client -connect example.com:443 -cipher ECDHE-RSA-AES256-GCM-SHA384
```

### 3. Check Cipher on Connection

```bash
openssl s_client -connect example.com:443 2>&1 | grep "Cipher is"
```

## Examples

```bash
openssl ciphers -v 'HIGH:!aNULL:!MD5' | wc -l
```
