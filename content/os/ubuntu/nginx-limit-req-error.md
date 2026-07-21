---
title: "[Solution] Ubuntu Server: nginx-limit-req-error"
description: "Fix Ubuntu nginx-limit-req-error. nginx rate limiting rejects too many requests."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx Limit Req Error

nginx rate limiting blocks legitimate traffic.

## Common Causes
- burst value too low
- rate limit too aggressive
- nodelay not configured
- Too many concurrent requests

## How to Fix
1. Check limit_req configuration
```bash
sudo nginx -T | grep limit_req
```
2. Increase burst
```bash
sudo nano /etc/nginx/sites-available/default
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

location /api/ {
    limit_req zone=api burst=50 nodelay;
}
```
3. Reload nginx
```bash
sudo nginx -t && sudo systemctl reload nginx
```

## Examples
```bash
$ sudo nginx -T | grep limit_req
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
```