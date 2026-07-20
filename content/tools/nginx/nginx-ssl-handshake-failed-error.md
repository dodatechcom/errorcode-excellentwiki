---
title: "[Solution] Nginx SSL Handshake Failed Error"
description: "The SSL/TLS handshake between client and server failed during connection."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The SSL/TLS handshake between client and server failed during connection.

## Common Causes

- **Protocol version mismatch**
- **Cipher suite mismatch**
- **Invalid or expired certificate**
- **SNI mismatch**
- **Client certificate required** but not provided

## How to Fix

1. Enable multiple protocols: `ssl_protocols TLSv1.2 TLSv1.3;`
2. Use broad cipher suite: `ssl_ciphers HIGH:!aNULL:!MD5:!RC4;`
3. Debug: `openssl s_client -connect example.com:443`
4. Check error logs: `tail -50 /var/log/nginx/error.log | grep SSL`

## Examples

**Debug:**
```bash
openssl s_client -connect example.com:443 2>&1 | grep -E 'Protocol|Cipher|Verify'
openssl s_client -connect example.com:443 -tls1_2
```