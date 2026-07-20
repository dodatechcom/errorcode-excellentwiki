---
title: "[Solution] Nginx OCSP Stapling Retrieval Error"
description: "The OCSP stapling mechanism fails to retrieve or cache a valid OCSP response."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The OCSP stapling mechanism fails to retrieve or cache a valid OCSP response.

## Common Causes

- **OCSP response expired** in Nginx cache
- **Responder returning malformed data**
- **Clock skew** causing rejection
- **ssl_trusted_certificate not configured**

## How to Fix

1. Set trusted cert: `ssl_trusted_certificate /path/to/ca-chain.pem;`
2. Set resolver: `resolver 1.1.1.1 8.8.8.8 valid=300s;`
3. Check clock: `date && ntpdate -q pool.ntp.org`
4. Test: `openssl s_client -connect example.com:443 -status`

## Examples

**Complete config:**
```nginx
server {
    listen 443 ssl;
    ssl_certificate /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/private/server.key;
    ssl_trusted_certificate /etc/ssl/certs/ca-chain.pem;
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 1.1.1.1 8.8.8.8 valid=300s;
}
```