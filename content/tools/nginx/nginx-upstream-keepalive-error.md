---
title: "[Solution] Nginx Upstream Keepalive Error"
description: "The keepalive connections to the upstream are misconfigured or exhausted."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The keepalive connections to the upstream are misconfigured or exhausted.

## Common Causes

- **Missing keepalive directive**
- **keepalive value too low**
- **Missing Connection header**
- **Backend not supporting keepalive**

## How to Fix

1. Add keepalive: `upstream backend { server 10.0.0.1:8080; keepalive 32; }`
2. Set headers: `proxy_http_version 1.1; proxy_set_header Connection "";`
3. Set timeout: `keepalive_timeout 60s;`

## Examples

**Complete:**
```nginx
upstream backend {
    server 10.0.0.1:8080; server 10.0.0.2:8080;
    keepalive 64; keepalive_requests 1000; keepalive_timeout 60s;
}
server {
    location / {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
    }
}
```