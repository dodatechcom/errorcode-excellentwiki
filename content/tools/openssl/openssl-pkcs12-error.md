---
title: "[Solution] OpenSSL PKCS12 Error"
description: "Fix OpenSSL PKCS12 errors when creating or parsing PKCS12 bundles fails"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL PKCS12 Error

PKCS12 errors occur when OpenSSL cannot create or read PKCS12 (.p12/.pfx) files.

## Common Causes

- Wrong password for PKCS12 file
- PKCS12 file corrupted
- MAC verification failed
- Unsupported PKCS12 algorithm

## Common Error Messages

```
error:14077418:SSL routines:SSL_CTX_new:tlsv1 alert unknown ca
```

## How to Fix

### 1. Parse PKCS12 File

```bash
openssl pkcs12 -in cert.p12 -info -noout -passin pass:password
```

### 2. Convert PKCS12 to PEM

```bash
openssl pkcs12 -in cert.p12 -out cert.pem -nodes -passin pass:password
```

### 3. Create PKCS12 Bundle

```bash
openssl pkcs12 -export -out bundle.p12 -inkey key.pem -in cert.pem -certfile ca.pem
```

## Examples

```bash
openssl pkcs12 -in bundle.p12 -passin pass:test -nodes | head -10
```
