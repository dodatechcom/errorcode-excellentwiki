---
title: "[Solution] OpenSSL SNI Error"
description: "Fix OpenSSL SNI errors when Server Name Indication extension causes connection failures"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL SNI Error

SNI errors occur when the Server Name Indication extension causes TLS connection problems.

## Common Causes

- SNI hostname does not match certificate
- Server does not support SNI
- SNI extension sent before TLS version negotiated
- Wildcard certificate does not match SNI

## Common Error Messages

```
error:14094418:SSL routines:ssl3_read_bytes:tlsv1 alert unknown ca
```

## How to Fix

### 1. Test SNI Connection

```bash
openssl s_client -connect example.com:443 -servername example.com
```

### 2. Disable SNI (Test Only)

```bash
openssl s_client -connect example.com:443 -noservername
```

### 3. Check SNI Support

```bash
openssl s_client -connect example.com:443 -tlsextdebug 2>&1 | grep SNI
```

## Examples

```bash
openssl s_client -connect example.com:443 -servername example.com 2>&1 | grep "Verify return code"
```
