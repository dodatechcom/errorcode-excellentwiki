---
title: "[Solution] Nginx Worker Connections Error"
description: "Nginx worker process hits the connection limit, refusing new connections because worker_connections is too low for the traffic volume."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Worker Connections Error

Nginx worker processes handle connections up to the configured `worker_connections` limit. An error occurs when the limit is reached and new connections are refused.

## Common Causes

- The `worker_connections` value is too low for the traffic volume
- Too many idle keepalive connections are consuming worker slots
- The `worker_rlimit_nofile` is not increased to support high connection counts
- The system file descriptor limit is lower than the Nginx configuration

## How to Fix

1. Increase worker connections in the events block:

```nginx
events {
    worker_connections 4096;
    multi_accept on;
    use epoll;
}
```

2. Increase the system file descriptor limit:

```bash
# Check current limit
ulimit -n

# Increase temporarily
ulimit -n 65536

# Make permanent in /etc/security/limits.conf
nginx soft nofile 65536
nginx hard nofile 65536
```

3. Set worker_rlimit_nofile to match:

```nginx
worker_rlimit_nofile 65536;

events {
    worker_connections 16384;
}
```

4. Restart Nginx to apply changes:

```bash
nginx -t && systemctl restart nginx
```

## Examples

```bash
# Check current worker connection usage
ss -s
# TCP:   1234 (estab 1000, closed 200, orphaned 50, timewait 50)
```

```nginx
# High-performance configuration
worker_processes auto;
worker_rlimit_nofile 65536;

events {
    worker_connections 16384;
    multi_accept on;
    use epoll;
}
```

## Related Errors

- [Worker Connections Overflow]({{< relref "/tools/nginx/nginx-worker-connections-overflow-error" >}}) -- connection overflow
- [Open File Limit]({{< relref "/tools/nginx/nginx-open-file-limit-error" >}}) -- file descriptor limits
