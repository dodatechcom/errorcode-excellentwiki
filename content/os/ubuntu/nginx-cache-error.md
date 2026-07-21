---
title: "[Solution] Ubuntu Server: nginx-cache-error"
description: "Fix Ubuntu nginx-cache-error. nginx proxy cache configuration error."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx Cache Error

nginx proxy cache fails to cache or serve cached content.

## Common Causes
- Cache directory not writable by nginx
- Cache zone not defined in config
- proxy_cache_path missing
- Cache key mismatch

## How to Fix
1. Check cache configuration
```bash
sudo nginx -T | grep proxy_cache
```
2. Create cache directory
```bash
sudo mkdir -p /var/cache/nginx/proxy_cache
sudo chown -R www-data:www-data /var/cache/nginx/proxy_cache
```
3. Configure cache zone
```bash
sudo nano /etc/nginx/nginx.conf
http {
    proxy_cache_path /var/cache/nginx/proxy_cache levels=1:2 keys_zone=my_cache:10m;
}
```

## Examples
```bash
$ sudo mkdir -p /var/cache/nginx/proxy_cache
$ sudo chown -R www-data:www-data /var/cache/nginx/proxy_cache
```