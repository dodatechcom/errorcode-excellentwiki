---
title: "[Solution] Nginx Ciphers Error"
description: "The configured SSL cipher suites are invalid or no common cipher exists with the client."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The configured SSL cipher suites are invalid or no common cipher exists with the client.

## Common Causes

- **Invalid cipher string** format
- **Using deprecated ciphers** (RC4, DES, MD5)
- **Strict cipher list** that few clients support
- **Cipher order** causing failures

## How to Fix

1. Use tested config: `ssl_ciphers HIGH:!aNULL:!MD5:!RC4:!3DES;`
2. List ciphers: `openssl ciphers -v 'HIGH:!aNULL' | head -20`
3. Test: `openssl s_client -connect example.com:443 -cipher ECDHE-RSA-AES128-GCM-SHA256`

## Examples

**Invalid:**
```nginx
ssl_ciphers BROKEN_CIPHER;
```
**Secure:**
```nginx
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
ssl_prefer_server_ciphers on;
ssl_ecdh_curve X25519:secp384r1;
```