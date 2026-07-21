---
title: "Certbot Nginx Authentication Module Error"
description: "Certbot nginx plugin cannot authenticate due to missing module"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Certbot Nginx Authentication Module Error

Certbot nginx plugin cannot authenticate due to missing module

## Common Causes

- nginx module ngx_http_ssl_module not loaded
- Certbot nginx plugin cannot restart nginx
- SSL configuration syntax error in nginx
- Certbot cannot write challenge files

## How to Fix

1. Check nginx modules: `nginx -V 2>&1 | grep ssl`
2. Install nginx-full: `sudo apt-get install nginx-full`
3. Test nginx: `sudo nginx -t`
4. Check challenge directory permissions

## Examples

```bash
# Check nginx SSL module
nginx -V 2>&1 | grep --color ssl

# Install nginx with all modules
sudo apt-get install nginx-full

# Test nginx config
sudo nginx -t
```
