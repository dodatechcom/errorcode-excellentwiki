---
title: "[Solution] Nginx Missing Server Block Error"
description: "Nginx cannot start because no server block is defined to handle incoming requests."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot start because no server block is defined to handle incoming requests.

## Common Causes

- **All server blocks removed** during cleanup
- **Commented out** server blocks
- **Empty conf.d directory**
- **Wrong include path**

## How to Fix

1. Add at minimum one server block
2. Check include paths: `grep -n include /etc/nginx/nginx.conf`
3. Restore default server block if deleted
4. Validate: `sudo nginx -t`

## Examples

**Broken:**
```nginx
http { # no server blocks defined }
```
**Fixed:**
```nginx
http {
    include /etc/nginx/conf.d/*.conf;
    server { listen 80 default_server; server_name _; return 404; }
}
```