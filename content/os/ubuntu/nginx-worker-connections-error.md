---
title: "[Solution] Ubuntu Server: nginx-worker-connections-error"
description: "Fix Ubuntu nginx-worker-connections-error. nginx worker connections limit reached."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx Worker Connections Error

nginx cannot accept new connections because worker limit is reached.

## Common Causes
- worker_connections too low
- Keep-alive timeout too long
- Too many concurrent connections
- Worker process crashed

## How to Fix
1. Check current limit
```bash
grep worker_connections /etc/nginx/nginx.conf
```
2. Increase limit
```bash
sudo nano /etc/nginx/nginx.conf
events {
    worker_connections 4096;
    multi_accept on;
}
```
3. Reload nginx
```bash
sudo nginx -t
sudo systemctl reload nginx
```

## Examples
```bash
$ grep worker_connections /etc/nginx/nginx.conf
worker_connections 768;

$ sudo nginx -T | grep worker_connections
worker_connections 768;
```
