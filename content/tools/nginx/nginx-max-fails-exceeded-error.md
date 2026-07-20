---
title: "[Solution] Nginx Max Fails Exceeded Error"
description: "A server in the upstream pool exceeded max_fails and is temporarily disabled."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

A server in the upstream pool exceeded max_fails and is temporarily disabled.

## Common Causes

- **Backend crashing** or returning 5xx
- **Network issues**
- **Timeout errors**
- **Health checks failing consistently**

## How to Fix

1. Increase tolerance: `server 10.0.0.1:8080 max_fails=10 fail_timeout=120s;`
2. Investigate: `grep upstream /var/log/nginx/error.log | tail -20`
3. Add retry: `proxy_next_upstream error timeout http_502 http_503;`
4. Fix the backend

## Examples

**Monitor:**
```bash
grep -c 'connect() failed' /var/log/nginx/error.log
grep -c 'upstream timed out' /var/log/nginx/error.log
```