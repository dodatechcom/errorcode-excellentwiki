---
title: "[Solution] Nginx No Live Upstreams Error"
description: "All servers in the upstream pool are marked as down or have failed health checks."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

All servers in the upstream pool are marked as down or have failed health checks.

## Common Causes

- **All backends down** or unreachable
- **Health checks failing** on all servers
- **max_fails threshold reached**
- **Network partition**

## How to Fix

1. Check backends: `curl -I http://backend1:8080/health`
2. Add backup server: `server 10.0.0.3:8080 backup;`
3. Adjust max_fails: `server 10.0.0.1:8080 max_fails=5 fail_timeout=60s;`
4. Review upstream config

## Examples

**With backup:**
```nginx
upstream app {
    server 10.0.0.1:8080 max_fails=5 fail_timeout=60s;
    server 10.0.0.2:8080 max_fails=5 fail_timeout=60s;
    server 10.0.0.3:8080 backup;
}
```