---
title: "[Solution] Nginx Client Closed Connection Error"
description: "The client terminated the connection before the server finished processing."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The client terminated the connection before the server finished processing.

## Common Causes

- **Browser timeout**
- **User navigated away**
- **Load balancer health check timeout**
- **Client too short timeout**

## How to Fix

1. Tune timeouts: `client_body_timeout 60s; client_header_timeout 60s;`
2. Investigate backend latency
3. Set proxy_read_timeout
4. Monitor 499: `awk '$9 == 499' access.log | wc -l`

## Examples

**Adjust:**
```nginx
client_body_timeout 120s;
client_header_timeout 60s;
send_timeout 30s;
```
**Monitor:**
```bash
grep ' 499 ' /var/log/nginx/access.log | tail -10
```