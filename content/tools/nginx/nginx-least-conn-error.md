---
title: "[Solution] Nginx Least Connections Error"
description: "The least_conn load balancing algorithm is not available or misconfigured."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The least_conn load balancing algorithm is not available or misconfigured.

## Common Causes

- **Module not compiled in**
- **Used inside server block** instead of upstream
- **Combined with incompatible directives**

## How to Fix

1. Check module: `nginx -V 2>&1 | grep http_upstream_least_conn`
2. Use inside upstream: `upstream backend { least_conn; ... }`
3. Recompile if missing

## Examples

**Valid:**
```nginx
upstream app {
    least_conn;
    server 10.0.0.1:8080 weight=3;
    server 10.0.0.2:8080 weight=2;
    server 10.0.0.3:8080 weight=1;
}
```