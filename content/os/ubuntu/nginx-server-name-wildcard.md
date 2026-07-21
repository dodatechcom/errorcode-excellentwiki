---
title: "Nginx Server Name Wildcard Error"
description: "Nginx server_name wildcard configuration not matching requests"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Server Name Wildcard Error

Nginx server_name wildcard configuration not matching requests

## Common Causes

- Wildcard pattern incorrect (must use *.domain.com, not *.domain)
- server_name directive placed inside location block
- Default server not catching unmatched requests
- Multiple server blocks with conflicting patterns

## How to Fix

1. Check wildcard syntax: `*.example.com` not `*example.com`
2. Set default_server for unmatched: `server_name _;`
3. Test: `curl -H 'Host: test.example.com' http://localhost/`
4. Review error log: `tail /var/log/nginx/error.log`

## Examples

```nginx
# Wildcard server name configuration
server {
    server_name *.example.com;
    # ...
}
server {
    server_name _;  # Default catch-all
    return 444;
}
```
