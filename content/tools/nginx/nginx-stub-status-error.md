---
title: "[Solution] Nginx Stub Status Error"
description: "The stub_status module is not enabled or the status endpoint is misconfigured."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The stub_status module is not enabled or the status endpoint is misconfigured.

## Common Causes

- **Module not compiled in**
- **stub_status outside location block**
- **Wrong context**

## How to Fix

1. Check: `nginx -V 2>&1 | grep http_stub_status`
2. Configure: `location /nginx_status { stub_status; allow 127.0.0.1; deny all; }`
3. Recompile if missing

## Examples

**Config:**
```nginx
server {
    listen 8080; server_name localhost;
    location /nginx_status {
        stub_status; access_log off; allow 127.0.0.1; deny all;
    }
}
```
**Check:**
```bash
curl http://localhost:8080/nginx_status
```