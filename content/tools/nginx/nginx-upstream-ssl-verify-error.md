---
title: "[Solution] Nginx Upstream SSL Verify Failed Error"
description: "Nginx cannot verify the SSL certificate presented by the upstream server."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot verify the SSL certificate presented by the upstream server.

## Common Causes

- **Self-signed certificate** on backend
- **Expired certificate**
- **Missing CA certificate**
- **Hostname mismatch**

## How to Fix

1. Provide CA: `proxy_ssl_trusted_certificate /path/to/ca.pem; proxy_ssl_verify on;`
2. Dev only: `proxy_ssl_verify off;`
3. Set SNI: `proxy_ssl_name backend.example.com; proxy_ssl_server_name on;`
4. Test: `openssl s_client -connect backend:8443 -CAfile ca.pem`

## Examples

**Full verification:**
```nginx
location / {
    proxy_pass https://backend:8443;
    proxy_ssl_trusted_certificate /etc/ssl/certs/ca.pem;
    proxy_ssl_verify on;
    proxy_ssl_verify_depth 3;
    proxy_ssl_name backend.example.com;
    proxy_ssl_server_name on;
}
```