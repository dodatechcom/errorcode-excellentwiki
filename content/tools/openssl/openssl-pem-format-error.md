---
title: "[Solution] OpenSSL PEM Format Error"
description: "Fix OpenSSL PEM format errors when reading or converting certificate files"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL PEM Format Error

PEM format errors occur when OpenSSL cannot parse PEM-encoded certificate or key files.

## Common Causes

- Missing PEM header/footer markers
- File is DER format not PEM
- Base64 encoding corruption
- Concatenated certificates not separated

## Common Error Messages

```
error:0906D06C:PEM routines:PEM_read_bio:no start line
```

## How to Fix

### 1. Verify PEM Format

```bash
openssl x509 -in cert.pem -text -noout
```

### 2. Convert DER to PEM

```bash
openssl x509 -in cert.der -inform DER -out cert.pem -outform PEM
```

### 3. Check File Contents

```bash
head -5 cert.pem
# Should show: -----BEGIN CERTIFICATE-----
```

## Examples

```bash
openssl pkcs12 -in cert.p12 -out cert.pem -nodes
```
