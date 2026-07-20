---
title: "[Solution] Nginx Slow Start Error"
description: "The slow_start parameter is used with incompatible load balancing methods."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The slow_start parameter is used with incompatible load balancing methods.

## Common Causes

- **slow_start with ip_hash** (incompatible)
- **slow_start with hash** (incompatible)
- **Module not compiled in**

## How to Fix

1. Remove ip_hash or use without slow_start
2. slow_start only works with least_conn or round-robin
3. Validate: `sudo nginx -t`

## Examples

**Compatible:**
```nginx
upstream backend {
    server 10.0.0.1:8080 slow_start=60s;
    server 10.0.0.2:8080 slow_start=60s;
    server 10.0.0.3:8080 backup;
}
```