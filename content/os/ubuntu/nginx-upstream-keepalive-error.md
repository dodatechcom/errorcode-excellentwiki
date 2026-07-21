---
title: "[Solution] Ubuntu Server: nginx-upstream-keepalive-error"
description: "Fix Ubuntu nginx-upstream-keepalive-error. nginx upstream keepalive connections fail."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx Upstream Keepalive Error

nginx upstream keepalive connections fail or cause errors.

## Common Causes
- keepalive directive missing in upstream block
- keepalive_timeout not configured
- Connection pool too small
- Backend closes connections prematurely

## How to Fix
1. Configure keepalive
```bash
sudo nano /etc/nginx/sites-available/default
upstream backend {
    server 127.0.0.1:3000;
    keepalive 32;
}
```
2. Set HTTP version to 1.1
```bash
location / {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Connection "";
}
```
3. Reload nginx
```bash
sudo nginx -t && sudo systemctl reload nginx
```

## Examples
```bash
$ sudo nginx -T | grep keepalive
# (empty -- not configured)
```