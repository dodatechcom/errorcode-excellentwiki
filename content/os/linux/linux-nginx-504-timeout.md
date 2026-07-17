---
title: "[Solution] Linux nginx 504 Gateway Timeout — Upstream Timeout"
description: "Fix Linux nginx 504 Gateway Timeout errors. Resolve upstream timeouts, slow backend responses, and proxy timeout issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nginx", "504", "gateway-timeout", "upstream", "proxy", "timeout"]
weight: 5
---

# Linux: nginx — 504 Gateway Timeout — upstream timeout

The nginx `504 Gateway Timeout` error means nginx received no response from the upstream server within the configured timeout period. Unlike a 502 (invalid response), a 504 means the connection was established but the upstream took too long to respond, so nginx gave up and returned an error to the client.

## What This Error Means

nginx has configurable timeouts for proxying: `proxy_connect_timeout` (default 60s), `proxy_read_timeout` (default 60s), and `proxy_send_timeout` (default 60s). When the upstream server exceeds `proxy_read_timeout` without sending a complete response, nginx logs a 504 and returns it to the client. The upstream may be performing a slow database query, waiting on a lock, or processing a CPU-heavy task.

## Common Causes

- Backend application processing a slow database query
- Upstream server overloaded (high CPU, memory, or I/O)
- Missing database index causing full table scans
- Application deadlocking on resources
- Network latency between nginx and upstream
- Proxy timeout values too low for the workload
- Upstream server running garbage collection or maintenance

## How to Fix

### 1. Check nginx Error Log

```bash
# View timeout details
sudo tail -50 /var/log/nginx/error.log

# Common message:
# "upstream timed out (110: Connection timed out) while reading response header from upstream"
```

### 2. Increase Proxy Timeouts

```nginx
# In nginx server or location block
proxy_connect_timeout 120s;
proxy_read_timeout 300s;
proxy_send_timeout 300s;

# For long-running operations
location /api/reports {
    proxy_pass http://backend;
    proxy_read_timeout 600s;
}
```

### 3. Optimize Backend Queries

```bash
# Check slow queries (MySQL)
mysql -e "SHOW PROCESSLIST;" | grep -v Sleep

# Enable slow query log
mysql -e "SET GLOBAL slow_query_log = 'ON'; SET GLOBAL long_query_time = 2;"

# Check for missing indexes
mysql -e "EXPLAIN SELECT * FROM orders WHERE customer_id = 123;"
```

### 4. Check Upstream Resource Usage

```bash
# CPU and memory
top -bn1 | head -20
free -h

# Disk I/O
iostat -x 1 3

# Connection count
ss -s

# Check if upstream has resource limits
ulimit -a
```

### 5. Add Upstream Keepalive and Buffering

```nginx
upstream backend {
    server 127.0.0.1:8080;
    keepalive 32;
}

server {
    location / {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Connection "";

        # Buffer the upstream response
        proxy_buffering on;
        proxy_buffer_size 4k;
        proxy_buffers 8 4k;
    }
}
```

### 6. Use Caching for Slow Endpoints

```nginx
# Cache responses from slow endpoints
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mycache:10m;

location /api/data {
    proxy_cache mycache;
    proxy_cache_valid 200 5m;
    proxy_pass http://backend;
}
```

### 7. Split Long Operations

```bash
# Instead of one long request, use a job queue
# Client starts job -> returns job ID
# Client polls for completion

# In the application:
# POST /api/export -> 202 Accepted {"job_id": "abc123"}
# GET /api/export/abc123 -> 200 OK (when ready)
```

## Examples

```bash
$ curl -I http://example.com/api/report
HTTP/1.1 504 Gateway Timeout

$ sudo tail -3 /var/log/nginx/error.log
2025/07/14 10:05:00 [error] 1234#1234: *5678 upstream timed out (110: Connection timed out)
while reading response header from upstream, client: 192.168.1.10,
server: example.com, upstream: "http://127.0.0.1:8080/api/report"

# Backend was running a slow query
$ mysql -e "SHOW PROCESSLIST;"
+----+------+-----------+------+---------+------+-------+-------------------------------------+
| Id | User| db        | State| Command | Time | Info  |                                     |
+----+------+-----------+------+---------+------+-------+-------------------------------------+
| 42 | app  | production| Copying to tmp table | Query | 180 | SELECT * FROM orders JOIN ... |
+----+------+-----------+------+---------+------+-------+-------------------------------------+

# Fix: add index
$ mysql -e "CREATE INDEX idx_orders_customer ON orders(customer_id);"
```

## Related Errors

- [nginx 502 bad gateway]({{< relref "/os/linux/linux-nginx-502-upstream" >}}) — Invalid upstream response
- [nginx 403 forbidden]({{< relref "/os/linux/linux-nginx-403-forbidden" >}}) — Permission denied
- [MySQL deadlock]({{< relref "/os/linux/linux-mysql-deadlock" >}}) — Database deadlock errors
