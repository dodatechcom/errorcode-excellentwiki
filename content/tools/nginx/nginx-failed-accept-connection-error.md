---
title: "[Solution] Nginx Failed to Accept New Connection Error"
description: "Nginx cannot accept new TCP connections because the accept mutex or socket is in a bad state."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot accept new TCP connections because the accept mutex or socket is in a bad state.

## Common Causes

- **File descriptor limit reached**
- **Socket backlog full**
- **Network interface saturated**
- **Port already in use**

## How to Fix

1. Increase FDs: `ulimit -n 65535`
2. Increase backlog: `listen 80 backlog=65535;`
3. Check ports: `ss -tlnp | grep :80`
4. Use reuseport: `listen 80 reuseport;`

## Examples

**Optimized:**
```nginx
listen 80 reuseport backlog=65535;
listen 443 ssl reuseport backlog=65535;
```
**Check:**
```bash
ls /proc/$(cat /run/nginx.pid)/fd | wc -l
cat /proc/$(cat /run/nginx.pid)/limits | grep 'Max open files'
```