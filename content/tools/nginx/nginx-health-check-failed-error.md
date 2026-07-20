---
title: "[Solution] Nginx Health Check Failed Error"
description: "Nginx or a third-party module detected that a backend server is unhealthy."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx or a third-party module detected that a backend server is unhealthy.

## Common Causes

- **Backend returning non-200**
- **Health endpoint errors**
- **Timeout on health checks**
- **Backend not deployed**

## How to Fix

1. Verify: `curl -I http://backend:8080/health`
2. Use proxy_next_upstream to failover
3. Fix the backend health endpoint

## Examples

**Config:**
```nginx
upstream backend {
    server 10.0.0.1:8080 max_fails=3 fail_timeout=30s;
    server 10.0.0.2:8080 max_fails=3 fail_timeout=30s;
}
location / {
    proxy_pass http://backend;
    proxy_next_upstream error timeout http_502 http_503;
}
```