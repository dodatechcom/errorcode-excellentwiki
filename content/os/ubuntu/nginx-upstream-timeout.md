---
title: "[Solution] Ubuntu Server: nginx-upstream-timeout"
description: "Fix Ubuntu nginx-upstream-timeout. nginx times out connecting to upstream server."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Nginx Upstream Timeout

nginx times out waiting for upstream application response.

## Common Causes
- Backend application too slow
- Upstream server overloaded
- Timeout values too low
- Network latency to upstream

## How to Fix
1. Increase timeout values
```bash
sudo nano /etc/nginx/sites-available/default
proxy_connect_timeout 60s;
proxy_read_timeout 60s;
proxy_send_timeout 60s;
```
2. Check upstream availability
```bash
curl -v http://localhost:3000/
```
3. Add retry logic
```bash
proxy_next_upstream error timeout http_502;
```

## Examples
```bash
$ sudo tail -20 /var/log/nginx/error.log
2023/03/15 10:00:00 [error] upstream timed out (110: Connection timed out)

$ curl -v http://localhost:3000/
* connect to 127.0.0.1 port 3000 failed: Connection refused
```
