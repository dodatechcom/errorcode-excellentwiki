---
title: "[Solution] Ubuntu Server: nginx-502-bad-gateway"
description: "Fix Ubuntu nginx-502-bad-gateway. nginx returns 502 Bad Gateway from upstream."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx 502 Bad Gateway

nginx returns 502 Bad Gateway when the upstream application is down.

## Common Causes
- Backend application (PHP-FPM, Node.js) not running
- Backend listening on wrong port or socket
- PHP-FPM process pool exhausted
- Timeout connecting to upstream

## How to Fix
1. Check backend service
```bash
sudo systemctl status php8.1-fpm
```
2. Check nginx error log
```bash
sudo tail -20 /var/log/nginx/error.log
```
3. Verify upstream configuration
```bash
sudo nginx -T | grep -A5 "location"
```

## Examples
```bash
$ sudo tail -20 /var/log/nginx/error.log
2023/03/15 10:00:00 [error] 1234#1234: *1 connect() failed (111: Connection refused)
while connecting to upstream, client: 1.2.3.4, server: example.com

$ sudo systemctl status php8.1-fpm
● php8.1-fpm.service
   Active: inactive (dead)
```
