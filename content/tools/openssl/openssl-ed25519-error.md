---
title: "[Solution] OpenSSL Ed25519 Error"
description: "Fix OpenSSL Ed25519 key errors when generating or using Ed25519 keys fails"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Ed25519 Error

Ed25519 errors occur when OpenSSL cannot generate or use Ed25519 elliptic curve keys.

## Common Causes

- OpenSSL version too old for Ed25519
- Key format not compatible with Ed25519
- Ed25519 not supported by engine
- Conversion between key types not allowed

## Common Error Messages

```
error:0800007D:PDF routines:PDF_password_bio_read:unsupported cipher
```

## How to Fix

### 1. Check Ed25519 Support

```bash
openssl genpkey -algorithm Ed25519 -out key.pem
```

### 2. Verify Key

```bash
openssl pkey -in key.pem -text -noout
```

### 3. Create Certificate with Ed25519

```bash
openssl req -new -key key.pem -out req.pem -nodes -algorithm Ed25519
```

## Examples

```bash
openssl pkey -in ed25519_key.pem -pubout -out ed25519_pub.pem
```
