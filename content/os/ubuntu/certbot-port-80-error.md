---
title: "[Solution] Ubuntu Server: certbot-port-80-error"
description: "Fix Ubuntu certbot-port-80-error. Certbot cannot bind to port 80 for HTTP challenge."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Certbot Port 80 Error

Certbot cannot bind to port 80 for HTTP-01 challenge.

## Common Causes
- Nginx or Apache already listening on port 80
- Other service using port 80
- Firewall blocking port 80

## How to Fix
1. Check what uses port 80
```bash
sudo ss -tlnp | grep :80
```
2. Use webroot mode instead
```bash
sudo certbot certonly --webroot -w /var/www/html -d example.com
```
3. Or stop web server temporarily
```bash
sudo systemctl stop nginx
sudo certbot certonly --standalone -d example.com
sudo systemctl start nginx
```

## Examples
```bash
$ sudo certbot certonly --standalone -d example.com
Problem binding to port 80: Could not bind to IPv4 or IPv6.
```