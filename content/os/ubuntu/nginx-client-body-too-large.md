---
title: "[Solution] Ubuntu Server: nginx-client-body-too-large"
description: "Fix Ubuntu nginx-client-body-too-large. nginx rejects uploads exceeding body size limit."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx Client Body Too Large

nginx returns 413 Request Entity Too Large for uploads.

## Common Causes
- client_max_body_size set too low
- Default 1M limit too restrictive
- Large file uploads rejected
- API endpoints needing large payloads

## How to Fix
1. Check current limit
```bash
grep client_max_body_size /etc/nginx/nginx.conf
```
2. Increase limit
```bash
sudo nano /etc/nginx/sites-available/default
client_max_body_size 50M;
```
3. Reload nginx
```bash
sudo nginx -t && sudo systemctl reload nginx
```

## Examples
```bash
$ curl -X POST -F "file=@large.iso" http://localhost/upload
<html>
<head><title>413 Request Entity Too Large</title></head>

$ grep client_max_body_size /etc/nginx/nginx.conf
client_max_body_size 1M;
```
