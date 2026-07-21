---
title: "Nginx DNS Resolver Error"
description: "Nginx cannot resolve upstream hostnames via DNS"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx DNS Resolver Error

Nginx cannot resolve upstream hostnames via DNS

## Common Causes

- resolver directive missing or pointing to non-existent DNS server
- DNS server unreachable from Nginx host
- resolver timeout too low for slow DNS responses
- resolver not configured for dynamic proxy_pass

## How to Fix

1. Add resolver: `resolver 8.8.8.8 8.8.4.4 valid=300s;` in server block
2. Test DNS: `nslookup upstream-host`
3. Increase timeout: `resolver_timeout 5s;`
4. Check Nginx error log for resolver errors

## Examples

```nginx
# Configure resolver in Nginx
server {
    resolver 8.8.8.8 8.8.4.4 valid=300s;
    resolver_timeout 5s;
    location /api/ {
        set $upstream http://backend:8080;
        proxy_pass $upstream;
    }
}
```
