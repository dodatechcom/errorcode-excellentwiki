---
title: "[Solution] Nginx Fail Timeout Expired Error"
description: "A server was marked as failed and will not be retried until fail_timeout expires."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

A server was marked as failed and will not be retried until fail_timeout expires.

## Common Causes

- **Server repeatedly failing** health checks
- **max_fails threshold** reached
- **Short fail_timeout** causing frequent ejections
- **Backend not recovering**

## How to Fix

1. Adjust: `server 10.0.0.1:8080 max_fails=3 fail_timeout=30s;`
2. Fix the failing backend
3. Set reasonable fail_timeout (30s-120s)
4. Monitor: `tail -f /var/log/nginx/error.log | grep upstream`

## Examples

**Balanced:**
```nginx
upstream backend {
    server 10.0.0.1:8080 max_fails=5 fail_timeout=60s;
    server 10.0.0.2:8080 max_fails=5 fail_timeout=60s;
}
```