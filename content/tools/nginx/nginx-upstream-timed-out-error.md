---
title: "[Solution] Nginx Upstream Timed Out Error"
description: "The upstream server did not respond within the configured timeout values."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The upstream server did not respond within the configured timeout values.

## Common Causes

- **Backend processing too slow**
- **Timeout values too low**
- **Backend overloaded**
- **Network latency** between Nginx and upstream

## How to Fix

1. Increase timeouts: `proxy_read_timeout 300s;`
2. Check backend: `curl -w '@curl-format.txt' http://backend:8080/api`
3. Use keepalive connections
4. Optimize backend queries

## Examples

**Extended:**
```nginx
proxy_connect_timeout 30s;
proxy_send_timeout 60s;
proxy_read_timeout 300s;
```
**With keepalive:**
```nginx
upstream backend { server 127.0.0.1:8080; keepalive 32; }
proxy_http_version 1.1;
proxy_set_header Connection "";
```