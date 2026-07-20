---
title: "[Solution] Nginx DH Key Too Small Error"
description: "The Diffie-Hellman key size is below the minimum acceptable threshold (typically < 2048 bits)."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The Diffie-Hellman key size is below the minimum acceptable threshold (typically < 2048 bits).

## Common Causes

- **Default DH params** from old OpenSSL (1024-bit)
- **Self-generated DH file** with insufficient length
- **Missing DH parameters file**

## How to Fix

1. Generate strong DH params: `openssl dhparam -out /etc/ssl/dhparam.pem 4096`
2. Reference in Nginx: `ssl_dhparam /etc/ssl/dhparam.pem;`
3. Prefer ECDHE: `ssl_ecdh_curve X25519:secp384r1;`
4. Verify: `openssl dhparam -in /etc/ssl/dhparam.pem -text -noout | head -2`

## Examples

**Generate:**
```bash
openssl dhparam -out /etc/ssl/dhparam.pem 4096
```
**Config:**
```nginx
ssl_dhparam /etc/ssl/dhparam.pem;
ssl_ecdh_curve X25519:secp384r1;
```