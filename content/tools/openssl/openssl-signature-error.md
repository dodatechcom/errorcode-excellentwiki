---
title: "[Solution] OpenSSL Signature Error"
description: "Fix OpenSSL signature verification errors when digital signature validation fails"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Signature Error

Signature errors occur when OpenSSL cannot verify or create digital signatures correctly.

## Common Causes

- Signature algorithm mismatch
- Public key does not match signing key
- Corrupted signature data
- Hash algorithm not supported

## Common Error Messages

```
error:0480006C:PEM routines:PEM_read_bio:unknown label
```

## How to Fix

### 1. Verify Signature

```bash
openssl dgst -sha256 -verify public.pem -signature data.sig data.txt
```

### 2. Create Signature

```bash
openssl dgst -sha256 -sign private.pem -out data.sig data.txt
```

### 3. Check Signature Algorithm

```bash
openssl x509 -in cert.pem -text | grep "Signature Algorithm"
```

## Examples

```bash
openssl dgst -sha256 -verify pub.pem -signature sig.bin message.bin
```
