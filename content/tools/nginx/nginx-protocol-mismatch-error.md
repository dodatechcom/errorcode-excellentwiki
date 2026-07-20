---
title: "[Solution] Nginx Protocol Mismatch Error"
description: "The client and server could not agree on a TLS protocol version during handshake."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The client and server could not agree on a TLS protocol version during handshake.

## Common Causes

- **Server only allows TLS 1.3** but client needs 1.2
- **Server disabled TLS 1.2** but old clients require it
- **Client too old** (only TLS 1.0/1.1)

## How to Fix

1. Enable both: `ssl_protocols TLSv1.2 TLSv1.3;`
2. Test: `openssl s_client -connect example.com:443 -tls1_2`
3. Never enable TLS 1.0/1.1 in production

## Examples

**Too restrictive:**
```nginx
ssl_protocols TLSv1.3;
```
**Balanced:**
```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
```