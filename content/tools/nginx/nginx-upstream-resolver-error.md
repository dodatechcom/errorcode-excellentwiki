---
title: "[Solution] Nginx Upstream Resolver Error"
description: "Nginx cannot resolve the upstream hostname due to DNS resolution failure."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot resolve the upstream hostname due to DNS resolution failure.

## Common Causes

- **DNS server unreachable**
- **Invalid resolver address**
- **DNS timeout**
- **Missing resolver directive**

## How to Fix

1. Configure resolver: `resolver 8.8.8.8 8.8.4.4 valid=300s;`
2. Use dynamic with resolver: `set $upstream http://backend.example.com:8080;`
3. Test DNS: `dig backend.example.com +short`
4. Check /etc/resolv.conf

## Examples

**Complete:**
```nginx
resolver 8.8.8.8 1.1.1.1 valid=300s ipv6=off;
resolver_timeout 5s;
server {
    listen 80; server_name app.example.com;
    location / { set $upstream http://backend.internal:8080; proxy_pass $upstream; }
}
```