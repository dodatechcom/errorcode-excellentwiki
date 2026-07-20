---
title: "[Solution] Nginx TLS Version Too Old Error"
description: "The server is configured to use deprecated TLS versions (1.0 or 1.1) that are no longer accepted."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The server is configured to use deprecated TLS versions (1.0 or 1.1) that are no longer accepted.

## Common Causes

- **Only TLS 1.0/1.1** in ssl_protocols
- **Client refusing** old TLS
- **PCI compliance** rejecting old protocols

## How to Fix

1. Use only modern: `ssl_protocols TLSv1.2 TLSv1.3;`
2. Remove TLS 1.0/1.1
3. Verify: `nginx -t` and `openssl s_client -connect example.com:443 -tls1_2`

## Examples

**Insecure:**
```nginx
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
```
**Secure:**
```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
```