---
title: "Nginx Invalid Upstream Configuration"
description: "Nginx upstream block has syntax errors or references non-existent servers"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Invalid Upstream Configuration

Nginx upstream block has syntax errors or references non-existent servers

## Common Causes

- Upstream server address unreachable
- Upstream block name conflicts with built-in names
- Health check parameters invalid
- Missing closing bracket in upstream block

## How to Fix

1. Test config: `sudo nginx -t`
2. Verify upstream: `grep -A10 upstream /etc/nginx/sites-enabled/*`
3. Check server reachability: `curl -v http://upstream-server:port`
4. Review error log: `tail /var/log/nginx/error.log`

## Examples

```nginx
# Correct upstream configuration
upstream backend {
    server backend1.example.com:8080;
    server backend2.example.com:8080;
    keepalive 32;
}
```
