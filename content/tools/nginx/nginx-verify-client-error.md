---
title: "[Solution] Nginx Verify Client Error"
description: "Client certificate verification failed during mutual TLS handshake."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Client certificate verification failed during mutual TLS handshake.

## Common Causes

- **Client did not send certificate**
- **Self-signed cert** not in trusted CA file
- **Certificate expired**
- **Intermediate CA missing**
- **ssl_verify_depth too shallow**

## How to Fix

1. Provide CA chain: `ssl_client_certificate /path/to/ca-bundle.pem;`
2. Use `optional` for optional access: `ssl_verify_client optional;`
3. Check client cert: `openssl s_client -connect example.com:443 -cert client.pem -key client-key.pem`
4. Ensure CA bundle includes all intermediates

## Examples

**Mutual TLS:**
```nginx
server {
    listen 443 ssl; server_name internal.example.com;
    ssl_certificate /etc/ssl/certs/server.pem;
    ssl_certificate_key /etc/ssl/private/server.key;
    ssl_client_certificate /etc/ssl/certs/ca.pem;
    ssl_verify_client on;
    ssl_verify_depth 3;
}
```